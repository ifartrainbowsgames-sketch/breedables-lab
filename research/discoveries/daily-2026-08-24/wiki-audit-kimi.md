## Executive summary

The wiki concept is now correct: it is a **learner-facing Academy + production log**, not a tool registry. The home page (`docs/index.md`) already uses the Outlands-style hub, card grids, and search hint. The biggest blockers are:

1. **Two critical Academy specs still contain `TODO/TBD`.**
2. **Most pages are image-less** despite the design benchmark requiring card thumbnails.
3. **Many package/lesson/lab pages probably do not pass the `software-page-standard.md` checklist** (verified training URLs, exercises, PASS/FAIL).
4. **`docs/production/tools/web-research-stack.md` looks stale** and likely still references the removed Wails stack / old ports.
5. **Navigation has orphan risks**: `docs/secondlife/` has only one page, `docs/studio/` has no index, and there are three overlapping “software index” pages in `docs/academy/software/`.

No MkDocs build warnings were reported, so the site renders—but that does not mean the content teaches yet.

---

## Wiki setup health (nav, hub, images, search UX)

| Area | Status | Notes / fix |
|------|--------|-------------|
| **Home hub** | ✅ Good | `docs/index.md` uses featured banner + card grids + `Ctrl+K` hint, matching `docs/studio/wiki-design-benchmarks.md`. |
| **Search UX** | ✅ Good | Material search is enabled; hint is visible. No `mkdocs_warnings` reported. |
| **Nav structure** | ⚠️ Needs review | `docs/production/*` files are labeled “Studio” section but live under `/production/`. `docs/secondlife/` has no index. `docs/studio/` has no index. |
| **Sticky quicknav** | ❌ Missing | `docs/studio/wiki-design-benchmarks.md` references `docs/javascripts/wiki-quicknav.js`; this file is not in the page inventory. Create it or remove the reference. |
| **Image coverage** | ❌ Poor | Only 7 pages report `has_images: true` out of ~80. Most lessons, labs, and research pages are wall-of-text. |
| **Image optimization script** | ⚠️ Verify | Benchmark references `scripts/optimize-wiki-images.py`. Verify it exists and runs in CI. |
| **Daily gap feed** | ❌ No data | `daily_gaps: null` in the audit. The daily pipeline is not producing Academy gap reports yet. |

---

## Broken or stale documentation (file path + fix)

### 1. `docs/academy/production-line.md`
- **Issue:** `contains TODO/TBD`.
- **Fix:** Replace every `TODO`/`TBD` with either:
  - a concrete stub + “Decision needed: see issue #N”, or
  - a link to a draft file in `docs/drafts/` so learners do not see incomplete content.

### 2. `docs/academy/professional-workflow/pipeline-stages.md`
- **Issue:** `contains TODO/TBD`.
- **Fix:** Same as above. Any stage without verified SL QA data should be marked “Draft — evidence needed” and linked to the matching Reference Creature experiment.

### 3. `docs/production/tools/web-research-stack.md`
- **Issue:** Title says “Go CLI & Chromium” and is 7,156 chars long; likely the pre-removal Wails/Go stack. User explicitly flagged “removed tools like Wails” and “wrong ports”.
- **Fix:** Rewrite to the current stack only:
  - **daily-wiki** for markdown generation,
  - **webscreen / browser tools** for research,
  - **Librarian** for link checking and gap queues,
  - **Kimi** for content editing.
  - Remove all Wails commands, `wails dev`, `localhost:34115`, or other old ports.
  - Add a “Status: Updated for current stack” header and a verification step: `grep -R "wails\|34115\|8080" docs/`.

### 4. `docs/index.md` — possible broken tutorial card link
- **Issue:** Snippet shows `[Tutorial arsenal](academy/resources/tutorials` without a visible closing `.md)`.
- **Fix:** Verify the source ends exactly with `.md)`. Suggested corrected line:
  ```markdown
  **[Tutorial arsenal →](academy/resources/tutorials.md)**
  ```

### 5. `docs/academy/start-here.md` — possible broken anchor
- **Issue:** Snippet ends with anchor `#layer-2-studio-labs-breedabl` (truncated). If the real heading id differs, the link is dead.
- **Fix:** Use a full page link instead of a fragile anchor:
  ```markdown
  [Studio labs →](tracks/a01-organic-pbr.md)
  ```
  Or add an explicit heading id:
  ```markdown
  ## Layer 2 · Studio labs (breedables projects) {#layer-2-studio-labs}
  ```

### 6. `docs/academy/software/software-index.md`, `docs/academy/software/index.md`, `docs/academy/software/packages/index.md`
- **Issue:** Three overlapping “software index” pages. Learners will not know which to click.
- **Fix:**
  - `docs/academy/software/index.md` → **learner hub** (big picture, three routes).
  - `docs/academy/software/packages/index.md` → **clickable tool cards only**.
  - `docs/academy/software/software-index.md` → either merge into the hub or rename to `wider-software-index.md` with a scope line: “Niche and alternate tools not in the main workflow.”

