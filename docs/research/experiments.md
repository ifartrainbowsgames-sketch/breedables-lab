---
title: "Studio experiments"
section: research
type: reference
---
# Studio experiments

Species-independent benchmarks from the Phase 0 survey. Each experiment must produce **artifacts**, not just notes.

Complete labs in git — documentation source of truth is this repo only.

## Recommended order

1. **E01** — PBR pipeline shootout
2. **E03** — Organic retopology benchmark
3. **E04** — Rig + retarget baseline
4. **E05** — Modern SL persistence fixture
5. **E02** — Image-to-3D baseline

E01 is cheap, reusable, and maps directly to Second Life Metallic/Roughness PBR. Image-to-3D stays useful but should not dictate the pipeline before topology, material, and rigging standards exist.

---

## E01 — PBR pipeline shootout

**Academy:** [Organic PBR material](../projects/organic-pbr-material.md), [Layered textures](../projects/layered-textures.md)  
**Tools:** [Material Maker](../tools/material-maker/index.md), [Ucupaint](../tools/ucupaint/index.md), DiffusedTexture (research)

**Outputs:** Base Color, Normal, Roughness, Metallic (when appropriate), source projects, in-world PBR screenshots

**Measurement table**
| Criterion | Material Maker | Ucupaint | Notes |
|-----------|----------------|----------|-------|
| Authoring time (min) | | | Same test mesh + brief |
| Seam quality (1–5) | | | |
| Editability / iteration (1–5) | | | |
| Phenotype repeatability (1–5) | | | Can you variant quickly? |
| SL in-world match (1–5) | | | Attach screenshot paths |
| License safety | MIT | GPL-3.0 | Document output use |
| **Pass?** | | | Any ≥4 avg + SL proof |

**Evidence:** `training/texturing/a01/`, `training/texturing/a02/`

---

## E02 — Image-to-3D baseline

**Tools:** [TripoSR](candidates/triposr.md), InstantMesh, TRELLIS.2 (hardware permitting)

**Outputs:** Input image, generated mesh, cleanup notes, retopo time estimate

**Measurement table**
| Criterion | TripoSR | Alt tool | Notes |
|-----------|---------|----------|-------|
| Silhouette fidelity (1–5) | | | |
| Topology usefulness (1–5) | | | Before retopo |
| UV / texture usefulness (1–5) | | | |
| Editability in Blender (1–5) | | | |
| Retopo time (min) | | | To animation-ready |
| SL upload readiness (1–5) | | | |
| License / output rights | MIT | | Workflow verification |
| **Pass?** | | | Blocker if rights unclear |

**Evidence:** `training/modeling/triposr/`

Yellow/red candidates stay research-only until cleared.

---

## E03 — Organic retopology benchmark

**Academy:** [Retopology](../projects/retopology-project.md)  
**Tools:** Blender native/manual, [RetopoFlow](../tools/retopoflow/index.md); postSilver retopology_tool for static/LOD comparison only

**Measurement table**
| Criterion | Native Blender | RetopoFlow | Notes |
|-----------|----------------|------------|-------|
| Time to target poly (min) | | | Same sculpt |
| Edge flow quality (1–5) | | | |
| Final poly count | | | Document target |
| UV / LOD handoff (1–5) | | | |
| Deformation on test rig (1–5) | | | |
| License / asset audit | — | See tool page | |
| **Pass?** | | | |

**Evidence:** `training/modeling/a03/`

---

## E04 — Rig and retarget baseline

**Academy:** [Rig + animation](../projects/rig-and-animation.md)  
**Tools:** [Blender](../tools/blender/index.md) + Rigify Basic Quadruped, [Blender Animation Retargeting](https://github.com/Mwni/blender-animation-retargeting)

**Steps:** rig → idle/walk → retarget → bake → Animesh-oriented export assumptions

**Measurement table**
| Criterion | Value | Notes |
|-----------|-------|-------|
| Rig setup time (min) | | |
| Bone mapping cleanup (1–5 difficulty) | | |
| Idle loop quality (1–5) | | |
| Second anim quality (1–5) | | |
| Root motion issues? | Y/N | |
| Retarget failures | | List cases |
| SL upload tested? | Y/N | |
| **Pass?** | | Two loops + export path |

**Evidence:** `training/rigging/a04/`

---

## E05 — Modern SL persistence fixture

**Academy:** [In-world fixture](../projects/in-world-fixture.md)  
**Platform:** Linkset Data, link messages, [LSL definitions](https://github.com/secondlife/lsl-definitions)

**Test:** script reset, re-rez, state ownership, module versioning, fake genetics state, debug visibility

**Measurement table**
| Test | Pass? | Notes |
|------|-------|-------|
| Script reset — state survives | | Linkset Data |
| Re-rez — state survives | | |
| Sim restart / region change | | If tested |
| Fake genetics round-trip | | |
| Debug visibility for QA | | Chat/HUD |
| Module version field | | |
| **Overall pass?** | | |

Compare lessons against historical XS Pet modular patterns (reference only — do not copy blindly).

**Evidence:** `training/lsl/a05/`

---

## Academy mapping

| Academy | Experiment |
|---------|------------|
| A01 Organic PBR Material | E01 |
| A02 Layered Texture Refinement | E01 |
| A03 Organic Retopology | E03 |
| A04 Rig + Two Animations | E04 |
| A05 Second Life Creature Fixture | E05 |

Watching a tutorial is not completion. Completion requires source files, exports, measurements, and in-world results where applicable.
