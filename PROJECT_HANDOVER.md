# PROJECT HANDOVER DOCUMENTATION

## 1. Project Overview

The **AI Research Paper Generator** is an end-to-end system that produces IEEE-style research papers from a user topic and optional structured inputs (authors, equations, diagrams, tables, notes).

Primary stack:
- Backend API: FastAPI
- Orchestration: LangGraph + LangChain
- LLM inference: Groq (current), with historical Ollama/OpenRouter migration traces
- Research retrieval: arXiv + optional web search
- Frontend: Next.js + React + Zustand + custom dashboard UI

High-level workflow:
1. User submits topic and metadata from frontend.
2. Backend creates an async task and persists it.
3. LangGraph runs agent pipeline: research -> writing -> formatting -> validation.
4. Progress updates are streamed through task state (`step`, `progress`, `message`, `stages`).
5. Final output includes structured paper content, LaTeX, validation metrics, and PDF/export endpoints.

---

## 2. System Architecture

### Frontend
- Next.js app in `nextjs-frontend/`
- Uses polling (`use-polling`) to fetch backend task status.
- Renders an 8-step pipeline UI synced with backend step IDs.
- Supports paper preview, validation view, and exports.

### Backend
- FastAPI app in `backend/api.py`.
- LangGraph routes in `backend/langgraph_routes.py` (mounted under `/api/langgraph`).
- Task lifecycle and persistence in `backend/services/graph_integration.py`.
- Agent orchestration in `backend/graph/paper_graph.py`.
- Shared state contract in `backend/graph/paper_state.py`.

### Agent Pipeline (LangGraph)
- `ResearchAgent` -> gather papers and synthesize research context.
- `WritingAgent` -> generate full paper sections (single-call mode).
- `FormattingAgent` -> convert sections into IEEE-compliant LaTeX/content.
- `ValidationAgent` -> Pydantic + structural/content checks and optional section regeneration.

### Model Manager
- Centralized in `backend/services/model_manager.py`.
- Current provider: Groq (`ChatGroq`).
- Supports preferred model + fallback list from environment.

### External Services
- Groq API (LLM inference).
- arXiv search via internal tool wrappers.
- Optional web search integration.

Flow:

`User -> Frontend -> FastAPI (/api/langgraph) -> GraphIntegrationService -> LangGraph pipeline -> ModelManager/Groq -> research + generation + formatting + validation -> persisted task/result -> frontend polling + download/export`

---

## 3. Directory Structure

Note: This tree focuses on tracked project code and key runtime folders (excluding heavy vendored folders like `node_modules` and `.venv` internals).

```text
IEEE-Paper-Generator/
├── .env
├── Dockerfile
├── docker-compose.yml
├── main.py
├── README.md
├── PROJECT_HANDOVER.md
├── requirements.txt
├── outputs/
│   ├── tasks.json
│   └── *.pdf
├── generated_assets/
├── backend/
│   ├── __init__.py
│   ├── api.py
│   ├── langgraph_routes.py
│   ├── agents_v2/
│   │   ├── __init__.py
│   │   ├── research_agent.py
│   │   ├── writing_agent.py
│   │   ├── formatting_agent.py
│   │   ├── validation_agent.py
│   │   └── review_agent.py
│   ├── graph/
│   │   ├── __init__.py
│   │   ├── paper_graph.py
│   │   └── paper_state.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── paper_models.py
│   └── services/
│       ├── __init__.py
│       ├── model_manager.py
│       ├── graph_integration.py
│       ├── ieee_formatter.py
│       ├── ieee_latex_builder.py
│       ├── pdf_generator.py
│       ├── equation_service.py
│       ├── diagram_processor.py
│       └── reference_manager.py
├── src/
│   ├── __init__.py
│   ├── connectors/
│   │   ├── __init__.py
│   │   └── arxiv_connector.py
│   ├── formatters/
│   │   ├── __init__.py
│   │   ├── ieee_formatter.py
│   │   └── equation_formatter.py
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── arxiv_tool.py
│   │   ├── web_search.py
│   │   ├── web_loader.py
│   │   └── knowledge_extractor.py
│   └── validators/
│       ├── __init__.py
│       ├── pydantic_models.py
│       ├── pydantic_validator.py
│       ├── content_validator.py
│       ├── ieee_validator.py
│       └── metrics.py
├── models/
│   └── paper_models.py
├── agents/
│   └── validation_agent.py
├── tests/
│   ├── __init__.py
│   ├── test_connectors.py
│   └── test_validators.py
└── nextjs-frontend/
    ├── Dockerfile
    ├── package.json
    ├── next.config.ts
    ├── tsconfig.json
    ├── public/
    └── src/
        ├── app/
        │   ├── layout.tsx
        │   ├── page.tsx
        │   ├── globals.css
        │   ├── ieee-generator/
        │   └── research-paper/
        ├── components/
        │   ├── header.tsx
        │   ├── providers.tsx
        │   ├── theme-provider.tsx
        │   ├── theme-toggle.tsx
        │   ├── ieee/
        │   └── ui/
        ├── features/
        │   ├── dashboard/
        │   └── paper/
        ├── hooks/
        │   ├── use-polling.ts
        │   └── use-theme.ts
        ├── services/
        │   └── api.ts
        ├── store/
        │   ├── paper-store.ts
        │   └── theme-store.ts
        ├── lib/
        │   └── utils.ts
        └── types/
            └── index.ts
```