### 7. `docs/secondlife/platform-baseline.md` — section has no index
- **Issue:** Only one file in `docs/secondlife/`. Visitors landing on “Second Life” in nav get a single page.
- **Fix:** Create `docs/secondlife/index.md` as a hub:
  ```markdown
  # Second Life for breedables creators

  This section is the **last layer** of the pipeline. Learn general 3D first, then adapt for SL.

  - [Platform baseline](platform-baseline.md) — Animesh, PBR, LI, Linkset Data
  - [Exporting from Blender](../academy/software/blender/b10-export-to-sl.md)
  - [Second Life adaptation](../academy/professional-workflow/second-life-adaptation.md)
  ```

### 8. `docs/studio/` and `docs/production/` — mixed “Studio” section
- **Issue:** `docs/studio/` has no index; `docs/production/tools/index.md` is the de-facto tool registry but is labelled for maintainers.
- **Fix:** Add `docs/studio/index.md` that links to:
  - `docs/studio/system-build-summary.md`
  - `docs/studio/wiki-design-benchmarks.md`
  - `docs/production/tools/index.md` (maintainer registry)
  - `docs/studio-roadmap.md`

### 9. `docs/academy/software/packages/*.md` — may not pass the standard
- **Issue:** `docs/academy/software/software-page-standard.md` requires verified training URLs, exercises, artifacts, PASS/FAIL. Most package pages are ~1,500–2,200 chars—too short to contain all of that.
- **Fix:** Audit each package card against the standard. Add missing sections and link to the matching lesson/lab rather than duplicating long tutorials.

### 10. `docs/studio/wiki-design-benchmarks.md` — references unverified files
- **Issue:** Mentions `docs/javascripts/wiki-quicknav.js` and `scripts/optimize-wiki-images.py`.
- **Fix:** List these files in the repo. If missing, create them or delete the references.

---

## Academy gaps (lessons/labs missing Watch/Read/Do)

Per `docs/academy/software/software-page-standard.md`, every lesson/tool/lab should have:
- **Watch** — verified video URL(s)
- **Read** — official/manual/doc link(s)
- **Do** — exercise + output artifact + PASS/FAIL criteria

| File path | Type | Likely gap |
|-----------|------|------------|
| `docs/academy/software/blender/b01-install-setup.md` | Lesson | Needs a “Do” artifact (e.g. screenshot of Blender 4.x splash) and PASS/FAIL. |
| `docs/academy/software/blender/b02-interface-navigation.md` | Lesson | Needs Watch/Read/Do with viewport navigation challenge. |
| `docs/academy/software/blender/b03-mesh-modeling.md` | Lesson | Needs exercise: blockout a simple creature head, PASS criteria. |
| `docs/academy/software/blender/b04-sculpting.md` | Lesson | Needs exercise: sculpt primary/secondary forms, artifact image. |
| `docs/academy/software/blender/b05-retopology.md` | Lesson | Needs exercise with triangle/quad budget and SL land-impact note. |
| `docs/academy/software/blender/b06-uv-unwrapping.md` | Lesson | Needs exercise: unwrap creature head, check texel density. |
| `docs/academy/software/blender/b07-texture-painting-pbr.md` | Lesson | Needs exercise: bake/export PBR maps, PASS/FAIL. |
| `docs/academy/software/blender/b08-rigging-weight-painting.md` | Lesson | Needs exercise: simple armature + weight paint for Animesh. |
| `docs/academy/software/blender/b09-animation.md` | Lesson | Needs exercise: export a looped idle/walk. |
| `docs/academy/software/blender/b10-export-to-sl.md` | Lesson | Needs exercise: export `.dae`, import to SL, screenshot in-world. |
| `docs/academy/tracks/a01-organic-pbr.md` | Lab | Needs exact Watch/Read/Do and output location in `training/`. |
| `docs/academy/tracks/a02-layered-textures.md` | Lab | Same as above. |
| `docs/academy/tracks/a03-retopology.md` | Lab | Same as above. |
| `docs/academy/tracks/a04-rig-animation.md` | Lab | Same as above. |
| `docs/academy/tracks/a05-sl-fixture.md` | Lab | Same as above; should link to `b10-export-to-sl.md`. |
| `docs/academy/resources/tutorials.md` | Resource | Long list but not a path. Add per-stage “Watch → Read → Do” mini-playlists. |
| `docs/academy/resources/complete-courses.md` | Resource | Add PASS/FAIL for how to consume each course. |

**Suggested copy block to insert at the top of each lesson/lab:**

```markdown
## In this lesson

- **Watch:** (video link to be verified)
- **Read:** (official docs link to be verified)
- **Do:** (exercise description)
- **Artifact:** (file or screenshot the learner must produce)
- **PASS/FAIL:** (how to check the artifact)
```

