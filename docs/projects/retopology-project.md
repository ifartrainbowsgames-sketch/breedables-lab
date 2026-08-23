---
title: "Retopology"
section: projects
type: project
---

# Retopology

!!! info "About this page"
    **Prerequisites** — [Lesson 3 — Mesh modeling for organic creatures](../tools/blender/mesh-modeling.md) through [Lesson 5 — Retopology](../tools/blender/retopology.md)  
    **Evidence folder** — `training/modeling/a03/`

A studio lab project that turns a high-poly organic sculpt into animation-ready retopology for Second Life breedables, producing documented meshes, wireframe proof, and a measurement note in the evidence folder.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Blender | [Blender](../tools/blender/index.md) | Native retopology tools, snapping, shrinkwrap, and final mesh export |
    | RetopoFlow docs | [RetopoFlow docs](http://docs.retopoflow.com/) | Documentation for the RetopoFlow add-on workflow |

=== "Paid tools"

    | Tool | Link | Best for |
    |---|---|---|
    | RetopoFlow | [RetopoFlow](../tools/retopoflow/index.md) | Dedicated quad-drawing retopology inside Blender |
    | TopoGun 3 | [TopoGun 3](../tools/topogun/index.md) | Standalone retopology and map baking |
    | ZBrush | [ZBrush](../tools/zbrush/index.md) | Sculpting source and ZRemesher baseline |

## Watch

| Topic | Video | Why this one |
|---|---|---|
| RetopoFlow 4 setup | [Installation & RetopoFlow mode](https://www.youtube.com/watch?v=Ds5Soybs610) | CG Cookie / Orange Turbine walkthrough for getting into retopology mode. |
| Blender retopo concepts | [Blender manual — retopology](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html) | Native-tools baseline from the official manual. |

## Read

| Source | Covers |
|---|---|
| [RetopoFlow docs](http://docs.retopoflow.com/) | RetopoFlow tools, hotkeys, and workflow. |
| [RetopoFlow GitHub](https://github.com/CGCookie/retopoflow) | Source repository, issue tracker, and GPL license notes. |
| [RetopoFlow tool page](../tools/retopoflow/index.md) | Studio license and usage notes for production approval. |

## Outcome

![Blender](../assets/inline/blender.png){ width="80" }

**Studio lab** · Animation-ready mesh for breedables  
**Evidence folder:** `training/modeling/a03/`

Retopologize a high-poly sculpt into **animation-ready topology** with a documented poly budget suitable for breedables (Animesh / uploaded mesh limits).

## Evidence note

The evidence folder `training/modeling/a03/` is currently empty. Do not fabricate renders, poly counts, timings, or deformation results. The first artifact to create is `training/modeling/a03/retopo.blend` (the retopologized mesh). Record every measured value in `training/modeling/a03/notes.md` as you go.

## Prerequisites

Complete [Lesson 3 — Mesh modeling for organic creatures](../tools/blender/mesh-modeling.md) through [Lesson 5 — Retopology](../tools/blender/retopology.md) before starting this lab.

## Breedables workflow

1. Start from a high-poly organic sculpt (creature head/body block — studio test asset OK).
2. Set a **target poly count** before retopology and record it in `notes.md` (use the studio tiers, e.g. 5 k / 10 k / 15 k, or a project-specific budget).
3. Retopo with edge flow for the mouth, eyes, and any limb joints.
4. Verify deformation with a quick bone test or shape-key check before signing off.
5. Hand off the clean mesh to UV + texturing or rigging.

**License:** RetopoFlow is GPL; bundled assets may have different terms — read the [RetopoFlow tool page](../tools/retopoflow/index.md) before production approval.

## Hands-on lab

Use the exact filenames below so the evidence folder can be reviewed without guessing.

1. Open the high-poly sculpt in Blender. If you do not have one, use the studio test asset and save it as `training/modeling/a03/source/sculpt.blend`.
2. Start a new retopology object. Work at the chosen target poly budget using RetopoFlow or Blender native tools.
3. Save the finished retopologized mesh as `training/modeling/a03/retopo.blend`. This is the **first required artifact**.
4. Create `training/modeling/a03/source/` if it does not exist and keep the original sculpt there.
5. Render a front and side wireframe and save them as `training/modeling/a03/wireframe.png`.
6. Create `training/modeling/a03/notes.md` and record: start/end time, tool used, final vertex/face/triangle count, target budget, and any deformation notes.
7. If you ran the [E03 organic retopology benchmark](../research/experiments.md#e03-organic-retopology-benchmark), update its row with the same measured data.

## Required artifacts

| Artifact | Exact path |
|----------|------------|
| High-poly reference | `training/modeling/a03/source/sculpt.blend` |
| Retopo result | `training/modeling/a03/retopo.blend` |
| Wireframe proof | `training/modeling/a03/wireframe.png` |
| Lab notes | `training/modeling/a03/notes.md` |

## Sign-off checklist

- [ ] `retopo.blend` exists at `training/modeling/a03/retopo.blend`.
- [ ] Final triangle count is written in `notes.md` and is within the target budget recorded at the start.
- [ ] Edge flow is checked at every deformation point (mouth, eyes, joints).
- [ ] `wireframe.png` shows a clean front and side wireframe of the retopologized mesh.
- [ ] `notes.md` includes tool used, time spent, and any deformation-test observations.
- [ ] E03 benchmark row is updated if the experiment was run.
- [ ] RetopoFlow license note is reviewed and recorded in `notes.md` if RetopoFlow was used.

## Next track

Continue to [Rig + animation](rig-and-animation.md) once the retopology sign-off checklist is complete.

## Do

1. Open or create the high-poly sculpt and save it as `training/modeling/a03/source/sculpt.blend`.
2. Set a target poly budget and record it in `training/modeling/a03/notes.md`.
3. Retopologize the sculpt using RetopoFlow or Blender native tools.
4. Save the finished retopo mesh as `training/modeling/a03/retopo.blend`.
5. Render front and side wireframes and save as `training/modeling/a03/wireframe.png`.
6. Record measured time, poly count, tool, and deformation notes in `training/modeling/a03/notes.md`.
7. Update the E03 benchmark row in the experiments doc if applicable.

## Produce

| Artifact | Path |
|----------|------|
| High-poly reference | `training/modeling/a03/source/sculpt.blend` |
| Retopo result | `training/modeling/a03/retopo.blend` |
| Wireframe proof | `training/modeling/a03/wireframe.png` |
| Lab notes | `training/modeling/a03/notes.md` |

## Done when

- [ ] `training/modeling/a03/retopo.blend` exists.
- [ ] Final triangle count in `notes.md` is within the documented target budget.
- [ ] Edge flow verified at mouth, eyes, and limb joints.
- [ ] `wireframe.png` contains front and side wireframe views.
- [ ] `notes.md` records tool, time, poly count, and deformation-test observations.
- [ ] E03 benchmark row updated if the experiment was run.
- [ ] RetopoFlow license note reviewed if RetopoFlow was used.

## Related

- [Lesson 3 — Mesh modeling for organic creatures](../tools/blender/mesh-modeling.md)
- [Lesson 5 — Retopology](../tools/blender/retopology.md)
- [RetopoFlow](../tools/retopoflow/index.md)
- [Rig + animation](rig-and-animation.md)
- [Studio experiments](../research/experiments.md)
