---
title: "Tool registry (maintainers)"
section: research
type: reference
---
# Tool registry (maintainers)

!!! info "Learners"
    **Do not start here.** Plugins do not teach Blender.

    → [Blender Foundations B01](../tools/blender/install-and-setup.md)  
    → [Full B01–B10 path](../tools/blender/index.md)  
    → [Studio labs](../academy/index.md)

This page is for **studio records** in git: licenses, evidence links, CLI lookup.

---

## Core DCC

| Tool | Type | Pipeline step | Page |
|------|------|---------------|------|
| [Blender](../tools/blender/index.md) | **Application** (not a plugin) | All 3D work | Full DCC — learn elsewhere first |

---

## Studio add-ons & assets (not Blender tutorials)

| Tool | Type | Pipeline step | Evidence |
|------|------|---------------|----------|
| [Material Maker](../tools/material-maker/index.md) | Standalone app | A01 textures | [Organic PBR material](../projects/organic-pbr-material.md) |
| [Ucupaint](../tools/ucupaint/index.md) | Blender **add-on** | A02 layers | [Layered textures](../projects/layered-textures.md) |
| [RetopoFlow](../tools/retopoflow/index.md) | Blender **add-on** | A03 retopo | [Retopology](../projects/retopology-project.md) |
| [TripoSR](candidates/triposr.md) | AI tool (research) | E02 blockouts | [Experiments](experiments.md) |
| [Poly Haven](../tools/poly-haven/index.md) | CC0 asset site | Reference HDRIs/textures | Log in `training/texturing/assets/` |
| [ambientCG](../tools/ambientcg/index.md) | CC0 asset site | Reference PBR | Log in `training/texturing/assets/` |
| [Web research stack](web-research-stack.md) | Go CLI + Chromium | R&D screening & search | `tools/webscreen/` |

---

## Internal status (reviewers only)

Librarian DB still tracks workflow status for approval workflows. **Learners should not see these labels on lesson pages.**

```powershell
cd tools\librarian
python -m librarian.cli list
python -m librarian.cli show --query "material"
python -m librarian.cli content-gaps
```

Approval taxonomy: [Decision model](decision-model.md) · [Promotion rules](promotion-rules.md)

---

## Research candidates

Tools not in baseline seed: [Research candidates](candidates/index.md)

Survey source: [Phase 0 report](index.md)
