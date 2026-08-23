---
title: "Paid vs free — comparison matrix"
section: research
type: reference
---
# Paid vs free — comparison matrix

**Do not assume** — we document from vendor pages and experiments. Update when pricing or licenses change; **never hardcode prices without source + date**.

Legend: **BSR** = Breedables Studio recommended route today (may change after experiments).

---

## References

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | PureRef | PureRef personal / boards |
| **Price model** | Paid; commercial license for business | Personal tier / free workflows |
| **License** | Closed source | — |
| **Good at** | Fast ref boards, client review | Same (personal use) |
| **Weak at** | License cost for commercial studio | Business use restrictions on free tier |
| **When to pay** | Commercial project volume | Hobby / personal breedables |
| **BSR** | Personal PureRef or repo reference folders |

---

## Sculpting

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | ZBrush | Blender |
| **Price model** | Subscription (Maxon) | Free |
| **License** | Commercial proprietary | **GNU GPL** |
| **Good at** | Industry-standard dynamesh/zremesher ecosystem, massive sculpt community | Full pipeline in one app, SL export path |
| **Weak at** | Cost; separate app | Very high poly can need more manual discipline |
| **When to pay** | Studio job requires ZBrush; speed on complex creatures | Indie, OSS-first, integrated Blender→SL |
| **BSR** | **Blender** (validate on Reference Creature) |

Official ZBrush learning: [ZBrush Getting Started](https://www.maxon.net/en/zbrush/getting-started) · [ZClassroom](https://www.maxon.net/en/zbrush/zclassroom)

---

## Retopology

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | Maya Quad Draw · TopoGun | Blender (+ RetopoFlow under review) |
| **Good at** | Studio speed, Quad Draw familiarity | No extra license |
| **When to pay** | Production retopo throughput | Learning + SL breedables budgets |
| **BSR** | **Blender** |

---

## Texture painting (PBR on mesh)

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | Substance 3D Painter · Mari | Blender · Krita |
| **Good at** | Painter: layer stacks, generators, industry standard; Mari: hero UDIM/VFX | Blender: integrated; Krita: 2D paint **GPL**, commercial use OK |
| **Weak at** | Cost; separate subscriptions | Blender: less painter-focused UX than Painter |
| **When to pay** | Texture-artist role in studio; heavy material iteration | Breedables OSS pipeline |
| **BSR** | **Blender** + **Material Maker**; Krita for 2D passes |

Official: [Substance 3D tutorials](https://helpx.adobe.com/substance-3d-tutorials.html) · [Mari learning](https://www.foundry.com/products/mari/learn)

---

## Procedural materials

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | Substance 3D Designer | Material Maker |
| **License** | Commercial | **MIT** |
| **BSR** | **Material Maker** |

---

## Rigging & animation

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | Maya | Blender |
| **BSR** | **Blender** (+ Rigify) |

Official Maya path: [Maya Quick Start](https://www.autodesk.com/learn/ondemand/collection/maya-quick-start)

---

## Lookdev

| | Professional | Free / OSS |
|---|-------------|------------|
| **Tool** | Marmoset Toolbag | Blender EEVEE/Cycles |
| **BSR** | Blender + **in-world SL** PBR verification |

---

## Important license note

**OPEN SOURCE CODE ≠ FREE ASSETS ≠ COMMERCIAL OUTPUT RIGHTS**

Always separate: application license · bundled assets · texture libraries · AI model weights · SL upload terms.

→ [Software page standard](../meta/software-page-standard.md) · [Production tools registry (maintainers)](tool-registry.md)

## Software map by production stage

**Research basis:** Gnomon game-character and creature curricula (Maya, ZBrush,
Substance, Marmoset, Mari); the Blender official Fundamentals path; vendor
learning portals.

For each stage: **professional route** · **free/open route** · **what we teach**.

| Production stage | Professional / paid route | Free / open route | What we teach |
|------------------|---------------------------|-------------------|---------------|
| References | PureRef — closed source (commercial licence for business) | PureRef personal / image boards | Reference gathering, anatomy sheets, style boards |
| Modeling | **Autodesk Maya** — paid | **Blender** — GPL | Blockout, clean modeling, modifiers, topology |
| Organic sculpting | **ZBrush** — paid | **Blender** — GPL | Primary → secondary → tertiary forms, creature anatomy |
| Retopology | Maya Quad Draw / **TopoGun** — paid | Blender native retopo | Deformation topology, poly budgets, edge flow |
| UVs | Maya / specialist UV tools | Blender UV Editor | Seams, texel density, packing |
| Baking | Substance Painter / Marmoset / TopoGun | Blender | High→low normal, AO, curvature, cage errors |
| Texture painting | **Substance 3D Painter** · **Mari** — paid | Blender painting · **Krita** | PBR maps, masks, hand paint, skin/fur/scales |
| Procedural materials | **Substance 3D Designer** — paid | **Material Maker** — MIT | Procedural PBR materials |
| 2D finishing | **Photoshop** — paid | **Krita** — GPL v3 | Texture cleanup, masks, decals |
| Clothing | **Marvelous Designer** — paid | Blender cloth / manual modeling | Cloth patterns, folds, cleanup |
| Rigging | Maya | Blender + Rigify | Skeletons, weights, constraints |
| Animation | Maya | Blender | Idle, walk, actions, loops |
| Lookdev / preview | **Marmoset Toolbag** — paid | Blender Cycles / EEVEE | Normal inspection, PBR check, presentation |
| Optimization | Maya / specialist | Blender | LODs, tri reduction, texture budgets |
| Final target | — | — | **Second Life** — mesh, PBR, Animesh, LSL, import, performance |

## The studio stack today

```text
References → Blender (model / sculpt / retopo / UV / bake / rig / anim)
           → Material Maker / Krita as needed
           → Second Life export and in-world QA
```

Paid tools are documented so learners **understand the industry** — not because
anyone must buy them. Every tool has a card in the
[software database](software-database.md).

