# Phase 0 Open-Source Breedables Technology Survey

Date: 2026-08-23

Goal: establish a species-independent production and learning toolbox before selecting the first commercial breedable.

## Decision model

Every candidate is classified on two axes.

License / commercial safety:
- GREEN — clearly commercial-friendly for our intended use.
- YELLOW — useful, but dependency, model-weight, asset, territorial, or other license terms require further review.
- RED — not suitable for commercial production under current terms.

Readiness:
- USE NOW — species-independent and practical now.
- EXPERIMENT — requires measured testing before approval.
- USE LATER — depends materially on the eventual species or product design.
- RESEARCH ONLY — useful for learning, not a production dependency.

Open-source code, model weights, bundled assets, generated outputs, and dependency licenses must be audited separately.

## Recommended baseline

### Texture / PBR

#### Material Maker — GREEN / USE NOW
- Repository: https://github.com/RodZill4/material-maker
- License: MIT unless otherwise specified in the repository.
- Role: procedural PBR texture authoring and 3D painting.
- Breedables use: reusable organic material generators for skin, fur-like surfaces, scales, shell, horn, eye surrounds, pads, claws, accessories, and environment props.
- Decision: first-choice open-source procedural material authoring candidate.

#### Ucupaint — GREEN / USE NOW
- Repository: https://github.com/ucupumar/ucupaint
- License: GPL-3.0.
- Role: Blender texture-layer management and painting.
- Breedables use: hand-painted refinement, masks, detail layers, phenotype variations, cleanup after procedural generation.
- Decision: test alongside Material Maker rather than as a replacement.

#### Poly Haven — GREEN / USE NOW
- Site: https://polyhaven.com/
- License: CC0 for HDRIs, textures, and 3D models.
- Breedables use: lighting environments, material references, props, benchmark assets.
- Decision: approved source with provenance recorded per asset.

#### ambientCG — GREEN / USE NOW
- Site: https://ambientcg.com/
- License: CC0 assets.
- Breedables use: PBR materials and reference assets.
- Decision: approved source with provenance recorded per asset.

#### DiffusedTexture — YELLOW / EXPERIMENT
- Repository: https://github.com/FrederikHasecke/diffused-texture-addon
- Code license: GPL-3.0.
- Risk: the total workflow depends on diffusion/checkpoint components whose licenses must be audited separately.
- Decision: compare output quality against Material Maker/Ucupaint; do not approve a checkpoint merely because the Blender add-on is open source.

#### Texture Diffusion — YELLOW / EXPERIMENT
- Repository: https://github.com/Shaamallow/texture-diffusion
- Code license: AGPL-3.0.
- Risk: model and checkpoint license chain varies.
- Decision: research candidate only until complete pipeline licensing is documented.

#### MatLat — RED / RESEARCH ONLY
- Repository: https://github.com/KAIST-Visual-AI-Group/MatLat
- Code may be open, but published pretrained checkpoint weights are CC BY-NC 4.0.
- Decision: do not use its pretrained weights in commercial Breedables Studio production.

## 3D generation / retopology / LOD

#### TripoSR — GREEN / EXPERIMENT
- Repository: https://github.com/VAST-AI-Research/TripoSR
- License: MIT for source code and pretrained model according to the official repository.
- Role: fast single-image 3D reconstruction with optional texture baking.
- Breedables use: concept/blockout/reference geometry generation, never assumed production-ready without cleanup.
- Decision: cleanest image-to-3D baseline in this survey; test first.

#### InstantMesh — YELLOW / EXPERIMENT
- Repository: https://github.com/TencentARC/InstantMesh
- Code license: Apache-2.0.
- Risk: model/dependency chain must be audited independently.
- Decision: test against TripoSR, but do not promote until model/dependency rights are recorded.

#### TRELLIS.2 — YELLOW / EXPERIMENT
- Repository: https://github.com/microsoft/TRELLIS.2
- Upstream states MIT for model/code, while some dependencies have separate terms.
- Decision: technically promising, but dependency-license audit is mandatory before commercial approval.

#### Hunyuan3D-2.1 — RED / RESEARCH ONLY
- Repository: https://github.com/Tencent-Hunyuan/Hunyuan3D-2.1
- License: custom Tencent Community License with territorial/use constraints.
- Decision: exclude from the commercial Second Life pipeline unless its licensing situation materially changes or legal review clears our intended distribution.

#### RetopoFlow — YELLOW / EXPERIMENT
- Repository: https://github.com/CGCookie/retopoflow
- Code: GPL; repository non-code assets have separate restrictions.
- Role: manual animation-friendly organic retopology workflow.
- Decision: strong benchmark tool; avoid assuming every bundled asset is freely redistributable.

#### postSilver retopology_tool — GREEN CODE / LIMITED USE
- Repository: https://github.com/postsilver/retopology_tool
- License: GPL-3.0.
- Role: automated QuadriFlow/LOD workflow.
- Limitation: not our primary rigged-character retopology path.
- Decision: test on static props and LOD experiments.

## Rigging / animation

#### Blender Rigify — GREEN / USE NOW
- Documentation: https://docs.blender.org/manual/en/latest/addons/rigify/index.html
- Bundled with Blender.
- Role: rig-generation baseline, including generic quadruped workflows.
- Decision: use for Academy rigging and neutral four-legged fixture tests before species selection.

