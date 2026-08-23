# Breedables Production Line — Master Spec

**Date:** 2026-08-23  
**Status:** DRAFT — Academy + studio source of truth  
**Related:** [Channel map](../studio/channel-map.md) · [Content requirements](../studio/channel-content-requirements.md) · [Wiki concept audit](../research/wiki-concept-audit.md)

This document explains the **full breedables production line** — every stage from research to in-world release — and for **each stage** defines:

1. **What it is for** (breedables context)  
2. **How we use it** in this studio  
3. **Free tools** · **Paid tools** · **Which is better for us** (with reasons, not color labels)  
4. **What people must learn** (videos, docs, labs, evidence)  
5. **Which channel** (Slack, wiki, repo) owns it  

**Rule:** Decisions require **evidence** (links, artifacts, measurements). See [content requirements](../studio/channel-content-requirements.md).

---

## Production line overview

```
Research → Concept → Model → Retopo/LOD → UV → Texture/PBR → Rig → Animate
    → Export/Optimize → SL Upload → Script/Engine → Genetics/Data → HUD/UI
        → In-world Test → Release → Maintain
```

| Stage | Academy track | Experiment | Primary repo |
|-------|---------------|------------|--------------|
| 0 Research & tools | — | — | `research/` |
| 1 Concept & art direction | *(A00 planned)* | — | `docs/art-style/`, `assets/references/` |
| 2 Modeling | *(A-model planned)* | — | `training/modeling/` |
| 3 Retopology & LOD | **A03** | E03 | `training/modeling/` |
| 4 UV mapping | part of A01/A02 | E01 | `training/texturing/` |
| 5 Texturing & PBR | **A01**, **A02** | E01 | `training/texturing/` |
| 6 Image-to-3D (optional) | *(research)* | E02 | `research/experiments/e02/` |
| 7 Rigging | **A04** | E04 | `training/rigging/` |
| 8 Animation | **A04** | E04 | `training/animation/` |
| 9 Export & optimization | *(A-export planned)* | — | `pipeline/export/`, `pipeline/optimization/` |
| 10 SL upload & PBR verify | part of A01/A05 | E01 | `training/secondlife/` |
| 11 LSL / engine | **A05** | E05 | `scripts/`, `training/lsl/` |
| 12 Genetics & data | *(A-data planned)* | E05 | `data/` |
| 13 HUD & UI | *(A-hud planned)* | — | `hud/` |
| 14 In-world testing | **A05** | E05 | `training/secondlife/`, `tests/` |
| 15 Release | — | — | `releases/`, `creatures/` |

---

## Stage template (use for every channel)

When we add or update any stage, fill **all** sections:

```markdown
## Stage N — Name

### What it is for (breedables)
[One paragraph: why this stage exists for SL breedables]

### How we use it
[Our studio workflow rules]

### Tools — free
| Tool | Link | Best for | License note |
|------|------|----------|--------------|

### Tools — paid
| Tool | Link | Best for | Cost note |
|------|------|----------|-----------|

### Which is better for us
[Plain comparison + studio pick + why — cite evidence when we have it]

### What learners must complete
- Watch: [video URLs]
- Read: [doc URLs]
- Do: [lab steps]
- Produce: [artifacts]

### Evidence folder
`path/in/repo/`

### Slack channel
#channel-name

### Wiki lesson
docs/academy/tracks/…
```

---

## Stage 0 — Research & tool selection

### What it is for (breedables)

Before building a species, we need a **species-independent** toolbox: tools that work for any creature (cat, dragon, etc.) with licenses and workflows safe for **commercial SL breedables**.

### How we use it

- Discover tools via GitHub, feeds, community, AI-assisted research  
- Record **evidence** in `research/reports/` — not approval colors in Slack  
- Run benchmarks (E01–E05) before trusting a tool in production  
- Librarian registry holds URLs, links, evidence paths  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Breedables Librarian** | `tools/librarian/` | Registry, link checks, Slack lookup |
| **GitHub** | https://github.com | Source code, issues, releases |
| **ChatGPT / Claude** | Slack apps | Draft research — human reviews |
| **MkDocs wiki** | this site | Published curriculum |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| *(none required at research stage)* | | |

### Which is better for us

**Librarian + git research reports** beat ad-hoc Slack bookmarks. AI drafts reports; **humans** approve after evidence exists.