Do **not** invent URLs. Use the verified links from `docs/academy/resources/official-docs.md` and `docs/academy/resources/training-videos-by-stage.md`, or leave a `<!-- TODO: verify URL -->` comment.

---

## Image gaps (slug + suggested source)

The home page references card images that probably do not exist yet, and most lessons have no inline visuals.

| Missing / likely missing asset | Suggested source |
|--------------------------------|------------------|
| `docs/assets/cards/start-here.png` | Custom 200×200 icon (roadmap / compass). |
| `docs/assets/cards/blender.png` | Blender Foundation press kit logo (do not hotlink; download and optimize). |
| `docs/assets/cards/breedables-research.png` | Screenshot from a breedable vendor or Reference Creature concept art. |
| `docs/assets/cards/second-life.png` | Second Life viewer screenshot or SL logo from official brand guidelines. |
| `docs/assets/cards/addons.png` | Collage of add-on icons (RetopoFlow, Ucupaint, Hard Ops, etc.). |
| `docs/assets/cards/production-line.png` | Pipeline diagram exported from `docs/academy/production-line.md`. |
| `docs/assets/cards/workflow.png` | Professional pipeline diagram (Maya → ZBrush → Substance → SL). |
| `docs/assets/cards/blender-path.png` | Screenshot of Blender 10-lesson folder or rendered creature. |
| `docs/assets/cards/studio-labs.png` | In-world screenshot placeholder or concept render. |
| `docs/assets/cards/tutorials.png` | Video-grid montage (use only fair-use thumbnails or custom graphic). |
| `docs/assets/inline/academy-overview.png` | Hub diagram from `overview.md`. |
| `docs/assets/inline/professional-workflow.png` | Stage pipeline diagram. |
| `docs/assets/packages/maya.png`, `zbrush.png`, `substance-painter.png`, etc. | Verify each exists; use vendor press kits or replace with text logo to avoid trademark issues. |
| `docs/assets/inbox/` | Reference Creature WIP screenshots should be dropped here and optimized. |

**Action:** run an automated asset inventory:
```bash
# list every image referenced in docs/
grep -oR 'assets/[^)]*' docs/ | sort -u
```
Compare against files on disk. Generate missing card thumbnails and run `scripts/optimize-wiki-images.py`.

---

## Top 5 fixes for today

### 1. Resolve TODO/TBD in the two master specs (human)
- **Files:** `docs/academy/production-line.md`, `docs/academy/professional-workflow/pipeline-stages.md`
- **Action:** For each `TODO`/`TBD`, either fill it with a concrete stub or move it to `docs/drafts/` and link a GitHub issue. Do not ship incomplete master specs.

### 2. Purge Wails / old ports from web-research-stack.md (human)
- **File:** `docs/production/tools/web-research-stack.md`
- **Action:** Rewrite to current daily-wiki + webscreen + Librarian + Kimi stack. Add a CI-style grep check to prevent regressions.

### 3. Add Watch/Read/Do + PASS/FAIL to every Blender lesson and studio lab (AI + human verify)
- **Files:** `docs/academy/software/blender/b01-install-setup.md` through `b10-export-to-sl.md`; `docs/academy/tracks/a01-organic-pbr.md` through `a05-sl-fixture.md`
- **Action:** AI drafts the blocks using verified URLs from existing resource pages. Human verifies URLs and PASS criteria.

### 4. Generate and optimize missing card images (automated + human art pass)
- **Files:** `docs/assets/cards/*.png`, `docs/assets/inline/*.png`
- **Action:** Script inventory of missing images; create 200×200 PNGs under 10 KB; run optimizer; update `docs/index.md` if any card references change.

### 5. Fix navigation / orphan roots (human)
- **Files:** create `docs/secondlife/index.md`, `docs/studio/index.md`; reconcile `docs/academy/software/index.md`, `software-index.md`, and `packages/index.md`; verify `docs/javascripts/wiki-quicknav.js` exists.
- **Action:** Give every top-level section an index hub and remove duplicate index pages or scope them clearly.

---

## Optional: breedables research angle

The Academy and the Reference Creature pipeline should feed each other:

- **Research pages** (`docs/research/breedables-inventory-and-software.md`, `docs/research/breedables-market-study.md`, `docs/research/breedables-case-studies.md`) already define what exists and what niches are open. Use them to decide which **A01–A05 lab** to prioritize.
- Every Reference Creature experiment should update the matching lab with:
  - in-world screenshots dropped in `docs/assets/inbox/`
  - land-impact and LI numbers
  - tool verdicts (e.g. “Ucupaint vs Material Maker for SL PBR”)
- Use `docs/production/tools/candidates/*.md` only as a research backlog. When a candidate graduates, add a learner-facing card in `docs/academy/software/packages/` and remove the EXPERIMENTAL language from Academy pages.
