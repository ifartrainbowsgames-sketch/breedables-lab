# Studio Channel Map — Every Channel, Function & Purpose

**Date:** 2026-08-23  
**Status:** DRAFT — foundation for Academy redesign  
**Related:** [Wiki concept audit](../research/wiki-concept-audit.md)

This document lists **every channel** in the Breedables Studio system — Slack, bots, wiki sections, repo folders, data stores, and AI interfaces — and states **what each one is for** vs **what it is supposed to do**.

Use this as the contract before redesign. If a channel has no clear function, it should not exist.

---

## How to read this

| Column | Meaning |
|--------|---------|
| **Function** | What it actually does **today** |
| **Supposed to do** | What it **should** do in the Academy-first studio |
| **Status** | `LIVE` · `PARTIAL` · `PLANNED` · `WRONG SHAPE` · `BLOCKED` |

---

## 1. Slack workspace channels (human chat)

> **Inventory note:** The Librarian bot cannot auto-list channels yet — missing Slack scopes `channels:read` and `groups:read`. Add them in [api.slack.com/apps](https://api.slack.com/apps) → **OAuth & Permissions** → reinstall app → rerun inventory (see §8).

Fill in your real `#channel-names` in the **Channel** column. Rows below are **recommended** studio channels plus blanks for yours.

| Channel | Type | Function (today) | Supposed to do | Status |
|---------|------|------------------|----------------|--------|
| `#general` | public | Default workspace chat | Announcements, studio-wide updates, links to new wiki lessons | `FILL IN` |
| `#breedables-knowledge` | public | *Not created* (roadmap only) | **Public face of the Academy wiki** — daily links, lesson drops, “start here” | `PLANNED` |
| `#academy` | public | *Unknown* | Learning discussion, homework help, A01–A05 progress, share artifacts | `FILL IN` |
| `#research-rnd` | public | *Unknown* | Tool discoveries, license questions, Phase 0-style notes before registry | `FILL IN` |
| `#production` | public | *Unknown* | Pipeline talk: Blender → SL export, experiments E01–E05 results | `FILL IN` |
| `#tools-registry` | public | *Unknown* | Librarian gaps, `/breedgaps` output, approval decisions (reviewer channel) | `FILL IN` |
| `#secondlife-inworld` | public | *Unknown* | In-world test results, PBR screenshots, Animesh/Linkset Data findings | `FILL IN` |
| `#releases` | public | *Unknown* | Release notes, version tags, what shipped to players | `FILL IN` |
| `#random` | public | Slack default | Off-topic; **not** a studio channel — exclude from wiki sync | `FILL IN` |
| *(add yours)* | | | | `FILL IN` |

### Rules for Slack channels

1. **Academy content** is discussed in `#academy` or `#breedables-knowledge` — not buried in DMs.  
2. **Registry/compliance** lives in `#tools-registry` — evidence packages only, **no color labels in Slack**.  
3. **Slash commands** work in any channel the bot is invited to; prefer dedicated channels above for clarity.  
4. **Do not** treat the Breedables Librarian **DM** as a workspace channel — DMs are off for this app.

---

## 2. Slack apps & bots (interfaces)

From your workspace **Agents & apps** sidebar:

| Channel / App | Function (today) | Supposed to do | Status |
|---------------|------------------|----------------|--------|
| **Breedables Librarian** | Slash commands in channels: `/breedstatus`, `/breedtool`, `/breedgaps` | **Registry lookup only** — tool facts, gaps, status counts; later link to wiki lessons | `LIVE` |
| **ChatGPT** | External AI chat (Slack app) | **Deep research & synthesis** — comparisons, license interpretation, draft lesson text; output → research reports | `PARTIAL` |
| **Claude** | External AI chat (Slack app) | Architecture review, implementation plans, code review; not source of truth | `PARTIAL` |
| **Cursor** | IDE agent integration | Implementation, repo edits, runs Librarian locally; connects to wiki via git | `PARTIAL` |
| **GitHub** | Repo notifications / linking | PRs, commits, wiki deploy, issue tracking | `PARTIAL` |
| **Slack** (platform) | Host for channels above | Coordination layer — not a wiki | `LIVE` |

### Librarian slash-command channels (logical)

These are **interaction channels** into the SQLite registry:

| Command | Function (today) | Supposed to do | Status |
|---------|------------------|----------------|--------|
| `/breedstatus` | Count tools by workflow status | Same + link to wiki registry page | `LIVE` |
| `/breedtool <query>` | Search tool records | Same + link to **Academy lesson** that uses the tool | `LIVE` / `WRONG SHAPE` |
| `/breedgaps` | List approval/license gaps | Split: **registry gaps** vs **content gaps** (missing videos/labs) | `WRONG SHAPE` |
| `@Breedables Librarian tool/status/gaps` | App mention text commands | Optional; same as slash commands | `LIVE` |

---

## 3. Wiki channels (MkDocs — published docs)

**URL:** https://ifartrainbowsgames-sketch.github.io/breedables-lab/

| Wiki section | Path | Function (today) | Supposed to do | Status |
|--------------|------|------------------|----------------|--------|
| **Home** | `docs/index.md` | Links + local preview instructions | **Start here by role**: Learner / Builder / Reviewer | `PARTIAL` |
| **Roadmap** | `docs/studio-roadmap.md` | Phases 0–6 + OSS recommendations | Studio master plan; updated when channels change | `LIVE` |
| **Decision model** | `docs/production/decision-model.md` | GREEN/YELLOW license taxonomy | **Reviewer-only** — move out of learner nav | `WRONG SHAPE` |
| **Tool registry overview** | `docs/production/tools/index.md` | Table of 7 seeded tools | **Maintainer registry** — link from lessons, not front door | `WRONG SHAPE` |
| **Tool pages (×7)** | `docs/production/tools/*.md` | License + status tables | **Footer on lessons only** — not standalone “learning” pages | `WRONG SHAPE` |
| **Research candidates (×10)** | `docs/production/tools/candidates/` | Survey leftovers, license notes | Reviewer reference during experiments | `PARTIAL` |
| **Experiments E01–E05** | `docs/production/experiments.md` | Lab specs for reviewers | **Academy labs** with Watch/Read/Do steps per experiment | `PARTIAL` |
| **Promotion rules** | `docs/production/promotion-rules.md` | When tools enter `approved/` | Reviewer policy doc | `LIVE` |
| **Second Life baseline** | `docs/secondlife/platform-baseline.md` | PBR, Animesh, LSL links | Platform **Read** links for Academy tracks | `LIVE` |
| **Academy overview** | `docs/academy/overview.md` | A01–A05 names only, no videos | **Full curriculum index** with lesson links | `WRONG SHAPE` |
| **Phase 0 survey summary** | `docs/research/phase-0-survey.md` | Pointer to full report | R&D archive — not Academy home | `LIVE` |
| **Wiki concept audit** | `docs/research/wiki-concept-audit.md` | Diagnosis of broken concept | Pre-redesign contract | `LIVE` |
| **This channel map** | `docs/studio/channel-map.md` | — | Living map of all channels; update when Slack/repo changes | `LIVE` |

### Wiki channels that **must exist** after redesign

| Planned path | Supposed to do | Status |
|--------------|----------------|--------|
| `docs/academy/tracks/a01-organic-pbr/` | Lessons: Watch, Read, Do, Produce | `PLANNED` |
| `docs/academy/resources/videos.md` | Master index of curated videos by subject | `PLANNED` |
| `docs/academy/resources/official-docs.md` | SL wiki, Blender manual, tool docs | `PLANNED` |
| `docs/studio/registry/` | Renamed tool pages (maintainer view) | `PLANNED` |

---

## 4. Repository folder channels (source of truth)

Each top-level folder is a **content channel** into GitHub.

| Folder | Function (today) | Supposed to do | Status |
|--------|------------------|----------------|--------|
| `docs/` | MkDocs wiki source | **Academy-first** published learning + maintainer studio docs | `PARTIAL` |
| `research/` | Phase 0 report + audit | R&D reports, license notes, decisions — feeds wiki drafts | `PARTIAL` |
| `research/reports/` | Long-form surveys & audits | Dated decision documents | `LIVE` |
| `research/discoveries/` | *Empty stub* | New tool/technique radar intake | `PLANNED` |
| `research/experiments/` | *Empty stub* | Experiment writeups, measurements, PASS/FAIL | `PLANNED` |
| `research/licenses/` | *Empty stub* | Commercial-use audit notes per tool | `PLANNED` |
| `training/` | README only; tracks listed | **Academy source files** — exercises, notes, student outputs | `WRONG SHAPE` |
| `training/blender/` | *Missing* | Blender fundamentals lessons | `PLANNED` |
| `training/modeling/` | *Missing* | Organic modeling for breedables | `PLANNED` |
| `training/texturing/` | *Missing* | PBR / Material Maker / Ucupaint labs | `PLANNED` |
| `training/rigging/` | *Missing* | Rigify quadruped path | `PLANNED` |
| `training/animation/` | *Missing* | Idle/walk, retargeting | `PLANNED` |
| `training/lsl/` | *Missing* | Scripting curriculum | `PLANNED` |
| `training/secondlife/` | *Missing* | In-world testing curriculum | `PLANNED` |
| `tools/` | README stub | Tool **files** and add-ons (not the Librarian DB) | `PLANNED` |
| `tools/approved/` | *Missing* | Production-approved tool installs | `PLANNED` |
| `tools/experimental/` | *Missing* | Tools under evaluation | `PLANNED` |
| `tools/rejected/` | *Missing* | Rejected tools + reasons | `PLANNED` |
| `tools/librarian/` | Python registry + Slack bot | **Facts channel** — SQLite, CLI, discovery queue | `LIVE` |
| `pipeline/` | README stub | Blender → export → optimize → validate automation | `PLANNED` |
| `scripts/` | README stub | LSL breedables engine modules | `PLANNED` |
| `data/` | README stub | Genes, traits, colors, rarity tables | `PLANNED` |
| `assets/` | README stub | CC0 assets + provenance | `PLANNED` |
| `creatures/cat/` | README stub | First species production tree | `PLANNED` |
| `hud/` | README stub | SL HUD/UI packages | `PLANNED` |
| `backend/` | README stub | Optional external services | `PLANNED` |
| `releases/` | README stub | Release notes & packages | `PLANNED` |
| `tests/` | README stub | Automated tests (engine + tools) | `PLANNED` |

---

## 5. Data & automation channels (machine interfaces)

| Channel | Location | Function (today) | Supposed to do | Status |
|---------|----------|------------------|----------------|--------|
| **Librarian SQLite DB** | `tools/librarian/.data/librarian.sqlite3` | 7 seeded tools, HTTP checks | Full registry + discovery queue + future video links | `LIVE` |
| **Librarian CLI** | `python -m librarian.cli` | init, add, list, check, gaps, seed, discover, ingest | Same + `research-queue`, `export-lesson-gaps` | `LIVE` |
| **Slack Socket Mode** | `python -m librarian.slack_app` | Bolt app while terminal runs | Always-on service; links to wiki | `PARTIAL` |
| **GitHub Actions: tests** | `.github/workflows/librarian-tests.yml` | pytest on librarian changes | CI gate for registry code | `LIVE` |
| **GitHub Actions: docs** | `.github/workflows/docs.yml` | Build + deploy MkDocs → `gh-pages` | Publish Academy wiki on every docs push | `LIVE` |
| **GitHub Pages** | `gh-pages` branch | Static wiki hosting | Public Academy URL | `PARTIAL` (enable in Settings) |
| **`.env` secrets** | `tools/librarian/.env` | Slack tokens, DB path | Local config only — never committed | `LIVE` |

---

## 6. Academy track channels (learning paths)

These are **logical channels** — one track = one subject corridor.

| Track | Maps to experiment | Function (today) | Supposed to do | Status |
|-------|-------------------|------------------|----------------|--------|
| **A01** Organic PBR Material | E01 | Name on overview page | Videos + Material Maker/Poly Haven links + lab + SL screenshot | `WRONG SHAPE` |
| **A02** Layered Texture Refinement | E01 | Name only | Ucupaint layers, phenotype variants, exercises | `WRONG SHAPE` |
| **A03** Organic Retopology | E03 | Name only | RetopoFlow/manual tutorials + mesh deliverable | `WRONG SHAPE` |
| **A04** Rig + Two Animations | E04 | Name only | Rigify + retargeting videos + idle/walk bake | `WRONG SHAPE` |
| **A05** SL Creature Fixture | E05 | Name only | LSL + Linkset Data lessons + in-world demo | `WRONG SHAPE` |

---

## 7. External learning channels (not owned by us)

These must be **linked from Academy lessons**, not replaced.

| External channel | Examples | Supposed to do | Status |
|------------------|----------|----------------|--------|
| **YouTube** | Blender, SL creator tutorials | Curated **Watch** links per track | `MISSING` |
| **Blender manual** | docs.blender.org | **Read** links per tool/track | `PARTIAL` (linked on some pages) |
| **Second Life wiki** | PBR, Animesh guides | **Read** links for A05 + texturing | `PARTIAL` |
| **Tool official docs** | Material Maker, TripoSR repos | Install + usage **Read** steps | `MISSING` |
| **Poly Haven / ambientCG** | Asset sites | **Read** + provenance rules | `PARTIAL` |
| **ChatGPT / Claude** (web) | Deep research | Draft reports → human review → git | `PARTIAL` |

---

## 8. How to complete the Slack channel inventory

1. Open [Slack app settings](https://api.slack.com/apps) → **Breedables Studio Librarian**.  
2. **OAuth & Permissions** → add bot scopes:  
   - `channels:read`  
   - `groups:read` (private channels, optional)  
3. **Reinstall to Workspace**.  
4. Run from `tools/librarian`:

```powershell
.venv\Scripts\Activate.ps1
python -m librarian.cli list-channels
```

*(Command does not exist yet — add in Librarian V1.1 or run one-off script.)*

5. Paste results into §1 table above and commit this file.

---

## 9. Channel routing rules (target architecture)

```
Learner question     → #academy or #breedables-knowledge → wiki lesson link
Tool approval        → #tools-registry → Librarian → research/reports/
New discovery        → #research-rnd → discover-github/ingest-feed → review
Experiment result    → #production → research/experiments/ → Academy lab update
In-world test        → #secondlife-inworld → screenshot + notes → A05 artifact
Release              → #releases → releases/ + player-facing notes
Deep research        → ChatGPT/Claude → markdown report → git → wiki
Facts lookup         → /breedtool in channel → registry (not lesson)
```

---

## 10. Mistakes to fix (channel misrouting)

| Mistake | Fix |
|---------|-----|
| Academy wiki shows registry labels | Move to `docs/studio/registry/`; Academy shows lessons |
| Slack DM used as main Librarian interface | Use channels; DM stays disabled |
| `training/` empty while `docs/academy/` claims Academy | One source: lessons in `docs/academy/tracks/` + artifacts in `training/` |
| Phase 0 survey used as curriculum | Survey stays in `research/`; Academy links out |
| `/breedgaps` only shows license gaps | Add **content gaps** (missing videos, broken lesson links) |
| No `#breedables-knowledge` | Create channel as wiki broadcast layer |

---

## 11. Next steps

1. **You:** Fill §1 with your real Slack `#channel` names (or add bot scopes so we can auto-list).  
2. **Studio:** Agree §9 routing rules.  
3. **Then write:** `2026-08-23-academy-redesign-spec.md` using this map.  
4. **Implement:** A01 track as first complete channel (Watch + Read + Do + Produce).

---

## References

- [Wiki concept audit](../research/wiki-concept-audit.md)  
- [Studio roadmap](../studio-roadmap.md)  
- [Librarian README](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/feature/studio-librarian-v1/tools/librarian/README.md)  
- [Channel content requirements](../studio/channel-content-requirements.md)
