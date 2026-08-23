---
title: "System build summary — what we built, how it works, where we're going"
section: meta
type: meta
---
# System build summary — what we built, how it works, where we're going

**Date:** 2026-08-23  
**Status:** Active on `feature/studio-librarian-v1` (local; not necessarily committed)  
**Audience:** Studio maintainers, future you, AI agents picking up the project

---

## One-sentence goal

**Teach professional creature/3D production (paid and free routes), step-by-step with real training links and artifacts — then deliver Second Life breedables — with git wiki as source of truth and a daily loop that improves content, not meta-infrastructure.**

→ Full spec: [Academy mission](../academy/index.md)

---

## Course correction (2026-08-23)

We are **not** abandoning the Academy. We **stopped** useless meta-docs and **started** the real product:

| Before | After |
|--------|-------|
| Registry labels on “lesson” pages | [Professional workflow](../pipeline.md) + [software packages](../research/software-database.md) |
| “Learn Blender” with no URLs | [Software page standard](software-page-standard.md) — verified training required |
| Invented lesson order | [Pipeline stages](../pipeline.md) mirroring Gnomon/industry |
| OSS-only blind spot | [Paid vs free matrix](../research/paid-vs-free-matrix.md) — three routes |

**Do not build:** new RAG bots, dashboards, crawlers. **Do build:** populate package cards, complete courses, lesson PASS criteria, Reference Creature evidence.

---

## What we built

### 1. Academy wiki (MkDocs) — the learner product

| Piece | Location | What it does |
|-------|----------|--------------|
| **Plain-English entry** | [start-here.md](../academy/index.md) | Explains the wiki without A01/B07 codes |
| **10 Blender lessons** | [software/blender/](../modeling/blender/index.md) | Install → model → texture → rig → export to SL |
| **5 studio labs** | [tracks/](../texturing/projects/organic-pbr-material.md) | Breedables proof projects with `training/` evidence |
| **Tutorial arsenal** | [tutorials.md](../academy/index.md) | Curated videos by pipeline stage |
| **Market research** | [breedables-market-study.md](../research/breedables-market-study.md) | SL breedables context for the studio |
| **Concept audit** | [wiki-concept-audit.md](wiki-concept-audit.md) | Why registry ≠ Academy; design rules |

**Navigation change:** Sidebar uses human names (`1 · Install & setup`, `Textures · Organic PBR`) instead of internal codes. Codes remain only in folder paths (`training/blender/b01/`, `training/texturing/a01/`) for automation.

---

### 2. Python Librarian — registry + daily health

| Piece | Location | What it does |
|-------|----------|--------------|
| **SQLite registry** | `tools/librarian/` | Tools, licenses, URLs, approval workflow |
| **`daily-wiki`** | `librarian.cli` | HTTP link checks, academy gaps, registry gaps |
| **`research-queue`** | `librarian.cli` | Export what needs human/AI research |
| **Code glossary** | `academy_manifest.py` | Maps A01/B07 → plain English for reports |
| **Trafilatura extract** | `librarian extract` | `page.html` → clean `content.md` after webscreen |
| **Kimi integration** | `kimi.py`, `wiki_context.py` | Human briefings + wiki evolution research |

**Run daily:**

```powershell
.\scripts\daily-wiki.ps1
```

---

### 3. Go webscreen — browser-grade research

| Piece | Location | What it does |
|-------|----------|--------------|
| **`screen`** | `tools/webscreen/` | chromedp: screenshot + HTML for JS pages |
| **`search` / `hunt`** | SearXNG client | Meta-search → screen top URLs |
| **Discoveries** | `research/discoveries/<slug>/` | `meta.json`, `page.png`, `page.html`, `content.md` |

**No Wails** — CLI + PowerShell only. CEF/Energy deferred.

---

### 4. CI & link hygiene (Tier 1)

| Piece | Location | What it does |
|-------|----------|--------------|
| **lychee** | `.github/workflows/wiki-links.yml` | PR + weekly link check on `docs/**/*.md` |
| **mkdocs strict** | `.github/workflows/docs.yml` | Build wiki; deploy GitHub Pages |
| **Librarian weekly** | `.github/workflows/librarian-weekly.yml` | Tests + daily-wiki gap export |

---

### 5. Kimi — wiki editor (Kimi Code CLI subscription)

| Piece | Output | What it does |
|-------|--------|--------------|
| **`--humanize`** | `report-human.md` | Plain-English morning briefing |
| **`--wiki-evolve`** | `wiki-evolution.md` | Whole-wiki research brief: UX, images, lessons, OSS tools |
| **`wiki-audit`** | `wiki-audit-kimi.md` | Kimi scans all `docs/` pages for stale/broken/outdated content |
| **`wiki-images`** | `docs/assets/manifest.json` | Kimi finds logo/card URLs → optimized PNGs |
| **`breedables-research`** | live inventory wiki page | Kimi updates breedables research |
| **`kimi-test`** | CLI | Verify Kimi Code OAuth or Open Platform API |

Kimi receives: mission, **full wiki page inventory**, nav structure, design benchmarks, lesson/lab structure, tool registry, today's gaps.

**Preferred:** `kimi login --region global` (Kimi Code subscription — no Open Platform top-up). Fallback: `MOONSHOT_API_KEY`.

**Not used for:** link checks, screening, extraction — those stay deterministic.

---

## Daily workflow (today)

