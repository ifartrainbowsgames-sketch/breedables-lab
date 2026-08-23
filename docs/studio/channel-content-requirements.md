# Channel Content Requirements — Evidence, Not Labels

**Date:** 2026-08-23  
**Status:** DRAFT — replaces color/status vocabulary in Slack and Academy  
**Related:** [Channel map](../studio/channel-map.md) · [Wiki concept audit](../research/wiki-concept-audit.md)

---

## Policy change (effective immediately)

### Kill the colors and status theater

**Do not use in Slack, Academy lessons, or learner-facing wiki:**

- `GREEN` / `YELLOW` / `RED`
- `EXPERIMENTAL` / `USE NOW` / `REVIEWING` as headline labels
- `/breedgaps` output that only says “not yet approved” without saying **what evidence is missing**

Those were internal R&D shorthand. They are **useless in Slack** and **confusing in a wiki**. Nobody learns from a color.

### Replace with evidence

A tool, track, or decision is real when it has **evidence attached**:

| Evidence type | What it is |
|---------------|------------|
| **Tutorial video** | Curated URL + 1-line why we picked it + track/subject tag |
| **Official doc link** | Authoritative read (Blender manual, SL wiki, tool README) |
| **Written explanation** | Plain-language “what this is for in breedables” (our words) |
| **Research note** | Dated report: comparison, license notes, risks — in `research/` |
| **Lab steps** | Numbered Do section: install → exercise → expected result |
| **Artifact file** | Committed `.blend`, texture, script, screenshot, export — with path |
| **In-world proof** | SL screenshot or LSL demo with date + region + setup notes |
| **Measurement** | Time, poly count, file size, pass/fail table from an experiment |
| **Human sign-off** | Name + date: “reviewed, OK to use for X” — one sentence |

**Slack posts and wiki pages link to evidence.** They do not repeat approval colors.

---

## Minimum evidence checklist (any channel)

Before calling a topic “documented” in any channel:

- [ ] At least **1 tutorial video** OR **1 official doc** linked  
- [ ] **Our explanation** (3+ sentences, breedables-specific)  
- [ ] **What to produce** (file, screenshot, or in-world result)  
- [ ] **Where it lives** (git path or wiki URL)  
- [ ] **Last verified** date (link still works, tool version noted)

No checklist complete → topic is **incomplete**, not “experimental.”

---

## 1. Slack workspace channels — required content

What each `#channel` **must contain over time** (pinned resources + ongoing posts).

### `#general`

| Must have | Purpose |
|-----------|---------|
| Pinned: link to **Academy start** wiki page | Everyone knows where to learn |
| Pinned: link to **channel map** | Know where to post |
| Announcements only: new lessons, releases | No tool license debates here |

**Posts should include:** wiki link + one-line summary. **Never:** status colors.

---

### `#breedables-knowledge` (create this)

| Must have | Purpose |
|-----------|---------|
| Daily or weekly **lesson drop** | Link to new/updated wiki lesson |
| Pinned **video index** | Link to `docs/academy/resources/videos.md` |
| Pinned **official docs index** | Link to SL + Blender hub page |

**Each post template:**

```
New: [Lesson title]
Watch: [video URL]
Read: [doc URL]
Do: [lab link]
Evidence: [git path or screenshot]
```

---

### `#academy`

| Must have | Purpose |
|-----------|---------|
| **A01–A05 progress thread** (one thread per track) | Students share artifacts |
| Homework help | Questions → answer links to wiki, not vibes |
| **Tutorial recommendations** | Members suggest videos → curator adds to wiki |

**Required in every help reply:** link to lesson + link to video/doc. **Forbidden:** “it’s still experimental.”

---

### `#research-rnd`

| Must have | Purpose |
|-----------|---------|
| **Discovery posts** with URL + screenshot + “why relevant” | Raw radar |
| **Research reports** linked (`research/reports/…`) | Deep work lives in git |
| License questions as **research notes**, not colors | Evidence for reviewers |

