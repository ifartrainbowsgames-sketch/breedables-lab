---
title: "Lesson 10 — Exporting to Second Life"
section: second-life
type: topic
---
# Lesson 10 — Exporting to Second Life

!!! abstract "Lesson 10 of 10 · [Blender foundations](../modeling/blender/index.md)"
    **Production stage** — 9–10 Export / Upload  
    **Prerequisites** — [Lesson 9](../rigging-animation/animation.md)  
    **Feeds studio lab** — [In-world fixture](../engineering/projects/in-world-fixture.md)  
    **Evidence folder** — `training/blender/b10/` (mirror to `training/secondlife/`)

## Outcome

You can export your creature from Blender and **upload it into Second Life** with correct LODs, a lightweight physics shape, PBR material, and (for Animesh) a working rig — with land impact you understand and can defend.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| SL mesh upload workflow | [Second Life official — YouTube](https://www.youtube.com/@SecondLife) | Official channel; SL upload UI changes, prefer current SL/Firestorm walkthroughs |
| Blender → SL export | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | General game-export habits that transfer to SL |

> SL viewer UI changes often — pin one **current** community upload walkthrough in the [videos index](../research/software-database.md) rather than an old one.

---

## Read

| Source | Link |
|--------|------|
| Manual — Collada (.dae) export | [Collada (Legacy)](https://docs.blender.org/manual/en/4.4/files/import_export/collada.html) |
| Manual — glTF 2.0 export | [glTF 2.0](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html) |
| SL — Mesh (overview) | [Mesh](https://wiki.secondlife.com/wiki/Mesh) |
| SL — Mesh & LOD | [Mesh and LOD](https://wiki.secondlife.com/wiki/Mesh_and_LOD) |
| SL — Upload Model UI reference | [Mesh/Upload Model UI reference](https://wiki.secondlife.com/wiki/Mesh/Upload_Model_UI_reference) |
| SL — Making mesh physics | [Making Mesh Physics](https://wiki.secondlife.com/wiki/Making_Mesh_Physics) · [Decomposing physics](https://wiki.secondlife.com/wiki/Mesh/Decomposing_a_mesh_for_physics_shape) |
| SL — Animesh | [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) |
| SL — Calculating land impact | [Download Weight (LI math)](https://wiki.secondlife.com/wiki/Mesh/Download_Weight) |

---

## Explain — export & upload, step by step

### Which format for what

Second Life's mesh uploader ingests **COLLADA (.dae)** for geometry (all four LODs + physics + rigging weights). PBR **materials** upload via **glTF 2.0** (or you apply the individual maps in the SL material editor). So a typical creature uses **both**: `.dae` for the mesh/rig, glTF/maps for the material.

- **Static prop:** `.dae` mesh + LODs + physics.
- **Animated creature (Animesh):** rigged `.dae` (weighted to the **SL avatar skeleton**) + LODs + physics, then animations uploaded separately, then set the object to Animesh in-world.

### Prepare in Blender before export

1. **Apply transforms:** `Ctrl`+`A` → All Transforms on the mesh. Un-applied scale is the #1 cause of broken uploads.
2. **Recalculate normals** (`Shift`+`N`); check no flipped faces (Face Orientation overlay).
3. **One material per intended SL face** (max 8). Keep the single-tile UVs from [Lesson 6](../modeling/uv-mapping.md).
4. **Name objects** clearly per LOD (e.g. `creature_LOD0`…`LOD3`, `creature_PHYS`).

### Build LODs and physics

1. **LODs:** from [Lesson 5](../modeling/retopology.md) you have High/Medium/Low/Lowest. You'll point the uploader at each. Supplying your own beats auto-decimation for both looks and land impact.
2. **Physics shape:** create a **very** simple collision mesh (a few boxes/hulls roughly filling the body). Complex physics inflates the physics weight and thus land impact. See [Making Mesh Physics](https://wiki.secondlife.com/wiki/Making_Mesh_Physics). Set physics type appropriately in-world (Prim vs Convex Hull) after upload.

### Export

- **Collada (.dae):** `File → Export → Collada (.dae)`. For rigged meshes enable **Include Armatures / skinning**; export selected objects; keep **Apply Modifiers** on. Export each LOD (or use the uploader's per-LOD file slots).
- **glTF (.glb/.gltf):** `File → Export → glTF 2.0` for the PBR material path; **Format glTF Binary (.glb)**, include the mesh + materials, +Y up as required.

### Upload in the SL viewer

1. **Build → Upload → Model** (or Firestorm's mesh uploader). Load your High LOD `.dae`.
2. In **Level of Detail**, load your Medium/Low/Lowest `.dae` files (or use Auto and compare).
3. In **Physics**, load your `_PHYS` shape; **Analyze**; keep it cheap.
4. For a creature, check **Include skin weight** and **Include joint positions** as appropriate (Animesh).
5. Read the **land impact** and **upload fee (L$)** the uploader shows. If LI is too high, go back to LODs/physics — don't just accept it. (See [Lesson 5](../modeling/retopology.md) for the LI = max(download, physics, server) rule.)
6. Upload, rez, apply your PBR material/maps, and for animated creatures enable **Animesh** and script the animation triggers (that's [In-world fixture](../engineering/projects/in-world-fixture.md)).

### Validate in-world (required)

Rez the creature, apply the material from [Lesson 7](../texturing/pbr-materials.md), play the idle/walk from [Lesson 9](../rigging-animation/animation.md), and screenshot with viewer version, region, and date. Record final land impact.

### Why this matters for breedables

This is the moment the whole pipeline pays off — or fails. Correct transforms, self-authored LODs, a cheap physics shape, and metallic/roughness materials are what make a breedable that looks good, animates, and stays within a buyer's land budget.

---

## Do — hands-on lab

1. Prepare the creature (apply transforms, normals, materials, names).
2. Export High + 3 LODs as `.dae`; export a simple `_PHYS` shape; export the material as glTF.
3. Upload via the SL viewer; load LODs + physics; record LI and upload fee (screenshot the uploader).
4. Rez, apply material, (Animesh) play an animation; screenshot in-world.
5. Save export files to `training/blender/b10/export/`; screenshots to `training/blender/b10/`.
6. `training/blender/b10/notes.md`: final LI, upload fee, per-LOD tri counts, physics approach, viewer/region/date.
7. Mirror the in-world proof to `training/secondlife/`.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Export package (.dae LODs, _PHYS, glTF) | `training/blender/b10/export/` |
| Uploader screenshot (LI + fee) | `training/blender/b10/uploader.png` |
| In-world proof | `training/blender/b10/sl-inworld.png` |
| Notes (LI, fee, tris, physics, viewer) | `training/blender/b10/notes.md` |
| SL mirror | `training/secondlife/` |

---

## Completed when

- [ ] Transforms applied; normals correct; ≤8 materials
- [ ] Four LODs + a cheap custom physics shape uploaded
- [ ] Land impact + upload fee recorded and defensible
- [ ] Creature rezzed in-world with PBR material (and animation if Animesh); dated screenshot committed

---

## Path complete

You have taken a creature from zero to an SL-ready, rigged, textured, animated upload. Continue with the outcome labs: [Organic PBR material](../texturing/projects/organic-pbr-material.md) → [In-world fixture](../engineering/projects/in-world-fixture.md), and browse the [add-on catalog](../modeling/blender/addon-catalog.md) and [tutorial arsenal](../academy/index.md) to go deeper.

## More tutorials

Lesson: [Lesson 10 — Exporting to Second Life](export-and-upload.md) · Track: [In-world fixture](../engineering/projects/in-world-fixture.md)

### Written docs (authoritative — read first)
- SL wiki — [Mesh](https://wiki.secondlife.com/wiki/Mesh) · [Mesh & LOD](https://wiki.secondlife.com/wiki/Mesh_and_LOD) · [Upload Model UI reference](https://wiki.secondlife.com/wiki/Mesh/Upload_Model_UI_reference)
- SL wiki — [Making Mesh Physics](https://wiki.secondlife.com/wiki/Making_Mesh_Physics) · [Decomposing a mesh for physics](https://wiki.secondlife.com/wiki/Mesh/Decomposing_a_mesh_for_physics_shape)
- SL wiki — [Download Weight (land impact math)](https://wiki.secondlife.com/wiki/Mesh/Download_Weight)
- SL wiki — [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide)
- Blender manual — [Collada (Legacy)](https://docs.blender.org/manual/en/4.4/files/import_export/collada.html) · [glTF 2.0 export](https://docs.blender.org/manual/en/latest/addons/scene_gltf2.html)

### Video
- **Second Life (official)** — platform & creation videos. [@secondlife](https://www.youtube.com/@secondlife)
- SL viewer UI changes often — pin one **current** community upload walkthrough in the [videos index](../research/software-database.md) and date it.
- Creator hub: [create.secondlife.com](https://create.secondlife.com/)

---
