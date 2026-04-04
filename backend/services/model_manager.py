"""ModelManager - centralized Groq model selection for LLM calls."""

import logging
import os
from typing import List, Optional

from langchain_groq import ChatGroq


logger = logging.getLogger(__name__)


class ModelManager:
    """Selects and uses the first available Groq model from a candidate list."""

    DEFAULT_MODEL = "llama-3.1-8b-instant"

    # Task-specific model assignment — larger models for quality-critical tasks
    MODELS_BY_TASK = {
        "research":   "llama-3.1-8b-instant",
        "writing":    "llama-3.3-70b-versatile",
        "validation": "llama-3.1-8b-instant",
        "review":     "llama-3.3-70b-versatile",
    }

    def __init__(
        self,
        models: Optional[List[str]] = None,
        api_key: Optional[str] = None,
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ):
        self.api_key = api_key or os.getenv("GROQ_API_KEY")
        self.temperature = temperature
        self.max_tokens = max_tokens

        configured_models = models or self._models_from_env()
        self.models = configured_models if configured_models else [self.DEFAULT_MODEL]

        self.current_model: Optional[str] = None
        self.current_llm: Optional[ChatGroq] = None

    def _models_from_env(self) -> List[str]:
        primary = os.getenv("GROQ_MODEL", os.getenv("DEFAULT_MODEL", self.DEFAULT_MODEL)).strip()
        fallback = os.getenv("GROQ_FALLBACK_MODELS", "").strip()

        ordered: List[str] = []
        if primary:
            ordered.append(primary)
        if fallback:
            for model in fallback.split(","):
                name = model.strip()
                if name and name not in ordered:
                    ordered.append(name)
        return ordered

    def _build_llm(self, model: str, max_tokens: Optional[int] = None) -> ChatGroq:
        return ChatGroq(
            api_key=self.api_key,
            model=model,
            temperature=self.temperature,
            max_tokens=max_tokens if max_tokens is not None else self.max_tokens,
            request_timeout=60,
        )

    def _candidate_models(self, preferred_model: Optional[str] = None) -> List[str]:
        resolved_preferred = preferred_model
        if resolved_preferred in {None, "", "free", "auto"}:
            resolved_preferred = None

        ordered: List[str] = []
        for model in [resolved_preferred, self.current_model, *self.models]:
            if model and model not in ordered:
                ordered.append(model)
        return ordered

    async def get_llm(self, preferred_model: Optional[str] = None) -> ChatGroq:
        """Return the first working Groq model after a lightweight probe."""
        if not self.api_key:
            raise RuntimeError("GROQ_API_KEY is not set")

        failures: List[str] = []
        for model in self._candidate_models(preferred_model):
            llm = self._build_llm(model)
            print(f"[MODEL] Using Groq model: {model}")
            logger.info("[MODEL] Trying Groq model: %s", model)
            try:
                await llm.ainvoke("Reply with: OK")
                self.current_model = model
                self.current_llm = llm
                return self.current_llm
            except Exception as exc:
                failures.append(f"{model}: {exc}")
                logger.warning("[MODEL] Groq model failed: %s", model)
                continue

        attempted = ", ".join(self._candidate_models(preferred_model))
        details = " | ".join(failures[-3:]) if failures else "No probe details"
        raise RuntimeError(f"No available Groq models. Tried: [{attempted}]. Details: {details}")

    async def ainvoke(self, prompt: str, preferred_model: Optional[str] = None):
        """Invoke prompt with automatic Groq model failover."""
        if not self.current_llm:
            await self.get_llm(preferred_model=preferred_model)

        try:
            return await self.current_llm.ainvoke(prompt)
        except Exception:
            logger.warning("[MODEL] Current Groq model failed during invocation, retrying fallback")
            self.current_llm = None
            await self.get_llm(preferred_model=preferred_model)
            return await self.current_llm.ainvoke(prompt)

    async def invoke_for(
        self,
        task: str,
        messages,
        preferred_model: Optional[str] = None,
        max_tokens: Optional[int] = None,
    ):
        """
        Invoke messages using the model assigned to the given task.
        Tries the task-specific model first; falls back to the current/default model.

        task:       one of "research", "writing", "validation", "review"
        messages:   list of LangChain message objects (SystemMessage, HumanMessage, …)
        max_tokens: optional per-call token budget override
        """
        task_model = self.MODELS_BY_TASK.get(task)
        if task_model:
            try:
                llm = self._build_llm(task_model, max_tokens=max_tokens)
                logger.info("[MODEL] Task '%s' using model: %s (max_tokens=%s)", task, task_model, max_tokens)
                print(f"[MODEL] Task '{task}' → {task_model} (max_tokens={max_tokens or self.max_tokens})")
                return await llm.ainvoke(messages)
            except Exception as exc:
                logger.warning(
                    "[MODEL] Task model '%s' failed for task '%s': %s — falling back to default",
                    task_model, task, exc,
                )
        # Fall back to current/default model
        if not self.current_llm:
            await self.get_llm(preferred_model=preferred_model)
        return await self.current_llm.ainvoke(messages)
