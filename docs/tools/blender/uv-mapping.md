---
title: "Lesson 6 — UV unwrapping"
section: tools
type: topic
---
# Lesson 6 — UV unwrapping

!!! abstract "Lesson 6 of 10 · [Blender foundations](index.md)"
    **Production stage** — 4 UV  
    **Prerequisites** — [Lesson 5](retopology.md)  
    **Feeds studio lab** — [Organic PBR material](../../projects/organic-pbr-material.md) / [Layered textures](../../projects/layered-textures.md)  
    **Evidence folder** — `training/blender/b06/` (mirror to `training/texturing/`)

## Outcome

You can **unwrap** your low-poly creature with well-placed seams and a packed, evenly-scaled UV layout — the foundation for every texture and PBR map you'll make in [Lesson 7](pbr-materials.md).

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| UV unwrapping fundamentals | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Beginner-friendly seam + unwrap explainers |
| UVs inside a full project | [Blender Guru — Donut series (UV part)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | Shows unwrapping in the texturing context |

---

## Read

| Source | Link |
|--------|------|
| Manual — UV unwrapping intro | [UV unwrapping](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/introduction.html) |
| Manual — Seams | [Marking seams](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/seams.html) |
| Manual — UV editor | [UV editor](https://docs.blender.org/manual/en/latest/editors/uv/index.html) |

---

## Explain — unwrapping step by step

### What a UV is

A UV map flattens your 3D surface onto a 2D square (the "UV space", 0–1) so a 2D texture can wrap onto it. Bad UVs = stretched, seam-visible textures no matter how good your painting is.

### Placing seams

1. Enter Edit Mode, switch to **edge** select. Open the **UV Editing** workspace (split view: mesh left, UV right).
2. Select edges where a "cut" should go and **Mark Seam** (`U` → Mark Seam, or right-click menu). Think of unfolding a stuffed animal: seams belong where they'll be **least visible** — underside of limbs, inside legs, along the belly, behind ears.
3. For a quadruped: a belly seam down the underside, seams up the inside of each leg, around the base of the tail and ears, and around the eyes/mouth.

### Unwrapping and checking

1. Select all (`A`), `U` → **Unwrap**. The flattened islands appear in the UV editor.
2. Turn on the **stretching overlay** (UV editor → Overlays → Display Stretch) — blue = good, red = stretched. Add or move seams until stretching is minimal.
3. Check **texel density is even** across islands (a big island and a small island at the same texture resolution get different detail). Use a **UV checker texture** (Blender's built-in `UV Grid` or `Color Grid` image) applied as a material — the squares should look square and same-sized everywhere.

### Packing efficiently

1. Select all UVs, `U` → or in the UV menu use **Pack Islands**. Give a small margin so bleed doesn't cross islands.
2. Fill the 0–1 space well — wasted UV space = wasted texture resolution = wasted SL texture memory.
3. For a breedable, one 1024 or 2048 texture set per creature is usually the target. Keep the whole creature in **one UV tile** (SL does not use UDIMs on upload) unless you deliberately split into multiple materials/faces (SL allows up to 8 material faces per object).

### Why this matters for breedables

Phenotype variation (A02) paints on top of these UVs — every colour morph, marking, and wear layer reuses this one layout. A clean, evenly-scaled, single-tile unwrap means every variant looks consistent and every texture byte counts against SL's texture budget efficiently.

---

## Do — hands-on lab

1. Mark seams on the B05 retopo mesh in low-visibility locations.
2. Unwrap; use the stretch overlay to get mostly-blue islands.
3. Apply a UV checker texture; confirm even, square texels across the body.
4. Pack islands into a single 0–1 tile with margin.
5. Export a UV layout PNG (UV editor → UV → **Export UV Layout**) → `training/blender/b06/uv-layout.png`.
6. Screenshot the checker on the model → `training/blender/b06/uv-checker.png`.
7. Save `.blend` → `training/blender/b06/unwrapped.blend`; mirror to `training/texturing/`.
8. `training/blender/b06/notes.md`: target texture resolution, number of material faces, seam rationale.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Unwrapped mesh | `training/blender/b06/unwrapped.blend` |
| Exported UV layout | `training/blender/b06/uv-layout.png` |
| Checker-on-model screenshot | `training/blender/b06/uv-checker.png` |
| Notes (resolution, faces, seams) | `training/blender/b06/notes.md` |

---

## Completed when

- [ ] Seams hidden in low-visibility areas
- [ ] Stretch overlay mostly blue; checker texels even and square
- [ ] Islands packed into a single 0–1 tile with margin
- [ ] UV layout PNG + notes committed

---

## Next

[Lesson 7 — Texture painting & PBR materials](pbr-materials.md)

## More tutorials

Lesson: [Lesson 6 — UV unwrapping](uv-mapping.md)

**Beginner**
- **Grant Abbitt** — seams + unwrap for beginners. [Channel](https://www.youtube.com/@grabbitt)
- Manual — [UV unwrapping intro](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/introduction.html) · [Marking seams](https://docs.blender.org/manual/en/latest/modeling/meshes/uv/unwrapping/seams.html)

**Intermediate / Advanced**
- Manual — [UV editor](https://docs.blender.org/manual/en/latest/editors/uv/index.html)
- Tools: [Zen UV](https://zenmastersteam.github.io/Zen-UV/latest/) (Paid), [TexTools](https://github.com/franMarz/TexTools-Blender) (Free), [UVPackmaster](https://uvpackmaster.com/) (Paid) — see [catalog](addon-catalog.md).

---