**Each discovery post must include:**

- Tool/project URL  
- What breedables problem it might solve  
- Link to draft report or “needs research” wiki task  

---

### `#production`

| Must have | Purpose |
|-----------|---------|
| **Experiment results** E01–E05 (measurements + files) | Pipeline truth |
| Blender → export → SL upload notes | Repeatable steps |
| Failure posts with **what we tried** + logs/screenshots | Learning from dead ends |

**Each result post must include:** experiment ID, artifacts path, pass/fail, screenshots.

---

### `#tools-registry` (reviewers only — not learners)

| Must have | Purpose |
|-----------|---------|
| **Evidence packages** per tool (not colors) | Approval decisions |
| Link to `research/licenses/` note when exists | Audit trail |
| Librarian record ID + wiki registry page | Machine + human sync |

**Approval post template:**

```
Tool: Material Maker
Evidence: research/experiments/e01-material-maker/ (blend + SL shots)
License note: research/licenses/material-maker.md
Video used: [URL]
Sign-off: [name, date]
Decision: approved for [specific use case only]
```

**Retire:** posting `/breedgaps` without listing **missing evidence files**.

---

### `#secondlife-inworld`

| Must have | Purpose |
|-----------|---------|
| **PBR in-world screenshots** (settings noted) | A01/A02 proof |
| **Animesh / rig tests** | A04 proof |
| **Linkset Data / LSL fixture demos** | A05 proof |
| Region, date, viewer version on every shot | Reproducibility |

---

### `#releases`

| Must have | Purpose |
|-----------|---------|
| Version tag + **changelog** link (`releases/`) | Player-facing truth |
| Links to **evidence** that shipped (meshes, scripts tested) | Not hype |

---

### `#random`

**Must have:** nothing studio-related. **Exclude** from wiki sync and bots.

---

## 2. Slack apps & bots — required output

### Breedables Librarian

| Command | Must return (redesign) | Must NOT return |
|---------|------------------------|-----------------|
| `/breedtool X` | Name, URL, **lesson link**, **video link**, **last artifact path** | Color labels |
| `/breedstatus` | Count of tools **with complete evidence** vs **missing evidence** | EXPERIMENTAL: 3 |
| `/breedgaps` | Bulleted **missing evidence** per item | “not yet approved” alone |

**Example gap (good):**

```
Material Maker — missing: install video, E01 artifact folder, license note
```

**Example gap (bad — retire):**

```
Material Maker — EXPERIMENTAL, not yet approved
```

---

### ChatGPT / Claude (Slack apps)

| Must produce | Format |
|--------------|--------|
| Draft **research reports** | Markdown → `research/reports/` |
| Draft **lesson text** (Watch/Read/Do) | Markdown → PR to `docs/academy/` |
| Comparison tables with **sources cited** | Not “GREEN” ratings |

**Must NOT produce:** final approval without human sign-off and artifacts.

---

### GitHub (app/notifications)

| Must surface | Purpose |
|--------------|---------|
| Wiki deploy success | Academy updated |
| New files in `research/experiments/` | Evidence landed |
| PRs touching `docs/academy/` | Curriculum review |

---

## 3. Wiki channels — required content per section

### Home (`docs/index.md`)

- [ ] **Start here: Learner** → Academy tracks  
- [ ] **Start here: Builder** → production + pipeline  
- [ ] **Start here: Reviewer** → research + registry  
- [ ] Link to video index + official docs index  
- [ ] **No** GREEN/EXPERIMENTAL on home page  

---

### Academy overview + tracks A01–A05

**Each track page must have:**

| Section | Required content |
|---------|------------------|
| **Outcome** | One sentence skill gained |
| **Watch** | ≥2 tutorial videos (title, URL, duration, why chosen) |
| **Read** | ≥2 official doc links |
| **Explain** | Our breedables-specific guide (500+ words or step list) |
| **Do** | Lab matching experiment (E01–E05) |
| **Produce** | Exact files/screenshots required |
| **Evidence folder** | `training/<track>/` or `research/experiments/<id>/` |
| **Completed when** | Checklist, not status label |