Folder purpose summary:
- `backend/`: Active API + LangGraph pipeline runtime.
- `src/`: Legacy/shared tools/connectors/formatters/validators used by pipeline components.
- `nextjs-frontend/`: UI, pipeline dashboard, preview/export client.
- `outputs/`: generated artifacts and persistent `tasks.json` state.
- `tests/`: focused connector/validator unit tests.
- `agents/`, `models/`, `main.py`: older/alternate paths kept in repo; not primary API execution path.

---

## 4. File Relationship Map

Core runtime relationships:

- `backend/api.py`
  -> creates FastAPI app and mounts `langgraph_routes.router`
  -> also contains legacy `/api/*` endpoints (in-memory task path)

- `backend/langgraph_routes.py`
  -> validates request payloads
  -> calls `GraphIntegrationService.generate_paper()`
  -> exposes status/download/export/validation APIs

- `backend/services/graph_integration.py`
  -> creates task IDs and `PaperState`
  -> persists/loads task snapshots from `outputs/tasks.json`
  -> invokes `PaperGenerationGraph.invoke()` in background
  -> computes and publishes step/progress/message

- `backend/graph/paper_graph.py`
  -> wires LangGraph nodes and edges
  -> instantiates `ResearchAgent`, `WritingAgent`, `FormattingAgent`, `ValidationAgent`

- `backend/agents_v2/research_agent.py`
  -> uses `src/tools/arxiv_tool.py` + `src/tools/web_search.py`
  -> synthesizes summary/key points

- `backend/agents_v2/writing_agent.py`
  -> uses `ModelManager.ainvoke()`
  -> generates full paper in a single LLM call
  -> parses text into section fields

- `backend/agents_v2/formatting_agent.py`
  -> uses `backend/services/ieee_formatter.py`
  -> produces LaTeX and formatted content

- `backend/agents_v2/validation_agent.py`
  -> validates against `backend/models/paper_models.py`
  -> can regenerate weak sections via `WritingAgent`

- `backend/services/model_manager.py`
  -> centralized model loading/fallback (Groq)
  -> all active agents rely on this manager

- `nextjs-frontend/src/services/api.ts`
  -> calls `/api/langgraph/*` endpoints

- `nextjs-frontend/src/features/dashboard/generation-dashboard.tsx`
  -> polls status endpoint
  -> maps backend `step/progress/message` into UI

Data flow between components is state-driven through `PaperState` and task snapshots in `GraphIntegrationService`.

---

## 5. Agent Pipeline

The UI and task service expose an 8-step conceptual pipeline. Actual execution combines some conceptual steps into a 4-node LangGraph.

### Conceptual/UI steps
1. **Model Selection**
   - ModelManager picks a working model.
2. **Research Agent**
   - Query arXiv and gather references.
3. **Knowledge Synthesis**
   - LLM summarizes findings and gaps.
4. **Paper Generation**
   - WritingAgent drafts all core sections.
5. **IEEE Formatting**
   - FormattingAgent structures and emits LaTeX.
6. **Validation Agent**
   - Pydantic and structure/content checks.
7. **Enhancement Pipeline**
   - Represented as a final post-processing stage in task progress (currently coarse-grained in integration service).
8. **Final Output**
   - Result marked complete with export-ready content.

