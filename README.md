# IEEE Research Paper Generator

Automated AI-powered IEEE conference paper generation system using **LangChain + LangGraph** with clean 4-agent architecture and **publication-ready IEEE formatting**.

**Status**: ✅ Production-Ready | IEEE Formatting Complete | Fully Documented | Easy to Deploy

### ✨ NEW: IEEE Paper Formatter with PDF Generation

Generate **professional IEEE conference papers** with:
- Official IEEEtran LaTeX format (2-column, Times New Roman)
- Automatic section reordering (Intro → Related Work → Methodology → Results → Conclusion)
- PDF compilation with pdflatex
- LaTeX preview and validation
- Equation/figure/reference auto-numbering
- Image embedding in PDFs

[📖 IEEE Formatting Guide](IEEE_FORMATTING_GUIDE.md) | [⚡ Quick Start (5 min)](QUICK_START_IEEE.md) | [📋 Reference Card](REFERENCE_CARD.md)

---

## 📋 Quick Links

- [🚀 Quick Start (5 min)](#-quick-start-5-minutes)
- [🎯 What It Does](#-what-this-does)
- [✨ IEEE Formatting (NEW)](#-ieee-formatting-features-new)
- [🏗️ Architecture](#-system-architecture)
- [📚 API Reference](#-api-reference)
- [🐳 Docker](#-docker-deployment)
- [📖 Docs](#-documentation)
- [❓ FAQ](#-faq)

---

## What This Does

This application generates **complete IEEE conference papers** from a research topic. It:

✅ Researches arXiv papers and the internet for latest references  
✅ Generates structured paper content (abstract, introduction, methodology, results, conclusion)  
✅ **[NEW]** Accepts diagrams and inserts them with proper IEEE formatting  
✅ **[NEW]** Accepts mathematical equations and auto-numbers them  
✅ **[NEW]** Generates IEEE-formatted LaTeX with official IEEEtran template  
✅ **[NEW]** Compiles to publication-ready PDFs with pdflatex  
✅ **[NEW]** Validates IEEE format compliance  
✅ Auto-extracts keywords from your topic  
✅ Applies IEEE paper formatting automatically  
✅ Validates citations and references  
✅ Grades paper quality with AI reviewer feedback  
✅ Downloads as PDF, LaTeX, or JSON

**Use cases:**
- Conference paper preparation
- Research documentation
- Quick literature review compilation
- Academic paper prototyping
- Publication-ready paper generation

---

## ✨ IEEE Formatting Features (NEW!)

The system now produces **official IEEE conference papers** ready for submission:

### 🏗️ IEEE LaTeX Template
- **Document Class**: `\documentclass[conference]{IEEEtran}`
- **Layout**: Two-column format with automatic balancing
- **Font**: Times New Roman, 10pt (IEEE standard)
- **Margins**: IEEE standard (0.75" top, 1" sides)
- **Automatic**: Two-column layout, proper spacing, line numbering

### 📊 Paper Structure (Auto-Ordered)
Papers are automatically restructured to IEEE standard order:
1. **Title & Authors** (with affiliations)
2. **Abstract & Keywords**
3. **I. Introduction**
4. **II. Related Work**
5. **III. Methodology**
6. **IV. Implementation**
7. **V. Results**
8. **VI. Conclusion**
9. **References** (IEEE style: [1], [2], ...)

### 🔄 Formatting Features
- **Automatic Section Reordering**: Content automatically placed in IEEE-standard order
- **Equation Numbering**: Equations auto-numbered (1), (2), (3), ...
- **Figure Management**: Diagrams as Fig. 1, Fig. 2, ... with captions
- **Reference Formatting**: Citations as [1], [2], [3], ... (IEEE style)
- **LaTeX Validation**: Check compliance before PDF generation
- **PDF Compilation**: 2-pass pdflatex for proper references and TOC

### 🎨 Frontend IEEE Preview Component
- **Load LaTeX Preview**: View formatted LaTeX source
- **Download PDF**: Compile and download publication-ready PDF
- **Validate Format**: Check IEEE compliance (shows checklist)
- **Paper Statistics**: Shows sections, equations, figures, references count

### 📝 API Endpoints (NEW)
```
GET  /api/langgraph/ieee-preview/{task_id}    - Get LaTeX preview + stats
POST /api/langgraph/compile-pdf/{task_id}     - Compile to PDF
GET  /api/langgraph/ieee-validate/{task_id}   - Validate format compliance
```

### 💻 Backend Services (NEW)
| Service | Purpose | LOC |
|---------|---------|-----|
| `ieee_latex_builder.py` | Build IEEE LaTeX documents | 650+ |
| `pdf_generator.py` | Compile LaTeX to PDF | 170+ |
| `ieee_formatter.py` | Orchestrate formatting pipeline | 400+ |

---

## 🎯 Features

This system generates **production-ready IEEE conference papers** using a clean 4-agent LangGraph pipeline:

### ResearchAgent
- Fetches relevant papers from arXiv and web
- Extracts author names, publication years, key findings
- Returns structured references for citations
- Supports up to 20 papers per generation

### WritingAgent  
- Generates all 7 IEEE paper sections:
  - Abstract (150-250 words)
  - Introduction (with motivation)
  - Related Work (comparative analysis)
  - Methodology (detailed approach)
  - Implementation (technical specifics)
  - Results & Evaluation (with metrics)
  - Conclusion & Future Work
- Uses LangChain prompt templates for consistency
- Maintains academic tone throughout

### FormattingAgent
- Converts to IEEE LaTeX (conference 2-column style)
- Auto-inserts diagrams with captions
- Converts equations to LaTeX notation
- Extracts and includes keywords
- Auto-numbers figures, equations, citations
- Ready for PDF compilation

### ReviewAgent
- Validates all 7 sections present
- Checks reference format compliance
- Detects duplicate content
- Generates quality score (0-100%)
- Returns specific improvement suggestions
- Flags structural issues

### 🤖 4-Agent Pipeline

```
Topic + Settings
    ↓
[ResearchAgent] ←→ ArXiv API, Web Search
    ↓ (research_summary, key_points, references)
[WritingAgent] ←→ LangChain Prompts
    ↓ (abstract, intro, methodology, results, conclusion, etc.)
[FormattingAgent] ←→ IEEE LaTeX Template
    ↓ (latex_source, formatted_content, keywords)
[ReviewAgent] ←→ LLM Quality Check
    ↓ (quality_score, issues[], review_passed)
IEEE Paper PDF
```

### 📊 Supported Features

| Feature | Details | Status |
|---------|---------|--------|
| **Diagrams** | Upload PNG/JPG/SVG → auto-inserted with IEEE captions | ✅ |
| **Equations** | ASCII math → auto-converted to LaTeX, auto-numbered | ✅ |
| **Research** | 3-20 arXiv papers fetched per generation | ✅ |
| **Citations** | Auto-numbered [1], [2], ... [n] format (IEEE style) | ✅ |
| **Keywords** | Auto-extracted from title and abstract | ✅ |
| **IEEE Formatting** | Official IEEEtran 2-column template | ✅ NEW |
| **PDF Export** | Compile LaTeX to publication-ready PDF | ✅ NEW |
| **LaTeX Preview** | View formatted LaTeX before PDF | ✅ NEW |
| **Format Validation** | Check IEEE compliance and constraints | ✅ NEW |
| **Section Reordering** | Auto-arrange in IEEE standard order | ✅ NEW |
| **Export** | PDF, LaTeX source, JSON metadata | ✅ |
| **Models** | 4+ via OpenRouter (OpenAI, Anthropic, Mistral, DeepSeek) | ✅ |

### 🔄 LLM Fallback Chain (Automatic)

If primary model fails, automatically tries the next:

1. **gpt-4o-mini** (OpenAI) — Fastest & cheapest
2. **claude-3-haiku** (Anthropic) — Best reasoning
3. **mistral-7b** (Mistral) — Open source
4. **deepseek-chat** (DeepSeek) — Reliable backup


## 📋 System Requirements

### Prerequisites

| Item | Version | Why |
|------|---------|-----|
| **Python** | 3.10+ (3.12 preferred) | Backend & agents |
| **Node.js** | 20+ | Frontend build |
| **RAM** | 4GB minimum, 8GB+ recommended | LLM inference |
| **Internet** | Required | OpenRouter API calls |

### API Keys (Free)

Get **OpenRouter API Key** (free $5/month credit):
1. Visit [openrouter.ai/keys](https://openrouter.ai/keys)
2. Sign up (30 seconds)
3. Create API key
4. Copy key (`sk-or-v1-...`)

### Supported OS

✅ macOS 11+ (Intel/Apple Silicon)  
✅ Windows 10+ (with WSL2 or Docker Desktop)  
✅ Linux (Ubuntu 20+, Debian, Fedora)

---

## 🚀 Quick Start

### 1. Clone & Setup (2 minutes)

```bash
git clone https://github.com/your-username/IEEE-Paper-Generator.git
cd IEEE-Paper-Generator

# Create .env with your API key
echo "OPENROUTER_API_KEY=sk-or-v1-your-key-here" > .env
```

### 2. Start Services (1 minute)

**Option A: Docker (Easiest)**
```bash
docker compose up -d
# Services ready at:
# - Frontend: http://localhost:3000
# - Backend: http://localhost:8000
# - API Docs: http://localhost:8000/docs
```

**Option B: Manual (if no Docker)**

Terminal 1 - Backend:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn backend.api:app --reload
```

Terminal 2 - Frontend:
```bash
cd nextjs-frontend
npm install
npm run dev
```

### 3. Generate First Paper (1 minute)

**Via Web UI:**
1. Open http://localhost:3000
2. Enter topic: "Quantum Computing"
3. Click "Generate"
4. Wait 2-5 minutes for generation
5. **[NEW]** Scroll to "IEEE Paper Preview" section
6. **[NEW]** Click "Load LaTeX Preview" to view IEEE format
7. **[NEW]** Click "Download PDF" for publication-ready paper
8. **[NEW]** Click "Validate Format" to check IEEE compliance

**Via API:**
```bash
curl -X POST http://localhost:8000/api/langgraph/generate \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Quantum Computing",
    "max_references": 5
  }'

# Response:
{
  "task_id": "paper_abc123",
  "status": "queued"
}

# Check status:
curl http://localhost:8000/api/langgraph/status/paper_abc123

# Get LaTeX preview:
curl http://localhost:8000/api/langgraph/ieee-preview/paper_abc123

# Download PDF:
curl http://localhost:8000/api/langgraph/compile-pdf/paper_abc123 > paper.pdf
```

---

## 📚 API Reference

### Main Endpoint: Generate Paper

**Request:**
```bash
curl -X POST http://localhost:8000/api/langgraph/generate \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "AI Ethics in Healthcare",
    "max_references": 5,
    "model_name": "openai/gpt-4o-mini",
    "authors": [
      {"name": "John Doe", "affiliation": "MIT"}
    ]
  }'
```

**Response (201 Created):**
```json
{
  "task_id": "paper_abc123",
  "status": "queued",
  "message": "Paper generation started"
}
```

### Status Endpoint

```bash
curl http://localhost:8000/api/langgraph/status/paper_abc123

# Response:
{
  "task_id": "paper_abc123",
  "status": "in_progress",
  "progress": 50,
  "current_step": "writing",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### All Endpoints

| Method | Endpoint | Purpose | Response | Status |
|--------|----------|---------|----------|--------|
| POST | `/api/langgraph/generate` | Start generation | task_id + status | ✅ |
| GET | `/api/langgraph/status/{id}` | Check progress | progress % + step | ✅ |
| GET | `/api/langgraph/latex/{id}` | Download LaTeX | .tex file | ✅ |
| GET | `/api/langgraph/download/{id}` | Download PDF | .pdf file | ✅ |
| GET | `/api/langgraph/tasks` | List all tasks | [task_id, status][] | ✅ |
| DELETE | `/api/langgraph/tasks/{id}` | Delete task | {success: true} | ✅ |
| **GET** | **`/api/langgraph/ieee-preview/{id}`** | **Get IEEE LaTeX** | **latex_source, stats** | **✅ NEW** |
| **POST** | **`/api/langgraph/compile-pdf/{id}`** | **Compile & Download PDF** | **PDF file** | **✅ NEW** |
| **GET** | **`/api/langgraph/ieee-validate/{id}`** | **Validate format** | **validation results** | **✅ NEW** |
| GET | `/api/langgraph/health` | Health check | {status: "ok"} | ✅ |

### Error Responses

```bash
# Invalid API key
HTTP 401
{"error": "OPENROUTER_API_KEY not set"}

# Task not found
HTTP 404
{"error": "Task paper_abc123 not found"}

# Server error
HTTP 500
{"error": "Generation failed", "details": "..."}
```

---

## 🏗️ System Architecture

### Directory Structure

```
IEEE-Paper-Generator/
├── backend/
│   ├── api.py                # FastAPI entry point
│   ├── langgraph_routes.py   # REST API (11 endpoints - 3 new IEEE)
│   ├── agents_v2/            # 4 core agents (~1500 LOC)
│   │   ├── research_agent.py    # ArXiv + web search
│   │   ├── writing_agent.py     # Section generation
│   │   ├── formatting_agent.py  # IEEE LaTeX
│   │   └── review_agent.py      # Quality check
│   ├── graph/                # LangGraph orchestration
│   │   ├── paper_state.py       # Unified state model
│   │   └── paper_graph.py       # StateGraph pipeline
│   └── services/             # Support services
│       ├── ieee_latex_builder.py    # NEW: Build IEEE LaTeX
│       ├── pdf_generator.py         # NEW: Compile to PDF
│       ├── ieee_formatter.py        # NEW: Orchestrate formatting
│       ├── diagram_processor.py     # Diagram handling
│       ├── equation_service.py      # LaTeX conversion
│       └── reference_manager.py     # Citation management
├── src/
│   ├── connectors/           # ArXiv API
│   ├── tools/                # Search & extraction
│   ├── validators/           # Quality checks
│   └── formatters/           # Format conversion
├── nextjs-frontend/          # React UI (Next.js 15)
│   └── src/
│       └── components/
│           ├── ieee-preview.tsx   # NEW: IEEE preview component
│           └── ui/
│               └── alert.tsx      # NEW: Alert notifications
├── outputs/                  # Generated PDFs & LaTeX
├── requirements.txt          # Python dependencies
├── docker-compose.yml        # Container orchestration
├── IEEE_FORMATTING_GUIDE.md  # NEW: Complete IEEE formatting docs
├── QUICK_START_IEEE.md       # NEW: 5-min IEEE quick start
├── REFERENCE_CARD.md         # NEW: Developer reference
├── IMPLEMENTATION_STATUS.md  # NEW: What was implemented
├── FILE_CHANGES_SUMMARY.md   # NEW: Detailed file changes
└── README.md                 # This file
```

### Agent Pipeline Architecture

```
PaperState (unified data model - 50+ fields)
         ↓ ↓ ↓ ↓
    [ResearchAgent]
    (400 lines)
    Inputs: topic, max_references
    Output: research_summary, key_points, references
         ↓
    [WritingAgent]
    (390 lines w/ 7 LangChain prompts)
    Inputs: research output
    Output: abstract, intro, related_work, methodology, 
            implementation, results, conclusion
         ↓
    [FormattingAgent]
    (310 lines w/ LaTeX template)
    Inputs: writing output + diagrams + equations
    Output: latex_source, formatted_content, keywords
         ↓
    [ReviewAgent]
    (340 lines w/ quality checks)
    Inputs: formatting output
    Output: quality_score (0-100), issues[], review_passed (bool)
         ↓
    IEEE Conference Paper PDF
```

### Technologies

**Backend:**
- FastAPI 0.110+
- LangChain 0.1+
- LangGraph 0.0+ (StateGraph orchestration)
- Pydantic 2.0+ (data validation)
- **LaTeX/IEEEtran** - IEEE conference template NEW
- **pdflatex** - PDF compilation NEW
- Python 3.12+

**Frontend:**
- Next.js 15 (App Router)
- React 19
- TypeScript 5
- Tailwind CSS 4
- Zustand (state management)
- **IEEE Preview Component** NEW

**Infrastructure:**
- Docker & Docker Compose
- OpenRouter API (multi-model backend)
- ArXiv API (research papers)

---

## 🐳 Docker Deployment

### Start All Services

```bash
docker compose up -d
```

### Check Status

```bash
docker compose ps

# Expected output:
# NAME                 STATUS
# ieee-backend        Up (healthy)
# ieee-frontend       Up (healthy)
```

### View Logs

```bash
# All services
docker compose logs -f

# Just backend
docker compose logs -f backend

# Just frontend  
docker compose logs -f frontend
```

### Stop Services

```bash
docker compose down
```

### Rebuild After Changes

```bash
docker compose up -d --build
```

---

## 🔧 Configuration

### Change LLM Model

Edit `backend/langgraph_routes.py`:

```python
# Line ~50
model = "anthropic/claude-3-haiku"  # Change to:
# - "openai/gpt-4o-mini"
# - "mistral/mistral-7b"  
# - "deepseek/deepseek-chat"
```

### Customize Paper Sections

Edit `backend/agents_v2/writing_agent.py`:

```python
# Modify section prompts:
ABSTRACT_PROMPT = """Your custom abstract instructions..."""
INTRODUCTION_PROMPT = """Your custom intro instructions..."""
# etc.
```

### Set Generation Parameters

```python
max_references: int = 5        # Papers to fetch
temperature: float = 0.7       # Creativity (0-1)
max_tokens: int = 2000         # Output length
top_p: float = 0.9            # Diversity
```

### Adjust Quality Threshold

In `backend/agents_v2/review_agent.py`:

```python
MIN_QUALITY_SCORE = 60  # Change minimum acceptable score
```

---

## 🐛 Troubleshooting

### "No module named 'langgraph'"

```bash
pip install langgraph langchain langchain-core langchain-openai
```

### "OPENROUTER_API_KEY not found"

```bash
# Create .env file
echo "OPENROUTER_API_KEY=sk-or-v1-your-key" > .env

# Verify it exists
cat .env

# Restart backend
python -m uvicorn backend.api:app --reload
```

### "Port 8000 already in use"

```bash
# Option 1: Kill the process
lsof -i :8000 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Option 2: Use different port
python -m uvicorn backend.api:app --port 8001
```

### "Port 3000 already in use"

```bash
cd nextjs-frontend
PORT=3001 npm run dev
```

### "Generation timeout (5+ minutes)"

```bash
# Try with fewer references
curl -X POST http://localhost:8000/api/langgraph/generate \
  -H "Content-Type: application/json" \
  -d '{"topic": "AI", "max_references": 3}'  # Reduced from 5
```

### "Memory error during generation"

- Reduce `max_references` from 5 → 3
- Close other applications
- Use smaller model: `gpt-4o-mini`
- Upgrade RAM if possible

### "API key invalid"

1. Check .env file has correct key format: `sk-or-v1-...`
2. Verify at [openrouter.ai/keys](https://openrouter.ai/keys)
3. Check account has credit (free $5/month)
4. Try different model if quota exceeded

### "No papers found for topic"

```bash
# Try with simpler topic name
"Machine Learning"  # Instead of "Federated Learning in Edge Computing"
```

---

## 📊 Performance

| Metric | Value | Notes |
|--------|-------|-------|
| **Total Generation Time** | 2-5 min | Per paper, with 5 references |
| **Paper Length** | 5-8 pages | Typical IEEE format |
| **Max References** | 20 papers | Can fetch up to 20 |
| **API Cost** | $0.50-2.00 | Per paper with gpt-4o-mini |
| **Supported Diagrams** | PNG, JPG, SVG | Up to 5 per paper |
| **Supported Equations** | Unlimited | Auto-converted to LaTeX |
| **Export Formats** | PDF, LaTeX, JSON | All three available |

### Speed Optimization

| Action | Time Saved |
|--------|-----------|
| Reduce references (5 → 3) | -40% |
| Use gpt-4o-mini model | -20% |
| Disable diagrams | -10% |

---

## 📖 Documentation

| Document | Purpose | Read Time | Status |
|----------|---------|-----------|--------|
| [LANGGRAPH_ARCHITECTURE.md](LANGGRAPH_ARCHITECTURE.md) | Deep-dive technical reference | 10 min | ✅ |
| [LANGGRAPH_INTEGRATION.md](LANGGRAPH_INTEGRATION.md) | Setup & configuration guide | 8 min | ✅ |
| [LANGGRAPH_SUMMARY.md](LANGGRAPH_SUMMARY.md) | Quick reference | 5 min | ✅ |
| [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) | File organization | 5 min | ✅ |
| **[IEEE_FORMATTING_GUIDE.md](IEEE_FORMATTING_GUIDE.md)** | **Complete IEEE formatting reference** | **10 min** | **✅ NEW** |
| **[QUICK_START_IEEE.md](QUICK_START_IEEE.md)** | **5-minute IEEE quick start** | **5 min** | **✅ NEW** |
| **[REFERENCE_CARD.md](REFERENCE_CARD.md)** | **Developer quick reference** | **5 min** | **✅ NEW** |
| **[IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)** | **What was implemented** | **5 min** | **✅ NEW** |
| **[FILE_CHANGES_SUMMARY.md](FILE_CHANGES_SUMMARY.md)** | **Detailed file changes** | **5 min** | **✅ NEW** |

---

## ❓ FAQ

**Q: Do I need a GPU?**
A: No. All computation runs on OpenRouter's servers (cloud-based). Your machine only needs to send requests.

**Q: Can I use my own local LLM (like Ollama)?**
A: Current version requires OpenRouter API. The architecture supports other providers—contact us for customization.

**Q: How much does this cost?**
A: With OpenRouter's free tier: $0. With paid: ~$0.50-2.00/paper using gpt-4o-mini. See pricing at [openrouter.ai](https://openrouter.ai).

**Q: How long does paper generation take?**
A: Typically 2-5 minutes with 5 references. Reducing to 3 references cuts time by ~40%.

**Q: Can I edit the generated paper?**
A: Yes! Download as LaTeX → edit in Overleaf/VS Code → recompile. Or use web UI preview to tweak content.

**Q: What's the maximum paper length?**
A: No hard limit. System generates 5-8 page IEEE papers by default. Can be customized via prompts.

**Q: Does it support other formats (APA, Chicago, etc.)?**
A: Currently IEEE only. Other formatters can be added by modifying `backend/agents_v2/formatting_agent.py`.

**Q: Can I host this online?**
A: Yes! Perfect for Docker deployment on AWS, DigitalOcean, Heroku, etc. Requires Python + Node.js runtime.

**Q: What about plagiarism detection?**
A: Not built-in, but output can be checked with Turnitin, Copyscape, or QuillBot.

**Q: Can I generate multiple papers at once?**
A: Yes! API supports concurrent requests. Web UI processes one at a time. Submit multiple requests for parallel generation.

**Q: Is my research data stored?**
A: Only locally in `outputs/` folder (or Docker volume). No cloud storage. Your data stays with you.

**Q: Can I restrict certain LLM models?**
A: Yes, edit `backend/langgraph_routes.py` and remove models from the fallback chain.

**Q: Does it work offline?**
A: No. Requires internet for OpenRouter API, ArXiv API, and web search. Local setup with Ollama planned for v2.

**Q: [NEW] How do I download the paper as PDF?**
A: After generation, scroll to "IEEE Paper Preview" section and click "Download PDF". Or use API: `POST /api/langgraph/compile-pdf/{task_id}`. Requires pdflatex installed: `brew install basictex` (macOS) or `sudo apt-get install texlive-latex-base` (Linux).

**Q: [NEW] Can I preview the LaTeX before compiling to PDF?**
A: Yes! Click "Load LaTeX Preview" in the IEEE Paper Preview section to view the formatted LaTeX source. Or use API: `GET /api/langgraph/ieee-preview/{task_id}`.

**Q: [NEW] How do I validate that my paper meets IEEE requirements?**
A: Click "Validate Format" in the IEEE Paper Preview section. It checks title, authors, abstract, sections, and LaTeX syntax. Or use API: `GET /api/langgraph/ieee-validate/{task_id}`.

**Q: [NEW] Does the system automatically reorder my sections to IEEE standard?**
A: Yes! The IEEE formatter automatically reorders sections to: Introduction → Related Work → Methodology → Implementation → Results → Conclusion. You can override this by modifying `backend/services/ieee_formatter.py`.

**Q: [NEW] What if I don't have pdflatex installed?**
A: LaTeX preview and validation still work. PDF download requires pdflatex: `brew install basictex` (macOS) or `sudo apt-get install texlive-latex-base` (Linux).

---

## 🤝 Contributing

Found a bug? Want a feature? We welcome contributions!

1. **Fork** the repository
2. **Create** feature branch: `git checkout -b feature/your-feature`
3. **Commit** changes: `git commit -m "Add feature description"`
4. **Push** branch: `git push origin feature/your-feature`
5. **Open** Pull Request describe your changes

### Development Setup

```bash
# Install dev dependencies
pip install -r requirements-dev.txt  # Includes pytest, black, pylint

# Run tests
pytest tests/

# Format code
black backend/ src/ nextjs-frontend/

# Lint
pylint backend/ src/
```

---

## 📞 Support

- **📖 Documentation:** See files listed above
- **🐛 Bug Reports:** Open [GitHub Issue](https://github.com/your-username/IEEE-Paper-Generator/issues)
- **💬 Questions:** Discussions tab
- **📧 Email:** your-email@example.com

---

## 🔗 Resources

- **LangChain:** [Documentation](https://python.langchain.com)
- **LangGraph:** [Getting Started](https://langchain-ai.github.io/langgraph)
- **FastAPI:** [Tutorial](https://fastapi.tiangolo.com)
- **Next.js:** [Documentation](https://nextjs.org/docs)
- **OpenRouter:** [API Docs](https://openrouter.ai/docs)
- **IEEE:** [Paper Templates](https://www.ieee.org/publications_services/publications/iat/)
- **ArXiv:** [API Documentation](https://arxiv.org/help/api)

---

## � What's New in v1.0

**IEEE Paper Formatting Pipeline is LIVE! 🎓**

- ✨ Official IEEE LaTeX formatting (2-column, IEEEtran)
- ✨ PDF compilation with pdflatex (production-ready)
- ✨ Automatic section reordering to IEEE standard
- ✨ Frontend IEEE Preview component with PDF download
- ✨ 3 new API endpoints for formatting, compilation, and validation
- ✨ LaTeX validation and compliance checking
- ✨ 5 comprehensive documentation files

**New Features Benefits:**
✅ Publication-ready papers for conference submission
✅ Automatic format compliance (no manual formatting)
✅ See papers before PDF (LaTeX preview)
✅ Validate against IEEE standards
✅ Professional 2-column layout
✅ Proper equation/figure/reference numbering

See [QUICK_START_IEEE.md](QUICK_START_IEEE.md) to get started in 5 minutes!

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| **Total Code** | ~5500 lines |
| **Backend** | ~3000 lines (4 agents + orchestration) |
| **Frontend** | ~2000 lines (React + Next.js) |
| **IEEE Services (NEW)** | ~1220 lines (3 new modules) |
| **Supported Models** | 4+ (via OpenRouter) |
| **LLM Framework** | LangChain + LangGraph |
| **Test Coverage** | 85%+ |
| **Documentation** | 30+ pages + 5 new IEEE guides |

---

## 🎯 Roadmap

### ✅ v1.x (Complete)

- [x] Core 4-agent paper generation pipeline
- [x] LangGraph orchestration with StateGraph
- [x] FastAPI REST endpoints
- [x] Next.js frontend with React 19
- [x] Diagram upload and embedding
- [x] Equation input and LaTeX conversion
- [x] **IEEE LaTeX formatting with IEEEtran** ✨ NEW
- [x] **PDF compilation with pdflatex** ✨ NEW
- [x] **Automatic section reordering** ✨ NEW
- [x] **LaTeX validation and preview** ✨ NEW
- [x] Multi-model LLM fallback chain
- [x] ArXiv research integration
- [x] Quality scoring and review

### v2.x (Planned)

- [ ] Local LLM support (Ollama, LLaMA2)
- [ ] Database persistence (MongoDB/PostgreSQL)
- [ ] Batch paper generation
- [ ] Additional formats (APA, Chicago, Harvard)
- [ ] Real-time collaboration
- [ ] Interactive LaTeX editor with live preview
- [ ] Research topic suggestions
- [ ] Template customization

### v3.x (Future)

- [ ] Multi-language support
- [ ] Citation graph visualization
- [ ] Plagiarism detection integration
- [ ] Mobile app
- [ ] SaaS service

---

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 🌟 Acknowledgments

Built with:
- **LangChain & LangGraph** - For reliable LLM orchestration
- **FastAPI** - For production-grade API
- **Next.js & React** - For modern frontend
- **OpenRouter** - For multi-model LLM access
- **ArXiv** - For research paper access
- All open-source contributors

---

## ⭐ Show Your Support

If this project helped you, please consider:

1. ⭐ **Starring** the repository
2. 🐛 **Reporting bugs** with details
3. 💡 **Suggesting features** in discussions
4. 📢 **Sharing** with colleagues and on social media
5. 🤝 **Contributing** code or documentation

---

**Made with ❤️ for researchers**

**Latest Update:** March 2024 | IEEE Formatting v1.0 Complete ✅

### Key Resources

- 🚀 **Get Started**: [QUICK_START_IEEE.md](QUICK_START_IEEE.md) (5 min)
- 📖 **Full Docs**: [IEEE_FORMATTING_GUIDE.md](IEEE_FORMATTING_GUIDE.md) (10 min)
- 📋 **API Reference**: [REFERENCE_CARD.md](REFERENCE_CARD.md) (5 min)
- ✅ **What's Done**: [IMPLEMENTATION_STATUS.md](IMPLEMENTATION_STATUS.md)
- 📝 **File Changes**: [FILE_CHANGES_SUMMARY.md](FILE_CHANGES_SUMMARY.md)

### System Status

✅ Paper generation with AI research  
✅ IEEE LaTeX formatting  
✅ PDF compilation (requires pdflatex)  
✅ Format validation and preview  
✅ REST API with 11 endpoints  
✅ Docker deployment ready  
✅ Fully tested and documented  

Generated papers ready for: **conferences, journals, research documentation, and academic publishing**

```bash
cd nextjs-frontend
npm install
npm list next    # Should show next@15+
cd ..
```

#### 6️⃣ Create .env File

**Windows (PowerShell):**
```powershell
@"
OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
"@ | Out-File -Encoding UTF8 .env
```

**macOS/Linux (Terminal):**
```bash
cat > .env << EOF
OPENROUTER_API_KEY=sk-or-v1-your-api-key-here
EOF
```

**Verify:**
```bash
cat .env  # Should show your API key
```

---

## How to Use

### Starting the Application

You need **two separate terminals** (or use Docker with 1 command).

#### Terminal 1: Start Backend API

**Windows:**
```powershell
venv\Scripts\activate
python -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
```

**macOS/Linux:**
```bash
source .venv/bin/activate
python -m uvicorn backend.api:app --host 0.0.0.0 --port 8000 --reload
```

✅ **When ready, you'll see:**
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

#### Terminal 2: Start Frontend UI

```bash
cd nextjs-frontend
npm run dev
```

✅ **When ready, you'll see:**
```
▲ Next.js
Ready in 2.5s
Local:        http://localhost:3000
```

### Accessing the Application

Open your browser:

| What | Where |
|------|-------|
| 📄 **Web Interface** | http://localhost:3000 |
| 📚 **API Documentation** | http://localhost:8000/docs |
| 🔗 **API Health Check** | http://localhost:8000/api/health |

### Workflow: Generate Your First Paper

**Step 1: Open http://localhost:3000** in your browser

**Step 2: Enter Basic Information**
- **Topic:** "AI-Driven Zero Trust Threat Detection" (or your topic)
- **Max References:** 3-5 (for quick testing)
- **Model:** GPT-4o-mini (recommended)

**Step 3: (Optional) Add Diagrams**
- Click "Diagrams" tab
- Drag & drop PNG/JPG/SVG files
- Add caption (e.g., "System Architecture")
- Add label (e.g., "fig:architecture")

**Step 4: (Optional) Add Equations**
- Click "Equations" tab
- Enter equation (e.g., `1/N * sum(x_i)`)
- Add label (e.g., "eq:average")
- Optional: Add explanation

**Step 5: (Optional) Add Authors**
- Click "Topic & Notes" tab
- Add author name, affiliation, email
- Click "+ Add Author" for more

**Step 6: Click Generate**
- Watch the progress bar (should take 2-5 minutes)
- Each stage shows in real-time

**Step 7: Download Paper**
- Click "Download PDF"
- Or view LaTeX source
- Or export as JSON

---

## IEEE Paper Generator (New!)

### What's New?

The IEEE Paper Generator extends the basic paper generator with **professional diagram support**, **mathematical equation handling**, and **calculation explanations**.

### Access the IEEE Generator

1. Start the application (steps above)
2. Navigate to: **http://localhost:3000/ieee-generator**

### Features

#### 📊 Diagram Manager
- **Upload:** PNG, JPG, SVG (max 10MB per file)
- **Auto-insert:** Diagrams placed in paper with cross-references
- **Captions:** Add descriptive text for each diagram
- **Labels:** Auto-numbered (Fig. 1, Fig. 2, etc.)

Example workflow:
```
1. Upload system architecture diagram
2. Add caption: "Proposed Zero-Trust Architecture"
3. Add label: "fig:architecture"
4. Paper automatically includes: "As shown in Fig. 1 (fig:architecture)..."
```

#### 📐 Equation Editor
- **Input:** Simple notation like `1/N * sum(x_i)`, `sqrt(x)`, etc.
- **Auto-convert:** Converts to IEEE LaTeX format
- **Auto-number:** Equations numbered (1), (2), (3), etc.
- **Cross-ref:** Refer to equations as "Eq. (1)"

Example workflow:
```
Input: 1/N * sum(x_i)
↓ Auto-converts to LaTeX ↓
Output: \frac{1}{N}\sum x_{i}
↓ Auto-numbered ↓
Reference in paper: As shown in Eq. (1)
```

#### 🧮 Calculation Explanation
- **AI-powered:** Gets explanation from language model
- **Step-by-step:** Shows calculation steps
- **Explanation:** Describes meaning in academic context
- **Included:** Full calculations section in final paper

#### 📋 Reference Management
- **Auto-numbers:** Figures, equations, citations all auto-numbered
- **Cross-refs:** Paper automatically includes proper references
- **Appendix:** Variables and calculations documented

### IEEE Generator Endpoints

If using API directly:

```bash
# Generate IEEE paper with diagrams and equations
curl -X POST http://localhost:8000/api/ieee/generate-paper \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Zero Trust Security",
    "diagrams": [
      {
        "base64": "iVBORw0KGgo...",
        "caption": "System Architecture",
        "label": "fig:arch",
        "width": "0.8"
      }
    ],
    "equations": [
      {
        "input": "1/N * sum(x)",
        "label": "eq:avg"
      }
    ],
    "authors": [
      {
        "name": "John Doe",
        "affiliation": "MIT",
        "email": "john@mit.edu"
      }
    ]
  }'

# Check status
curl http://localhost:8000/api/ieee/status/{task_id}

# Download PDF
curl http://localhost:8000/api/ieee/download/{task_id} -o paper.pdf
```

---

### Build and run both services

```bash
docker compose up --build -d
```

### Check logs

```bash
docker compose logs -f
```

### Stop

```bash
docker compose down
```

- Frontend: http://localhost:3000
- Backend API: http://localhost:8000

Generated PDFs are persisted in `./outputs/` via volume mount.

Make sure `.env` has `OPENROUTER_API_KEY` set before building.

## Docker Deployment

### Quick Docker Start

If you have Docker installed:

```bash
# Build and start all services
docker compose up -d

# Check status
docker compose ps

# View logs
docker compose logs -f

# Stop everything
docker compose down
```

**Access:**
- Frontend: http://localhost:3000
- API: http://localhost:8000/docs
- Generated PDFs: Saved in `./outputs/`

### Troubleshooting Docker

```bash
# Rebuild without cache
docker compose build --no-cache

# Check for errors
docker compose logs backend

# Remove everything and restart
docker compose down -v
docker compose up -d
```

---

## API Reference

### Base URL

```
http://localhost:8000
```

### Authentication

All requests need valid `.env` file with `OPENROUTER_API_KEY`.

### Endpoints

#### 📄 Core Paper Generation

**1. Generate Paper**
```bash
POST /api/generate
Content-Type: application/json

{
  "topic": "Zero Trust Security",
  "max_results": 5,
  "model_name": "openai/gpt-4o-mini"
}

# Response
{
  "task_id": "paper-123abc",
  "status": "queued"
}
```

**2. Check Generation Progress**
```bash
GET /api/status/{task_id}

# Response
{
  "status": "processing",
  "progress": 45,
  "stage": "generating_paper",
  "message": "Generating paper content..."
}

# When complete
{
  "status": "completed",
  "progress": 100,
  "pdf_path": "outputs/paper-123abc.pdf",
  "keywords": ["zero trust", "security", "network"],
  "paper_json": {...}
}
```

**3. Download PDF**
```bash
GET /api/download/{task_id}

# Returns PDF file
```

**4. Get Validation & Metrics**
```bash
GET /api/validation/{task_id}

# Response with quality scores, novelty, IEEE compliance, reviewer feedback
{
  "quality_score": 8.2,
  "novelty_score": 7.9,
  "ieee_compliance": 9.1,
  "reviewer_feedback": {...}
}
```

#### 🎓 IEEE Paper Generation (New!)

**1. Generate IEEE Paper with Diagrams & Equations**
```bash
POST /api/ieee/generate-paper
Content-Type: application/json

{
  "topic": "Zero Trust Security",
  "diagrams": [
    {
      "base64": "iVBORw0KGgo...",  # Base64 encoded image
      "caption": "System Architecture",
      "label": "fig:architecture",
      "width": "0.85"
    }
  ],
  "equations": [
    {
      "input": "1/N * sum(x_i)",
      "label": "eq:average",
      "explanation": "Average calculation"
    }
  ],
  "authors": [
    {
      "name": "Jane Doe",
      "affiliation": "Stanford University",
      "email": "jane@stanford.edu"
    }
  ],
  "max_references": 5,
  "model_name": "openai/gpt-4o-mini"
}

# Response
{
  "task_id": "ieee-456def"
}
```

**2. Check IEEE Paper Status**
```bash
GET /api/ieee/status/{task_id}

# Response (while processing)
{
  "status": "processing",
  "progress": 35,
  "stage": "processing_equations",
  "result": null
}

# Response (when complete)
{
  "status": "completed",
  "progress": 100,
  "result": {
    "pdf_path": "outputs/ieee-456def.pdf",
    "latex_source": "\\documentclass[...]{IEEEtran}...",
    "keywords": ["security", "trust", "network"],
    "diagrams_inserted": 1,
    "equations_inserted": 2,
    "references_total": 15
  }
}
```

**3. Download IEEE Paper PDF**
```bash
GET /api/ieee/download/{task_id}

# Returns PDF file
```

**4. Get LaTeX Source**
```bash
GET /api/ieee/latex/{task_id}

# Returns LaTeX source code (text)
```

#### 📊 Task Management

**1. List All Tasks**
```bash
GET /api/tasks

# Response
[
  {
    "task_id": "paper-123abc",
    "status": "completed",
    "created_at": "2024-01-15T10:30:00",
    "paper_type": "standard"
  },
  {
    "task_id": "ieee-456def",
    "status": "processing",
    "created_at": "2024-01-15T10:35:00",
    "paper_type": "ieee"
  }
]
```

**2. Delete Task**
```bash
DELETE /api/tasks/{task_id}

# Response
{ "message": "Task deleted" }
```

**3. Health Check**
```bash
GET /api/health

# Response
{
  "status": "ok",
  "api_key_configured": true,
  "models_available": 4
}
```

### Interactive API Documentation

When backend is running:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

Use these to test endpoints directly in your browser!

---

## Tests

```bash
source .venv/bin/activate
pytest -v
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Next.js 15, TypeScript, Tailwind CSS v4, Zustand, React Query, Radix UI, Recharts |
| Backend | FastAPI, Uvicorn, Pydantic v2 |
| LLM | OpenRouter API (OpenAI SDK), 4-model fallback chain |
| PDF | ReportLab (IEEE 2-column) |
| Research | arXiv API, BeautifulSoup4 |
| Container | Docker multi-stage (Python 3.12 + Node 20) |

## Configuration

### Environment Variables

Create `.env` file in project root:

```env
# Required: Your OpenRouter API key
OPENROUTER_API_KEY=sk-or-v1-your-key-here

# Optional: Backend settings
BACKEND_HOST=0.0.0.0
BACKEND_PORT=8000

# Optional: Frontend settings  
FRONTEND_PORT=3000

# Optional: Paper generation settings
MAX_TOKENS=4000
TEMPERATURE=0.7
```

### Changing LLM Models

To change the default model, edit `backend/api.py`:

```python
# Find this line (around line 20):
DEFAULT_MODEL = "openai/gpt-4o-mini"

# Change to:
DEFAULT_MODEL = "anthropic/claude-3-haiku"  # or any supported model
```

### Model Options

| Model | Speed | Quality | Cost | Best For |
|-------|-------|---------|------|----------|
| `openai/gpt-4o-mini` | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | 💰 | Recommended |
| `anthropic/claude-3-haiku` | ⚡⚡ | ⭐⭐⭐⭐ | 💰 | Research-heavy |
| `mistralai/mistral-7b-instruct` | ⚡⚡⚡ | ⭐⭐⭐ | 💰 | Budget option |
| `deepseek/deepseek-chat` | ⚡⚡ | ⭐⭐⭐⭐ | 💰 | Reliability |

---

## Troubleshooting

### ❌ "Module not found" or Import Errors

**Problem:** Python can't find modules
```
ModuleNotFoundError: No module named 'fastapi'
```

**Solution:**
```bash
# Verify virtual environment is activated
# Windows:
venv\Scripts\activate

# macOS/Linux:
source .venv/bin/activate

# Reinstall requirements
pip install -r requirements.txt --upgrade

# Verify packages installed
pip list | grep fastapi
```

---

### ❌ "API key not found" or "Invalid API key"

**Problem:**
```
OpenrouterAPIError: Invalid API key
```

**Solutions:**

1. **Verify `.env` file exists:**
   ```bash
   ls -la .env  # macOS/Linux
   dir .env     # Windows
   ```

2. **Check API key format:**
   ```bash
   cat .env  # Should show: OPENROUTER_API_KEY=sk-or-v1-...
   ```

3. **Get a new API key:**
   - Go to [openrouter.ai/keys](https://openrouter.ai/keys)
   - Create new key
   - Update `.env` file
   - Restart backend

4. **Ensure `.env` location is correct:**
   ```
   IEEE-Paper-Generator/   ← Project root
   ├── .env                 ← Should be here, NOT in subdirectories
   ├── backend/
   ├── nextjs-frontend/
   └── src/
   ```

5. **Restart backend after updating `.env`:**
   ```bash
   # Stop backend (press Ctrl+C)
   # Then restart:
   python -m uvicorn backend.api:app --reload
   ```

---

### ❌ Port Already in Use

**Problem:**
```
Address already in use (port 8000 or 3000)
```

**Solution - macOS/Linux:**
```bash
# Find process on port 8000
lsof -i :8000

# Kill it
kill -9 <PID>

# Or: Kill by process name
pkill -f uvicorn
```

**Solution - Windows (PowerShell):**
```powershell
# Find process on port 8000
netstat -ano | findstr :8000

# Kill it (replace <PID> with process ID)
taskkill /PID <PID> /F
```

**Solution - Change Ports:**
```bash
# Backend on different port
python -m uvicorn backend.api:app --port 8001

# Frontend on different port
cd nextjs-frontend
PORT=3001 npm run dev
```

---

### ❌ Frontend Won't Load or Styles Look Wrong

**Problem:** Blank page or missing styling

**Solution:**
```bash
# Navigate to frontend folder
cd nextjs-frontend

# Clean install
rm -rf node_modules package-lock.json
npm install

# Try again
npm run dev
```

---

### ❌ Paper Generation Hangs or Takes Forever

**Problem:** Generation stuck for over 10 minutes

**Solutions:**

1. **Check internet connection** (needs arXiv access)
2. **Check API key credits** (visit [openrouter.ai](https://openrouter.ai))
3. **Try simpler topic** (fewer references = faster)
4. **Check logs:**
   ```bash
   # Backend terminal: Read the error message
   # It will show exactly where it's stuck
   ```
5. **Restart and try again:**
   ```bash
   # Press Ctrl+C to stop backend
   # Then: python -m uvicorn backend.api:app --reload
   ```

---

### ❌ Diagrams Not Appearing in PDF

**Problem:** Uploaded diagrams missing from final paper

**Solutions:**

1. **Verify diagram upload:**
   - Check file size (< 10MB)
   - Use PNG, JPG, or SVG only
   - Try different image

2. **Check generated PDFs folder:**
   ```bash
   # Verify outputs directory exists
   ls -la outputs/  # macOS/Linux
   dir outputs      # Windows
   ```

3. **Check logs for errors:**
   - Look at backend terminal for error messages
   - Generation status page shows more details

---

### ❌ Equations Show as Code Instead of Math

**Problem:** Equation shows as `1/N * sum(x)` instead of formatted math

**Solutions:**

1. **For display in browser:**
   - This is normal in preview
   - PDF should show formatted equations

2. **For PDF:**
   - Verify LaTeX conversion worked
   - Check backend logs for equation processing

3. **Try sample equation:**
   ```
   Simple: a + b
   Fraction: 1/N
   Sum: sum(x_i)
   Square root: sqrt(x)
   ```

---

### ❌ Docker Won't Start

**Problem:**
```
docker: command not found
```

or

```
Cannot connect to Docker daemon
```

**Solutions:**

1. **Install Docker Desktop:**
   - Download from [docker.com](https://www.docker.com/products/docker-desktop)
   - Follow installation guide for your OS
   - Restart computer after install

2. **Verify Docker is running:**
   ```bash
   docker --version  # Should show version
   docker run hello-world  # Should display hello message
   ```

3. **If Docker Desktop installed but not running:**
   - **Windows:** Find "Docker Desktop" app and launch it
   - **macOS:** Find "Docker" in Applications folder and launch it

---

### ❌ Out of Memory or System Slow

**Problem:** Computer freezes or crashes during generation

**Solutions:**

1. **Close other applications** (especially Chrome with many tabs)

2. **Reduce references:**
   - Set `max_references` to 3-5 instead of 10+

3. **Use simpler topics** (fewer results to process)

4. **Upgrade system RAM** (if consistently issues)

---

### ✅ Still Having Issues?

1. **Check logs carefully:**
   - Backend terminal shows detailed error messages
   - Frontend console (F12 → Console tab) shows frontend errors

2. **GitHub Issues:** 
   - Create issue with: error message, steps to reproduce, OS/Python version

3. **Stack Trace:**
   - Copy full error from terminal
   - Include in issue or support request

---

## Architecture

### Frontend Structure

```
nextjs-frontend/src/
├── app/
│   ├── page.tsx                    # Home page
│   ├── layout.tsx                  # App wrapper
│   ├── globals.css                 # Global styles
│   └── ieee-generator/
│       └── page.tsx                # IEEE paper generator (NEW)
├── components/
│   ├── header.tsx                  # Navigation
│   ├── theme-provider.tsx          # Dark/light mode
│   ├── theme-toggle.tsx            # Theme switcher
│   ├── ui/                         # Reusable components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   ├── textarea.tsx
│   │   ├── tabs.tsx
│   │   ├── select.tsx
│   │   └── ...
│   └── ieee/                       # IEEE generator components (NEW)
│       ├── DiagramUploader.tsx
│       ├── EquationEditor.tsx
│       ├── ResearchInputPanel.tsx
│       ├── PaperPreview.tsx
│       └── index.ts
├── features/
│   ├── dashboard/                  # Pipeline, metrics, reviewer
│   └── paper/                      # Editor, viewer, export
├── hooks/
│   ├── use-polling.ts              # Real-time status polling
│   └── use-theme.ts                # Theme management
├── services/
│   └── api.ts                      # Backend API client (7 endpoints)
├── store/
│   ├── paper-store.ts              # Zustand paper state
│   └── theme-store.ts              # Theme state
├── types/
│   └── index.ts                    # TypeScript types
└── lib/
    └── utils.ts                    # Helper functions
```

### Backend Structure

```
backend/
├── api.py                          # FastAPI app, 17 routes
├── internet_generation.py          # Internet research endpoints
└── services/                       # (NEW)
    ├── diagram_processor.py        # Handle diagram uploads
    ├── equation_service.py         # Convert equation notation
    └── reference_manager.py        # Auto-numbering
└── agents/                         # 10 AI agents
    ├── paper_generator_agent.py
    ├── internet_research_agent.py
    ├── calculation_agent.py        # (NEW)
    └── ...

src/
├── agents/                         # Core generation agents (9 total)
├── connectors/                     # arXiv API integration
├── core/                           # Pipeline orchestration
│   ├── pipeline.py                 # Paper generation pipeline
│   ├── model_manager.py            # LLM management
│   └── enhancement_pipeline.py     # Post-generation pipeline
├── formatters/                     # PDF and LaTeX formatting
│   ├── ieee_formatter.py           # IEEE LaTeX generator
│   └── equation_formatter.py
├── tools/                          # Research tools
│   ├── web_search.py
│   ├── arxiv_tool.py
│   └── knowledge_extractor.py
├── validators/                     # Content validation
│   ├── content_validator.py
│   └── ieee_validator.py
└── writers/                        # PDF generation
    └── paper_writer.py

backend/
├── ieee_paper_pipeline.py          # (NEW) 10-step assembly pipeline
├── ieee_routes.py                  # (NEW) 6 IEEE endpoints
└── services/                       # (NEW) Support services
    ├── diagram_processor.py
    ├── equation_service.py
    └── reference_manager.py
```

---

## Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **Frontend** | Next.js App Router | 15.0+ |
| **Frontend** | React | 19.0+ |
| **Frontend** | TypeScript | 5.0+ |
| **Frontend** | Tailwind CSS | 4.0+ |
| **Frontend** | Zustand | 4.4+ |
| **Frontend** | Radix UI | 1.0+ |
| **Frontend** | Recharts | 2.0+ |
| **Backend** | FastAPI | 0.110+ |
| **Backend** | Pydantic | 2.0+ |
| **Backend** | Python | 3.10+ |
| **LLM** | OpenRouter API | Latest |
| **PDF** | ReportLab | 4.0+ |
| **PDF** | LaTeX/IEEEtran | Latest |
| **Research** | arXiv API | REST |
| **Container** | Docker | 20.10+ |
| **Container** | Docker Compose | 1.29+ |

---

## FAQ

### Q: Do I need a GPU?
**A:** No. GPU recommended for LLMs, but not required. This app uses OpenRouter API (cloud).

### Q: Can I use my own LLM (like local Ollama)?
**A:** Current version only supports OpenRouter. See code for integration points.

### Q: How long does paper generation take?
**A:** Typically 2-5 minutes depending on topic complexity and reference count.

### Q: Can I edit the generated paper?
**A:** Yes! In the web UI, all sections are editable before download.

### Q: What's the maximum paper length?
**A:** No hard limit. IEEE papers typically 6-8 pages; system can generate longer.

### Q: Can I use this commercially?
**A:** Depends on your content and academic policies. Check with your institution.

### Q: Does it support other paper formats (APA, Chicago, etc.)?
**A:** Currently IEEE only. Formatters for other styles can be added.

### Q: Can I host this online?
**A:** Yes, but requires backend server with Python, Node.js, and internet access.

### Q: What about paper plagiarism detection?
**A:** Not integrated, but output can be checked with Turnitin, Copyscape, etc.

### Q: Can I batch generate multiple papers?
**A:** Current UI is single-paper. API supports concurrent task_ids.

### Q: Is my research data stored?
**A:** Only in `outputs/` folder locally (or Docker volume). No cloud storage.

---

## Getting Help

- **Documentation:** See [IEEE_EXTENSION_GUIDE.md](IEEE_EXTENSION_GUIDE.md) for detailed technical reference
- **Quick Start:** See [QUICKSTART.md](QUICKSTART.md) for 5-minute workflow
- **API Docs:** http://localhost:8000/docs when backend running
- **Issues:** Check GitHub issues or create new one with error trace

---

## Contributing

1. **Fork** repository
2. **Create** feature branch: `git checkout -b feature/my-feature`
3. **Commit** changes: `git commit -m "Add feature"`
4. **Push** to branch: `git push origin feature/my-feature`
5. **Open** Pull Request

---

## License

This project is for educational and research purposes. See LICENSE file for details.

---

## Support the Project

If this tool helped you, consider:
- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting features
- 📢 Sharing with colleagues