### What learners must complete

- Read: [Phase 0 survey summary](../research/phase-0-survey.md)  
- Read: [Content requirements](../studio/channel-content-requirements.md)  
- Do: Add one discovery note to `research/discoveries/` with URL + breedables use case  

### Evidence folder

`research/reports/`, `research/discoveries/`

### Slack channel

`#research-rnd`, `#tools-registry`

---

## Stage 1 — Concept & art direction

### What it is for (breedables)

Define **look and rules** before modeling: proportions, silhouette, material style, rarity visual language — species-independent principles first, specific creature later.

### How we use it

- Reference boards in `assets/references/` (respect copyright — no unlicensed redistribution)  
- Written art rules in `docs/art-style/` (to create)  
- Concept can use sketches, TripoSR blockouts (E02), or manual Blender blockout  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** | https://www.blender.org/ | Blockout meshes, grease pencil |
| **PureRef** | https://www.pureref.com/ | Reference boards *(free tier)* |
| **Pen & paper / Krita** | https://krita.org/ | 2D concept *(Krita free)* |

### Tools — paid

| Tool | Link | Best for | Cost note |
|------|------|----------|-----------|
| **PureRef** pro | pureref.com | Larger boards | Optional |
| **Photoshop** | adobe.com | Photo bashing concepts | Subscription |

### Which is better for us

**Blender blockout + PureRef/Krita** — fully free path sufficient for breedables pre-production. Paid Photoshop only if team already owns it.

### What learners must complete

- Watch: *(curate: Blender blocking basics — URL TBD)*  
- Read: `docs/art-style/` when created  
- Produce: reference board + simple blockout `.blend`  

### Evidence folder

`assets/references/`, `training/modeling/concept/`

### Slack channel

`#production`, `#academy`

---

## Stage 2 — Modeling (organic mesh)

### What it is for (breedables)

Create the **3D creature mesh**: body, head, limbs, organic forms suitable for retopo, rigging, and SL land-impact limits later.

### How we use it

- High-poly sculpt or medium-poly box modeling in Blender  
- Species-independent **neutral quadruped fixture** for Academy before cat species  
- Image-to-3D (E02) for **concept only** — never ship without retopo cleanup  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** | https://www.blender.org/ | Full modeling pipeline |
| **Blender sculpt tools** | bundled | Organic forms |
| **TripoSR** | https://github.com/VAST-AI-Research/TripoSR | Image → blockout mesh (E02) |
| **InstantMesh** | https://github.com/TencentARC/InstantMesh | Compare vs TripoSR (research) |

### Tools — paid

| Tool | Link | Best for | Cost note |
|------|------|----------|-----------|
| **ZBrush** | pixologic.com | Industry sculpt | Paid — not required if Blender suffices |
| **Tripo / Meshy** (SaaS) | various | AI mesh gen | Pay per gen — audit ToS for commercial |

### Which is better for us

**Blender** is the studio hub — free, GPL, full pipeline. **TripoSR** for fast blockouts when E02 evidence shows acceptable cleanup cost. **ZBrush** optional for artists who already use it — not a studio dependency.

### What learners must complete

- Watch: Blender organic modeling fundamentals *(URLs TBD — add to video index)*  
- Read: [Blender tool page](../production/tools/blender.md)  
- Do: neutral quadruped blockout mesh  
- Produce: `.blend` in `training/modeling/`  

### Evidence folder

`training/modeling/`

### Slack channel

`#academy`, `#production`

---

## Stage 3 — Retopology & LOD

### What it is for (breedables)

Animation-ready **clean topology**, sensible poly budget, optional LOD for SL land impact.

### How we use it

- Manual retopo for rigged creatures (primary path)  
- RetopoFlow as benchmark tool (license/asset audit required)  
- postSilver tool for **static props / LOD experiments only**  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** (manual) | blender.org | Full control, rigged characters |
| **RetopoFlow** | https://github.com/CGCookie/retopoflow | Speed benchmark *(GPL code; check bundled assets)* |
| **postSilver retopology_tool** | https://github.com/postsilver/retopology_tool | Auto QuadriFlow / LOD on static meshes |

### Tools — paid

