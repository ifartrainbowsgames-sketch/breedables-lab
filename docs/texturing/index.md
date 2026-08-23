---
title: "Texturing & Materials"
section: texturing
type: index
question: "How do I create professional surfaces and PBR materials?"
---
# Texturing & Materials

!!! abstract "This section answers one question"
    *How do I create professional surfaces and PBR materials?*

Everything about how a surface looks — PBR authoring, texture painting,
procedural materials, baking, masks and map sets. Second Life uses a
metallic/roughness workflow, so that is the workflow taught here.

## Topics

| Page | What it covers |
|------|----------------|
| [PBR materials](pbr-materials.md) | Metallic/roughness authoring that reads correctly in SL |

## Software

| Tool | Licence & role |
|------|----------------|
| [Material Maker](software/material-maker.md) | Free · MIT — procedural PBR generator |
| [Ucupaint](software/ucupaint.md) | Free — layer-based painting inside Blender |
| [Substance 3D Painter](software/substance-painter.md) | Paid — industry texturing standard |
| [Foundry Mari](software/mari.md) | Paid — high-end VFX texture painting |
| [Adobe Photoshop](software/photoshop.md) | Paid — general image editing |
| [Krita](software/krita.md) | Free · GPL — open-source painting |
| [Marmoset Toolbag](software/marmoset-toolbag.md) | Paid — baking and lookdev |
| [Marvelous Designer](software/marvelous-designer.md) | Paid — cloth and accessories |
| [Poly Haven](software/poly-haven.md) | CC0 — HDRIs, textures, models |
| [ambientCG](software/ambientcg.md) | CC0 — PBR material library |
| [3DTextures.me](https://3dtextures.me/) | CC0 — hand-authored sets, strong stylised and sci-fi selection |
| [cgbookcase](https://www.cgbookcase.com/) | Free PBR textures; smaller library, check each licence |
| [ShareTextures](https://www.sharetextures.com/) | Large free library — **licence varies per material, check before shipping** |

## Hands-on projects

Each project ends in committed evidence, not a watched video.

| Project | Outcome |
|---------|---------|
| [Organic PBR material](projects/organic-pbr-material.md) | Author fur/skin/scale and verify it in-world |
| [Layered textures](projects/layered-textures.md) | Non-destructive wear, dirt and colour variation |

## Pipeline stages owned by this section

These are the production-line stages this section is responsible for.

### Stage 5 — Texturing & PBR (Second Life Metallic/Roughness)

Author **PBR materials** that read correctly in Second Life: skin, fur-like surfaces, scales, eyes, accessories — with phenotype variation support.

!!! tip "Studio pick"
    **Material Maker + Ucupaint + Blender** — free, open pipeline aligned with E01. **Substance Painter** better for teams already subscribed; run E01 comparison before adopting. **Poly Haven / ambientCG** for CC0 inputs — always record provenance.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | blender.org | Shader editor, baking |
    | **Material Maker** | https://github.com/RodZill4/material-maker | Procedural PBR generators |
    | **Ucupaint** | https://github.com/ucupumar/ucupaint | Layers, hand paint in Blender |
    | **Poly Haven** | https://polyhaven.com/ | CC0 HDRIs, textures, models |
    | **ambientCG** | https://ambientcg.com/ | CC0 PBR materials |

=== "Paid tools"

    | Tool | Link | Best for | Cost note |
    |------|------|----------|-----------|
    | **Substance 3D Painter** | adobe.com | Industry texturing | Subscription — powerful but not required |
    | **Substance Designer** | adobe.com | Node materials | Overlap with Material Maker |
    | **Quixel / Megascans** | quixel.com | Scan libraries | License varies |

**How we use it**

- Procedural bases (Material Maker) + hand refinement (Ucupaint)  
- CC0 assets from Poly Haven / ambientCG with **provenance per file**  
- Validate **in-world** — Blender render alone is not enough

**What to complete**

- Studio labs: [Organic PBR material](../texturing/projects/organic-pbr-material.md), [Layered textures](../texturing/projects/layered-textures.md)  
- Experiments:   
- Read: [SL PBR wiki](https://wiki.secondlife.com/wiki/PBR_Materials), [platform baseline](../second-life/platform-baseline.md)  
- Produce: texture sets + **SL in-world screenshot**

**Evidence folder** — `training/texturing/a01/`, `training/texturing/a02/`, `research/experiments/e01/`  
**Related pages** — [Lesson 7 — Texture & PBR](../texturing/pbr-materials.md) · [Organic PBR material](../texturing/projects/organic-pbr-material.md) · [Layered textures](../texturing/projects/layered-textures.md)
