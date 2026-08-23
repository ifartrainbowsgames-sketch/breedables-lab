---
title: "Meta"
section: meta
type: index
question: "How is this wiki maintained?"
---
# Meta

!!! abstract "This section answers one question"
    *How is this wiki maintained?*

Records about the wiki itself, kept out of the reader-facing navigation so they
do not compete with production knowledge. Maintainers only.

| Page | What it covers |
|------|----------------|
| [Wiki style guide](wiki-style-guide.md) | The architecture and page rules, and why each exists |
| [Software page standard](software-page-standard.md) | What every tool card must contain |
| [Build plan](build-plan.md) | Page-by-page status tracking |
| [System build summary](system-build-summary.md) | What the tooling is and how it fits together |
| [Wiki concept audit](wiki-concept-audit.md) | Historical record of an earlier structural failure |

## The rules are enforced, not suggested

The information architecture lives in
`tools/librarian/librarian/wiki_schema.py` as data. Three things read it:

1. **`wiki-lint`** — validates placement, page types, duplicate topics,
   repeated headings and table-of-contents size. Runs in CI; a bad page fails
   the build.
2. **`wiki_page.py`** — renders pages from JSON in house style. Kimi supplies
   content, never layout, so generated pages cannot invent structure.
3. **`wiki-worker`** — the unattended loop. It derives its task queue from real
   gaps and commits only to a dated branch.

```powershell
cd tools/librarian
python -m librarian.cli wiki-lint            # validate the architecture
python -m librarian.cli wiki-worker --queue  # what needs doing
```
