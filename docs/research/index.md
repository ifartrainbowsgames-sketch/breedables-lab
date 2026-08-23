---
title: "Research & Tools"
section: research
type: index
question: "What are we currently evaluating?"
---
# Research & Tools

!!! abstract "This section answers one question"
    *What are we currently evaluating?*

Everything that is **not yet** canonical production knowledge — the
software database, new tool discoveries, licensing reviews, experiments and the
research queue. Once something here becomes a verified workflow it moves into
its subject section and this page keeps only a pointer.

## Topics

| Page | What it covers |
|------|----------------|
| [Software database](software-database.md) | Every tool the studio knows about, by subject |
| [Paid vs free matrix](paid-vs-free-matrix.md) | Licences, advantages, when paying is justified |
| [Studio experiments](experiments.md) | E01–E05 benchmarks and their measurements |
| [Tool registry](tool-registry.md) | Maintainer registry and Librarian commands |
| [Tool candidates](candidates/index.md) | Under evaluation, not approved |
| [Decision model](decision-model.md) | How a tool gets approved |
| [Promotion rules](promotion-rules.md) | When a candidate becomes production |
| [Web research stack](web-research-stack.md) | The Go CLI and Chromium research tooling |

## Market research

| Page | What it covers |
|------|----------------|
| [Breedables inventory & software](breedables-inventory-and-software.md) | Master list of SL breedable lines and their stacks |
| [Case studies](breedables-case-studies.md) | Per-product detail: what worked, what declined |
| [Market & design study](breedables-market-study.md) | Patterns and opportunity analysis |

## Source reports

Wiki pages are summaries. The full research reports live in the repository, not
the wiki, and are the record of record when the two disagree.

| Report | Location |
|--------|----------|
| Phase 0 open-source toolbox survey | `research/reports/2026-08-23-open-source-toolbox-survey.md` |
| Daily discoveries | `research/discoveries/` |

When a canonical report changes, update the linked wiki pages **and** the
Librarian seed data together.

## Pipeline stages owned by this section

These are the production-line stages this section is responsible for.

### Stage 0 — Research & tool selection

Before building a species, we need a **species-independent** toolbox: tools that work for any creature (cat, dragon, etc.) with licenses and workflows safe for **commercial SL breedables**.

!!! tip "Studio pick"
    **Librarian + git research reports** beat ad-hoc bookmarks. AI drafts reports; **humans** approve after evidence exists.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Breedables Librarian** | `tools/librarian/` | Registry, link checks, wiki lookup |
    | **GitHub** | https://github.com | Source code, issues, releases |
    | **ChatGPT / Claude** | AI assistants | Draft research — human reviews |
    | **MkDocs wiki** | this site | Published curriculum |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | *(none required at research stage)* | | |

**How we use it**

- Discover tools via GitHub, feeds, community, AI-assisted research  
- Record **evidence** in `research/reports/` — not approval colors in chat  
- Run benchmarks (E01–E05) before trusting a tool in production  
- Librarian registry holds URLs, links, evidence paths

**What to complete**

- Read: [Phase 0 survey summary](index.md)  
- Read: [Software & Tools hub](index.md)  
- Do: Add one discovery note to `research/discoveries/` with URL + breedables use case

**Evidence folder** — `research/reports/`, `research/discoveries/`  
**Related pages** — [Software & Tools](index.md) · [Tools registry](tool-registry.md) · [Phase 0 survey](index.md)

### Stage 6 — Image-to-3D (research / blockout)

Fast **concept geometry** from reference art — not a replacement for modeling standards.

!!! tip "Studio pick"
    **TripoSR (local, open)** for controlled E02 evidence. Hosted SaaS only after explicit commercial/legal review. **Hunyuan3D** excluded from commercial SL pipeline per Phase 0 research.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **TripoSR** | GitHub | First baseline (MIT code/model per upstream) |
    | **InstantMesh** | GitHub | Comparison |
    | **TRELLIS.2** | GitHub | Research — dependency audit required |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Tripo3D** (SaaS) | tripo3d.ai | Hosted gen — check commercial ToS |
    | **Meshy** | meshy.ai | Hosted gen — check ToS |

**How we use it**

- E02 benchmark only until evidence shows SL-ready output with acceptable cleanup  
- Never ship raw AI mesh without retopo + license audit

**What to complete**

- Experiments:  (after E01, E03, E04, E05)  
- Produce: comparison table + cleaned mesh attempt

**Evidence folder** — `research/experiments/e02/`  
**Related pages** — [TripoSR](candidates/triposr.md) · [Research candidates](candidates/index.md)