```text
┌─────────────────────────────────────────────────────────────────┐
│  YOU / CURSOR                                                    │
│  Read wiki-evolution.md → edit docs/ → commit training/ evidence │
└───────────────────────────────┬─────────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────────┐
│  scripts/daily-wiki.ps1                                          │
│  · Link checks (httpx)                                            │
│  · Academy + registry gaps                                        │
│  · report-human.md (Kimi or local)                                │
│  · wiki-evolution.md (Kimi or local)                              │
└───────┬─────────────────────────────┬─────────────────────────────┘
        │                             │
┌───────▼──────────┐         ┌────────▼─────────┐
│  MkDocs wiki     │         │  webscreen (Go)    │
│  docs/ + nav     │         │  chromedp + hunt   │
│  start-here      │         │  SearXNG (Docker)  │
└──────────────────┘         └────────────────────┘
        │
┌───────▼──────────────────────────────────────────┐
│  CI: lychee + mkdocs --strict + librarian tests   │
└──────────────────────────────────────────────────┘
```

### Three reports every morning

| File | Purpose |
|------|---------|
| `research/discoveries/daily-YYYY-MM-DD/report.md` | Machine metrics |
| `.../report-human.md` | What happened, in plain English |
| `.../wiki-evolution.md` | What to improve tomorrow |

---

## Design principles we fixed

1. **Academy teaches; registry administers** — learners never see `GREEN` / `EXPERIMENTAL` on lesson pages.
2. **Plain English first** — [start-here.md](../academy/index.md) is the model; codes are for folders only.
3. **Evidence, not watching** — every lesson/lab requires artifacts in `training/`.
4. **Git is source of truth** — not Slack; wiki publishes from `docs/`.
5. **Screening ≠ approval** — discoveries stay in `research/` until a human promotes them.
6. **Deterministic Tier 1, optional AI Tier 2** — links/screen/extract without LLM; Kimi for synthesis and evolution briefs.

---

## What is working now

| Check | Result (2026-08-23) |
|-------|---------------------|
| `mkdocs build --strict` | Passes (with known external-link warnings in strict mode for out-of-docs paths) |
| Daily wiki (40–120 URLs) | 0 link failures after tutorial URL fixes |
| Librarian tests | 19 passed |
| webscreen Go build | OK |
| Kimi API | Key configured; **needs API balance recharge** for live Kimi output |
| B01–B10 lesson pages | Written with Watch/Read/Do structure |
| `training/blender/b01–b10/` | Placeholder READMEs; **learner artifacts still empty** |

---

## Future goals

### Near term (weeks)

| Goal | How |
|------|-----|
| **Kimi live daily** | Recharge platform.kimi.ai; verify `kimi-test` → full `wiki-evolution.md` |
| **Fill `training/`** | First real learner artifacts for lesson 1 and Organic PBR lab |
| **RetopoFlow registry** | Resolve commercial-type gap flagged in daily reports |
| **Commit integration work** | Single PR: Academy nav, Tier 1 stack, Kimi, start-here |
| **Rotate exposed API key** | Key was pasted in chat — revoke and replace in `.env` |

### Medium term (Phase 2 — research automation)

| Goal | Tool |
|------|------|
| **`verify-tutorials`** | Batch webscreen all tutorial arsenal URLs |
| **Wire discoveries → Librarian** | Stale screen detection, ingest queue |
| **webscreen hunt on breedables topics** | Ozimals, KittyCatS, Animesh genetics → `research/discoveries/` |
| **ArchiveBox / SingleFile** | Long-lived evidence for market research citations |

### Long term (Phase 3+)

| Goal | Tool / approach |
|------|-----------------|
| **Cursor/RAG over wiki** | ragdocs-mcp or OmniDocs-RAG on `docs/` + discoveries |
| **MCP “check gaps before recommending tools”** | Cursor rule tied to Librarian |
| **Populate all B-lesson headers** | Consistent “Lesson N — Title” on B02–B10 |
| **Phase 5 build plan** | Real content in every `training/` folder; A-tracks with in-world proof |
| **Optional Ollama** | Local embeddings only if offline RAG needed — Cursor + Kimi cover synthesis |
| **Slack weekly digest** | Post `report-human.md` + top item from `wiki-evolution.md` |

---

## Key paths (cheat sheet)

| Path | Role |
|------|------|
| `docs/academy/start-here.md` | **Learners start here** |
| `docs/studio-roadmap.md` | Phased OSS roadmap (broader than this doc) |
| `tools/librarian/` | Registry + daily-wiki + Kimi |
| `tools/webscreen/` | chromedp + SearXNG CLI |
| `scripts/daily-wiki.ps1` | One-command morning loop |
| `research/discoveries/daily-*/` | Daily reports + evolution briefs |
| `.env` | Slack tokens, `MOONSHOT_API_KEY` (gitignored) |

---

## Commands reference

```powershell
# Morning loop (human + evolution briefs)
.\scripts\daily-wiki.ps1

# Full URL pass + browser rescreen on failures
.\scripts\daily-wiki.ps1 --url-limit 120 --screen-failures

# Test Kimi API
cd tools\librarian
python -m librarian.cli kimi-test

# Screen one URL
cd tools\webscreen
go run ./cmd/webscreen screen --url "https://wiki.secondlife.com/wiki/Ozimals"

# Build wiki
mkdocs build --strict
```

---

## Related docs

- [Studio roadmap](../roadmap.md) — phases 0–6, OSS recommendations
- [Web research stack](../research/web-research-stack.md) — chromedp, trafilatura, lychee, Kimi role
- [Wiki concept audit](wiki-concept-audit.md) — what went wrong and how we fixed the concept
- [Wiki design benchmarks](wiki-style-guide.md) — Outlands/Fandom patterns we copy
- Research discoveries — `research/discoveries/` in the git repo (not published in MkDocs)

---

*Generated as a maintainer snapshot of the 2026-08-23 build session. Update this page when major architecture changes.*
