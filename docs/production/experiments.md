# Studio experiments (E01–E05)

Species-independent benchmarks from the Phase 0 survey. Each experiment must produce **artifacts**, not just notes.

## Recommended order

1. **E01** — PBR pipeline shootout
2. **E03** — Organic retopology benchmark
3. **E04** — Rig + retarget baseline
4. **E05** — Modern SL persistence fixture
5. **E02** — Image-to-3D baseline

E01 is cheap, reusable, and maps directly to Second Life Metallic/Roughness PBR. Image-to-3D stays useful but should not dictate the pipeline before topology, material, and rigging standards exist.

---

## E01 — PBR pipeline shootout

**Tools:** [Material Maker](tools/material-maker.md), [Ucupaint](tools/ucupaint.md), DiffusedTexture (research)

**Outputs:** Base Color, Normal, Roughness, Metallic (when appropriate), source projects, in-world PBR screenshots

**Measure:** authoring time, seam quality, editability, phenotype repeatability, Second Life appearance, license safety

---

## E02 — Image-to-3D baseline

**Tools:** [TripoSR](tools/triposr.md), InstantMesh, TRELLIS.2 (hardware permitting)

**Measure:** silhouette, topology, UV/texture usefulness, editability, retopology time, SL upload readiness, license chain

Yellow/red candidates stay research-only until cleared.

---

## E03 — Organic retopology benchmark

**Tools:** Blender native/manual, [RetopoFlow](tools/retopoflow.md); postSilver retopology_tool for static/LOD comparison only

**Measure:** time, edge flow, poly count, UV/LOD handoff, deformation on basic rig

---

## E04 — Rig and retarget baseline

**Tools:** [Blender](tools/blender.md) + Rigify Basic Quadruped, [Blender Animation Retargeting](https://github.com/Mwni/blender-animation-retargeting)

**Steps:** rig → idle/walk → retarget → bake → Animesh-oriented export assumptions

**Record:** bone mapping, cleanup effort, root motion, failure cases

---

## E05 — Modern SL persistence fixture

**Platform:** Linkset Data, link messages, [LSL definitions](https://github.com/secondlife/lsl-definitions)

**Test:** script reset, re-rez, state ownership, module versioning, fake genetics state, debug visibility

Compare lessons against historical XS Pet modular patterns (reference only — do not copy blindly).

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
