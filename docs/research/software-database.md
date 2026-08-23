---
title: "Software database"
section: research
type: reference
---
# Software database

!!! abstract "This page answers one question"
    *What software does this studio know about, and where is it documented?*

Every tool the studio has evaluated, in one table, pointing at its **canonical
page**. This page is an index — it deliberately holds no workflow instructions.
The subject sections teach; this lists.

**Legend:** ⭐ studio default for its job · **CC0** public-domain asset source.

## 3D modelling & sculpting

| Tool | Cost | What it's for | Canonical page |
|------|------|---------------|----------------|
| **Blender** ⭐ | Free · GPL | Modelling, sculpting, retopo, UV, rig, anim, export | [Blender](../modeling/blender/index.md) |
| Autodesk Maya | Paid | Industry modelling and animation standard | [Maya](../modeling/software/maya.md) |
| ZBrush | Paid | Industry organic sculpting standard | [ZBrush](../modeling/software/zbrush.md) |
| TopoGun | Paid | Dedicated retopology and map baking | [TopoGun](../modeling/software/topogun.md) |
| RetopoFlow | Free · GPL | Guided retopology inside Blender | [RetopoFlow](../modeling/software/retopoflow.md) |
| PureRef | Free tier / paid | Reference boards | [PureRef](../modeling/software/pureref.md) |

## Texturing & materials

| Tool | Cost | What it's for | Canonical page |
|------|------|---------------|----------------|
| **Material Maker** ⭐ | Free · MIT | Node-based procedural PBR generator | [Material Maker](../texturing/software/material-maker.md) |
| **Ucupaint** ⭐ | Free | Layer-based texture painting in Blender | [Ucupaint](../texturing/software/ucupaint.md) |
| Substance 3D Painter | Paid | Industry texturing standard | [Substance Painter](../texturing/software/substance-painter.md) |
| Substance 3D Designer | Paid | Node materials — overlaps Material Maker | [Paid vs free](paid-vs-free-matrix.md) |
| Foundry Mari | Paid | High-end VFX texture painting | [Mari](../texturing/software/mari.md) |
| Adobe Photoshop | Paid | General image editing | [Photoshop](../texturing/software/photoshop.md) |
| Krita | Free · GPL | Open-source painting | [Krita](../texturing/software/krita.md) |
| Marmoset Toolbag | Paid | Baking and lookdev | [Marmoset](../texturing/software/marmoset-toolbag.md) |
| Marvelous Designer | Paid | Cloth and accessories | [Marvelous Designer](../texturing/software/marvelous-designer.md) |
| **Poly Haven** | **CC0** | HDRIs, textures, models | [Poly Haven](../texturing/software/poly-haven.md) |
| **ambientCG** | **CC0** | PBR material library | [ambientCG](../texturing/software/ambientcg.md) |

## Rigging & animation

| Tool | Cost | What it's for | Canonical page |
|------|------|---------------|----------------|
| **Rigify** ⭐ | Free · bundled | Quadruped meta-rig generator | [Add-on catalog](../modeling/blender/addon-catalog.md) |
| Avastar | Paid | Exact Second Life skeleton for Blender | [Rigging & Animation](../rigging-animation/index.md) |
| Rokoko Studio Live | Free tier | Motion capture into Blender | [Candidate](candidates/rokoko-studio-live.md) |
| Animation Retargeting | Free | Reuse animation libraries across rigs | [Candidate](candidates/animation-retargeting.md) |

## Second Life

| Tool | Cost | What it's for | Canonical page |
|------|------|---------------|----------------|
| Second Life viewer | Free | Upload, in-world QA, LSL editing | [Viewer & tools](../second-life/viewer-and-tools.md) |

## Under evaluation — not approved

These are **research candidates**. None is cleared for production; see
[promotion rules](promotion-rules.md).

| Tool | Area | Card |
|------|------|------|
| TripoSR | Image-to-3D | [TripoSR](candidates/triposr.md) |
| InstantMesh | Image-to-3D | [InstantMesh](candidates/instantmesh.md) |
| TRELLIS.2 | Image-to-3D | [TRELLIS.2](candidates/trellis2.md) |
| Hunyuan3D-2.1 | Image-to-3D | [Hunyuan3D](candidates/hunyuan3d.md) — excluded from commercial use |
| DiffusedTexture | AI texturing | [DiffusedTexture](candidates/diffused-texture.md) |
| Texture Diffusion | AI texturing | [Texture Diffusion](candidates/texture-diffusion.md) |
| MatLat | Materials | [MatLat](candidates/matlat.md) |
| postSilver retopology_tool | Retopology | [postSilver](candidates/postsilver-retopology.md) |

## Official documentation

| Area | Source |
|------|--------|
| Blender | [Manual](https://docs.blender.org/manual/en/latest/) · [Python API](https://docs.blender.org/api/current/) |
| Material Maker | [docs.materialmaker.org](https://docs.materialmaker.org/) |
| Ucupaint | [Ucupaint wiki](https://ucupumar.github.io/ucupaint-wiki/) |
| RetopoFlow | [docs.retopoflow.com](http://docs.retopoflow.com/) |
| Poly Haven | [CC0 licence](https://polyhaven.com/license) |
| ambientCG | [Licence](https://ambientcg.com/license) |
| Second Life — PBR | [PBR Materials](https://wiki.secondlife.com/wiki/PBR_Materials) |
| Second Life — mesh | [Mesh upload](https://wiki.secondlife.com/wiki/Mesh) |
| Second Life — LSL | [LSL Portal](https://wiki.secondlife.com/wiki/LSL_Portal) |
| Second Life — animation | [How to create animations](https://wiki.secondlife.com/wiki/How_to_create_animations) |
| Second Life — Animesh | [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) |

## Maintaining this page

```powershell
cd tools/librarian
python -m librarian.cli show --query "<tool name>"
python -m librarian.cli wiki-videos      # refreshes per-software video sections
```

Adding a tool: create its card in the correct **subject** section, then add one
row here. Never document a tool twice — see the
[wiki style guide](../meta/wiki-style-guide.md).
