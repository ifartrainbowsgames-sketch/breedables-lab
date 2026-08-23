---
title: "Lesson 3 — Mesh modeling for organic creatures"
section: tools
type: topic
---
# Lesson 3 — Mesh modeling for organic creatures

!!! abstract "Lesson 3 of 10 · [Blender foundations](index.md)"
    **Production stage** — 2 Modeling  
    **Prerequisites** — [Lesson 2](interface-and-navigation.md)  
    **Evidence folder** — `training/blender/b03/` (mirror final mesh to `training/modeling/`)

## Outcome

You can box-model a **clean, all-quad organic creature base** — a quadruped body with head, limbs, and tail — using the core edit-mode tools and modifiers, with edge flow good enough to sculpt and rig later.

---

## Watch

!!! tip "Play it in Tutorials"
    The player lives on [Tutorials](../../tutorials/blender/index.md). Titles below stay so you can see what we picked.


| Topic | Video | Why this one |
|-------|-------|--------------|
| Modeling fundamentals | [Blender Guru — Donut series (modeling parts)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | Teaches extrude/loop-cut/subdivision surface in context |
| Organic / creature modeling | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Creature and character base-mesh workflows for beginners |

→ Full Blender playlist: [Video library — Blender](../../research/software-database.md)

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
4. Add **loop cuts** at joints (shoulder, elbow, hip, knee) — you need extra loops exactly where the mesh will bend for rigging in [Lesson 8](rigging-and-skinning.md).
5. Use the **Subdivision Surface modifier** (`Ctrl`+`2`) as a *preview* of the smooth result while you keep the control cage low-poly. Toggle wireframe (`Z` → Wireframe) to check flow.

### Edge-flow rules that pay off later

- **Quads only** where you can. Triangles and n-gons deform badly and confuse sculpt/retopo tools. Enable **Statistics** overlay and watch the tri/quad count.
- **Loops follow muscle/joint direction.** Rings around limbs, loops along the spine.
- **Even quads.** Avoid long thin faces on areas that will be textured — they stretch UVs in [Lesson 6](uv-mapping.md).
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

[Lesson 4 — Sculpting basics](sculpting.md)

## More tutorials

Lesson: [Lesson 3 — Mesh modeling for organic creatures](mesh-modeling.md)

**Beginner**
- **Blender Guru — Donut series** (modeling parts). The canonical first course. [Playlist](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z)
- **Grant Abbitt** — bite-size modeling fundamentals & low-poly creatures. [Channel](https://www.youtube.com/@grabbitt)
- Manual — [Mesh modeling](https://docs.blender.org/manual/en/latest/modeling/meshes/index.html) · [Modeling introduction](https://docs.blender.org/manual/en/latest/modeling/introduction.html)

**Intermediate**
- **CG Cookie** — structured modeling courses (topology, form). [Channel](https://www.youtube.com/@cg_cookie) · paid courses on cgcookie.com
- Manual — [Mesh editing tools](https://docs.blender.org/manual/en/latest/modeling/meshes/editing/index.html) · [Modifiers](https://docs.blender.org/manual/en/latest/modeling/modifiers/index.html)

### Advanced — hard-surface (accessories, tack, HUD props)
- **Josh Gambrell / Blender Bros** — hard-surface workflow. [Hard surface Part 1](https://www.youtube.com/watch?v=pHZda9jqWgU) · [Channel](https://www.youtube.com/@JoshGambrell) · [Blender Bros (Paid)](https://www.blenderbros.com/)
- Add-ons for hard-surface: [Hard Ops / Boxcutter](addon-catalog.md#paid-but-worth-it), [MACHIN3tools](addon-catalog.md#free-community).

---

## Geometry nodes

Procedural systems — scatter fur/spikes, generate variation, build non-destructive props. Not required for a first creature, but powerful for **breedable trait variation** and asset generation.

**Beginner**
- **Blender Studio — Geometry Nodes** intro content. [Channel](https://www.youtube.com/@BlenderStudio)
- **Ryan King Art** — beginner geometry-node tutorials. [Channel](https://www.youtube.com/@RyanKingArt)
- Manual — [Geometry nodes](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/index.html)

**Intermediate / Advanced**
- **Default Cube** — [Blender Geometry Nodes tutorial](https://www.youtube.com/watch?v=B80oeXrCn8w) and the broader channel. [Default Cube](https://www.youtube.com/channel/UCdpWKLNfbROyoGPV46-zaUQ)
- **CGMatter** — [Introduction to Geometry Nodes course](https://www.youtube.com/@CGMatter) (a ~5-hour foundation; free on channel, paid extended version).
- Manual — [Fields](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/fields.html) · [Instances](https://docs.blender.org/manual/en/latest/modeling/geometry_nodes/instances.html)

---
