---
title: "Lesson 5 — Retopology"
section: modeling
type: topic
---
# Lesson 5 — Retopology

!!! abstract "Lesson 5 of 10 · [Blender foundations](blender/index.md)"
    **Production stage** — 3 Retopo/LOD  
    **Prerequisites** — [Lesson 4](sculpting.md)  
    **Feeds studio lab** — [Retopology](projects/retopology-project.md)  
    **Evidence folder** — `training/blender/b05/` (mirror to `training/modeling/a03/`)

## Outcome

You can build a **clean low-poly mesh** over your high-detail sculpt with animation-ready edge flow, and you understand how triangle count and Level of Detail (LOD) drive **Second Life land impact** — so your creature is cheap to rez.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Manual retopology | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Clear beginner retopo-over-sculpt walkthroughs |
| Retopology in context | [Blender Guru — YouTube](https://www.youtube.com/@BlenderOfficial) *(also see [Blender official](https://www.youtube.com/@BlenderOfficial))* | Broader modeling context |

→ [Video library — retopo & all software](../research/software-database.md)

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/h6E9N10rN5s" title="Royal Skies Blender retopology beginner" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

## Read

| Source | Link |
|--------|------|
| Manual — Retopology | [Retopology](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html) |
| Manual — Shrinkwrap modifier | [Shrinkwrap](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/shrinkwrap.html) |
| SL — Mesh & LOD | [Mesh and LOD](https://wiki.secondlife.com/wiki/Mesh_and_LOD) |
| SL — Download weight (land impact math) | [Mesh/Download Weight](https://wiki.secondlife.com/wiki/Mesh/Download_Weight) |
| SL — Calculating land impact | [Download Weight (LI math)](https://wiki.secondlife.com/wiki/Mesh/Download_Weight) |

---

## Explain — retopology and SL land impact, step by step

### Why retopology exists

Your B04 sculpt might be millions of triangles. Second Life (and any real-time engine) needs a **low-poly** mesh that *looks* detailed via baked normal maps. Retopology = building a new, efficient quad mesh that follows the sculpt's surface.

### How land impact actually works in SL

Second Life does **not** charge by prim count for mesh. Each mesh object gets a **land impact** = the **highest** of three weights ([Mesh/Download Weight](https://wiki.secondlife.com/wiki/Mesh/Download_Weight)):

1. **Download (streaming) weight** — driven by triangle counts across your **four LOD models** and the object's size. This is usually the one you control at retopo time.
2. **Physics weight** — driven by the physics/collision shape (see [Lesson 10](../second-life/export-and-upload.md)).
3. **Server weight** — driven by scripts and linkset complexity.

Key consequences for retopo:

- **Fewer triangles → lower download weight → lower land impact → lower upload fee.** Budget your high LOD deliberately (a small breedable pet is often fine well under ~5–10k tris; confirm against your own upload preview).
- SL uses **4 LOD levels** (High, Medium, Low, Lowest). The uploader can auto-generate them, but auto-decimation often looks bad; you get lower LI and better silhouettes by supplying your own lower-poly LODs. **Bigger objects keep their high LOD visible from farther away**, so large creatures cost more unless their LODs are lean.
- A dense mesh with tiny far LODs can still have low download weight; a small mesh with heavy LODs can be surprisingly expensive. Always check the **land impact readout in the upload preview** before committing.

### Manual retopo workflow

1. Keep the sculpt visible. Create a **new mesh** (or start from a plane) for the retopo.
2. Turn on **snapping** (magnet icon) → **Snap to Face**, enable **Project Individual Elements**, and switch on **retopology overlay** (or add a tiny **Shrinkwrap** modifier targeting the sculpt) so new geometry sticks to the surface.
3. Use the **Poly Build** tool (or extrude edges) to lay quads along the surface, following the same edge-flow rules from [Lesson 3](mesh-modeling.md): loops around joints, along the spine and limbs.
4. Model **one half**, use a Mirror modifier with clipping.
5. Concentrate density where the mesh **deforms** (joints, mouth) and where the **silhouette** matters; keep flat areas sparse.
6. When done, apply Mirror, recalculate normals (`Shift`+`N`), and check for non-manifold geometry.

Tools that speed this up (optional, evaluate against evidence): **[RetopoFlow](blender/addon-catalog.md#free-community)** for guided quad drawing; **QuadriFlow** (built into Blender) for a fast auto-retopo base you then clean up. Manual retopo remains the primary path for anything that deforms.

### Building LODs

- **High LOD** = your retopo mesh.
- **Medium / Low / Lowest** = progressively decimated versions (Decimate modifier or manual). Preserve silhouette; drop interior detail first.
- Export each as a separate object/file for the uploader ([Lesson 10](../second-life/export-and-upload.md)).

### Why this matters for breedables

Breedables are **rezzed in quantity** — a ranch may hold dozens. Land impact is a hard budget for buyers. A disciplined retopo + LOD pass is the single biggest lever on whether your creature is commercially viable in-world.

---

## Do — hands-on lab

1. Retopologise the B04 sculpt into a clean quad low-poly mesh with joint loops.
2. Record the **triangle count** of the High LOD.
3. Make Medium, Low, and Lowest LODs (Decimate or manual); record each tri count.
4. In your SL viewer's upload preview, load the High LOD and read the **land impact** estimate; screenshot it.
5. Screenshots: retopo wireframe over sculpt → `training/blender/b05/retopo-wire.png`; LI readout → `training/blender/b05/land-impact.png`.
6. Save `.blend` → `training/blender/b05/retopo.blend`; mirror final mesh to `training/modeling/a03/`.
7. `training/blender/b05/notes.md`: tri counts per LOD, LI estimate, and what you'd cut to reduce it.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Retopo + LOD meshes | `training/blender/b05/retopo.blend` |
| Retopo wireframe screenshot | `training/blender/b05/retopo-wire.png` |
| Land impact estimate screenshot | `training/blender/b05/land-impact.png` |
| Notes (tri counts per LOD, LI, cut plan) | `training/blender/b05/notes.md` |
| A03 mirror | `training/modeling/a03/` |

---

## Completed when

- [ ] Low-poly quad mesh follows the sculpt with joint loops
- [ ] Four LODs produced, tri counts recorded
- [ ] Land impact estimate captured from the upload preview
- [ ] You can explain why LI = max(download, physics, server) weight

---

## Next

[Lesson 6 — UV unwrapping](uv-mapping.md)

## More tutorials

Lesson: [Lesson 5 — Retopology](retopology.md) · Track: [Retopology](projects/retopology-project.md)

**Beginner**
- **Grant Abbitt** — retopo-over-sculpt walkthroughs. [Channel](https://www.youtube.com/@grabbitt)
- Manual — [Retopology](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html) · [Shrinkwrap modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/deform/shrinkwrap.html)

**Intermediate / Advanced**
- **CG Cookie** (makers of RetopoFlow) — retopology courses. [Channel](https://www.youtube.com/@cg_cookie)
- Tool: [RetopoFlow](https://github.com/CGCookie/retopoflow) — [catalog entry](blender/addon-catalog.md#free-community) · [registry page](software/retopoflow.md)
- SL context: [Mesh & LOD](https://wiki.secondlife.com/wiki/Mesh_and_LOD) · [Download Weight / land impact](https://wiki.secondlife.com/wiki/Mesh/Download_Weight)

---
