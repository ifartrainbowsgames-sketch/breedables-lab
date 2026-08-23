# Breedables production line

!!! info "About this page"
    **Date** — 2026-08-23  
    **Status** — DRAFT — Academy + studio source of truth  
    **Related** — [Software & Tools](software/index.md) · [Blender Foundations](software/blender/index.md) · [Wiki concept audit](../research/wiki-concept-audit.md)

This document explains the **full breedables production line** — every stage from research to in-world release — and for **each stage** defines:

1. **What it is for** (breedables context)  
2. **How we use it** in this studio  
3. **Free tools** · **Paid tools** · **Which is better for us** (with reasons, not color labels)  
4. **What people must learn** (videos, docs, labs, evidence)  
5. **Where docs live** (this wiki + `training/` evidence folders)  

**Rule:** Decisions require **evidence** (links, artifacts, measurements). See [Academy overview](overview.md).

---

## Production line overview

```
Research → Concept → Model → Retopo/LOD → UV → Texture/PBR → Rig → Animate
    → Export/Optimize → SL Upload → Script/Engine → Genetics/Data → HUD/UI
        → In-world Test → Release → Maintain
```

| # | Stage | Studio lab | Benchmark | Where the work lands |
|---|-------|------------|-----------|----------------------|
| 0 | Research & tool selection | — | — | `research/` |
| 1 | Concept & art direction | *planned* | — | `docs/art-style/`, `assets/references/` |
| 2 | Modeling | *planned* | — | `training/modeling/` |
| 3 | Retopology & LOD | [Retopology](tracks/a03-retopology.md) | [E03](../production/experiments.md#e03-organic-retopology-benchmark) | `training/modeling/` |
| 4 | UV mapping | covered by the texturing labs | [E01](../production/experiments.md#e01-pbr-pipeline-shootout) | `training/texturing/` |
| 5 | Texturing & PBR | [Organic PBR material](tracks/a01-organic-pbr.md), [Layered textures](tracks/a02-layered-textures.md) | [E01](../production/experiments.md#e01-pbr-pipeline-shootout) | `training/texturing/` |
| 6 | Image-to-3D *(optional)* | *research only* | [E02](../production/experiments.md#e02-image-to-3d-baseline) | `research/experiments/e02/` |
| 7 | Rigging | [Rig + animation](tracks/a04-rig-animation.md) | [E04](../production/experiments.md#e04-rig-and-retarget-baseline) | `training/rigging/` |
| 8 | Animation | [Rig + animation](tracks/a04-rig-animation.md) | [E04](../production/experiments.md#e04-rig-and-retarget-baseline) | `training/animation/` |
| 9 | Export & optimization | *planned* | — | `pipeline/export/`, `pipeline/optimization/` |
| 10 | Second Life upload & PBR verify | [Organic PBR material](tracks/a01-organic-pbr.md), [In-world fixture](tracks/a05-sl-fixture.md) | [E01](../production/experiments.md#e01-pbr-pipeline-shootout) | `training/secondlife/` |
| 11 | LSL / engine | [In-world fixture](tracks/a05-sl-fixture.md) | [E05](../production/experiments.md#e05-modern-sl-persistence-fixture) | `scripts/`, `training/lsl/` |
| 12 | Genetics & data | *planned* | [E05](../production/experiments.md#e05-modern-sl-persistence-fixture) | `data/` |
| 13 | HUD & UI | *planned* | — | `hud/` |
| 14 | In-world testing | [In-world fixture](tracks/a05-sl-fixture.md) | [E05](../production/experiments.md#e05-modern-sl-persistence-fixture) | `training/secondlife/`, `tests/` |
| 15 | Release | — | — | `releases/`, `creatures/` |

---


## Stage 0 — Research & tool selection

Before building a species, we need a **species-independent** toolbox: tools that work for any creature (cat, dragon, etc.) with licenses and workflows safe for **commercial SL breedables**.

!!! tip "Studio pick"
    **Librarian + git research reports** beat ad-hoc bookmarks. AI drafts reports; **humans** approve after evidence exists.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Breedables Librarian** | `tools/librarian/` | Registry, link checks, wiki lookup |
    | **GitHub** | https://github.com | Source code, issues, releases |
    | **ChatGPT / Claude** | AI assistants | Draft research — human reviews |
    | **MkDocs wiki** | this site | Published curriculum |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | *(none required at research stage)* | | |

**How we use it**

- Discover tools via GitHub, feeds, community, AI-assisted research  
- Record **evidence** in `research/reports/` — not approval colors in chat  
- Run benchmarks (E01–E05) before trusting a tool in production  
- Librarian registry holds URLs, links, evidence paths

**What to complete**

- Read: [Phase 0 survey summary](../research/phase-0-survey.md)  
- Read: [Software & Tools hub](software/index.md)  
- Do: Add one discovery note to `research/discoveries/` with URL + breedables use case

**Evidence folder** — `research/reports/`, `research/discoveries/`  
**Related pages** — [Software & Tools](software/index.md) · [Tools registry](../production/tools/index.md) · [Phase 0 survey](../research/phase-0-survey.md)

---
## Stage 1 — Concept & art direction

Define **look and rules** before modeling: proportions, silhouette, material style, rarity visual language — species-independent principles first, specific creature later.

!!! tip "Studio pick"
    **Blender blockout + PureRef/Krita** — fully free path sufficient for breedables pre-production. Paid Photoshop only if team already owns it.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | https://www.blender.org/ | Blockout meshes, grease pencil |
    | **PureRef** | https://www.pureref.com/ | Reference boards *(free tier)* |
    | **Pen & paper / Krita** | https://krita.org/ | 2D concept *(Krita free)* |

=== "Paid tools"

    | Tool | Link | Best for | Cost note |
    |------|------|----------|-----------|
    | **PureRef** pro | pureref.com | Larger boards | Optional |
    | **Photoshop** | adobe.com | Photo bashing concepts | Subscription |

**How we use it**

- Reference boards in `assets/references/` (respect copyright — no unlicensed redistribution)  
- Written art rules in `docs/art-style/` (to create)  
- Concept can use sketches, TripoSR blockouts (E02), or manual Blender blockout

**What to complete**

- Watch: [Blender Guru — Donut modeling](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) · [Lesson 3 — lesson](software/blender/b03-mesh-modeling.md)  
- Read: [PureRef package](software/packages/pureref.md) · `assets/references/` when created  
- Produce: reference board + simple blockout `.blend`

**Evidence folder** — `assets/references/`, `training/modeling/concept/`  
**Related pages** — [Lesson 3 — Mesh modeling](software/blender/b03-mesh-modeling.md) · [Lesson 4 — Sculpting](software/blender/b04-sculpting.md)

---
## Stage 2 — Modeling (organic mesh)

Create the **3D creature mesh**: body, head, limbs, organic forms suitable for retopo, rigging, and SL land-impact limits later.

!!! tip "Studio pick"
    **Blender** is the studio hub — free, GPL, full pipeline. **TripoSR** for fast blockouts when E02 evidence shows acceptable cleanup cost. **ZBrush** optional for artists who already use it — not a studio dependency.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | https://www.blender.org/ | Full modeling pipeline |
    | **Blender sculpt tools** | bundled | Organic forms |
    | **TripoSR** | https://github.com/VAST-AI-Research/TripoSR | Image → blockout mesh (E02) |
    | **InstantMesh** | https://github.com/TencentARC/InstantMesh | Compare vs TripoSR (research) |

=== "Paid tools"

    | Tool | Link | Best for | Cost note |
    |------|------|----------|-----------|
    | **ZBrush** | pixologic.com | Industry sculpt | Paid — not required if Blender suffices |
    | **Tripo / Meshy** (SaaS) | various | AI mesh gen | Pay per gen — audit ToS for commercial |

**How we use it**

- High-poly sculpt or medium-poly box modeling in Blender  
- Species-independent **neutral quadruped fixture** for Academy before cat species  
- Image-to-3D (E02) for **concept only** — never ship without retopo cleanup

**What to complete**

- Watch: [Grant Abbitt — modeling](https://www.youtube.com/@grabbitt) · [Video library — Blender](resources/video-library.md#blender)  
- Read: [Blender tool page](../production/tools/blender.md)  
- Do: neutral quadruped blockout mesh  
- Produce: `.blend` in `training/modeling/`

**Evidence folder** — `training/modeling/`  
**Related pages** — [Lesson 3 — Mesh modeling](software/blender/b03-mesh-modeling.md) · [Lesson 4 — Sculpting](software/blender/b04-sculpting.md)

---
## Stage 3 — Retopology & LOD

Animation-ready **clean topology**, sensible poly budget, optional LOD for SL land impact.

!!! tip "Studio pick"
    **Blender manual retopo** for anything that deforms. **RetopoFlow** if E03 proves time savings worth license/asset review. **postSilver** for props/LOD side tests — not primary creature path.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** (manual) | blender.org | Full control, rigged characters |
    | **RetopoFlow** | https://github.com/CGCookie/retopoflow | Speed benchmark *(GPL code; check bundled assets)* |
    | **postSilver retopology_tool** | https://github.com/postsilver/retopology_tool | Auto QuadriFlow / LOD on static meshes |

=== "Paid tools"

    | Tool | Link | Best for | Cost note |
    |------|------|----------|-----------|
    | **RetopoFlow** (Blender Market) | blender market | Support CG Cookie | Often same add-on; verify license |
    | **TopoGun** | topogun.com | Standalone retopo | Paid — rarely needed with Blender |

**How we use it**

- Manual retopo for rigged creatures (primary path)  
- RetopoFlow as benchmark tool (license/asset audit required)  
- postSilver tool for **static props / LOD experiments only**

**What to complete**

- Studio labs: [Retopology](tracks/a03-retopology.md)  
- Experiments:   
- Watch: [Royal Skies — retopology](https://www.youtube.com/watch?v=h6E9N10rN5s) · [Lesson 5 — lesson](software/blender/b05-retopology.md) · [Video library — retopo](resources/video-library.md#blender)  
- Produce: retopo mesh + timing log

**Evidence folder** — `training/modeling/a03/`, `research/experiments/e03/`  
**Related pages** — [Lesson 5 — Retopology](software/blender/b05-retopology.md) · [A03 Retopology](tracks/a03-retopology.md)

---
## Stage 4 — UV mapping

Clean UVs for PBR texturing, phenotype variants, and efficient texture resolution in SL.

!!! tip "Studio pick"
    **Blender built-in UV** until pain points prove otherwise. Paid UV tools only after measured bottleneck.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender UV tools** | bundled | Standard workflow |
    | **UVPackmaster** *(check license)* | GitHub/market | Packing — evaluate if needed |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **UVPackmaster** | extensions | Faster packing |
    | **RizomUV** | rizomuv.com | Pro UV — optional |

**How we use it**

- Blender UV editing; minimize seams on visible areas  
- Pack for shared texture space across LODs where applicable

**What to complete**

- Part of **A01/A02** labs  
- Produce: UV layout screenshots + exported UV PNG

**Evidence folder** — `training/texturing/`  
**Related pages** — [Lesson 6 — UV unwrapping](software/blender/b06-uv-unwrapping.md)

---
## Stage 5 — Texturing & PBR (Second Life Metallic/Roughness)

Author **PBR materials** that read correctly in Second Life: skin, fur-like surfaces, scales, eyes, accessories — with phenotype variation support.

!!! tip "Studio pick"
    **Material Maker + Ucupaint + Blender** — free, open pipeline aligned with E01. **Substance Painter** better for teams already subscribed; run E01 comparison before adopting. **Poly Haven / ambientCG** for CC0 inputs — always record provenance.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | blender.org | Shader editor, baking |
    | **Material Maker** | https://github.com/RodZill4/material-maker | Procedural PBR generators |
    | **Ucupaint** | https://github.com/ucupumar/ucupaint | Layers, hand paint in Blender |
    | **Poly Haven** | https://polyhaven.com/ | CC0 HDRIs, textures, models |
    | **ambientCG** | https://ambientcg.com/ | CC0 PBR materials |

=== "Paid tools"

    | Tool | Link | Best for | Cost note |
    |------|------|----------|-----------|
    | **Substance 3D Painter** | adobe.com | Industry texturing | Subscription — powerful but not required |
    | **Substance Designer** | adobe.com | Node materials | Overlap with Material Maker |
    | **Quixel / Megascans** | quixel.com | Scan libraries | License varies |

**How we use it**

- Procedural bases (Material Maker) + hand refinement (Ucupaint)  
- CC0 assets from Poly Haven / ambientCG with **provenance per file**  
- Validate **in-world** — Blender render alone is not enough

**What to complete**

- Studio labs: [Organic PBR material](tracks/a01-organic-pbr.md), [Layered textures](tracks/a02-layered-textures.md)  
- Experiments:   
- Read: [SL PBR wiki](https://wiki.secondlife.com/wiki/PBR_Materials), [platform baseline](../secondlife/platform-baseline.md)  
- Produce: texture sets + **SL in-world screenshot**

**Evidence folder** — `training/texturing/a01/`, `training/texturing/a02/`, `research/experiments/e01/`  
**Related pages** — [Lesson 7 — Texture & PBR](software/blender/b07-texture-painting-pbr.md) · [Organic PBR material](tracks/a01-organic-pbr.md) · [Layered textures](tracks/a02-layered-textures.md)

---
## Stage 6 — Image-to-3D (research / blockout)

Fast **concept geometry** from reference art — not a replacement for modeling standards.

!!! tip "Studio pick"
    **TripoSR (local, open)** for controlled E02 evidence. Hosted SaaS only after explicit commercial/legal review. **Hunyuan3D** excluded from commercial SL pipeline per Phase 0 research.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **TripoSR** | GitHub | First baseline (MIT code/model per upstream) |
    | **InstantMesh** | GitHub | Comparison |
    | **TRELLIS.2** | GitHub | Research — dependency audit required |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Tripo3D** (SaaS) | tripo3d.ai | Hosted gen — check commercial ToS |
    | **Meshy** | meshy.ai | Hosted gen — check ToS |

**How we use it**

- E02 benchmark only until evidence shows SL-ready output with acceptable cleanup  
- Never ship raw AI mesh without retopo + license audit

**What to complete**

- Experiments:  (after E01, E03, E04, E05)  
- Produce: comparison table + cleaned mesh attempt

**Evidence folder** — `research/experiments/e02/`  
**Related pages** — [TripoSR](../production/tools/triposr.md) · [Research candidates](../production/tools/research-candidates.md)

---
## Stage 7 — Rigging

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

- Studio labs: [Rig + animation](tracks/a04-rig-animation.md) (rig portion)  
- Experiments:   
- Produce: Rigify quadruped rig `.blend`

**Evidence folder** — `training/rigging/a04/`  
**Related pages** — [Lesson 8 — Rigging](software/blender/b08-rigging-weight-painting.md) · [Rig + animation](tracks/a04-rig-animation.md)

---
## Stage 8 — Animation

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

- Studio labs: [Rig + animation](tracks/a04-rig-animation.md) (animation portion)  
- Produce: idle + walk baked clips + notes

**Evidence folder** — `training/animation/a04/`  
**Related pages** — [Lesson 9 — Animation](software/blender/b09-animation.md) · [Rig + animation](tracks/a04-rig-animation.md)

---
## Stage 9 — Export & optimization

Deliver **SL-ready** meshes and materials: poly limits, land impact awareness, glTF export paths for PBR.

!!! tip "Studio pick"
    **Blender glTF** for PBR material path (studio baseline). **Avastar** worth evaluating for mesh/rig export to SL — paid but SL-specific; add E-export experiment when cat species starts.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender glTF exporter** | bundled | PBR material export |
    | **Custom Python in pipeline/** | repo | Repeatable export |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Avastar** | avastar.de | SL-specific Blender rig/export — **strong paid option for SL** |
    | **Catalyst** | various | SL mesh tools |

**How we use it**

- Blender export presets in `pipeline/export/`  
- Optimization passes in `pipeline/optimization/`  
- Pre-upload validation in `pipeline/validation/`

**What to complete**

- Read: SL mesh upload docs on [create.secondlife.com](https://create.secondlife.com/)  
- Produce: exported glTF/SL upload package + LI notes

**Evidence folder** — `pipeline/export/`, `training/secondlife/export/`  
**Related pages** — [Lesson 10 — Export to SL](software/blender/b10-export-to-sl.md)

---
## Stage 10 — Second Life upload & PBR verification

Confirm assets **look and behave correctly in the real runtime** — not just in Blender.

!!! tip "Studio pick"
    Official **SL viewer + wiki** — no substitute. Budget for test sandbox land as ops cost.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Second Life viewer** | secondlife.com | Upload & test |
    | **SL wiki PBR** | [PBR Materials](https://wiki.secondlife.com/wiki/PBR_Materials) | Official reference |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Land for testing** | SL premium/plot | Stable test region |

**How we use it**

- Upload PBR materials via glTF 2.0 workflow  
- Screenshot under consistent windlight/sky  
- Compare to Blender reference — document differences

**What to complete**

- Part of **A01**, **A05**  
- Produce: dated in-world screenshots with viewer version

**Evidence folder** — `training/secondlife/`  
**Related pages** — [Lesson 10 — Export to SL](software/blender/b10-export-to-sl.md) · [A05 SL fixture](tracks/a05-sl-fixture.md) · [Platform baseline](../secondlife/platform-baseline.md)

---
## Stage 11 — LSL / breedables engine scripting

Runtime logic: breeding, aging, movement, food, persistence, updates — modular engine in `scripts/`.

!!! tip "Studio pick"
    **In-viewer + git** for script modules. No paid tool required.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **SL script editor** | in viewer | Deploy LSL |
    | **lsl-definitions** | GitHub | API accuracy |
    | **VS Code + LSL syntax** | community extensions | External editing |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | *(none required)* | | |

**How we use it**

- Modern patterns: **Linkset Data**, Animesh, PBR — study XS Pet for lessons, do not copy blindly  
- Canonical definitions: [lsl-definitions](https://github.com/secondlife/lsl-definitions)  
- Fake-trait fixture in E05 before species-specific genetics

**What to complete**

- Studio labs: [In-world fixture](tracks/a05-sl-fixture.md)  
- Experiments:   
- Produce: LSL modules + test harness in-world

**Evidence folder** — `scripts/`, `training/lsl/a05/`  
**Related pages** — [A05 SL fixture](tracks/a05-sl-fixture.md) · [LSL engine overview](../studio/lsl-engine-overview.md)

---
## Stage 12 — Genetics & data definitions

Data-driven **traits, colors, rarity, mutations** separate from code — enables balance without rewriting engine.

!!! tip "Studio pick"
    **Git-tracked data files** as source of truth; spreadsheets for draft only.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Git + text editor** | — | Schema and tables |
    | **Python validation scripts** | `pipeline/validation/` | Schema checks |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Spreadsheets** (Excel/Sheets) | — | Design-phase tuning — export to git |

**How we use it**

- JSON/YAML or similar in `data/genes/`, `data/traits/`, etc.  
- Engine reads definitions; designers tune tables

**What to complete**

- Read: `data/README.md`  
- Do: design fake-trait tables for E05 fixture

**Evidence folder** — `data/`  
**Related pages** — [Production line](production-line.md) · [Decision model](../production/decision-model.md)

---
## Stage 13 — HUD & player UI

In-world menus, breeding UI, status displays, updater flows — packaged in `hud/`.

!!! tip "Studio pick"
    Build custom HUD art in Blender + our PBR pipeline for consistency.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | — | HUD texture assets |
    | **SL UI primitives** | wiki | Buttons, dialogs |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **FUI designers** | various | Optional texture packs |

**How we use it**

- LSL + SL UI conventions  
- Separate from creature body scripts where possible

**What to complete**

- *(Track A-hud — to define after A05)*

**Evidence folder** — `hud/`  
**Related pages** — [Production line](production-line.md) *(A-hud track planned)*

---
## Stage 14 — In-world testing & QA

Prove breeding loop, persistence, animations, and updates work under real SL conditions (re-rez, reset, sim restart).

!!! tip "Studio pick"
    Structured test checklist in wiki + GitHub issues for traceability.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Alt accounts** | SL | Multi-user breeding tests |
    | **GitHub Issues** | github.com | Bug tracking |

**How we use it**

- Test scripts in `tests/`  
- Checklists per release  
- Log bugs in git issues with repro steps + screenshots

**Evidence folder** — `tests/`, `training/secondlife/qa/`  
**Related pages** — [A05 SL fixture](tracks/a05-sl-fixture.md) · [Experiments](../production/experiments.md)

---
## Stage 15 — Release & maintenance

Ship versioned packages to players; document changes; support updates via engine updater module.

!!! tip "Studio pick"
    Git tags + markdown release notes tied to test evidence.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Git tags** | GitHub | Version markers |
    | **MkDocs** | this wiki | Player-facing docs *(if public)* |

**How we use it**

- Release notes in `releases/`  
- Creature-specific packages in `creatures/<species>/`  
- Announce in `#releases` with links to evidence-tested builds

**Evidence folder** — `releases/`, `creatures/`  
**Related pages** — [Promotion rules](../production/promotion-rules.md) · [Studio roadmap](../studio-roadmap.md)

---

## Academy track index (learning paths)

| Track | Stage(s) | Status |
|-------|----------|--------|
| **A01** Organic PBR Material | 4–5, 10 | Spec in production line — **fill videos next** |
| **A02** Layered Texture Refinement | 4–5 | Same |
| **A03** Organic Retopology | 3 | Same |
| **A04** Rig + Two Animations | 7–8 | Same |
| **A05** SL Creature Fixture | 10–11, 14 | Same |
| **A00** Concept *(planned)* | 1 | Template only |
| **A-model** Modeling *(planned)* | 2 | Template only |
| **A-export** SL export *(planned)* | 9 | Template only |
| **A-data** Genetics *(planned)* | 12 | Template only |
| **A-hud** HUD *(planned)* | 13 | Template only |

Every track page uses **Watch · Read · Explain · Do · Produce · Completed when** — see [Academy overview](overview.md).

---

## Tool comparison rules (studio-wide)

When writing “which is better”:

1. State **breedables-specific** criterion (SL PBR, quadruped rig, commercial license, etc.)  
2. List **free option first**  
3. Paid only if it wins on measured evidence from an experiment  
4. Link to **E01–E05** or `research/experiments/` result  
5. **Never** use GREEN/YELLOW/RED in learner-facing text  

---

## Next actions (in order)

1. **Approve** this production line as the master map  
2. Create `docs/academy/resources/videos.md` — start curating real URLs per stage  
3. Build **A01 lesson page** first (full Watch/Read/Do/Produce)  
4. Update Librarian `/breedtool` to link lesson + evidence path  
5. Add E01 evidence folder with first complete artifact package  

---

## References

- [Software & Tools](software/index.md)  
- [Blender Foundations](software/blender/index.md)  
- [Tutorial arsenal](resources/tutorials.md)  
- [Experiments](../production/experiments.md)  
- [Second Life baseline](../secondlife/platform-baseline.md)  
- [Phase 0 survey](../research/phase-0-survey.md)

---

## For maintainers — stage template

??? note "Copy this skeleton when adding or updating a stage"

    Every stage answers the same five questions in the same order, so readers can
    scan any stage the way they scanned the last one. Use **bold labels**, not
    `###` headings — headings here would flood the table of contents.

    ```markdown
    ## Stage N — Name

    One paragraph: why this stage exists for Second Life breedables.

    !!! tip "Studio pick"
        What we chose and **why** — cite evidence when we have it.

    === "Free tools"

        | Tool | Link | Best for |
        |------|------|----------|

    === "Paid tools"

        | Tool | Link | Best for | Cost note |
        |------|------|----------|-----------|

    **How we use it**

    - Studio workflow rules

    **What to complete**

    - Watch / Read / Do / Produce

    **Evidence folder** — `path/in/repo/`
    **Related pages** — links to lessons and studio labs
    ```

    **Rule:** a studio pick is only valid with evidence behind it — a link, an
    artifact, or a measurement. See [Academy overview](overview.md).
