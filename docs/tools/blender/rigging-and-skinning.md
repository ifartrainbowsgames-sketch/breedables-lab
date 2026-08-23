---
title: "Lesson 8 — Rigging & weight painting"
section: tools
type: topic
---
# Lesson 8 — Rigging & weight painting

!!! abstract "Lesson 8 of 10 · [Blender foundations](index.md)"
    **Production stage** — 7 Rigging  
    **Prerequisites** — [Lesson 7](pbr-materials.md)  
    **Feeds studio lab** — [Rig + animation](../../projects/rig-and-animation.md)  
    **Evidence folder** — `training/blender/b08/` (mirror to `training/rigging/a04/`)

## Outcome

You can build a **quadruped armature**, skin the creature to it, and paint clean **deformation weights** so it bends without pinching — a rig suitable for **Second Life Animesh** animated creatures.

---

## Watch

!!! tip "Play it in Tutorials"
    The player lives on [Tutorials](../../tutorials/blender/index.md). Titles below stay so you can see what we picked.


| Topic | Video | Why this one |
|-------|-------|--------------|
| Rigging fundamentals | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Beginner rigging + weight painting for game characters |
| Rigify quadruped | [Blender official — YouTube](https://www.youtube.com/@BlenderOfficial) | Official demos of the bundled Rigify system |

> Add a verified Rigify-quadruped and a weight-painting video to the [videos index](../../research/software-database.md) — A04 slots are open.

---

## Read

| Source | Link |
|--------|------|
| Manual — Armatures | [Armatures](https://docs.blender.org/manual/en/latest/animation/armatures/index.html) |
| Manual — Rigify | [Rigify add-on](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) |
| Manual — Skinning / parenting | [Skinning](https://docs.blender.org/manual/en/latest/animation/armatures/skinning/index.html) |
| Manual — Weight paint | [Weight painting](https://docs.blender.org/manual/en/latest/sculpt_paint/weight_paint/index.html) |
| SL — Animesh | [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) |

---

## Explain — rigging for Animesh, step by step

### What SL Animesh needs

[Animesh](https://wiki.secondlife.com/wiki/Animesh_User_Guide) lets a **rezzed object** (not just an avatar) play skeletal animations — this is exactly how a breedable creature walks and idles. Important constraints:

- Animesh plays animations on the **Second Life avatar skeleton** (the standard SL bones, including collision/Bento bones). A creature rig for Animesh must ultimately map to **SL's named bones** — this is where **[Avastar](addon-catalog.md#paid-but-worth-it)** (paid) or a hand-built SL-bone armature earns its place: it provides the correct SL skeleton and export.
- Animesh has a **triangle limit** and counts toward land impact; keep the mesh lean (see [Lesson 5](retopology.md)).
- For learning the *mechanics* of rigging and weighting, **Rigify** (free, bundled) is the studio baseline; for the *actual SL export path* you retarget/transfer to the SL skeleton (Avastar or manual) in [Lesson 10](export-and-upload.md).

### Build the armature

1. With the textured mesh from B07, either:
   - **Rigify path (learning):** enable Rigify (Preferences → Add-ons), `Shift`+`A` → Armature → add the **Basic Quadruped** meta-rig, scale/position bones to match your creature, then **Generate Rig**; or
   - **Avastar path (SL delivery):** add the Avastar armature so you start from SL's exact bones.
2. Position bones **inside** the mesh at the real joint pivots (elbow, knee, spine, neck, tail, jaw). Use front/side ortho views for accuracy.
3. Keep bone **roll** consistent and name bones clearly — animation (B09) and export depend on names.

### Skin the mesh

1. Select the **mesh**, then shift-select the **armature**, `Ctrl`+`P` → **With Automatic Weights**. This creates vertex groups per bone and a starting weight map.
2. Enter **Pose Mode** on the armature, rotate a limb bone, and watch how the mesh deforms — this reveals problems.

### Weight painting — the real work

1. Select the mesh → **Weight Paint** mode; select a bone in Pose mode to paint its influence (red = 1.0 full, blue = 0.0 none).
2. Rules:
   - Weights per vertex should **sum to 1.0**. Use **Normalize All** to enforce it.
   - **Smooth** across joints so bends are gradual, not creased.
   - Fix **pinching** at joints by feathering influence across the joint loops you added in B03/B05.
   - No stray weights (a tail vertex accidentally weighted to a front leg causes spikes when animated).
3. Test by posing each bone through its full range and correcting as you go. This iteration *is* the skill.

### Why this matters for breedables

A breedable that pinches, tears, or spikes when it walks is unsellable. Clean weights on a quadruped are reusable across every phenotype of the species, so this rig is a long-lived studio asset.

---

## Do — hands-on lab

1. Rig the B07 creature (Rigify quadruped for learning; note if you also built the SL/Avastar skeleton).
2. Skin with automatic weights, then hand-correct weights at all joints, tail, neck, and jaw.
3. Pose-test the full range; screenshot a clean bent pose (e.g. leg lifted) → `training/blender/b08/pose-test.png`.
4. Screenshot the weight map on a key bone → `training/blender/b08/weights.png`.
5. Save `.blend` → `training/blender/b08/rigged.blend`; mirror to `training/rigging/a04/`.
6. `training/blender/b08/notes.md`: rig type, bone naming scheme, joints that needed manual fixes, SL-bone mapping plan.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Rigged + skinned creature | `training/blender/b08/rigged.blend` |
| Clean pose-test screenshot | `training/blender/b08/pose-test.png` |
| Weight map screenshot | `training/blender/b08/weights.png` |
| Notes (rig type, bone map, fixes) | `training/blender/b08/notes.md` |
| A04 mirror | `training/rigging/a04/` |

---

## Completed when

- [ ] Quadruped armature with bones at real joint pivots, clear names
- [ ] Mesh skinned; weights normalized and hand-corrected (no pinch/spike)
- [ ] Full-range pose test passes
- [ ] SL-bone mapping plan noted for export

---

## Next

[Lesson 9 — Basic animation](animation.md)

## More tutorials

Lesson: [Lesson 8 — Rigging & weight painting](rigging-and-skinning.md) · Track: [Rig + animation](../../projects/rig-and-animation.md)

**Beginner**
- **CGDive — "Rigging isn't Scary" (Level 1)** — free, structured rigging + weight-paint basics. [Channel](https://www.youtube.com/@CGDive) · [Site](https://cgdive.com/blender-rigging-isnt-scary/)
- **Grant Abbitt** — rig + weight paint a simple character. [Channel](https://www.youtube.com/@grabbitt)
- Manual — [Armatures](https://docs.blender.org/manual/en/latest/animation/armatures/index.html) · [Rigify](https://docs.blender.org/manual/en/latest/addons/rigify/index.html)

**Intermediate / Advanced**
- **CGDive** — advanced weight painting, IK/FK, quadruped rigs. [Channel](https://www.youtube.com/@CGDive)
- Manual — [Skinning](https://docs.blender.org/manual/en/latest/animation/armatures/skinning/index.html) · [Weight paint](https://docs.blender.org/manual/en/latest/sculpt_paint/weight_paint/index.html)
- SL path: [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) · tools [Avastar](addon-catalog.md#paid-but-worth-it) / [Auto-Rig Pro](addon-catalog.md#paid-but-worth-it).

---
