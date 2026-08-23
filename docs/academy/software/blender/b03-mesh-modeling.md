# B03 — Mesh Modeling for Organic Creatures

**Learning path:** [Blender Foundations](index.md) · Lesson 3 of 10
**Production stage:** 2 Modeling · **Prerequisites:** [B02](b02-interface-navigation.md)
**Evidence folder:** `training/blender/b03/` (mirror final mesh to `training/modeling/`)

## Outcome

You can box-model a **clean, all-quad organic creature base** — a quadruped body with head, limbs, and tail — using the core edit-mode tools and modifiers, with edge flow good enough to sculpt and rig later.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Modeling fundamentals | [Blender Guru — Donut series (modeling parts)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | Teaches extrude/loop-cut/subdivision surface in context |
| Organic / creature modeling | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Creature and character base-mesh workflows for beginners |

---

## Read

| Source | Link |
|--------|------|
| Manual — Mesh modeling | [Meshes](https://docs.blender.org/manual/en/latest/modeling/meshes/index.html) |
| Manual — Mesh tools (extrude, loop cut, etc.) | [Editing mesh](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/index.html) |
| Manual — Mirror modifier | [Mirror modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/mirror.html) |
| Manual — Subdivision Surface | [Subdivision Surface modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/subdivision_surface.html) |

---

## Explain — box-modeling a creature base, step by step

### Core tools to master first

- **Extrude** (`E`) — pull new geometry from a selection; the backbone of box modeling.
- **Loop cut** (`Ctrl`+`R`) — add edge loops; scroll to add more, click then move to place.
- **Inset** (`I`) — inset a face inward, good for eyes/mouth.
- **Bevel** (`Ctrl`+`B`) — soften edges.
- **Knife** (`K`) and **Merge** (`M`) — cut in / weld verts.

### The mirror workflow (build one half)

Creatures are symmetric, so model one side and mirror the other:

1. Start from a cube. Enter Edit Mode, delete the `-X` half of the faces.
2. Add a **Mirror modifier** (Properties → wrench icon → Add Modifier → Mirror). Enable **Clipping** so centre verts weld to the seam.
3. Everything you now do on the `+X` side is reflected. Keep the origin at world centre.

### Blocking out the body

1. Extrude the cube along `Y` a few times to make a body cylinder-ish tube; keep faces roughly square.
2. Extrude a **neck and head** up/forward from the front faces; extrude a **tail** from the back.
3. Extrude **four legs** downward from the belly loops. Use `E` then `S`+`0` to keep leg cross-sections tidy, then extrude down toward the feet.
4. Add **loop cuts** at joints (shoulder, elbow, hip, knee) — you need extra loops exactly where the mesh will bend for rigging in [B08](b08-rigging-weight-painting.md).
5. Use the **Subdivision Surface modifier** (`Ctrl`+`2`) as a *preview* of the smooth result while you keep the control cage low-poly. Toggle wireframe (`Z` → Wireframe) to check flow.

### Edge-flow rules that pay off later

- **Quads only** where you can. Triangles and n-gons deform badly and confuse sculpt/retopo tools. Enable **Statistics** overlay and watch the tri/quad count.
- **Loops follow muscle/joint direction.** Rings around limbs, loops along the spine.
- **Even quads.** Avoid long thin faces on areas that will be textured — they stretch UVs in [B06](b06-uv-unwrapping.md).
- **Apply scale** (`Ctrl`+`A` → Scale) before finishing so modifiers and later rigs behave.

### Why this matters for breedables

This base becomes every phenotype of a species. A clean, symmetric, quad base sculpts cleanly (B04), retopologises predictably (B05), unwraps without stretching (B06), and rigs without pinching (B08). Time spent on edge flow here is repaid at every later stage.

---

## Do — hands-on lab

1. From `sl-startup.blend`, model a **neutral quadruped base** (no species detail yet) using the mirror + extrude workflow above. Keep it under ~2–4k faces on the control cage.
2. Place loop cuts at all four leg joints, the neck, and the tail base.
3. Keep a Subdivision Surface modifier for preview but **do not apply it** yet.
4. Verify: all quads (or note any unavoidable tris), scale applied, origin centred.
5. Screenshot solid + wireframe views → `training/blender/b03/base-solid.png`, `training/blender/b03/base-wire.png`.
6. Save `.blend` to `training/blender/b03/quadruped-base.blend` and copy the final mesh to `training/modeling/`.
7. Write `training/blender/b03/notes.md`: face count, any tris/n-gons and why.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Quadruped base mesh | `training/blender/b03/quadruped-base.blend` |
| Solid + wireframe screenshots | `training/blender/b03/base-solid.png`, `base-wire.png` |
| Mesh copy for modeling track | `training/modeling/` |
| Notes (poly count, topology) | `training/blender/b03/notes.md` |

---

## Completed when

- [ ] Symmetric quadruped base with head, four legs, tail
- [ ] Mostly quads; joints have supporting loops
- [ ] Scale applied, origin at world centre
- [ ] Screenshots + notes committed

---

## Next

[B04 — Sculpting Basics](b04-sculpting.md)
