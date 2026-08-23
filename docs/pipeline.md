---
title: "Production pipeline"
type: reference
---
# Production pipeline

!!! abstract "This page answers one question"
    *What is the full path from reference to a creature living in Second Life?*

The Academy mirrors **real** character and creature pipelines used in games, film
and VFX — not an invented sequence. Schools such as Gnomon teach multi-tool
workflows (Maya + ZBrush + Substance Painter + Marmoset); creature workshops run
reference → ZBrush → Maya → Marvelous Designer → Substance Painter.

This page is the **map**. Each stage names what it is for, the professional
tools, the free alternative, and the studio route — then links to the section
that owns the subject in depth.

## The sections that own each stage

| Stages | Section | Question it answers |
|--------|---------|---------------------|
| 0–4 | [3D Modeling](modeling/index.md) | What tools and workflows do I use to create the model? |
| 5–7 | [Texturing & Materials](texturing/index.md) | How do I create professional surfaces and PBR materials? |
| 8–9 | [Rigging & Animation](rigging-animation/index.md) | How do I make the creature deform and move? |
| 10–13 | [Second Life Production](second-life/index.md) | How do I get the finished asset into Second Life correctly? |
| runtime | [Breedables Engineering](engineering/index.md) | How does the breedable system actually work? |

## Three routes at every stage

| Route | Purpose |
|-------|---------|
| **Professional** | What studios commonly use, so you understand industry language |
| **Free / open source** | What you can use without a subscription — GPL, MIT, CC0 where verified |
| **Studio pick** | What we use today, updated after [experiments](research/experiments.md) |

We say where the free tool is **sufficient**, where the paid tool **saves real
time**, and when an upgrade is **justified** — from evidence, not assumption.
Full comparison: [paid vs free matrix](research/paid-vs-free-matrix.md).

## Learning it in order

Follow the [Blender foundations path](academy/paths/blender-foundations.md); it
walks these stages as ten lessons.

---

## Stages in detail

Each stage: **what it is for (creatures)** · **professional tools** · **free/OSS tools** · **studio route** · **artifact**.

---

## 0 — Reference / concept

**For:** Anatomy, silhouette, style, breedable identity before geometry.

| Route | Tools |
|-------|--------|
| Professional | PureRef (commercial license for business use) |
| Free | PureRef personal tier, simple image boards, Blender ref planes |
| **Breedables** | PureRef personal or repo `assets/references/` boards |