| Tool | Link | Best for | Cost note |
|------|------|----------|-----------|
| **RetopoFlow** (Blender Market) | blender market | Support CG Cookie | Often same add-on; verify license |
| **TopoGun** | topogun.com | Standalone retopo | Paid — rarely needed with Blender |

### Which is better for us

**Blender manual retopo** for anything that deforms. **RetopoFlow** if E03 proves time savings worth license/asset review. **postSilver** for props/LOD side tests — not primary creature path.

### What learners must complete

- Track: **A03**  
- Experiment: **E03**  
- Watch: retopo tutorials *(URLs TBD)*  
- Produce: retopo mesh + timing log  

### Evidence folder

`training/modeling/a03/`, `research/experiments/e03/`

### Slack channel

`#production`, `#academy`

---

## Stage 4 — UV mapping

### What it is for (breedables)

Clean UVs for PBR texturing, phenotype variants, and efficient texture resolution in SL.

### How we use it

- Blender UV editing; minimize seams on visible areas  
- Pack for shared texture space across LODs where applicable  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender UV tools** | bundled | Standard workflow |
| **UVPackmaster** *(check license)* | GitHub/market | Packing — evaluate if needed |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **UVPackmaster** | extensions | Faster packing |
| **RizomUV** | rizomuv.com | Pro UV — optional |

### Which is better for us

**Blender built-in UV** until pain points prove otherwise. Paid UV tools only after measured bottleneck.

### What learners must complete

- Part of **A01/A02** labs  
- Produce: UV layout screenshots + exported UV PNG  

### Evidence folder

`training/texturing/`

### Slack channel

`#academy`

---

## Stage 5 — Texturing & PBR (Second Life Metallic/Roughness)

### What it is for (breedables)

Author **PBR materials** that read correctly in Second Life: skin, fur-like surfaces, scales, eyes, accessories — with phenotype variation support.

### How we use it

- Procedural bases (Material Maker) + hand refinement (Ucupaint)  
- CC0 assets from Poly Haven / ambientCG with **provenance per file**  
- Validate **in-world** — Blender render alone is not enough  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** | blender.org | Shader editor, baking |
| **Material Maker** | https://github.com/RodZill4/material-maker | Procedural PBR generators |
| **Ucupaint** | https://github.com/ucupumar/ucupaint | Layers, hand paint in Blender |
| **Poly Haven** | https://polyhaven.com/ | CC0 HDRIs, textures, models |
| **ambientCG** | https://ambientcg.com/ | CC0 PBR materials |

### Tools — paid

| Tool | Link | Best for | Cost note |
|------|------|----------|-----------|
| **Substance 3D Painter** | adobe.com | Industry texturing | Subscription — powerful but not required |
| **Substance Designer** | adobe.com | Node materials | Overlap with Material Maker |
| **Quixel / Megascans** | quixel.com | Scan libraries | License varies |

### Which is better for us

**Material Maker + Ucupaint + Blender** — free, open pipeline aligned with E01. **Substance Painter** better for teams already subscribed; run E01 comparison before adopting. **Poly Haven / ambientCG** for CC0 inputs — always record provenance.

### What learners must complete

