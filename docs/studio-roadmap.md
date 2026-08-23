# Breedables studio roadmap

Date: 2026-08-23

Goal: grow from an empty scaffold into a **living, linked, daily-improving** studio knowledge base — tool registry, readable wiki, AI-assisted research, and Slack as the interface.

## Architecture split

| Layer | Owner | Role |
|-------|-------|------|
| **Facts** | Python Librarian | URLs, licenses, HTTP checks, dedupe, gaps, discovery queue |
| **Synthesis** | ChatGPT / Claude | Comparisons, license interpretation, recommendations, report writing |
| **Interface** | Slack | `/breedtool`, `/breedgaps`, future Canvas wiki |
| **Published docs** | GitHub + static wiki | Human-readable specs, links, decisions |
| **IDE context** | MCP RAG (optional) | Cursor/Claude search over repo docs |

The Librarian must never decide commercial safety from one license field alone. Discovery is not approval.

---

## Phase 0 — Baseline survey & registry (done)

**Status:** Complete on `feature/studio-librarian-v1`

**Deliverables:**
- [Phase 0 toolbox survey](research/phase-0-survey.md) (wiki summary; [full report on GitHub](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/feature/studio-librarian-v1/research/reports/2026-08-23-open-source-toolbox-survey.md))
- [Breedables Studio Librarian](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/tools/librarian) — SQLite registry, CLI, Slack Bolt (Socket Mode)
- Curated seed: Blender, Material Maker, Ucupaint, TripoSR, RetopoFlow, Poly Haven, ambientCG
- Live Slack commands: `/breedstatus`, `/breedtool`, `/breedgaps`

**Studio OSS (in use):**
| Project | Role | Link |
|---------|------|------|
| **breedables-studio-librarian** | Custom tool registry + Slack lookup | `tools/librarian/` |
| **slack-bolt** | Slack app framework (Socket Mode) | https://github.com/slackapi/bolt-python |
| **python-dotenv** | Local `.env` loading | https://github.com/theskumar/python-dotenv |
| **httpx** | Link health + GitHub metadata | https://github.com/encode/httpx |

---

## Phase 1 — Readable wiki from Git (in progress)

**Status:** MkDocs Material configured; 17 tool/candidate pages, experiments, SL baseline; GitHub Pages workflow added.

**Deliverables:**
- MkDocs site under `docs/` generated from markdown in this repo
- Phase 0 survey split into per-tool pages under `docs/production/tools/`
- GitHub Pages via `.github/workflows/docs.yml` → `gh-pages` branch

**Run locally:**

```powershell
pip install -r requirements-docs.txt
mkdocs serve
```

**Live URL (after deploy):** https://ifartrainbowsgames-sketch.github.io/breedables-lab/

**Recommended OSS:**
| Project | Role | License | Link |
|---------|------|---------|------|
| **MkDocs** | Static site generator (Python) | BSD-2-Clause | https://github.com/mkdocs/mkdocs |
| **Material for MkDocs** | Search, nav, dark mode, code blocks | MIT | https://github.com/squidfunk/mkdocs-material |

**Alternative (if non-devs need a GUI wiki):**
| Project | Role | License | Link |
|---------|------|---------|------|
| **Wiki.js** | Git two-way sync, pretty UI | AGPL-3.0 | https://github.com/requarks/wiki |
| **BookStack** | Shelf/book/chapter structure, easy editing | MIT | https://github.com/BookStackApp/BookStack |

**Daily loop (manual → scripted):**
1. Librarian `gaps` → pick top item
2. AI writes structured markdown report
3. Commit to `docs/` or `research/reports/`
4. MkDocs rebuild → published wiki

---

## Phase 2 — Research queue & daily automation

**Goal:** `/breedgaps` becomes an **AI to-do list**; links stay fresh without manual runs.

**Deliverables:**
- `research-queue` CLI command (export gaps + discovered items as JSON/markdown)
- Report template: `research/reports/TEMPLATE-tool-review.md`
- Windows Task Scheduler (or cron) for scheduled `check`, `discover-github`, `ingest-feed`
- Weekly Slack post: gap summary + link failures

**Recommended OSS:**
| Project | Role | License | Link |
|---------|------|---------|------|
| **linkchecker** | Deep scheduled link crawls (supplement Librarian HTTP checks) | GPL-2.0+ | https://github.com/linkchecker/linkchecker |
| **Breedables webscreen** | Go CLI: chromedp screening + SearXNG search → `research/discoveries/` | MIT (scaffold) | `tools/webscreen/` · [wiki](production/tools/web-research-stack.md) |
| **lychee** | CI link checks on `docs/**/*.md` | MIT | `.github/workflows/wiki-links.yml` |
| **trafilatura** | Post-screen HTML → markdown extract | Apache-2.0 | `python -m librarian.cli extract` |
| **SearXNG** | Self-hosted meta-search JSON API | AGPL-3.0 | https://github.com/searxng/searxng |

**Librarian V1.1 (build in-repo):**
1. Structured research-request queue for ChatGPT
2. Scheduled link/version checks
3. GitHub release-watch subscriptions
4. Weekly compact change report

