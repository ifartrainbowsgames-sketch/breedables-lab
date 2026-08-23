---
title: "Organic PBR material"
section: texturing
type: project
---

# Organic PBR material

!!! info "About this page"
    **Prerequisites** — [Lesson 6 — UV unwrapping](../../modeling/uv-mapping.md) and [Lesson 7 — Texture painting & PBR materials](../pbr-materials.md)  
    **Evidence folder** — `training/texturing/a01/`

A hands-on project that produces a complete organic PBR material set (base color, roughness, normal) for Second Life, with exact filenames and pass conditions so an empty evidence folder can be filled systematically.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Blender | [Blender](https://www.blender.org/) | UV unwrapping, texture painting, Principled BSDF material setup, and PNG export |
    | Material Maker | [Material Maker](https://github.com/RodZill4/material-maker) | Procedural organic patterns such as fur, scales, or leaf veins when hand-painting is too slow |

=== "Paid tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Adobe Substance 3D Painter | [Adobe Substance 3D Painter](https://www.adobe.com/products/substance3d-painter.html) | Layered hand-painted/detail work; optional and must be documented if used |

## Watch

| Topic | Video | Why this one |
|---|---|---|
| Blender shader basics | [Blender 4.0 Beginner Tutorial — Part 1](https://www.youtube.com/watch?v=B0J27sf02NU) | Official Blender Foundation channel; stable intro to the node editor used for PBR setup |
| PBR texturing workflow | [PBR Texturing in Blender (Ryan King Art)](https://www.youtube.com/watch?v=4_xYiw1nL5M) | Practical metallic/roughness setup that maps directly to Second Life PBR expectations |
| Material Maker intro | [Material Maker — procedural PBR](https://www.youtube.com/watch?v=8MMSS2F5vtc) | Procedural alternative to hand-painting; useful for breedable skin/fur variants |
| SL PBR upload | [Gaia Clift — SL mesh upload](https://www.youtube.com/watch?v=uZ5KyLvivkw) | Viewer-side upload workflow; pair with [Second Life platform baseline](../../second-life/platform-baseline.md) |

## Read

| Source | Covers |
|---|---|
| [Blender manual — shader nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/index.html) | Node editor concepts used to wire PBR maps |
| [Blender manual — UV unwrapping](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/introduction.html) | How to produce a clean single-tile UV layout before painting |
| [Material Maker wiki](https://github.com/RodZill4/material-maker/wiki) | Procedural material export settings if Material Maker is used |
| [Second Life wiki — PBR Materials](https://wiki.secondlife.com/wiki/PBR_Materials) | Viewer-side material channel expectations |
| [Poly Haven license](https://polyhaven.com/license) | CC0 provenance requirements for any reference assets used |

## Outcome

By the end of this lab you will have authored one organic PBR material — fur, skin, scales, or a leaf-like surface — that:

- Uses the **metallic/roughness** workflow compatible with Second Life PBR.
- Exports cleanly as PNG at a documented power-of-two resolution.
- Looks correct in the Blender viewport **and** in-world on a test prim.

Watching tutorials alone does **not** complete this lab. You must commit the exact artifacts listed below to `training/texturing/a01/`.

!!! danger "Prerequisites"
    **This lab does not teach Blender.** Complete [Lesson 6 — UV unwrapping](../../modeling/uv-mapping.md) and [Lesson 7 — Texture painting & PBR materials](../pbr-materials.md) first. Material Maker is optional and is a separate app, not a Blender lesson.

## First artifact — base color map

The first file you must place in the evidence folder is the base color map. Do not move on to roughness or normal until this file passes its checklist.

**Target file**

```
training/texturing/a01/maps/organic-basecolor_1024.png
```

**Exact steps**

1. Create the folder tree: `training/texturing/a01/source/` and `training/texturing/a01/maps/`.
2. Open Blender and load or create a simple organic test mesh (a subdivided cube, a studio test head, or a small body block). Save it as `training/texturing/a01/source/organic-material.blend`.
3. UV unwrap the mesh to a single 0–1 UV tile. No overlapping UV islands outside the tile.
4. Create a new image texture named `organic-basecolor_1024.png`, resolution **1024 × 1024**, 8-bit sRGB.
5. Paint or generate the organic base color directly on the mesh. Use only your own work or CC0 assets.
6. Save the image to `training/texturing/a01/maps/organic-basecolor_1024.png` using Blender's `Image > Save As` or File Output node.
7. Append one line to `training/texturing/a01/notes.md`: `base color: 1024x1024 PNG, sRGB, <source description>`.

**Pass conditions for first artifact**

- [ ] File exists at exactly `training/texturing/a01/maps/organic-basecolor_1024.png`.
- [ ] File is a 1024 × 1024 PNG.
- [ ] It is assigned to the Base Color socket of a Principled BSDF material in `organic-material.blend`.
- [ ] It renders correctly in the Blender material viewport (shaded or rendered mode) with no pink/missing texture.
- [ ] `notes.md` records whether it was hand-painted, procedurally generated, or derived from a CC0 asset with the asset name/URL.

## Full project workflow

After the base color map passes, finish the remaining PBR channels and validate them in-world.

1. **Pick a species surface** (e.g. rabbit fur, dragon scale, leaf). One material, one species — do not build a generic shader library yet.
2. **Blockout in Blender:** low-poly test mesh or reuse a studio test head/body block. Store the source blend under `source/`.
3. **Author remaining PBR maps:** `organic-roughness_1024.png` (non-color, linear) and `organic-normal_1024.png` (non-color, OpenGL Y+ unless Second Life expects otherwise). For organic materials, Metallic is usually 0.0; leave it as a constant value in the material, not a map, unless you have a specific reason.
4. **Optional Material Maker pass:** if you use it, save the `.mm` source as `training/texturing/a01/source/organic-material.mm` and export PNGs to `maps/`.
5. **Bake / export** at power-of-two resolution (1024 or 2048 — document the choice in `notes.md`).
6. **SL validation:** upload the material to a test prim in-world, take a screenshot, and note the lighting environment.

## Hands-on lab

1. Complete the [first artifact](#first-artifact-base-color-map) steps above and verify the pass conditions before continuing.
2. Create `organic-roughness_1024.png` (1024 × 1024, linear, grayscale or RGB non-color) and plug it into the Roughness socket.
3. Create `organic-normal_1024.png` (1024 × 1024, non-color, OpenGL normal) and plug it into the Normal socket via a Normal Map node.
4. Export a viewport screenshot from Blender and save it as `training/texturing/a01/blender-viewport.png`. The screenshot must clearly show the textured mesh in rendered or material-preview mode.
5. Upload the textures and apply them to a test prim in Second Life. Capture the in-world view and save it as `training/texturing/a01/sl-inworld.png`.
6. Finalize `training/texturing/a01/notes.md` with: resolution chosen, Blender/Material Maker versions, any CC0 asset IDs used, and one known limitation or next fix.

## Required artifacts

| Artifact | Exact path |
|----------|------------|
| Blender source scene | `training/texturing/a01/source/organic-material.blend` |
| Base color map | `training/texturing/a01/maps/organic-basecolor_1024.png` |
| Roughness map | `training/texturing/a01/maps/organic-roughness_1024.png` |
| Normal map | `training/texturing/a01/maps/organic-normal_1024.png` |
| Lab notes | `training/texturing/a01/notes.md` |
| Blender viewport proof | `training/texturing/a01/blender-viewport.png` |
| SL in-world proof | `training/texturing/a01/sl-inworld.png` |

If you use Material Maker, also commit `training/texturing/a01/source/organic-material.mm`.

## Sign-off checklist

- [ ] All required artifacts are present at the exact paths listed above.
- [ ] Maps use metallic/roughness workflow, not legacy spec/gloss.
- [ ] Base color is saved as sRGB; roughness and normal are saved as non-color/linear.
- [ ] All maps share the same resolution (1024 × 1024 or 2048 × 2048).
- [ ] UVs are within a single 0–1 tile with no overlapping islands outside the tile.
- [ ] Provenance is recorded in `notes.md` for any CC0 texture, HDR, or reference asset used.
- [ ] `blender-viewport.png` and `sl-inworld.png` both show the same material on the test mesh/prim.
- [ ] `notes.md` documents the Blender version and, if used, the Material Maker version.
- [ ] Lesson link recorded in `notes.md` points back to this wiki page, not to duplicate docs elsewhere.

## Next track

[Layered textures](layered-textures.md) adds Ucupaint layers and wear/variation on top of this base material.

## Related

- [Lesson 7 — Texture painting & PBR materials](../pbr-materials.md)
- [Lesson 6 — UV unwrapping](../../modeling/uv-mapping.md)
- [Layered textures](layered-textures.md)
- [Second Life platform baseline](../../second-life/platform-baseline.md)
- [Material Maker](../software/material-maker.md)
- [Poly Haven](../software/poly-haven.md)
- [ambientCG](../software/ambientcg.md)
- [Adobe Substance 3D Painter](../software/substance-painter.md)