#### Blender Animation Retargeting — GREEN / EXPERIMENT
- Repository: https://github.com/Mwni/blender-animation-retargeting
- License: GPL-3.0-or-later.
- Role: armature-to-armature pose/animation transfer, alignment, mapping, baking.
- Decision: first open retargeting benchmark.

#### Rokoko Studio Live Blender — YELLOW / OPTIONAL EXPERIMENT
- Repository: https://github.com/Rokoko/rokoko-studio-live-blender
- License: LGPL-3.0 for plugin.
- Risk: external ecosystem dependency and strong human-motion focus.
- Decision: comparison tool, not core dependency.

## Second Life platform baseline

### PBR Materials — USE NOW
- Reference: https://wiki.secondlife.com/wiki/PBR_Materials
- Second Life uses Metallic/Roughness PBR and glTF 2.0 material upload.
- Decision: all material experiments should ultimately be judged in Second Life, not only Blender renders.

### Animesh — USE NOW
- Reference: https://wiki.secondlife.com/wiki/Animesh_User_Guide
- Role: runtime target for independent animated creature objects.
- Decision: part of the pre-species animation/rigging curriculum.

### Linkset Data — USE NOW / ARCHITECTURE TEST
- Reference: https://create.secondlife.com/script/lsl-reference/functions/lllinksetdatawrite/
- Role: persistent state storage at linkset level.
- Decision: test directly before finalizing persistence architecture; do not copy older breedable persistence patterns without comparison.

### Canonical LSL definitions — USE NOW
- Repository: https://github.com/secondlife/lsl-definitions
- Role: authoritative current LSL/SLua definition source for tooling and validation.

### XS Pet / historical open breedable scripts — GREEN REFERENCE / RESEARCH
- Reference: https://outworldz.com/Secondlife/Posts/Breedable-pet/
- Historical modular breedable code includes aging, breeding, eating, movement, food, eggs, homes, transport, updating, and debugging concerns.
- Decision: study architecture patterns and failure modes, but modernize around current Second Life capabilities such as Linkset Data, Animesh, and PBR.

## First five experiments

### E01 — PBR pipeline shootout
Use one generic organic test mesh.

Compare:
- Material Maker
- Ucupaint
- DiffusedTexture

Outputs:
- Base Color
- Normal
- Roughness
- Metallic only when physically appropriate
- source project files
- Second Life PBR screenshots

Measure:
- authoring time
- seam quality
- editability
- repeatability for phenotype variants
- Second Life appearance
- license safety

### E02 — Image-to-3D baseline
Use the same reference image with:
- TripoSR
- InstantMesh
- TRELLIS.2, hardware permitting

Measure:
- silhouette accuracy
- topology
- UV usefulness
- texture usefulness
- editability
- retopology time
- SL upload readiness
- license/dependency status

Yellow candidates remain research-only until cleared.

### E03 — Organic retopology benchmark
Use the same deliberately messy organic mesh.

Compare:
- Blender native/manual workflow
- RetopoFlow

Measure:
- time
- edge flow around deformation areas
- polygon count
- UV/LOD handoff
- deformation quality on a basic rig

Use postSilver tooling only as a static/LOD automation comparison.

### E04 — Rig and retarget baseline
Use a neutral four-legged organic test mesh.

Steps:
- Rigify Basic Quadruped baseline
- create or import a simple idle and walk
- retarget with Blender Animation Retargeting
- bake final clips
- test Animesh-oriented export/runtime assumptions

Record bone mapping, cleanup effort, root-motion behavior, and failure cases.

### E05 — Modern SL persistence fixture
Build a non-shipping, fake-trait fixture with a few small LSL scripts.

Use:
- link messages for runtime events
- Linkset Data for durable state where appropriate

Test:
- script reset
- re-rez
- state ownership
- missing/outdated module behavior
- deterministic fake genetics state
- debug visibility

Compare lessons against XS Pet's historical modular architecture.

## Academy mapping

Every experiment doubles as training and must produce an artifact.

- A01 Organic PBR Material -> E01
- A02 Layered Texture Refinement -> E01
- A03 Organic Retopology -> E03
- A04 Rig + Two Animations -> E04
- A05 Second Life Creature Fixture -> E05

Watching a tutorial is not completion. Completion requires source files, exported assets, notes/measurements, and where applicable an in-world Second Life result.

## Current recommended order

1. E01 PBR pipeline shootout
2. E03 organic retopology benchmark
3. E04 rig/retarget baseline
4. E05 modern SL persistence fixture
5. E02 image-to-3D baseline

Reason: E01 is cheap, species-independent, immediately reusable, and maps directly to Second Life's current Metallic/Roughness PBR workflow. Image-to-3D remains useful, but it should not dictate the production pipeline before we have validated topology/material/rigging standards.

## Promotion rule

A tool enters `tools/approved/` only after:
- license and dependency review recorded
- reproducible setup documented
- a concrete Breedables Studio experiment completed
- output artifact saved
- measured result documented
- explicit PASS decision

A compelling demo, star count, or AI hype is not an approval criterion.
