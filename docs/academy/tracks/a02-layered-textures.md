# Layered textures

![Ucupaint / Blender](../../assets/inline/blender.png){ width="80" }

**Studio lab** · Wear, dirt, and color variation on PBR  
**Evidence folder:** `training/texturing/a02/` *(internal id A02)*

!!! danger "Prerequisites"
    Complete the **[Organic PBR lab](a01-organic-pbr.md)** and **[Blender lesson 7](../software/blender/b07-texture-painting-pbr.md)** first.

**Production stage:** Texturing (layer stacks, wear, variation)  
**Experiment:** [E01 PBR pipeline shootout](../../production/experiments.md#e01-pbr-pipeline-shootout)  
**Primary tools:** Blender, [Ucupaint](../../production/tools/ucupaint.md)

## Outcome

Add **non-destructive layers** (dirt, wear, color variation) on top of an A01 base material without destroying the original maps. Export an updated map set ready for Second Life PBR upload.

---

## Watch

| Topic | Video | Notes |
|-------|-------|-------|
| Ucupaint workflow | [Ucupaint — Turn Blender Into Substance Painter](https://www.youtube.com/watch?v=d3KrMwAWJI0) | Layer channels, PBR painting in Blender |
| Base PBR (prerequisite) | [A01 videos](../resources/videos.md#a01-organic-pbr) | Complete A01 first |

→ [Video library — Ucupaint & texture tools](../resources/video-library.md#ucupaint)

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/d3KrMwAWJI0" title="Ucupaint — layered PBR in Blender" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

## Read

| Source | Link |
|--------|------|
| Ucupaint wiki | [ucupumar.github.io/ucupaint-wiki](https://ucupumar.github.io/ucupaint-wiki/) |
| Ucupaint video list | [Official tutorial index](https://ucupumar.github.io/ucupaint-wiki/video-tutorials/) |
| Blender texture paint | [Texture paint manual](https://docs.blender.org/manual/en/latest/sculpt_paint/texture_paint/index.html) |

Tool page: [Ucupaint](../../production/tools/ucupaint.md)

---

## Explain — Breedables workflow

1. Import A01 exported maps as the **base layer** in Ucupaint.
2. Add at least three layers: e.g. **base color variation**, **edge wear (roughness)**, **dirt mask (multiply)**.
3. Document blend modes and mask sources in `notes.md`.
4. Bake/export full map set — do not rely on viewport-only layers for SL upload.
5. Compare editability vs redoing the whole material in Material Maker (E01 measurement).

**Free vs paid:** Ucupaint is free (GPL). Substance Painter is optional benchmark only.

---

## Do — Hands-on lab

1. Open A01 `.blend` or re-import A01 maps onto the same test mesh.
2. Enable Ucupaint; stack ≥3 layers with documented names.
3. Export to `training/texturing/a02/maps/`.
4. Capture before/after viewport screenshots.
5. Optional: SL upload one variant for comparison with A01 baseline.

---

## Produce — Required artifacts

| Artifact | Path |
|----------|------|
| Layer stack notes (blend modes, masks) | `training/texturing/a02/notes.md` |
| Updated PBR maps | `training/texturing/a02/maps/` |
| Viewport before/after | `training/texturing/a02/layers-before-after.png` |
| Source `.blend` with layers | `training/texturing/a02/source/` |

---

## Sign-off checklist

- [ ] A01 maps used as documented base (link commit hash in notes)
- [ ] ≥3 layers with named purpose
- [ ] Exported maps match SL metallic/roughness workflow
- [ ] E01 measurement row filled for Ucupaint layered pass

---

## Next track

[Retopology](a03-retopology.md)
