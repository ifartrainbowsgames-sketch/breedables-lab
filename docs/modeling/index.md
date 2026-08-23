---
title: "3D Modeling"
section: modeling
type: index
question: "What tools and workflows do I use to create the model?"
---
# 3D Modeling

!!! abstract "This section answers one question"
    *What tools and workflows do I use to create the model?*

Everything about building creature geometry — reference, blockout, mesh
modelling, sculpting, retopology, UVs and level-of-detail. This is the canonical
home for modelling software and workflows; other sections link here rather than
repeat them.

## Topics

| Page | What it covers |
|------|----------------|
| [Blender](blender/index.md) | The studio's default 3D application |
| [Install & setup](blender/install-and-setup.md) | Right LTS build, units and viewport for SL scale |
| [Interface & navigation](blender/interface-and-navigation.md) | Moving around before you model |
| [Mesh modeling](mesh-modeling.md) | Box-model a clean organic creature base |
| [Sculpting](sculpting.md) | Organic form with dynamic topology and multires |
| [Retopology](retopology.md) | Animation-ready topology and land impact |
| [UV mapping](uv-mapping.md) | Seams, texel density and packing |
| [Blender add-on catalog](blender/addon-catalog.md) | Which add-ons to install, and when |

## Software

| Tool | Licence & role |
|------|----------------|
| [Blender](blender/index.md) | Free · GPL — studio default |
| [Autodesk Maya](software/maya.md) | Paid — industry modelling standard |
| [ZBrush](software/zbrush.md) | Paid — industry sculpting standard |
| [TopoGun](software/topogun.md) | Paid — dedicated retopology |
| [RetopoFlow](software/retopoflow.md) | Free · GPL — Blender retopology add-on |
| [PureRef](software/pureref.md) | Reference boards |

## Hands-on projects

Each project ends in committed evidence, not a watched video.

| Project | Outcome |
|---------|---------|
| [Retopology project](projects/retopology-project.md) | Retopologise a sculpt to a documented poly budget |

## Pipeline stages owned by this section

These are the production-line stages this section is responsible for.

### Stage 1 — Concept & art direction

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

- Watch: [Blender Guru — Donut modeling](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) · [Lesson 3 — lesson](../modeling/mesh-modeling.md)  
- Read: [PureRef package](../modeling/software/pureref.md) · `assets/references/` when created  
- Produce: reference board + simple blockout `.blend`

**Evidence folder** — `assets/references/`, `training/modeling/concept/`  
**Related pages** — [Lesson 3 — Mesh modeling](../modeling/mesh-modeling.md) · [Lesson 4 — Sculpting](../modeling/sculpting.md)

### Stage 2 — Modeling (organic mesh)

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

- Watch: [Grant Abbitt — modeling](https://www.youtube.com/@grabbitt) · [Video library — Blender](../research/software-database.md)  
- Read: [Blender tool page](../modeling/blender/index.md)  
- Do: neutral quadruped blockout mesh  
- Produce: `.blend` in `training/modeling/`

**Evidence folder** — `training/modeling/`  
**Related pages** — [Lesson 3 — Mesh modeling](../modeling/mesh-modeling.md) · [Lesson 4 — Sculpting](../modeling/sculpting.md)

### Stage 3 — Retopology & LOD

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

- Studio labs: [Retopology](../modeling/projects/retopology-project.md)  
- Experiments:   
- Watch: [Royal Skies — retopology](https://www.youtube.com/watch?v=h6E9N10rN5s) · [Lesson 5 — lesson](../modeling/retopology.md) · [Video library — retopo](../research/software-database.md)  
- Produce: retopo mesh + timing log

**Evidence folder** — `training/modeling/a03/`, `research/experiments/e03/`  
**Related pages** — [Lesson 5 — Retopology](../modeling/retopology.md) · [Retopology](../modeling/projects/retopology-project.md)

### Stage 4 — UV mapping

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
**Related pages** — [Lesson 6 — UV unwrapping](../modeling/uv-mapping.md)
