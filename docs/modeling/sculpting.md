---
title: "Lesson 4 — Sculpting basics"
section: modeling
type: topic
---
# Lesson 4 — Sculpting basics

!!! abstract "Lesson 4 of 10 · [Blender foundations](blender/index.md)"
    **Production stage** — 2 Modeling  
    **Prerequisites** — [Lesson 3](mesh-modeling.md)  
    **Evidence folder** — `training/blender/b04/`

## Outcome

You can take the creature base from B03 and add **organic form and surface detail** — muscle mass, folds, scales, fur clumps — using Blender's sculpt brushes, dynamic topology, and multiresolution, producing a high-detail sculpt ready for retopology.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Sculpting introduction | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Grant's beginner sculpting explainers are the clearest for game/creature work |
| Sculpting in a full project | [Blender Guru — Donut series (sculpt section)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | Shows sculpt mode alongside the rest of the pipeline |

---

## Read

| Source | Link |
|--------|------|
| Manual — Sculpting | [Sculpting](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/index.html) |
| Manual — Sculpt brushes | [Brushes](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/tools/index.html) |
| Manual — Dyntopo | [Dynamic topology](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/tool_settings/dyntopo.html) |
| Manual — Multiresolution | [Multiresolution modifier](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/multiresolution.html) |

---

## Explain — sculpting for creatures, step by step

### Two ways to get sculpt resolution

- **Multiresolution modifier** — subdivides your existing (clean B03) mesh in levels. Best when you already have good topology and want to keep it. You sculpt at high levels and can later bake the detail to a normal map. **This is the studio default** because it plays nicely with retopo/baking.
- **Dynamic Topology (Dyntopo)** — adds/removes geometry under the brush as you sculpt. Best for free-form exploration where topology doesn't matter yet. Detail becomes a dense triangle soup that you *will* retopologise in [Lesson 5](retopology.md).

For a first creature, either works; multires is more controllable.

### Essential brushes

| Brush | Shortcut | Use |
|-------|----------|-----|
| Draw | `X`→Draw / default | Add/subtract mass; hold `Ctrl` to invert |
| Grab | `G` | Pull large forms into place |
| Smooth | `Shift` (hold with any brush) | Relax and blend — use constantly |
| Clay Strips | `C` | Build up muscle in flat strokes |
| Crease | — | Sharp folds, mouth lines, scale edges |
| Inflate | `I` | Puff out volume |
| Pinch | `P` | Tighten edges together |

Brush **size** = `F`, **strength** = `Shift`+`F`. Enable **X symmetry** (header) so both sides sculpt at once.

### A sensible order

1. Duplicate the B03 base so you keep the clean cage; add a **Multires** modifier, subdivide 2–3 levels.
2. **Big to small.** Establish primary forms (body mass, head shape) with Grab and Clay Strips at low multires level before adding detail.
3. Add a level, refine **secondary forms** (muscles, brow, cheeks, joints).
4. Add a level, add **tertiary detail** (skin folds, scales, fur direction, pores). Use Crease for scale/plate seams, alphas/stencils for repeated texture.
5. Smooth aggressively between passes; sculpting is as much about relaxing forms as adding them.

### Keep it retopo-friendly

Do **not** ship a sculpt to SL directly — millions of triangles = catastrophic land impact. The sculpt's job is to be the **source of shape and a normal-map bake target**. You will build a low-poly version in [Lesson 5](retopology.md) and bake this detail onto it in [Lesson 7](../texturing/pbr-materials.md).

### Why this matters for breedables

Sculpting is where a creature gets its personality and species identity. Because the deliverable to SL is always low-poly, sculpting is a *source asset* step: high detail here, captured as normal/AO maps later, so the in-world mesh stays cheap.

---

## Do — hands-on lab

1. Duplicate `quadruped-base.blend` mesh; add Multires and subdivide.
2. Sculpt a specific species pass (e.g. a scaled reptile or a furry mammal) with X symmetry: primary → secondary → tertiary.
3. Keep the multires **base level** intact (don't collapse it) so you retain clean topology.
4. Screenshot the finished sculpt (matcap view) → `training/blender/b04/sculpt.png`.
5. Save `.blend` to `training/blender/b04/creature-sculpt.blend`.
6. Note in `training/blender/b04/notes.md`: multires levels, final triangle count, which method (multires/dyntopo) and why.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| High-detail sculpt | `training/blender/b04/creature-sculpt.blend` |
| Matcap render | `training/blender/b04/sculpt.png` |
| Notes (levels, tri count, method) | `training/blender/b04/notes.md` |

---

## Completed when

- [ ] Sculpt shows clear primary → secondary → tertiary detail
- [ ] Base topology preserved (multires) or noted as dyntopo for retopo
- [ ] Triangle count recorded (confirms why retopo is next)
- [ ] Screenshot + notes committed

---

## Next

[Lesson 5 — Retopology](retopology.md)

## More tutorials

Lesson: [Lesson 4 — Sculpting basics](sculpting.md)

**Beginner**
- **Grant Abbitt** — clearest beginner sculpting for creatures/game art. [Channel](https://www.youtube.com/@grabbitt)
- Manual — [Sculpting](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/index.html) · [Brushes](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/tools/index.html)

**Intermediate / Advanced**
- **CG Cookie** — sculpting courses & anatomy. [Channel](https://www.youtube.com/@cg_cookie)
- Manual — [Dyntopo](https://docs.blender.org/manual/en/latest/sculpt_paint/sculpting/tool_settings/dyntopo.html) · [Multiresolution](https://docs.blender.org/manual/en/latest/modeling/modifiers/generate/multiresolution.html)

---
