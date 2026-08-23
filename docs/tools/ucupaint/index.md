---
title: "Ucupaint"
section: tools
type: software
---

# Ucupaint

!!! info "About this page"
    **Prerequisites** — Comfortable Blender UV unwrapping, material nodes, and Edit Mode. Complete [Lesson 6 — UV unwrapping](../blender/uv-mapping.md) and [Organic PBR material](../../projects/organic-pbr-material.md) first.  
    **Evidence folder** — `training/texturing/a02/`

Ucupaint is an open-source Blender add-on for non-destructive, layer-based texture painting and PBR material management. It turns Blender's node tree into a Photoshop-style layer stack so you can hand-paint breedable coats, masks, and phenotype variations without leaving Blender.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Ucupaint | [Ucupaint](https://github.com/ucupumar/ucupaint) | Non-destructive layer painting and PBR texture management directly inside Blender. |

=== "Paid tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Adobe Substance 3D Painter | [Adobe Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html) | Industry-standard procedural and hand-painted texturing with advanced baking. |

## Watch

!!! tip "Play it in Tutorials"
    The player lives on [Tutorials](../../tutorials/ucupaint.md). Titles below stay so you can see what we picked.


| Topic | Video | Why this one |
|---|---|---|
| Ucupaint workflow | [Ucupaint — layered PBR in Blender](https://www.youtube.com/watch?v=d3KrMwAWJI0) | Primary reference for the Substance-like layer workflow inside Blender. |
| Developer tutorials | [Ucupumar — Ucupaint tutorials](https://www.youtube.com/@ucupumar) | Official developer channel covering new features and layer techniques. |

## Read

| Source | Covers |
|---|---|
| [Ucupaint wiki](https://ucupumar.github.io/ucupaint-wiki/) | Official installation, layer types, channel system, masks, baking, and FAQ. |
| [Ucupaint GitHub repository](https://github.com/ucupumar/ucupaint) | Source code, releases, issue tracker, and GPL-3.0 license text. |

## Before you start

Ucupaint is a Blender add-on, not a beginner Blender course. You must already know Blender UVs, materials, and Edit Mode. If your mesh has stretched UVs or no material slot, Ucupaint cannot fix that for you. Work through [Lesson 6 — UV unwrapping](../blender/uv-mapping.md) and build at least one complete material in [Organic PBR material](../../projects/organic-pbr-material.md) before installing the add-on.

## What Ucupaint does

Ucupaint wraps Blender's material node tree into a manageable layer panel. Each layer can carry multiple PBR channels—Color, Roughness, Normal, Height, Metallic, and others—and you control visibility with masks, opacity, and blending modes. The stack stays editable until you bake it into plain image textures for export. This makes it practical for concept iteration, cleanup, and hand-painted detail without building massive node networks by hand.

## Core concepts

**Layer** — One paintable slot that can contain several PBR channels at once.

**Channel** — A single material property such as Color, Roughness, or Normal, managed per layer.

**Mask** — A grayscale control that hides or reveals parts of a layer non-destructively.

**Group** — A folder-like container for organizing related layers and masks.

**Bake** — The process that flattens the editable layer stack into export-ready image textures.

## Breedables use cases

- **Hand-painted refinement** over procedural base coats from [Material Maker](../material-maker/index.md) or [Adobe Substance 3D Painter](../substance-painter/index.md).
- **Detail layers** for fur patterns, whisker spots, scale plates, and claw tips.
- **Phenotype masks** so a single mesh can produce several coat variations.
- **Cleanup** after procedural generation to fix seams, stretching, or color drift.
- **Rapid iteration** inside Blender before committing textures to the Second Life export step.

## Installation

1. Download the latest release `.zip` from the [GitHub releases page](https://github.com/ucupumar/ucupaint/releases).
2. In Blender, open **Edit > Preferences > Add-ons > Install...** and select the `.zip`.
3. Enable the **Ucupaint** add-on.
4. Select your mesh, open the **Ucupaint** panel in the material properties, and create a new paint layer set.
5. Verify that the generated node group connects to the Principled BSDF and that UVs read correctly before painting.

## Basic texture workflow

1. **Prepare the mesh.** Finish retopology and UV unwrapping; assign a material slot.
2. **Create a Ucupaint layer set.** The add-on builds the node group and image textures automatically.
3. **Paint the base color** on the Color channel using Blender's Texture Paint mode.
4. **Add detail layers** for roughness variation, normal detail, or secondary color patterns.
5. **Use masks** to restrict layers to specific body parts or phenotype zones.
6. **Adjust blending** with opacity and layer modes until the look matches the concept art.
7. **Bake the result** to PNG images and save them next to your `.blend` file for the Second Life upload step.
8. **Record the outcome** in [Studio experiments](../../research/experiments.md) with render comparisons and file sizes.

## Decision status

Ucupaint is currently a **test candidate**, not a replacement for [Material Maker](../material-maker/index.md). The studio is evaluating it alongside Material Maker for layer-based refinement. Comparison criteria include baking speed, maximum practical layer count, mask edge quality, and how cleanly the baked textures fit the Second Life upload workflow. Results are tracked in [Studio experiments](../../research/experiments.md).

## License and output considerations

Ucupaint is released under **GPL-3.0**. The license covers the add-on source code and any modifications you redistribute, not the image textures you paint with it. Still, if the studio ships a customized fork or bundled tool based on Ucupaint, that work must remain GPL-3.0. Document any studio-authored tooling derived from Ucupaint in the license row of [Studio experiments](../../research/experiments.md).

## Librarian lookup

Query the studio librarian for the latest release, installation notes, and evidence files:

```powershell
python -m librarian.cli show --query "ucupaint"
```

Evidence files for academy track A02 live under `training/texturing/a02/`.

## Do

1. Install the latest Ucupaint release from GitHub.
2. Create a new Ucupaint layer set on a mesh with valid UVs.
3. Paint a base color layer in Blender Texture Paint mode.
4. Add roughness and normal detail layers.
5. Use masks to isolate patterns to body regions.
6. Bake the layer stack to export-ready PNG textures.
7. Record results and license notes in the studio experiments log.

## Produce

| Artifact | Path |
|----------|------|
| Primary tutorial video | `https://www.youtube.com/watch?v=d3KrMwAWJI0` |
| Official documentation | `https://ucupumar.github.io/ucupaint-wiki/` |
| Source repository | `https://github.com/ucupumar/ucupaint` |
| Studio evidence folder | `training/texturing/a02/` |

## Related

- [Lesson 6 — UV unwrapping](../blender/uv-mapping.md)
- [Organic PBR material](../../projects/organic-pbr-material.md)
- [Layered textures](../../projects/layered-textures.md)
- [Material Maker](../material-maker/index.md)
- [Adobe Substance 3D Painter](../substance-painter/index.md)
- [Studio experiments](../../research/experiments.md)
