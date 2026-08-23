## Mission check

We are still aligned with the two outputs: build the Reference Creature pipeline **and** build a teachable Academy. The recent concept audit correctly diagnosed the main risk: the Academy has structure (B01–B10, A01–A05) but almost no actual training content — no verified video links, no named exercises, no artifact screenshots, no PASS/FAIL criteria. Today’s evolution brief fixes that by populating the **first learner-facing pages with real content** rather than building more empty scaffolding.

The only active registry gap is **RetopoFlow’s commercial type**. Resolving it unlocks the Retopology lesson, which is a bottleneck for both the free OSS route and the Reference Creature mesh.

---

## Top 3 wiki improvements (specific pages)

### 1. Turn `docs/academy/software/blender/b03-mesh-modeling.md` into a real lesson

Current state: skeleton.  
Target: a complete lesson that produces `training/blender/b03/creature-blockout.blend` and a screenshot.

What to add:
- **Watch:** Blender Fundamentals section on mesh modeling (link to `https://www.blender.org/support/tutorials/`; curate the specific playlist/video after verification).
- **Read:** Blender Manual — Mesh Editing (`https://docs.blender.org/manual/en/latest/modeling/meshes/`) and Modifiers (`https://docs.blender.org/manual/en/latest/modeling/modifiers/`).
- **Do:** Exercise “Creature blockout” — build a low-poly quadruped body from a reference image, keep all faces quads, use mirror + subdivision workflow.
- **Artifact:** `training/blender/b03/creature-blockout.blend` + viewport screenshot.
- **PASS/FAIL:**
  - PASS: all-manifold mesh, no Ngons, symmetry across X, named collections, screenshot committed.
  - FAIL: missing reference image, triangles/Ngons in deformable areas, no screenshot.

### 2. Resolve `RetopoFlow` and write `docs/academy/software/blender/b05-retopology.md`

Current state: registry gap (`commercial type unknown`) and empty B05 page.  
Target: a three-route retopology page with a clear license note.

What to add:
- **Professional route:** Maya Quad Draw / TopoGun (explain why studios use it).
- **Free-OSS route:** Blender native retopology tools (retopo flow with shrinkwrap, snaps, grease pencil guides).
- **Breedables recommended route:** RetopoFlow add-on, **after** we confirm its commercial type and whether paid licensing is required for studio use.
- **Registry action:** Update `production/tools/index.md` or the Librarian entry for RetopoFlow. CG Cookie’s RetopoFlow is GPL-3.0 code on GitHub (`https://github.com/CGCookie/retopoflow`), but the Blender Market distribution may have a separate commercial license. We need to record both.
- **Artifact:** `training/blender/b05/retopo-creature.blend` with clean animation topology.

### 3. Populate `docs/academy/tracks/a01-organic-pbr.md` as the first Studio Lab

Current state: skeleton.  
Target: an end-to-end lab that connects Blender UVs, Material Maker procedural skin, Poly Haven / ambientCG CC0 assets, and SL PBR upload.

What to add:
- **Prerequisites:** B06 UV unwrapping + B07 texture painting/PBR.
- **Watch/Read:** Material Maker docs/wiki linked from `https://github.com/RodZill4/material-maker`; SL PBR wiki page (`https://wiki.secondlife.com/wiki/PBR_Materials`).
- **Do:** Author a reusable organic skin material using Material Maker, export Base Color / Normal / Roughness / Ambient Occlusion, apply in Blender, then upload to Second Life.
- **Artifact:** `training/texturing/a01/` containing the Material Maker project, exported PNG maps, Blender file, and an in-world screenshot.
- **PASS/FAIL:**
  - PASS: 4 PBR maps exported at 1K or 2K, no tiling seams on test mesh, SL upload screenshot shows expected material.
  - FAIL: missing map channel, visible seams, no in-world evidence.

---

## Open-source tools to research

| Tool | Why now | What to verify |
|------|---------|----------------|
| **Material Maker** | Needed for A01 Organic PBR lab and as the free Substance Designer replacement. | Current stable release, export node setup for Base Color/Normal/Roughness/AO, whether it runs on Blender 4.x as an add-on or only standalone. |
| **Ucupaint** | Potential free alternative to Substance Painter-style layer painting inside Blender. | Compatibility with Blender 4.x LTS, layer export workflow, whether it bakes well for SL PBR. |
| **RetopoFlow** | Blocks B05 lesson and retopo stage of Reference Creature. | GPL-3.0 vs Blender Market commercial license distinction; recommended install path for learners. |
| **Poly Haven** + **ambientCG** | CC0 texture libraries for learners who cannot photograph their own sources. | Which CC0 assets are useful for creature skin/scale/fur; how to credit/use in an open-source project. |
| **Krita** | Free 2D texture finishing (gimp alternative to Photoshop). | Best brush packs for hand-painted skin, export to PNG for SL, tablet setup. |

---

## One lesson/lab to prioritize today

**B03 — Mesh modeling for creatures** (`docs/academy/software/blender/b03-mesh-modeling.md`)

Reason: this is the first lesson that produces a real artifact and it feeds every later stage (sculpt, retopo, UV, rig, SL export). A beginner who completes B03 has something to show and can move through the rest of the pipeline with confidence. It also gives the Reference Creature team a shared blockout standard early.

Target artifact by end of day:  
`training/blender/b03/creature-blockout.blend` + `training/blender/b03/viewport-screenshot.png` + `training/blender/b03/PASS.md` self-checklist.

---

## Daily task list (human / AI / automated)

### Human must do
1. Open Blender 4.x LTS, complete the B03 creature-blockout exercise, and commit the `.blend` + screenshot to `training/blender/b03/`.
2. Research RetopoFlow licensing: read the Blender Market page and the `LICENSE` file in `https://github.com/CGCookie/retopoflow`, then update the Librarian/registry entry with the correct `commercial_type`.
3. Verify the current stable Material Maker release and confirm whether the GitHub release works for exporting PBR maps out of the box.

### AI can draft
1. Draft the full `docs/academy/software/blender/b03-mesh-modeling.md` lesson using the structure above, populated with verified official links and PASS/FAIL.
2. Draft a three-route `docs/academy/software/blender/b05-retopology.md` page, leaving a TODO for the RetopoFlow license note.
3. Draft `docs/academy/tracks/a01-organic-pbr.md` Studio Lab outline, with placeholders for any video URLs that still need verification.

### Already automated
- Daily wiki link checking (5 links checked, 0 failed — keep running).
- Registry gap detection (currently flagging RetopoFlow commercial_type).
- Evidence-folder scaffolding from the existing lesson/studio-lab JSON state.

---

## Optional: breedables market angle

The most successful SL breedables (e.g., Meeroo, KittyCatS, ABC horses) rely on **recognizable, emotionally appealing creature designs** more than on technical complexity. A learner who finishes B03 → B05 → A01 can already produce a distinctive pet body and skin, which is the core visual hook of a breedable product.

Today’s market insight to capture on the wiki: **start with one strong creature silhouette + one reusable PBR skin**, then iterate. The Reference Creature should not chase AAA detail; it should prove that a small team using only Blender + Material Maker + CC0 assets can ship a cute, animated, breedable-ready pet in-world. Document that evidence in `training/` so future learners can replicate it.
