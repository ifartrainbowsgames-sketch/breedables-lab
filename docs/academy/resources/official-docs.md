# Official documentation index

Primary **Read** links for Academy tracks and the tools registry. Prefer these over blog posts when explaining studio workflow.

---

## Core DCC

| Tool | Official docs | Registry page |
|------|---------------|---------------|
| Blender | https://docs.blender.org/manual/en/latest/ | [Blender](../../production/tools/blender.md) |
| Material Maker | https://github.com/RodZill4/material-maker/wiki | [Material Maker](../../production/tools/material-maker.md) |
| Ucupaint | https://github.com/ucupumar/ucupaint | [Ucupaint](../../production/tools/ucupaint.md) |

---

## 3D AI / retopo (review tracks)

| Tool | Official docs | Registry page |
|------|---------------|---------------|
| TripoSR | https://github.com/VAST-AI-Research/TripoSR | [TripoSR](../../production/tools/triposr.md) |
| RetopoFlow | https://github.com/CGCookie/retopoflow | [RetopoFlow](../../production/tools/retopoflow.md) |

---

## CC0 asset libraries

| Tool | License / docs | Registry page |
|------|----------------|---------------|
| Poly Haven | https://polyhaven.com/license | [Poly Haven](../../production/tools/poly-haven.md) |
| ambientCG | https://ambientcg.com/license | [ambientCG](../../production/tools/ambientcg.md) |

---

## Second Life platform

| Topic | Link |
|-------|------|
| PBR materials | https://wiki.secondlife.com/wiki/PBR_Materials |
| Mesh upload | https://wiki.secondlife.com/wiki/Mesh |
| LSL portal | https://wiki.secondlife.com/wiki/LSL_Portal |
| Animations | https://wiki.secondlife.com/wiki/How_to_create_animations |
| Studio baseline | [Platform baseline](../../secondlife/platform-baseline.md) |

---

## How Librarian uses this list

Each registry tool should have `doc_urls` pointing here or to the tool's own manual. Gaps surface via:

```bash
python -m librarian.cli gaps
python -m librarian.cli research-queue
```