**Artifact:** Reference sheet (front/side + detail callouts) in `training/references/`  
**PASS:** Named sources, scale notes, color palette intent  
**Academy:** [PureRef package](modeling/software/pureref.md) · [Video library — reference gathering](modeling/software/pureref.md#videos) · [Start here](academy/index.md)

---

## 1 — Blockout

**For:** Proportions, major forms, rig-friendly masses — low detail, fast iteration.

| Route | Tools |
|-------|--------|
| Professional | Maya |
| Free/OSS | **Blender** (GPL) |
| **Breedables** | Blender |

**Artifact:** Blockout mesh in `training/blender/b03/` or modeling folder  
**Academy:** [Lesson 3 — Mesh modeling](modeling/mesh-modeling.md)

---

## 2 — High-poly sculpt

**For:** Primary → secondary → tertiary forms, creature anatomy, surface detail.

| Route | Tools |
|-------|--------|
| Professional | **ZBrush** (Maxon) |
| Free/OSS | **Blender** sculpt + multires/dyntopo |
| **Breedables** | Blender (validate against Reference Creature) |

**Artifact:** High-poly sculpt `.blend` or exported sculpt  
**Academy:** [Lesson 4 — Sculpting](modeling/sculpting.md) · [ZBrush package card](modeling/software/zbrush.md)

---

## 3 — Retopology

**For:** Animation-ready topology, polygon budget, clean edge flow for deformation.

| Route | Tools |
|-------|--------|
| Professional | Maya Quad Draw, TopoGun |
| Free/OSS | Blender (native retopo, optional RetopoFlow add-on — license under review) |
| **Breedables** | Blender + RetopoFlow experiments |

**Artifact:** Low-poly game mesh + poly count note  
**PASS:** Loops at joints; manifold; budget met; silhouette held  
**Academy:** [Lesson 5](modeling/retopology.md) · [Retopology lab](modeling/projects/retopology-project.md)

---

## 4 — UV mapping

**For:** Seams, texel density, packing for texture resolution budget.

| Route | Tools |
|-------|--------|
| Professional | Maya UV, RizomUV (specialist) |
| Free/OSS | **Blender UV Editor** |
| **Breedables** | Blender |

**Artifact:** UV layout screenshot + `.blend`  
**Academy:** [Lesson 6](modeling/uv-mapping.md)

---

## 5 — High → low baking

**For:** Normal, AO, curvature (and related) from high to low mesh.

| Route | Tools |
|-------|--------|
| Professional | Substance Painter, Marmoset Toolbag, TopoGun |
| Free/OSS | **Blender** bake |
| **Breedables** | Blender (document cage errors in evidence)

**Artifact:** Map set without major bake artifacts  
**Academy:** *(baking lesson — integrate into B07 or dedicated bake lab)*

---

## 6 — Texture / material authoring

**For:** PBR maps, masks, hand painting, skin/fur/scales breakup.

| Route | Tools |
|-------|--------|
| Professional | **Substance 3D Painter**, **Mari** (hero/VFX/UDIM) |
| Free/OSS | Blender painting, **Krita** (2D), **Material Maker** (procedural) |
| **Breedables** | Blender + Material Maker + Ucupaint layers (A02 lab) |

**Artifact:** Base Color, Normal, Roughness, Metallic (as needed)  
**Academy:** [Lesson 7](texturing/pbr-materials.md) · [Organic PBR lab](texturing/projects/organic-pbr-material.md)

---

## 7 — Lookdev / preview

**For:** Validate normals, PBR response, presentation before engine/SL.

| Route | Tools |
|-------|--------|
| Professional | **Marmoset Toolbag** |
| Free/OSS | **Blender** Cycles / EEVEE |
| **Breedables** | Blender + **in-world** PBR check on SL test prim |

---

## 8 — Rigging & skinning

**For:** Skeleton, weights, constraints, clean deformation.

| Route | Tools |
|-------|--------|
| Professional | Maya |
| Free/OSS | **Blender** (+ Rigify) |
| **Breedables** | Blender Rigify |

**Artifact:** Rigged mesh + weight paint captures  
**Academy:** [Lesson 8](rigging-animation/rigging-and-skinning.md) · [Rig lab](rigging-animation/projects/rig-and-animation.md)

---

## 9 — Animation

**For:** Idle, walk, action loops for breedables / Animesh.

| Route | Tools |
|-------|--------|
| Professional | Maya |
| Free/OSS | **Blender** |
| **Breedables** | Blender |

**Artifact:** Two loopable clips + export notes  
**Academy:** [Lesson 9](rigging-animation/animation.md)

---

## 10 — Optimization / LOD

**For:** Triangle reduction, material/texture budgets, platform limits.

| Route | Tools |
|-------|--------|
| Professional | Maya + studio tools |
| Free/OSS | Blender |
| **Breedables** | Blender → SL land impact documented |

---

## 11 — Export

**For:** FBX/glTF (or SL pipeline), textures, rig, animations packaged.

| Route | Tools |
|-------|--------|
| **Breedables** | Blender → SL upload workflow |

**Academy:** [Lesson 10 — Export to SL](second-life/export-and-upload.md)

---

## 12 — Second Life delivery

**For:** Mesh upload, PBR materials, Animesh, LODs, physics, LSL fixture.

**Academy:** [In-world fixture lab](engineering/projects/in-world-fixture.md) · [SL adaptation](second-life/adapting-professional-work.md) · [Platform baseline](second-life/platform-baseline.md)

---

## 13 — In-world QA

**For:** Land impact, animation playback, script loop, persistence.

**Artifact:** In-world photos + LSL test logs in `training/lsl/`
