---
title: "Rig + animation"
section: projects
type: project
---

# Rig + animation

!!! info "About this page"
    **Prerequisites** — Complete Blender rigging and animation lessons first  
    **Evidence folder** — `training/rigging/a04/`

Studio lab for a breedable-appropriate quadruped rig and two loopable animations. This project fills the evidence folder `training/rigging/a04/` with a rigged scene, bone map, animation sources, and export notes. The page focuses on the first deliverable so an empty folder becomes actionable immediately.

!!! tip "Studio pick"
    Blender + Rigify (bundled). It provides a standard quadruped armature that can be scaled to creature proportions, and it produces a documented bone map for retargeting experiments.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Blender | [Blender](https://www.blender.org) | Rigging, animation, and export |
    | Rigify | [Rigify](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) | Generating a quadruped control rig |

## Watch

| Topic | Video | Why this one |
|---|---|---|
| Blender rigging intro | [Armatures introduction (manual)](https://docs.blender.org/manual/en/latest/animation/armatures/introduction.html) | Read and follow along in Blender before building the rig |
| Quadruped rigging | [Darkfall - quadruped rigging intro](https://www.youtube.com/watch?v=6Km2tRFTxvs) | Creature rig workflow for four-legged breedables |

## Read

| Source | Covers |
|---|---|
| [Rigify add-on](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) | Quadruped rig generation and bone layers |
| [NLA documentation](https://docs.blender.org/manual/en/latest/editors/nla/index.html) | Organising multiple animation clips |
| [Uploading a rigged mesh](https://wiki.secondlife.com/wiki/Mesh/Uploading_and_wearing_a_rigged_mesh) | SL mesh upload requirements |
| [How to create animations](https://wiki.secondlife.com/wiki/How_to_create_animations) | SL animation source workflow |
| [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) | In-world animated mesh setup |

## Outcome

Rig an approved quadruped test mesh and deliver **two loopable animations** (idle + a second action such as eat, play, or walk) with clear export notes for Second Life Animesh upload.

## Evidence folder status

The evidence folder is empty. The first required artifact is the rigged scene file. Do not begin keyframe animation until `training/rigging/a04/rigged.blend` exists and passes the rig checklist below.

## First artifact: rigged scene

The exact first deliverable is `training/rigging/a04/rigged.blend`. It must contain the mesh, the generated Rigify armature (or a documented manual armature), and clean vertex groups. Save this file before opening the NLA editor or adding any keyframes.

## Breedables workflow

1. Start from the approved test mesh (retopologised creature from the modelling project).
2. Build a Rigify quadruped metarig and scale it to match the mesh, or document a manual armature.
3. Save a bone-name map in `training/rigging/a04/bone-map.md` for retargeting.
4. Generate the rig, parent the mesh, and refine weight painting on neck, legs, and tail.
5. Create an **idle loop** (2-4 s) and a **second action loop**.
6. Export or pack the animations and document the SL upload path used.

## Hands-on lab

Follow the steps below in order. Each step produces a file or a verification that must be saved before moving on.

## Required artifacts

All artifacts are relative to `training/rigging/a04/`. The renderer will format the exact paths from the artifacts list.

## Sign-off checklist

Every item below must be true before the project is marked complete. If an upload test is blocked by permissions, document the blocker instead.

## Next track

After this project is signed off, move on to [In-world fixture](in-world-fixture.md) to connect the asset with breedables behaviour.

## Do

1. Open the approved quadruped test mesh and **Save As** `training/rigging/a04/rigged.blend`.
2. Add a Rigify quadruped metarig or a documented manual armature matching the creature proportions.
3. Rename bones to a project convention and record every deformation bone in `training/rigging/a04/bone-map.md`.
4. Generate the Rigify rig, parent the mesh to it with automatic weights, then refine weight painting on neck, legs, and tail.
5. Pose the rig through a full range of motion and fix any stray deformation or spikes.
6. Save `rigged.blend` again. This is the first artifact.
7. Create an idle loop action (2-4 s) and a second action (eat, play, or walk).
8. Store animation source clips in `training/rigging/a04/animations/idle.blend` and `training/rigging/a04/animations/eat.blend`.
9. Export animation files to `training/rigging/a04/animations/` in the format chosen for Second Life upload.
10. Capture a viewport preview and save it as `training/rigging/a04/preview.mp4` or `preview.gif`.
11. Write `training/rigging/a04/notes.md` including bone-map notes, retargeting effort, and SL upload steps or blockers.

## Produce

| Artifact | Path |
|----------|------|
| Rigged Blender scene | `training/rigging/a04/rigged.blend` |
| Bone mapping notes | `training/rigging/a04/bone-map.md` |
| Idle animation source | `training/rigging/a04/animations/idle.blend` |
| Second animation source | `training/rigging/a04/animations/eat.blend` |
| Animation exports folder | `training/rigging/a04/animations/` |
| Viewport preview | `training/rigging/a04/preview.mp4` |
| Lab notes | `training/rigging/a04/notes.md` |

## Done when

- [ ] `training/rigging/a04/rigged.blend` opens without errors and contains one armature and one mesh.
- [ ] `training/rigging/a04/bone-map.md` lists every deformation bone and its purpose.
- [ ] Neck, legs, and tail (if present) deform smoothly without collapsing or stray vertex spikes.
- [ ] The rig controls are usable before any animation keyframes are added.
- [ ] Two distinct loopable animations exist in `training/rigging/a04/animations/`.
- [ ] `training/rigging/a04/preview.mp4` or `preview.gif` plays the loops clearly.
- [ ] `training/rigging/a04/notes.md` documents the export format and SL upload path, including any blockers.

## Related

- [Rigging & weight painting](../tools/blender/rigging-and-skinning.md)
- [Basic animation](../tools/blender/animation.md)
- [Exporting to Second Life](../tools/blender/export-and-upload.md)
- [Studio experiments](../research/experiments.md)
- [Blender](../tools/blender/index.md)
- [In-world fixture](in-world-fixture.md)
