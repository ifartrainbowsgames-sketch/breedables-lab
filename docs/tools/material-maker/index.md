---
title: "Material Maker"
section: tools
type: software
---
# Material Maker

![Material Maker](../../assets/inline/material-maker.png){ width="120" }

!!! info "About this page"
    **Canonical home** — everything about Material Maker lives here  
    **Studio status** — **USE NOW** for procedural bases; promote to production after [E01](../../research/experiments.md#e01-pbr-pipeline-shootout) passes with committed evidence  
    **Not a Blender tool** — it is a separate application; it does not teach Blender, UVs or shader nodes

Material Maker is a standalone node-based generator for procedural PBR
textures. The studio uses it to build **reusable organic material generators** —
skin, fur-like surfaces, scales, shell, horn, claws, pads — so a breedable's
phenotype variants come from one graph instead of a folder of hand-painted maps.

## At a glance

| | |
|---|---|
| **Licence** | Open source — [MIT](https://github.com/RodZill4/material-maker/blob/master/LICENSE.md) |
| **Cost** | Free, including commercial use |
| **Official site** | [materialmaker.org](https://materialmaker.org/) |
| **Download** | [GitHub releases](https://github.com/RodZill4/material-maker/releases) |
| **Source** | [RodZill4/material-maker](https://github.com/RodZill4/material-maker) |
| **Documentation** | [docs.materialmaker.org](https://www.materialmaker.org/) |
| **Paid equivalent** | Adobe Substance 3D Designer — see [paid vs free](../../research/paid-vs-free-matrix.md) |

## Before you use it

Material Maker generates maps; it does not apply them. Learn the Blender side first:

1. [PBR materials](../blender/pbr-materials.md) — how metallic/roughness works and where maps plug in.
2. [Organic PBR material project](../../projects/organic-pbr-material.md) — the lab this tool feeds.

## Official learning

| Type | Resource |
|------|----------|
| Manual | [docs.materialmaker.org](https://www.materialmaker.org/) |
| First steps | [Getting started](https://github.com/RodZill4/material-maker/wiki) |
| Node reference | [200+ nodes](https://github.com/RodZill4/material-maker/wiki) |
| Export to Blender | [Exporting materials](https://github.com/RodZill4/material-maker/wiki) |
| Author's channel | [@RodZill4](https://www.youtube.com/@RodZill4) |

## Exercise

Author one **procedural skin or fur** material and export the map set for a
Second Life PBR test prim.

**Pass when:** node graph screenshot committed, PNG exports committed, and the
material verified in EEVEE *and* in-world.
**Evidence folder:** `training/texturing/a01/`

## Studio notes

- First-choice open-source procedural authoring candidate.
- Registry lookup: `python -m librarian.cli show --query "material maker"`

## Videos

!!! tip "Play it in Tutorials"
    The player lives on [Tutorials](../../tutorials/material-maker.md). Titles below stay so you can see what we picked.


**Beginner**


**[Material Maker Official Website](https://material-maker.app/)** — Official hub for downloading Material Maker, browsing docs, and finding community resources for procedural texture creation.

**[Material Maker Official User Manual](https://material-maker.app/doc1.0/index.html)** — Comprehensive official documentation covering the node graph, PBR export, and painting workflows used to build game-ready creature materials.

**[RodZilla (Material Maker Developer) YouTube Channel](https://www.youtube.com/@RodZilla3D)** — The developer's official channel for release overviews, feature demos, and tutorial videos about Material Maker.

**[Material Maker on itch.io](https://rodzilla.itch.io/material-maker)** — Official download mirror with version history, devlogs, and community comments for the latest releases.

**Intermediate**


**[Material Maker GitHub Repository](https://github.com/RodZill4/material-maker)** — Source code, issue tracker, and bundled example materials for users who want to customize or extend the tool.

**[Material Maker Example Material Library](https://github.com/RodZill4/material-maker/tree/master/material_maker/examples)** — Built-in procedural material examples to dissect node networks and learn how to author tileable creature skin, scales, and fur patterns.

---