---

### `docs/academy/resources/videos.md` (create)

| Must have |
|-----------|
| Master table: subject, URL, level, track (A01–A05), curator, last_checked |
| Blender, texturing, rigging, LSL, SL creator categories |
| Minimum **30 curated links** before calling Academy “started” |

---

### `docs/academy/resources/official-docs.md` (create)

| Must have |
|-----------|
| Second Life PBR, Animesh, Linkset Data, LSL definitions |
| Blender manual sections per track |
| Tool official docs (Material Maker, Rigify, etc.) |

---

### Production / experiments (`docs/production/experiments.md`)

| Must have per experiment |
|--------------------------|
| Hypothesis |
| Tools used (link to lessons, not license table) |
| Step-by-step procedure |
| **Measurement table** (blank + example filled) |
| **Evidence folder path** |
| Pass/fail criteria in plain language |

---

### Tool registry pages (maintainer-only after redesign)

| Must have |
|-----------|
| Official URL, install steps |
| **Evidence index** (links to experiments + license notes + videos) |
| Last HTTP check date |
| **No** survey color as page title |

---

### Second Life baseline

| Must have |
|-----------|
| Every SL wiki link from Phase 0 survey |
| **Explain** paragraphs: how each applies to breedables |
| Cross-links to A05 lessons |

---

### Research / audit docs

| Must have |
|-----------|
| Dated reports, decisions, sources |
| For reviewers — not linked from learner “Start here” |

---

## 4. Repository folders — required artifacts

| Folder | Must contain (evidence types) |
|--------|-------------------------------|
| `research/reports/` | Dated markdown research with citations |
| `research/experiments/` | One subfolder per E01–E05 with README + outputs |
| `research/licenses/` | Per-tool license audit prose (not color rating) |
| `research/discoveries/` | Short MD per discovery: URL, date, follow-up |
| `training/blender/` | Exercise files + notes from A-blender lessons |
| `training/texturing/` | `.blend`, exported PBR, SL screenshots (A01/A02) |
| `training/modeling/` | Meshes from modeling labs |
| `training/rigging/` | Rig files, test animations (A04) |
| `training/animation/` | Baked clips, retarget notes |
| `training/lsl/` | Script fixtures, test harness (A05) |
| `training/secondlife/` | In-world test logs, screenshots |
| `tools/approved/` | Only tools with **full evidence package** + README |
| `tools/librarian/` | Facts DB; gaps = **missing evidence fields** |
| `assets/cc0/` | Files + `provenance.md` per asset used |
| `releases/` | Versioned notes + links to tested artifacts |
| `pipeline/` | Documented scripts + before/after examples |
| `scripts/` | LSL modules + test notes |
| `data/` | Schema docs + example gene/trait tables |

**Empty folder rule:** folder exists in README but has no artifacts → channel is **empty**; wiki must not pretend otherwise.

---

## 5. Academy tracks — evidence requirements (detail)

### A01 — Organic PBR Material

| Type | Minimum |
|------|---------|
| Tutorial videos | 2+ (Blender PBR + Material Maker or procedural) |
| Official docs | SL PBR wiki, Blender shader docs |
| Explanation | Our skin/fur material workflow for breedables |
| Lab | E01 procedure |
| Produce | `.blend`, exported maps, **in-world SL screenshot** |
| Evidence path | `training/texturing/a01/` |

---

### A02 — Layered Texture Refinement

| Type | Minimum |
|------|---------|
| Tutorial videos | 2+ (Ucupaint or layer painting) |
| Official docs | Ucupaint repo/docs |
| Explanation | Phenotype variant workflow |
| Lab | E01 variant branch |
| Produce | Layer files + comparison screenshot |
| Evidence path | `training/texturing/a02/` |

