# Tool registry (maintainers)

!!! info "Learners"
    **Do not start here.** Plugins do not teach Blender.

    → [Blender Foundations B01](../../academy/software/blender/b01-install-setup.md)  
    → [Full B01–B10 path](../../academy/software/blender/index.md)  
    → [Studio labs](../../academy/overview.md)

This page is for **studio records** in git: licenses, evidence links, CLI lookup.

---

## Core DCC

| Tool | Type | Pipeline step | Page |
|------|------|---------------|------|
| [Blender](blender.md) | **Application** (not a plugin) | All 3D work | Full DCC — learn elsewhere first |

---

## Studio add-ons & assets (not Blender tutorials)

| Tool | Type | Pipeline step | Evidence |
|------|------|---------------|----------|
| [Material Maker](material-maker.md) | Standalone app | A01 textures | [A01 lab](../../academy/tracks/a01-organic-pbr.md) |
| [Ucupaint](ucupaint.md) | Blender **add-on** | A02 layers | [A02 lab](../../academy/tracks/a02-layered-textures.md) |
| [RetopoFlow](retopoflow.md) | Blender **add-on** | A03 retopo | [A03 lab](../../academy/tracks/a03-retopology.md) |
| [TripoSR](triposr.md) | AI tool (research) | E02 blockouts | [Experiments](../experiments.md) |
| [Poly Haven](poly-haven.md) | CC0 asset site | Reference HDRIs/textures | Log in `training/texturing/assets/` |
| [ambientCG](ambientcg.md) | CC0 asset site | Reference PBR | Log in `training/texturing/assets/` |
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

Approval taxonomy: [Decision model](../decision-model.md) · [Promotion rules](../promotion-rules.md)

---

## Research candidates

Tools not in baseline seed: [Research candidates](research-candidates.md)

Survey source: [Phase 0 report](../../research/phase-0-survey.md)
