---
title: "Rigging & Animation"
section: rigging-animation
type: index
question: "How do I make the creature deform and move?"
---
# Rigging & Animation

!!! abstract "This section answers one question"
    *How do I make the creature deform and move?*

Everything about making geometry move — armatures, joints, skinning and
weight painting, constraints, IK/FK, animation cycles and retargeting. Second
Life's Animesh imposes its own limits, covered in
[Second Life Production](../second-life/index.md).

## Topics

| Page | What it covers |
|------|----------------|
| [Rigging & skinning](rigging-and-skinning.md) | Quadruped armatures and clean deformation weights |
| [Animation](animation.md) | Idle and walk cycles, baked for export |

## Software

| Tool | Licence & role |
|------|----------------|
| [Blender + Rigify](../modeling/blender/index.md) | Free · GPL — bundled quadruped meta-rig |
| [Avastar](../research/tool-registry.md) | Paid — exact Second Life skeleton for Blender |
| [Rokoko Studio Live](../research/candidates/rokoko-studio-live.md) | Under evaluation — motion capture |
| [Animation retargeting](../research/candidates/animation-retargeting.md) | Under evaluation — reuse animation libraries |

## Hands-on projects

Each project ends in committed evidence, not a watched video.

| Project | Outcome |
|---------|---------|
| [Rig + animation](projects/rig-and-animation.md) | Quadruped rig with two loopable animations |

## Pipeline stages owned by this section

These are the production-line stages this section is responsible for.

### Stage 7 — Rigging

Deformation-ready **armature** for idle, walk, and future breedable animations — quadruped-first, species-agnostic fixture.

!!! tip "Studio pick"
    **Rigify (free, bundled)** for curriculum and E04. Paid rig addons only if E04 shows Rigify bottleneck.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | blender.org | Rigging environment |
    | **Rigify** | [Blender manual](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) | Quadruped baseline |
    | **Auto-Rig Pro** *(check)* | various | Alternative — evaluate in research |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Auto-Rig Pro** | blendermarket | Faster rig setup |
    | **Rigging addons** (various) | market | Time savers |

**How we use it**

- **Rigify** Basic Quadruped as Academy baseline  
- Custom bone cleanup for SL export constraints  
- Document bone naming for animation retarget

**What to complete**

- Studio labs: [Rig + animation](../rigging-animation/projects/rig-and-animation.md) (rig portion)  
- Experiments:   
- Produce: Rigify quadruped rig `.blend`

**Evidence folder** — `training/rigging/a04/`  
**Related pages** — [Lesson 8 — Rigging](../rigging-animation/rigging-and-skinning.md) · [Rig + animation](../rigging-animation/projects/rig-and-animation.md)

### Stage 8 — Animation

**Idle + walk** minimum for Animesh-style creatures; baked clips for SL constraints.

!!! tip "Studio pick"
    **Blender + retarget add-on** for E04. **Mixamo** rarely fits quadrupeds — research only. **Rokoko** optional comparison, not core.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | blender.org | Keyframe, NLA, bake |
    | **Blender Animation Retargeting** | https://github.com/Mwni/blender-animation-retargeting | Retarget benchmark |
    | **Mixamo** | mixamo.com | Free humanoid clips — limited for quadrupeds |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Rokoko** ecosystem | rokoko.com | Mocap — human-focused |
    | **iClone / others** | various | mocap pipelines |

**How we use it**

- Author or import animations  
- **Blender Animation Retargeting** for transfer between armatures  
- Bake to SL-friendly format; test root motion behavior

**What to complete**

- Studio labs: [Rig + animation](../rigging-animation/projects/rig-and-animation.md) (animation portion)  
- Produce: idle + walk baked clips + notes

**Evidence folder** — `training/animation/a04/`  
**Related pages** — [Lesson 9 — Animation](../rigging-animation/animation.md) · [Rig + animation](../rigging-animation/projects/rig-and-animation.md)

## Videos

**Beginner**

**[Avastar Official Documentation](https://avastar.machinimatrix.org/)** — The official manual for the Avastar Blender add-on covers setup, skeleton, and Second Life export.

**[Second Life Wiki: Avastar](https://wiki.secondlife.com/wiki/Avastar)** — Linden Lab's wiki page explains how Avastar fits into Second Life mesh and rigging workflows.

**[Avastar Product Page and Tutorials](https://www.machinimatrix.org/avatar/)** — Homepage for the Avastar add-on with links to documentation, purchase, and tutorial content.

**[Machinimatrix YouTube Channel](https://www.youtube.com/@machinimatrix)** — Official video channel from the Avastar developer with recorded walkthroughs and feature overviews.

**[Second Life Official YouTube Channel](https://www.youtube.com/@SecondLife)** — Official Second Life videos covering mesh upload, avatar creation, and in-world best practices.

**Intermediate**

**[Avastar — Second Life rigging](https://www.youtube.com/results?search_query=avastar+blender+second+life)** — SL-specific rig export from Blender

**[Machinimatrix Blog](https://blog.machinimatrix.org/)** — Creator Gaia Clary's blog publishes release notes, workflow guides, and embedded video tutorials.

---