### LangGraph runtime nodes
- Node 1: `research`
- Node 2: `write`
- Node 3: `format`
- Node 4: `validate`

Progress callback maps these nodes to conceptual step IDs and percentages.

---

## 6. Data Flow

Full lifecycle:
1. Frontend submits `GenerateRequest` (`topic`, `model_name`, optional structure data).
2. `POST /api/langgraph/generate` creates `task_id` and initial `PaperState`.
3. Task is persisted to `outputs/tasks.json` and background pipeline starts.
4. ModelManager resolves model.
5. Research step fetches documents and synthesizes context.
6. Writing step produces sections (single-call generation + parsing).
7. Formatting step generates IEEE LaTeX and normalized formatted content.
8. Validation step normalizes and validates against strict Pydantic schema.
9. Task status endpoint returns live step/progress/message/stages.
10. On completion, frontend can call validation/download/export endpoints.
11. Completed/failed tasks are auto-cleaned after retention delay and pruned by age/count policies.

---

## 7. Model Usage

Current implementation:
- Provider: **Groq** (`ChatGroq`), configured via `backend/services/model_manager.py`.
- Key env vars:
  - `GROQ_API_KEY`
  - `GROQ_MODEL`
  - `GROQ_FALLBACK_MODELS`
  - `DEFAULT_MODEL` (compat alias)

How switching works:
- `GraphIntegrationService` passes preferred model from request/task.
- `ModelManager` builds candidate model list:
  - preferred model
  - current working model
  - env-configured model list
- Performs lightweight probe (`ainvoke("Reply with: OK")`) and selects first working model.
- On invocation failure, retries with fallbacks.

About Ollama/OpenRouter:
- The repository contains migration history from OpenRouter and Ollama.
- Active runtime path is Groq-based.
- To reintroduce Ollama, implement provider branching in `ModelManager` (e.g., `MODEL_PROVIDER=groq|ollama`) and expose provider-specific env config.

---

## 8. API Endpoints

### Active LangGraph endpoints (`/api/langgraph/*`)
- `POST /api/langgraph/generate`
  - Create async generation task.
- `GET /api/langgraph/status/{task_id}`
  - Return `status`, `step`, `progress`, `message`, `stages`, optional `result`.
- `GET /api/langgraph/validation/{task_id}`
  - Return validation metrics and optional IEEE/enhancement reports.
- `GET /api/langgraph/download/{task_id}`
  - Return compiled/fallback PDF.
- `GET /api/langgraph/latex/{task_id}`
  - Return LaTeX source.
- `GET /api/langgraph/export/json/{task_id}`
  - Export result JSON file.
- `GET /api/langgraph/export/txt/{task_id}`
  - Export plain text.
- `GET /api/langgraph/export/latex/{task_id}`
  - Export `.tex` file.
- `GET /api/langgraph/tasks`
  - List tracked tasks.
- `DELETE /api/langgraph/tasks/{task_id}`
  - Delete task.
- `GET /api/langgraph/graph-info`
  - Return graph nodes/edges metadata.
- `GET /api/langgraph/ieee-preview/{task_id}`
  - Return IEEE formatting preview payload.
- `POST /api/langgraph/compile-pdf/{task_id}`
  - Compile and return PDF.
- `GET /api/langgraph/ieee-validate/{task_id}`
  - Validate IEEE output structure.
- `GET /api/langgraph/health`
  - Health + model provider metadata.

### Legacy endpoints in `backend/api.py` (`/api/*`)
Also present but represent older in-memory flow:
- `/api/generate`, `/api/status/{task_id}`, `/api/download/{task_id}`, etc.
- `/export/ieee-pdf`, `/export/ieee-latex`

Recommendation: treat `/api/langgraph/*` as the primary contract.

---

## 9. State Management

Task storage:
- Persistent file: `outputs/tasks.json`
- Managed by `GraphIntegrationService`.

Task lifecycle:
1. **Creation**: queued task + initialized `PaperState`.
2. **Processing**: step updates emitted throughout pipeline.
3. **Completion/Failure**: result or error persisted.
4. **Cleanup policies**:
   - delayed delete completed/failed tasks after ~60s
   - cap total tasks (`MAX_TASKS=20`) by removing oldest
   - remove expired tasks older than ~1 hour

Status shape includes:
- `status`, `step`, `progress`, `message`, `stages`
- timestamps: `created_at`, `started_at`, `completed_at`
- `error` and optional final `result`

