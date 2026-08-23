---
title: "Wiki design benchmarks — what we copy (and what we skip)"
section: meta
type: meta
---
# Wiki design benchmarks — what we copy (and what we skip)

**Status:** DESIGN REFERENCE — guides MkDocs Material layout and Kimi image tasks  
**Compared:** [Outlands Wiki](https://wiki.uooutlands.com/Main_Page) (MediaWiki), Fandom/Gamepedia, Wiki.js, MkDocs Material

We stay on **MkDocs + git** (Kimi writes markdown, GitHub Pages deploys). We copy **patterns**, not platforms.

---

## Benchmark wikis

| Wiki | Platform | Best parts | Skip |
|------|----------|------------|------|
| [Outlands Wiki](https://wiki.uooutlands.com/Main_Page) | MediaWiki | Hub main page, featured banner, image card grids, category link walls, item counts | PHP stack, no git-native AI pipeline |
| [Fandom / Gamepedia](https://community.fandom.com/wiki/Help:FandomDesktop) | MediaWiki | Pinned quick nav while scrolling, fluid width, dark/light themes, infoboxes | Ads, proprietary hosting |
| [Wiki.js](https://js.wiki/) | Node.js | Beautiful reader UI, asset manager, git sync option | Extra server if we already have MkDocs |
| [MkDocs Material](https://squidfunk.github.io/mkdocs-material/) | Static | Instant search (Ctrl+K), tabs, mobile, zero ops | Not a WYSIWYG wiki out of the box |
| [Diátaxis](https://diataxis.fr/) | Framework, not software | One page = **one** job: tutorial, how-to, reference, or explanation | Its four-way folder split — our stage/lesson split already works |

---

## Patterns we implement

### 1. Hub main page (Outlands → `docs/index.md`)

| Outlands | Breedables Lab |
|----------|----------------|
| King's Faire featured banner | **Latest research** banner (Kimi inventory) |
| Main Pages 3×2 image grid | **Main pages** + **Popular pages** card grids |
| New Player / World / PvP columns | **Learn · Build · Research · Studio** columns |
| Search box | Material search + **Ctrl+K** hint |

### 2. Package index cards (Fandom tile nav → `docs/academy/software/packages/index.md`)

Every software tool gets a **clickable card** with logo, title, one-line description.

### 3. Images everywhere (Fandom + Outlands)

- **Card thumbs:** `docs/assets/cards/{slug}.png` (200×200, &lt;10 KB)
- **Inline headers:** `docs/assets/inline/{slug}.png`
- **Kimi discovers URLs:** `python -m librarian.cli wiki-images`
- **Your screenshots:** drop MB files in `docs/assets/inbox/` → `python scripts/optimize-wiki-images.py`

### 4. Sticky quick navigation (Fandom pinned local nav)

Hub pages show a **quick-link bar** that stays visible while scrolling (see `docs/javascripts/wiki-quicknav.js`).

### 5. Reader UX (Material features enabled in `mkdocs.yml`)

- `navigation.instant` — faster page changes  
- `navigation.tabs.sticky` — top-level tabs stay visible while scrolling  
- `navigation.top` — back-to-top while scrolling long inventory pages  
- `navigation.footer` — prev/next links, so every page has an obvious next step  
- `navigation.indexes` — sections open on a real landing page, not a dead folder  
- `search.suggest` + `search.highlight` — typeahead search  
- `toc.follow` + `toc_depth: 3` — TOC tracks scroll and stays short  
- `content.action.edit` — edit-this-page pencil straight to GitHub  

**Deliberately off:** `navigation.expand`. With ~90 pages an expanded sidebar is
longer than most pages, which defeats the point of a sidebar.

---

## Kimi automation map

| Task | Command | Output |
|------|---------|--------|
| Find card/logo URLs | `wiki-images` | `docs/assets/manifest.json` + PNG cards |
| Update breedables research | `breedables-research` | `docs/research/breedables-inventory-and-software.md` |
| Daily UX/content brief | `daily-wiki --wiki-evolve` | `research/discoveries/daily-*/wiki-evolution.md` |
| Whole-wiki audit | `wiki-audit` or `daily-wiki --wiki-audit` | `research/discoveries/daily-*/wiki-audit-kimi.md` |

---

## Image licensing rules (for Kimi + humans)

1. **Software logos** — trademark/fair use for identification; link to official site on package page.  
2. **Wikimedia** — use thumbnail URLs; note license in manifest.  
3. **Breedables vendor art** — only official promotional images; never scrape user uploads.  
4. **Your work** — commit `training/` screenshots; optimize before wiki embed.

---

## Next UX upgrades (backlog)

- [ ] Infobox template for breedables case studies (species, status, marketplace link)  
- [ ] Auto-generated hub stats line (“N articles · last Kimi update …”)  
- [ ] Breedables line cards on research hub (KittyCats, Meeroos, …) with Kimi-found art  
- [ ] `wiki-images` in weekly CI after Kimi login available on runner  

→ [System build summary](system-build-summary.md) · [Wiki concept audit](wiki-concept-audit.md)

---

## Page style rules (the ones that actually keep it readable)

These are not preferences — every one of them fixes a real defect this wiki had.

| Rule | Why | What it looked like when broken |
|------|-----|--------------------------------|
| **Never repeat a heading on one page.** Recurring labels get `**bold**`, not `###`. | Repeated headings flood the table of contents until it is useless. | `production-line.md` had 8 headings × 16 stages = 128 near-identical TOC rows. |
| **Aim for under ~25 TOC entries per page.** | A TOC you cannot scan is decoration. | Same page: ~130 entries. Now 22. |
| **Answer first.** The decision goes in `!!! tip "Studio pick"` above the evidence tables. | Readers want the pick; the tables justify it. | The pick was buried under two tool tables. |
| **Sentence case titles, no internal codes.** "Mesh modeling for organic creatures", never "B03 — Mesh Modeling". | Codes are folder names. Learners do not know them. | 9 of 10 lesson titles led with `B0N`; the 10th did not. |
| **Page metadata goes in an `!!! info "About this page"` card.** | Loose bold lines without trailing double-spaces silently collapse into one run-on paragraph. | Every lesson page from 2 to 10 rendered its metadata as a single blob. |
| **Free vs paid comparisons go in `=== "Free tools"` content tabs.** | Halves page height and puts the comparison side by side. | Two stacked tables per stage, 32 tables on one page. |
| **Maintainer material goes last, inside `??? note`.** | Templates and cheat sheets are not what a learner opens the page for. | The stage template was the second thing on the production line page. |
| **Anchors: one dash per separator.** `#5-high-low-baking`, not `#5--high--low-baking`. | Hand-written double dashes silently 404. | 18 dead in-page links across 14 files. |

**Enforcement:** `mkdocs build --strict` fails the build on any broken link or
anchor, and [`.github/workflows/wiki-links.yml`](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/main/.github/workflows/wiki-links.yml)
checks external URLs weekly. The heading and casing rules are written into the
Kimi wiki-evolution prompt (`tools/librarian/librarian/kimi.py`), so drafted
pages arrive in house style rather than needing a cleanup pass.

---

## How the rules are enforced

The architecture is **data**, not prose. It lives in
`tools/librarian/librarian/wiki_schema.py` and everything else reads from it,
so the structure cannot drift by being described differently in two places.

| Layer | File | What it prevents |
|-------|------|------------------|
| The contract | `wiki_schema.py` | Sections, page types, and which folder each type lives in |
| The gate | `wiki_lint.py` | Wrong section, duplicate topic, repeated headings, oversized TOC, internal codes, run-on metadata |
| The author | `wiki_page.py` | Kimi writing Markdown at all — it emits JSON and a renderer owns the layout |
| The loop | `wiki_worker.py` | Unattended work touching `main`, or writing a page that fails the gate |
| CI | `.github/workflows/wiki-lint.yml` | Any of the above reaching the published site |

### Navigation is derived, not maintained

There is no `nav:` block in `mkdocs.yml`. [Awesome Nav](https://lukasgeiter.github.io/mkdocs-awesome-nav/)
builds the sidebar from the folder tree plus a `.nav.yml` in each folder. Put a
page in the right folder and it appears; there is nothing to keep in sync.

### Front matter is required

```yaml
---
title: "Retopology"
section: modeling      # must match the folder the file is in
type: topic            # index | topic | software | project | path | reference | candidate | meta
---
```

`type` decides where the page is allowed to live. A `software` page must sit in
`<section>/software/`, a `project` in `<section>/projects/`, an Academy `path`
in `academy/paths/`. The linter fails the build otherwise.

### Commands

```powershell
cd tools/librarian
python -m librarian.cli wiki-lint             # validate everything
python -m librarian.cli wiki-worker --queue   # what needs doing, in priority order
python -m librarian.cli wiki-worker --once    # one maintenance cycle
python -m librarian.cli wiki-worker --loop --interval 1800
```

### Why Kimi cannot break the layout any more

Kimi is never asked for Markdown. It returns a JSON object describing content —
title, summary, studio pick, tool rows, section bodies — and `wiki_page.render`
turns that into house style: metadata card, answer-first studio pick, free/paid
tool tabs, unique headings. If the rendered page fails `wiki-lint`, the write is
refused and the cycle reports the rejection instead of committing it.

That is the whole trick: **generate, validate, then write** — with the validator
holding a veto.

