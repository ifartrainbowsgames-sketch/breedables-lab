---
title: "Studio labs"
section: projects
type: index
question: "What do I build to prove I can do it?"
---
# Studio labs

!!! abstract "This section answers one question"
    *What do I build to prove I can do it?*

A lesson ends when you understand something. A lab ends when there is a file in
the repository that someone else can open. These five labs are the difference
between having watched the Academy and having done it.

Every lab names an **evidence folder** under `training/`. Work that never
reaches its evidence folder does not count, and cannot be reviewed.

## The five labs

| Lab | You produce | Evidence folder |
|-----|-------------|-----------------|
| [Retopology](retopology-project.md) | An animation-ready low-poly mesh at a documented polygon budget, with wireframe proof | `training/modeling/a03/` |
| [Organic PBR material](organic-pbr-material.md) | A complete base colour / roughness / normal set for fur, skin or scales, checked in-world | `training/texturing/a01/` |
| [Layered textures](layered-textures.md) | Non-destructive wear, dirt and colour variation over that base material | `training/texturing/a02/` |
| [Rig + animation](rig-and-animation.md) | A quadruped rig plus two loopable clips, with a bone map and export notes | `training/rigging/a04/` |
| [In-world fixture](in-world-fixture.md) | A rezzable mesh and an LSL state machine proving a hunger/energy loop survives a restart | `training/lsl/a05/` |

## Order to do them in

The labs assume the [Blender lessons](../tools/blender/index.md) are behind you,
and they build on each other rather than standing alone:

1. **Retopology** needs a sculpt from lessons 3–5.
2. **Organic PBR material** needs UVs from lesson 6 and the retopologised mesh.
3. **Layered textures** edits the material the previous lab produced.
4. **Rig + animation** needs a clean, animation-ready mesh — that is what lab 1 was for.
5. **In-world fixture** needs everything above, plus lesson 10's export route.

Skipping ahead is possible, but each lab's pass conditions assume the earlier
artifacts exist and will fail review without them.

## What makes a lab pass

Every lab page states its own pass conditions. They share the same shape:

- The named files exist in the evidence folder, with the filenames the page asks for.
- A measurement is recorded — polygon count, texel density, land impact, script memory — not an impression.
- Where the platform is involved, there is an **in-world** capture. A Blender viewport render is not proof that Second Life agrees.

Findings that contradict the wiki are worth more than findings that confirm it.
If a lab's numbers do not hold, record that in the lab's evidence folder and
raise it — the [platform baseline](../second-life/platform-baseline.md) is only
as good as the last time someone checked it.