---

### A03 — Organic Retopology

| Type | Minimum |
|------|---------|
| Tutorial videos | 2+ (manual retopo + RetopoFlow if used) |
| Official docs | Blender retopo docs |
| Explanation | Edge flow for deformation areas |
| Lab | E03 procedure |
| Produce | Retopo mesh + timing notes |
| Evidence path | `training/modeling/a03/` |

---

### A04 — Rig + Two Animations

| Type | Minimum |
|------|---------|
| Tutorial videos | 2+ (Rigify quadruped + retargeting) |
| Official docs | Rigify manual, retarget add-on README |
| Explanation | Bone mapping notes for quadruped |
| Lab | E04 procedure |
| Produce | Rig + idle/walk baked |
| Evidence path | `training/rigging/a04/`, `training/animation/a04/` |

---

### A05 — Second Life Creature Fixture

| Type | Minimum |
|------|---------|
| Tutorial videos | 2+ (LSL basics, Linkset Data if available) |
| Official docs | LSL definitions repo, Linkset Data API |
| Explanation | Persistence design for breedables (modern, not XS clone) |
| Lab | E05 procedure |
| Produce | LSL scripts + in-world demo video or screenshot series |
| Evidence path | `training/lsl/a05/`, `training/secondlife/a05/` |

---

## 6. External channels — curation rules

| Source | Requirement |
|--------|-------------|
| **YouTube** | Title, URL, channel, date added, track tag, “why this one” |
| **Blender manual** | Deep link to section, not homepage only |
| **SL wiki** | Link + note if outdated; prefer create.secondlife.com when better |
| **Tool GitHub** | Link to README + license file + releases page |
| **AI drafts** | Never publish without human review + evidence check |

---

## 7. Librarian database — field redesign (evidence-first)

**Add / prioritize fields** (conceptual — implement in V1.1):

| Field | Purpose |
|-------|---------|
| `primary_video_url` | Main tutorial |
| `doc_urls` (JSON list) | Official reads |
| `lesson_wiki_path` | Link to Academy lesson |
| `evidence_path` | Git folder with artifacts |
| `license_note_path` | `research/licenses/…` |
| `last_evidence_review` | Date a human checked |
| `evidence_complete` | boolean — checklist done |

**Deprioritize for Slack output:** `commercial_type`, workflow `status` as primary message.

---

## 8. What we remove from Slack and learner wiki

| Remove | Replace with |
|--------|--------------|
| `GREEN / YELLOW / RED` | Research note link |
| `EXPERIMENTAL / USE NOW` headlines | “Evidence: complete / incomplete” + what’s missing |
| `/breedgaps` approval shaming | `/breedgaps` missing videos, docs, artifacts |
| Tool pages as learning entry | Lesson pages as entry; tools in footer |
| “Survey rating” column | “Evidence package” column |

---

## 9. Definition of done — studio-wide

The redesign is done when:

- [ ] Every Slack studio channel (§1) has **pinned evidence hub links**  
- [ ] A01 wiki page has **real video URLs** and a **filled evidence folder**  
- [ ] `/breedtool Blender` returns a **lesson link + video**, not license colors  
- [ ] No learner-facing page uses GREEN/EXPERIMENTAL as primary info  
- [ ] `research/experiments/e01/` exists with at least one **complete** evidence package  

---

## 10. Next file to write

After this requirements doc is agreed:

**`2026-08-23-academy-redesign-spec.md`**

- Nav structure (Academy first)  
- Lesson markdown template (Watch / Read / Explain / Do / Produce / Evidence)  
- A01 filled example with **real URLs**  
- Librarian Slack response format change spec  

---

## References

- [Studio channel map](../studio/channel-map.md)  
- [Wiki concept audit](../research/wiki-concept-audit.md)  
- [Phase 0 survey](../research/phase-0-survey.md) — research input only, not curriculum  
