# Wiki-First Strategy — Build Here, Publish to Slack Later

**Date:** 2026-08-23  
**Status:** ACTIVE — overrides Slack-as-wiki experiments  
**Related:** [Production line](../academy/production-line.md) · [Channel map](channel-map.md) · [Content requirements](channel-content-requirements.md)

---

## Decision

1. **Delete or retire** scattered documentation living in Slack (Canvases, pinned chaos, old threads as “docs”).  
2. **Build the complete wiki in this repository** (`docs/` + MkDocs → GitHub Pages).  
3. **Later**, sync or publish **from git → Slack** (Canvas, `#breedables-knowledge` links, bot responses) — Slack is a **display layer**, not the editor.

**Source of truth:** GitHub + `docs/` markdown.  
**Not source of truth:** Slack messages, Canvas drafts, DM threads.

---

## Why

- Slack docs have no version history, no review flow, no links structure, no Academy lesson template.  
- We already proved the mistake: registry colors in Slack/wiki hybrid confused learners.  
- MkDocs gives search, nav, evidence links, and CI deploy.  
- Slack is where people **talk** and get **notifications** — not where we **author** curriculum.

---

## Phase A — Clean Slack (manual, you + team)

Do this in the **Breedables** workspace:

| Action | Where |
|--------|--------|
| Remove or archive **Studio Canvases** that duplicate wiki topics | Slack Canvas |
| Unpin outdated doc pins; replace with single pin: **wiki URL** | Each `#channel` |
| Stop posting long-form docs in threads — post **wiki link + summary** only | All studio channels |
| Keep **Breedables Librarian** for lookup only until wiki URLs replace `/breedtool` walls of text | Bot |

**Do not delete `#channels`.** Only remove **documentation content** that will live in git.

**Single pin for every studio channel (after wiki is live):**

```
Studio wiki (source of truth):
https://ifartrainbowsgames-sketch.github.io/breedables-lab/

Academy start:
https://ifartrainbowsgames-sketch.github.io/breedables-lab/academy/production-line/
```

---

## Phase B — Complete wiki here (our work in repo)

Build out `docs/` until a new member can learn breedables **without Slack docs**.

### Required wiki sections (checklist)

- [x] Production line (all stages, tools free/paid) — [production-line.md](../academy/production-line.md)  
- [x] Channel map + content requirements  
- [ ] **Academy tracks A01–A05** — full lessons (Watch / Read / Explain / Do / Produce)  
- [ ] **Video index** — `docs/academy/resources/videos.md`  
- [ ] **Official docs index** — `docs/academy/resources/official-docs.md`  
- [ ] **Per-stage tool pages** — evidence footers, not color labels  
- [ ] **Experiments E01–E05** — lab sheets with measurement tables  
- [ ] **Second Life** — expanded platform guide  
- [ ] **LSL / engine** — module overview (when scripts exist)  
- [ ] **Genetics / data** — when schemas exist  
- [ ] **Reviewer registry** — move `production/tools/` under `studio/registry/` (maintainer nav)  

### Nav target (learner-first)

```
Home
Academy
  ├── Overview
  ├── Production line
  ├── Tracks (A01…A05)
  └── Resources (videos, official docs)
Second Life
Studio (maintainers)
  ├── Channel map
  ├── Content requirements
  └── Registry / experiments
Research (archive)
```

### Definition of “complete wiki”

- [ ] Every production line stage has ≥1 lesson or explicit “coming soon” with evidence checklist  
- [ ] A01 has **real video URLs** + E01 lab + evidence folder in git  
- [ ] No learner page uses GREEN/EXPERIMENTAL as primary info  
- [ ] `mkdocs build --strict` passes  
- [ ] GitHub Pages live  

---

## Phase C — Put wiki into Slack (after Phase B)

Options (pick one later — do not block Phase B):

| Method | Effort | Notes |
|--------|--------|-------|
| **Link-only** | Low | Bot + pins post wiki URLs; `#breedables-knowledge` daily lesson link |
| **Canvas sync** | Medium | Librarian V1.1 — approved pages → Canvas with review gate |
| **Beever Atlas / similar** | High | Auto-ingest Slack ↔ wiki — only if needed |

**Recommended first:** link-only + `/breedtool` returns wiki lesson URL.

---

## What we do NOT do

- Write new long docs in Slack Canvas while Phase B is in progress  
- Treat `/breedgaps` approval colors as Academy content  
- Duplicate content: if it’s in git, Slack gets a **link**, not a copy-paste  

---

## Immediate next steps

1. **You:** Archive/delete Slack Canvas docs (manual).  
2. **Us:** Build A01 lesson + video index in `docs/academy/`.  
3. **Us:** Reorganize MkDocs nav (Academy first, Production/registry under Studio).  
4. **When wiki complete:** one announcement in `#general` with wiki URL only.  
5. **Then:** wire Librarian to return wiki links in Slack.

---

## References

- [Wiki concept audit](../research/wiki-concept-audit.md)  
- [Production line](../academy/production-line.md)  
