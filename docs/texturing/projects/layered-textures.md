---
title: "Layered textures"
section: texturing
type: project
---

# Layered textures

!!! info "About this page"
    **Prerequisites** — Complete the Organic PBR lab and Lesson 7 — Texture painting & PBR materials first.  
    **Evidence folder** — `training/texturing/a02/`

A hands-on texturing project that adds non-destructive wear, dirt, and color variation layers on top of the Organic PBR lab base material using Ucupaint in Blender. The goal is to export an updated, Second Life-ready PBR map set and document the layer stack so the result can be recreated or edited later.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Blender | [Blender](https://www.blender.org) | Layered material editing, baking, and export to Second Life. |
    | Ucupaint | [Ucupaint](https://github.com/ucupumar/ucupaint) | Non-destructive PBR layer stacks inside Blender. |

=== "Paid tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Adobe Substance 3D Painter | [Adobe Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html) | Optional benchmark for editability comparison. |

## Watch

| Topic | Video | Why this one |
|---|---|---|
| Ucupaint workflow | [Ucupaint — Turn Blender Into Substance Painter](https://www.youtube.com/watch?v=d3KrMwAWJI0) | Shows layer channels and PBR painting directly inside Blender. |

## Read

| Source | Covers |
|---|---|
| [Ucupaint wiki](https://ucupumar.github.io/ucupaint-wiki/) | Layer channel setup, masks, and export. |
| [Ucupaint video tutorials index](https://ucupumar.github.io/ucupaint-wiki/video-tutorials/) | Official tutorial collection for specific layer workflows. |
| [Blender texture paint manual](https://docs.blender.org/manual/en/latest/sculpt_paint/texture_paint/index.html) | Blender's native texture painting basics. |

## Outcome

Add at least three non-destructive layers — base color variation, edge wear (roughness), and dirt (multiply) — on top of the Organic PBR lab maps. Export the full updated PBR map set so it can be uploaded to Second Life without depending on viewport-only layers. The project measures Ucupaint's editability against the Material Maker benchmark used in the studio experiment.

## Breedables workflow

1. Use the Organic PBR lab maps as the **Base** layer in Ucupaint.
2. Add three named layers with documented blend modes and mask sources.
3. Record every layer's purpose, channels affected, blend mode, and mask source in `training/texturing/a02/notes.md`.
4. Bake/export the complete map set — do not leave effects only in the viewport.
5. Compare editability against the Material Maker workflow in the studio experiments page.

## Evidence note

The evidence folder `training/texturing/a02/` is currently empty. The first artifact to produce is `training/texturing/a02/notes.md`. It must list the source base-map path, the commit hash, at least three named layers with blend modes and mask sources, and the exact filenames for exported maps. No rendered results are invented; screenshots and maps are produced by following the steps below.

## Hands-on lab

Follow the exact steps in the **Do** block. Every file must be saved to the exact path listed in the **Required artifacts** section. Name layers and exports consistently so the notes file can reconstruct the stack without opening Blender.

## Required artifacts

All artifacts must live under `training/texturing/a02/`.

- `notes.md` — base map source, commit hash, layer names, blend modes, mask sources, and exported filenames.
- `source/a02_layered.blend` — the Blender scene containing the intact Ucupaint layer stack.
- `maps/a02_basecolor.png` — updated base color map.
- `maps/a02_roughness.png` — updated roughness map.
- `maps/a02_normal.png` — updated normal map.
- `maps/a02_metallic.png` — updated metallic map (omit if your base material has none).
- `layers-before.png` — viewport screenshot of the base material before adding variation layers.
- `layers-after.png` — viewport screenshot of the final layered material.

## Sign-off checklist

A maintainer can verify this project when every box is ticked.

- [ ] `notes.md` exists and references the Organic PBR lab source path and commit hash.
- [ ] At least three layers are listed with unique names, affected channels, blend modes, and mask sources.
- [ ] `source/a02_layered.blend` opens and the Ucupaint layer stack is intact.
- [ ] `maps/` contains `a02_basecolor.png`, `a02_roughness.png`, `a02_normal.png`, and `a02_metallic.png` (if applicable).
- [ ] Exported maps use the correct Second Life color space setup: base color in sRGB; roughness, normal, and metallic in non-color data.
- [ ] `layers-before.png` and `layers-after.png` clearly show the same mesh with and without the variation layers.
- [ ] A row for this Ucupaint layered pass has been added or updated in the studio experiments page.

## Next track

Move on to [Retopology](../../modeling/projects/retopology-project.md) when this project is signed off.

## Do

1. Open the Organic PBR lab `.blend` or re-import its exported maps (`basecolor.png`, `roughness.png`, `normal.png`, `metallic.png`) onto the same test mesh.
2. Install/enable Ucupaint, create a new Ucupaint material on the mesh, and set the Organic PBR lab maps as the **Base** layer. Save the scene as `training/texturing/a02/source/a02_layered.blend`.
3. Capture a viewport screenshot of the unlayered base material and save it as `training/texturing/a02/layers-before.png`.
4. Create a new `training/texturing/a02/notes.md` file. Record the source base-map path and the current Git commit hash.
5. Add at least three non-destructive layers with these documented names and purposes:
- `color_variation` — affects Base Color, uses a MixRGB/overlay blend, masked by procedural noise or cavity.
- `edge_wear` — affects Roughness, uses lighten/subtract blend, masked by pointiness, bevel, or curvature.
- `dirt_mask` — affects Base Color, uses Multiply blend, masked by ambient occlusion or painted mask.
6. For each layer, add a row to `notes.md` containing: layer name, affected channels, blend mode, and exact mask source (node type/texture name).
7. Bake or export the updated full PBR map set to `training/texturing/a02/maps/` using exact filenames:
- `a02_basecolor.png`
- `a02_roughness.png`
- `a02_normal.png`
- `a02_metallic.png` (if your material uses metallic).
8. Set the correct color space on exported images before upload: base color sRGB; roughness, normal, and metallic non-color data.
9. Capture a viewport screenshot of the final layered material and save it as `training/texturing/a02/layers-after.png`.
10. Optional: upload `a02_basecolor.png`, `a02_roughness.png`, and `a02_normal.png` to Second Life and compare the result with the Organic PBR lab baseline.

## Produce

| Artifact | Path |
|----------|------|
| Layer stack notes | `training/texturing/a02/notes.md` |
| Source Blender scene with Ucupaint layers | `training/texturing/a02/source/a02_layered.blend` |
| Updated base color map | `training/texturing/a02/maps/a02_basecolor.png` |
| Updated roughness map | `training/texturing/a02/maps/a02_roughness.png` |
| Updated normal map | `training/texturing/a02/maps/a02_normal.png` |
| Updated metallic map | `training/texturing/a02/maps/a02_metallic.png` |
| Viewport before screenshot | `training/texturing/a02/layers-before.png` |
| Viewport after screenshot | `training/texturing/a02/layers-after.png` |

## Done when

- [ ] `notes.md` exists and references the Organic PBR lab source path and commit hash.
- [ ] At least three layers are listed with unique names, affected channels, blend modes, and mask sources.
- [ ] `source/a02_layered.blend` opens and the Ucupaint layer stack is intact.
- [ ] `maps/` contains `a02_basecolor.png`, `a02_roughness.png`, `a02_normal.png`, and `a02_metallic.png` if applicable.
- [ ] Exported maps use Second Life metallic/roughness color-space rules.
- [ ] `layers-before.png` and `layers-after.png` show the same mesh with and without the variation layers.
- [ ] A row for the Ucupaint layered pass is recorded in the studio experiments page.

## Related

- [Organic PBR material](organic-pbr-material.md)
- [Lesson 7 — Texture painting & PBR materials](../pbr-materials.md)
- [Ucupaint](../software/ucupaint.md)
- [Studio experiments](../../research/experiments.md)
- [Retopology](../../modeling/projects/retopology-project.md)