---

## 10. Output Format

Generated paper targets IEEE conference style and includes:
- Title
- Abstract
- Keywords
- Main sections:
  - Introduction
  - Related Work
  - Methodology / Proposed Methodology
  - Implementation
  - Results and Discussion
  - Conclusion
- References
- Optional equations/figures/tables insertion

Output artifacts:
- Structured JSON-like result object
- LaTeX source (`latex_source`)
- PDF (via pdflatex when available, ReportLab fallback)

---

## 11. Extension Guide

### Add a new agent
1. Create agent file under `backend/agents_v2/`.
2. Extend `PaperState` with required fields.
3. Wire node in `backend/graph/paper_graph.py`.
4. Add step mapping/progress in `backend/services/graph_integration.py`.
5. Update frontend step definitions (`nextjs-frontend/src/types/index.ts`) if UI should reflect new stage.

### Change LLM provider
1. Update `backend/services/model_manager.py` to support provider abstraction.
2. Add provider env vars to `.env`.
3. Keep `GraphIntegrationService` and agents unchanged (they already depend on ModelManager).

### Improve research retrieval
- Extend `src/tools/arxiv_tool.py` and `src/tools/web_search.py`.
- Add re-ranking, deduplication, citation metadata quality checks.

### Improve output quality
- Enhance one-shot writing prompt and parser robustness in `backend/agents_v2/writing_agent.py`.
- Add stronger validation rules in `backend/models/paper_models.py` and `ValidationAgent`.

### Add vector DB / RAG
- Introduce embedding + retrieval service in `backend/services/`.
- Inject retrieved context into `ResearchAgent` and/or `WritingAgent` prompts.

---

## 12. Known Limitations

1. **Architecture drift / legacy overlap**
- `backend/api.py` still contains older endpoint path and imports that may not be used in active flow.
- `main.py`, `agents/`, `models/` include legacy artifacts.

2. **Frontend type drift**
- `nextjs-frontend/src/types/index.ts` still has some stale fields/options (e.g., health type naming, legacy model options text).

3. **Enhancement stage granularity**
- UI exposes enhancement step, but current LangGraph runtime is 4 core nodes; enhancement is coarse in task service.

4. **Citation accuracy and factual correctness**
- LLM-generated synthesis can hallucinate or mis-cite; validation is structural, not full semantic verification.

5. **One-shot parsing fragility**
- WritingAgent now parses section headers from one LLM response; malformed model output may degrade section extraction.

6. **Task retention behavior**
- Completed tasks are auto-removed quickly (60s), which can surprise users expecting long-lived history.

7. **Dependency ecosystem sensitivity**
- `langchain-groq` version must stay compatible with installed `langchain-core` and `langchain` versions.

---

## 13. Setup Instructions

### Prerequisites
- Python 3.10+ (project also used with 3.12)
- Node.js 18+
- npm

### Backend setup
1. Create/activate virtual environment.
2. Install deps:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure `.env`:
   - Set `GROQ_API_KEY`
   - Optionally tune `GROQ_MODEL`, `GROQ_FALLBACK_MODELS`
4. Start backend:
   ```bash
   python -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
   ```

### Frontend setup
1. Install frontend deps:
   ```bash
   cd nextjs-frontend
   npm install
   ```
2. Optional API override:
   - `NEXT_PUBLIC_API_URL=http://localhost:8000`
3. Start frontend:
   ```bash
   npm run dev
   ```

### Docker setup
From project root:
```bash
docker compose up --build
```

### Health checks
- LangGraph backend health:
  - `GET http://localhost:8000/api/langgraph/health`
- Legacy health:
  - `GET http://localhost:8000/api/health`

### Optional Ollama note
Current runtime uses Groq. Ollama startup is not required unless provider support is reintroduced.

---

## Additional Continuation Notes

- Primary development target should be `backend/langgraph_routes.py` + `backend/services/graph_integration.py` + `backend/graph/*` + `backend/agents_v2/*`.
- Prefer cleaning or deprecating legacy endpoint paths in `backend/api.py` to reduce confusion.
- If updating frontend health/model UI, align `nextjs-frontend/src/types/index.ts` with current backend health schema.
- Keep step IDs synchronized between backend (`GraphIntegrationService`) and frontend (`PIPELINE_STEPS`).