**Ideas to borrow (optional install):**
| Project | Borrow | Link |
|---------|--------|------|
| **DataHub** / **OpenMetadata** | Gap queues, ownership, workflow status | https://github.com/datahub-project/datahub · https://github.com/open-metadata/OpenMetadata |
| **Zotero** | Curated paper/library export → ingest | https://www.zotero.org/ |

---

## Phase 3 — AI search in Cursor & IDE

**Goal:** Ask “what’s our RetopoFlow license status?” inside Cursor from **your** docs, not the open web.

**Deliverables:**
- MCP server indexing `breedables-lab` markdown + research reports
- Cursor rule or skill: “check Librarian gaps before recommending tools”

**Recommended OSS:**
| Project | Role | License | Link |
|---------|------|---------|------|
| **self-docs** | Doc RAG pipeline, MCP semantic search | Apache-2.0 | https://github.com/AdamRussak/self-doc |
| **OmniDocs-RAG** | Index GitHub repos + markdown, MCP tools | Check repo | https://github.com/ElvinBayramov/OmniDocs-RAG |
| **OpenDocuments** | Self-hosted RAG over GitHub, files, web (cited answers) | Check repo | https://github.com/joungminsung/OpenDocuments |

**Alternative (markdown-folder RAG engine):**
| Project | Role | Link |
|---------|------|------|
| **cmw-rag** | MkDocs/markdown folder indexing, incremental reindex | https://github.com/arterm-sedov/cmw-rag |

---

## Phase 4 — Academy & paper research

**Goal:** Track learning resources, PDFs, and license notes for the studio academy — not just GitHub tools.

**Deliverables:**
- `research/licenses/` entries linked from tool pages
- YouTube URL registry in Librarian (V1.1)
- Experiment evidence records (E01–E05 from Phase 0 survey)

**Recommended OSS:**
| Project | Role | License | Link |
|---------|------|---------|------|
| **ResearchShelf** | Self-hosted paper library, DOI fetch, FTS, Python 3.11+ | AGPL-3.0 | https://pypi.org/project/researchshelf/ |
| **GROBID** | PDF metadata & reference extraction (pairs with ResearchShelf) | Apache-2.0 | https://github.com/kermitt2/grobid |

**Librarian V1.1 (build in-repo):**
5. YouTube resource registry and duplicate detection
6. Experiment evidence + benchmark records
7. Asset provenance records

---

## Phase 5 — Slack living wiki

**Goal:** Approved research surfaces in Slack as a **browsable wiki**, not only slash-command replies.

**Deliverables:**
- Slack Canvas sync for approved tool summaries (review gate before publish)
- Channel `#breedables-knowledge` as the public face of the registry

**Recommended OSS:**
| Project | Role | License | Link |
|---------|------|---------|------|
| **Beever Atlas** | Slack → structured wiki + knowledge graph + MCP for agents | Apache-2.0 | https://github.com/Beever-AI/beever-atlas |
| **Outline** | Notion-like team wiki, Slack integration | BSL-1.1 | https://github.com/outline/outline |

**Tradeoff:** Beever Atlas is the closest match to “Slack chat becomes wiki daily” but needs Docker (Neo4j, Weaviate). Lighter path: **Librarian → markdown → MkDocs** plus optional Canvas sync in V1.1.

**Librarian V1.1 (build in-repo):**
8. Slack Canvas sync with review/approval gates

---

## Phase 6 — Production catalog & backstage (later)

**Goal:** When the studio grows, treat breedables components (scripts, assets, releases) like a **software catalog**.

**Recommended OSS (evaluate when needed):**
| Project | Role | License | Link |
|---------|------|---------|------|
| **Backstage** | Developer portal, software catalog, docs plugin | Apache-2.0 | https://github.com/backstage/backstage |

Only adopt if custom Librarian + MkDocs becomes too small for multi-team scale.

---

## Daily improvement loop (all phases)

```
Morning   → Python: check links, discover feeds/repos, export research-queue
Midday    → AI: deep research on top gaps, write markdown report
Afternoon → Human: approve status changes in Librarian
Evening   → Git commit docs → MkDocs publish → optional Slack summary
```

Over time: `/breedgaps` shrinks, `docs/` fills with linked pages, Cursor answers from your corpus.

---

## Phase summary

| Phase | Focus | Primary OSS |
|-------|-------|-------------|
| **0** | Registry + Slack lookup | Librarian, slack-bolt *(done)* |
| **1** | Readable wiki | MkDocs Material |
| **2** | Research queue + schedules | linkchecker + Librarian V1.1 |
| **3** | IDE / Cursor search | self-docs or OmniDocs-RAG (MCP) |
| **4** | Papers & academy | ResearchShelf, GROBID |
| **5** | Slack living wiki | Beever Atlas or Outline + Canvas sync |
| **6** | Full studio catalog | Backstage *(if needed)* |

---

## References

- [Librarian README](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/feature/studio-librarian-v1/tools/librarian/README.md)
- [Phase 0 survey](research/phase-0-survey.md)
- [Research flow](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/feature/studio-librarian-v1/research/README.md)