- Tracks: **A01**, **A02**  
- Experiment: **E01**  
- Read: [SL PBR wiki](https://wiki.secondlife.com/wiki/PBR_Materials), [platform baseline](../secondlife/platform-baseline.md)  
- Produce: texture sets + **SL in-world screenshot**  

### Evidence folder

`training/texturing/a01/`, `training/texturing/a02/`, `research/experiments/e01/`

### Slack channel

`#academy`, `#secondlife-inworld`

---

## Stage 6 — Image-to-3D (research / blockout)

### What it is for (breedables)

Fast **concept geometry** from reference art — not a replacement for modeling standards.

### How we use it

- E02 benchmark only until evidence shows SL-ready output with acceptable cleanup  
- Never ship raw AI mesh without retopo + license audit  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **TripoSR** | GitHub | First baseline (MIT code/model per upstream) |
| **InstantMesh** | GitHub | Comparison |
| **TRELLIS.2** | GitHub | Research — dependency audit required |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **Tripo3D** (SaaS) | tripo3d.ai | Hosted gen — check commercial ToS |
| **Meshy** | meshy.ai | Hosted gen — check ToS |

### Which is better for us

**TripoSR (local, open)** for controlled E02 evidence. Hosted SaaS only after explicit commercial/legal review. **Hunyuan3D** excluded from commercial SL pipeline per Phase 0 research.

### What learners must complete

- Experiment: **E02** (after E01, E03, E04, E05)  
- Produce: comparison table + cleaned mesh attempt  

### Evidence folder

`research/experiments/e02/`

### Slack channel

`#research-rnd`

---

## Stage 7 — Rigging

### What it is for (breedables)

Deformation-ready **armature** for idle, walk, and future breedable animations — quadruped-first, species-agnostic fixture.

### How we use it

- **Rigify** Basic Quadruped as Academy baseline  
- Custom bone cleanup for SL export constraints  
- Document bone naming for animation retarget  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** | blender.org | Rigging environment |
| **Rigify** | [Blender manual](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) | Quadruped baseline |
| **Auto-Rig Pro** *(check)* | various | Alternative — evaluate in research |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **Auto-Rig Pro** | blendermarket | Faster rig setup |
| **Rigging addons** (various) | market | Time savers |

### Which is better for us

**Rigify (free, bundled)** for curriculum and E04. Paid rig addons only if E04 shows Rigify bottleneck.

### What learners must complete

- Track: **A04** (rig portion)  
- Experiment: **E04**  
- Produce: Rigify quadruped rig `.blend`  

### Evidence folder

`training/rigging/a04/`

### Slack channel

`#academy`, `#production`

---

## Stage 8 — Animation

### What it is for (breedables)

**Idle + walk** minimum for Animesh-style creatures; baked clips for SL constraints.

### How we use it

- Author or import animations  
- **Blender Animation Retargeting** for transfer between armatures  
- Bake to SL-friendly format; test root motion behavior  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** | blender.org | Keyframe, NLA, bake |
| **Blender Animation Retargeting** | https://github.com/Mwni/blender-animation-retargeting | Retarget benchmark |
| **Mixamo** | mixamo.com | Free humanoid clips — limited for quadrupeds |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **Rokoko** ecosystem | rokoko.com | Mocap — human-focused |
| **iClone / others** | various | mocap pipelines |

### Which is better for us

**Blender + retarget add-on** for E04. **Mixamo** rarely fits quadrupeds — research only. **Rokoko** optional comparison, not core.

### What learners must complete

- Track: **A04** (animation portion)  
- Produce: idle + walk baked clips + notes  

### Evidence folder

`training/animation/a04/`

### Slack channel

`#academy`, `#production`

---

## Stage 9 — Export & optimization

### What it is for (breedables)

Deliver **SL-ready** meshes and materials: poly limits, land impact awareness, glTF export paths for PBR.

### How we use it

- Blender export presets in `pipeline/export/`  
- Optimization passes in `pipeline/optimization/`  
- Pre-upload validation in `pipeline/validation/`  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender glTF exporter** | bundled | PBR material export |
| **Custom Python in pipeline/** | repo | Repeatable export |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **Avastar** | avastar.de | SL-specific Blender rig/export — **strong paid option for SL** |
| **Catalyst** | various | SL mesh tools |

### Which is better for us

**Blender glTF** for PBR material path (studio baseline). **Avastar** worth evaluating for mesh/rig export to SL — paid but SL-specific; add E-export experiment when cat species starts.

### What learners must complete

- Read: SL mesh upload docs on [create.secondlife.com](https://create.secondlife.com/)  
- Produce: exported glTF/SL upload package + LI notes  

### Evidence folder

`pipeline/export/`, `training/secondlife/export/`

### Slack channel

`#production`, `#secondlife-inworld`

---

## Stage 10 — Second Life upload & PBR verification

### What it is for (breedables)

Confirm assets **look and behave correctly in the real runtime** — not just in Blender.

### How we use it

- Upload PBR materials via glTF 2.0 workflow  
- Screenshot under consistent windlight/sky  
- Compare to Blender reference — document differences  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Second Life viewer** | secondlife.com | Upload & test |
| **SL wiki PBR** | [PBR Materials](https://wiki.secondlife.com/wiki/PBR_Materials) | Official reference |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **Land for testing** | SL premium/plot | Stable test region |

### Which is better for us

Official **SL viewer + wiki** — no substitute. Budget for test sandbox land as ops cost.

### What learners must complete

- Part of **A01**, **A05**  
- Produce: dated in-world screenshots with viewer version  

### Evidence folder

`training/secondlife/`

### Slack channel

`#secondlife-inworld`

---

## Stage 11 — LSL / breedables engine scripting

### What it is for (breedables)

Runtime logic: breeding, aging, movement, food, persistence, updates — modular engine in `scripts/`.

### How we use it

- Modern patterns: **Linkset Data**, Animesh, PBR — study XS Pet for lessons, do not copy blindly  
- Canonical definitions: [lsl-definitions](https://github.com/secondlife/lsl-definitions)  
- Fake-trait fixture in E05 before species-specific genetics  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **SL script editor** | in viewer | Deploy LSL |
| **lsl-definitions** | GitHub | API accuracy |
| **VS Code + LSL syntax** | community extensions | External editing |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| *(none required)* | | |

### Which is better for us

**In-viewer + git** for script modules. No paid tool required.

### What learners must complete

- Track: **A05**  
- Experiment: **E05**  
- Produce: LSL modules + test harness in-world  

### Evidence folder

`scripts/`, `training/lsl/a05/`

### Slack channel

`#academy`, `#secondlife-inworld`

---

## Stage 12 — Genetics & data definitions

### What it is for (breedables)

Data-driven **traits, colors, rarity, mutations** separate from code — enables balance without rewriting engine.

### How we use it

- JSON/YAML or similar in `data/genes/`, `data/traits/`, etc.  
- Engine reads definitions; designers tune tables  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Git + text editor** | — | Schema and tables |
| **Python validation scripts** | `pipeline/validation/` | Schema checks |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **Spreadsheets** (Excel/Sheets) | — | Design-phase tuning — export to git |

### Which is better for us

**Git-tracked data files** as source of truth; spreadsheets for draft only.

### What learners must complete

- Read: `data/README.md`  
- Do: design fake-trait tables for E05 fixture  

### Evidence folder

`data/`

### Slack channel

`#production`, `#research-rnd`

---

## Stage 13 — HUD & player UI

### What it is for (breedables)

In-world menus, breeding UI, status displays, updater flows — packaged in `hud/`.

### How we use it

- LSL + SL UI conventions  
- Separate from creature body scripts where possible  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Blender** | — | HUD texture assets |
| **SL UI primitives** | wiki | Buttons, dialogs |

### Tools — paid

| Tool | Link | Best for |
|------|------|----------|
| **FUI designers** | various | Optional texture packs |

### Which is better for us

Build custom HUD art in Blender + our PBR pipeline for consistency.

### What learners must complete

- *(Track A-hud — to define after A05)*  

### Evidence folder

`hud/`

### Slack channel

`#production`

---

## Stage 14 — In-world testing & QA

### What it is for (breedables)

Prove breeding loop, persistence, animations, and updates work under real SL conditions (re-rez, reset, sim restart).

### How we use it

- Test scripts in `tests/`  
- Checklists per release  
- Log bugs back to `#production` with repro steps + screenshots  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Alt accounts** | SL | Multi-user breeding tests |
| **GitHub Issues** | github.com | Bug tracking |

### Which is better for us

Structured test checklist in wiki + GitHub issues for traceability.

### Evidence folder

`tests/`, `training/secondlife/qa/`

### Slack channel

`#secondlife-inworld`, `#production`

---

## Stage 15 — Release & maintenance

### What it is for (breedables)

Ship versioned packages to players; document changes; support updates via engine updater module.

### How we use it

- Release notes in `releases/`  
- Creature-specific packages in `creatures/<species>/`  
- Announce in `#releases` with links to evidence-tested builds  

### Tools — free

| Tool | Link | Best for |
|------|------|----------|
| **Git tags** | GitHub | Version markers |
| **MkDocs** | this wiki | Player-facing docs *(if public)* |

### Which is better for us

Git tags + markdown release notes tied to test evidence.

### Evidence folder

`releases/`, `creatures/`

### Slack channel

`#releases`

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

Every track page must follow [content requirements](../studio/channel-content-requirements.md): **Watch · Read · Explain · Do · Produce · Evidence**.

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

- [Channel map](../studio/channel-map.md)  
- [Content requirements](../studio/channel-content-requirements.md)  
- [Experiments](../production/experiments.md)  
- [Second Life baseline](../secondlife/platform-baseline.md)  
- [Phase 0 survey](../research/phase-0-survey.md)  
