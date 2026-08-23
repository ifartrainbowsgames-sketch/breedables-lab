# Organic PBR material

![Blender](../../assets/inline/blender.png){ width="80" }

**Studio lab** · Texturing for Second Life  
**Evidence folder:** `training/texturing/a01/` *(internal id A01)*

!!! danger "Prerequisites"
    **This lab does not teach Blender.**

    Complete **[Blender lesson 6](../software/blender/b06-uv-unwrapping.md)** (UV) and **[lesson 7](../software/blender/b07-texture-painting-pbr.md)** (PBR) first.

    Material Maker is optional — it is a **separate app**, not a Blender lesson.

**Production stage:** Texturing & PBR (Second Life metallic/roughness)  
**Primary tools:** Blender (core), Material Maker (optional app), Poly Haven / ambientCG (reference assets)

## Outcome

You can author an **organic PBR material** (fur, skin, scales, or leaf-like surface) that:

- Uses **metallic/roughness** workflow compatible with Second Life PBR
- Exports cleanly as PNG (or EXR where needed) with documented resolution
- Looks correct in Blender viewport **and** in-world on a test prim

Watching tutorials alone does **not** complete this lab. You must commit evidence.

---

## Watch (curated videos)

| Topic | Video | Why this one |
|-------|-------|--------------|
| Blender shader basics | [Blender 4.0 Beginner Tutorial — Part 1](https://www.youtube.com/watch?v=B0J27sf02NU) | Official Blender Foundation channel; stable intro to nodes |
| PBR texturing workflow | [PBR Texturing in Blender (Ryan King Art)](https://www.youtube.com/watch?v=4_xYiw1nL5M) | Practical metallic/roughness setup for game/SL-style assets |
| Material Maker intro | [Material Maker — procedural PBR](https://www.youtube.com/watch?v=8MMSS2F5vtc) | Procedural alternative to hand-painting; good for breedable skin variants |
| SL PBR in practice | [Gaia Clift — SL mesh upload](https://www.youtube.com/watch?v=uZ5KyLvivkw) | Upload workflow; pair with [platform baseline](../../secondlife/platform-baseline.md) |

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/4_xYiw1nL5M" title="PBR texturing in Blender" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

→ [Video library — all texturing tools](../resources/video-library.md)

---

## Read (official docs)

| Source | Link |
|--------|------|
| Blender manual — shader nodes | [Shader nodes introduction](https://docs.blender.org/manual/en/latest/render/shader_nodes/intro.html) |
| Blender manual — UV | [UV mapping](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/introduction.html) |
| Material Maker wiki | [Material Maker documentation](https://github.com/RodZill4/material-maker/wiki) |
| Second Life wiki — PBR | [PBR Materials](https://wiki.secondlife.com/wiki/PBR_Materials) |
| Poly Haven license | [CC0 license](https://polyhaven.com/license) |

Full index: [Official docs](../resources/official-docs.md)

---

## Explain — Breedables workflow

1. **Pick a species surface** (e.g. rabbit fur, dragon scale, leaf). One material, one species — not a generic shader library yet.
2. **Blockout in Blender:** low-poly test mesh or reuse a studio test head/body block.
3. **Author PBR maps:** Base Color, Roughness, Normal (Metallic usually 0 for organic).
4. **Optional Material Maker pass** for procedural variation seeds (store `.mm` source + exported PNGs).
5. **Bake / export** at power-of-two resolution (1024 or 2048 — document choice).
6. **SL validation:** upload material, apply to test prim, screenshot in-world with lighting note.

**Free vs paid:** Blender + Material Maker + CC0 libraries cover A01. Substance Painter is optional; document if used.

---

## Do — Hands-on lab

1. Unwrap UVs on test mesh (single UDIM or single tile — document which).
2. Build principled BSDF material with exported maps.
3. Export maps to `training/texturing/a01/maps/`.
4. Write `training/texturing/a01/notes.md` with: resolution, tool versions, any CC0 asset IDs used.
5. Capture Blender viewport screenshot → `training/texturing/a01/blender-viewport.png`
6. Capture SL in-world screenshot → `training/texturing/a01/sl-inworld.png`

---

## Produce — Required artifacts

| Artifact | Path |
|----------|------|
| Source blend (or Material Maker project) | `training/texturing/a01/source/` |
| Exported PBR maps | `training/texturing/a01/maps/` |
| Lab notes | `training/texturing/a01/notes.md` |
| Blender viewport proof | `training/texturing/a01/blender-viewport.png` |
| SL in-world proof | `training/texturing/a01/sl-inworld.png` |

---

## Sign-off checklist

- [ ] Maps are metallic/roughness (not legacy spec/gloss unless converted)
- [ ] Provenance recorded for any CC0 texture/HDR used
- [ ] Lesson link is this wiki page (git), not duplicate docs elsewhere

---

## Next track

[Layered textures](a02-layered-textures.md) adds Ucupaint layers and wear/variation on top of this base.
