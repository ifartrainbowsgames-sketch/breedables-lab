---
title: "Blender"
section: modeling
type: index
question: "What tools and workflows do I use to create the model?"
---
# Blender

![Blender](../../assets/inline/blender.png){ width="120" }

!!! info "About this page"
    **Canonical home** — everything about Blender as a tool lives here  
    **Studio status** — **USE NOW**, the primary free path for almost every stage  
    **Learning path** — [Blender foundations](../../academy/paths/blender-foundations.md) walks the ten lessons in order

Blender is the studio's default 3D application. It covers modelling, sculpting,
retopology, UV, baking, texturing, rigging, animation and Second Life export in
one free, open-source package — which is why the Academy teaches it as the
backbone instead of a paid multi-tool pipeline.

## At a glance

| | |
|---|---|
| **Licence** | Open source — [GNU GPL v3](https://www.blender.org/about/license/) |
| **Cost** | Free, including commercial use |
| **Official site** | [blender.org](https://www.blender.org/) |
| **Download** | [blender.org/download](https://www.blender.org/download/) — use the **LTS** release |
| **Manual** | [docs.blender.org/manual](https://docs.blender.org/manual/en/latest/) |
| **Python API** | [docs.blender.org/api](https://docs.blender.org/api/current/) |
| **Requirements** | [Minimum hardware](https://www.blender.org/download/requirements/) |

## Where Blender is used in this studio

| Stage | Canonical page |
|-------|----------------|
| Modelling | [Mesh modeling](../mesh-modeling.md) · [Sculpting](../sculpting.md) |
| Retopology & UV | [Retopology](../retopology.md) · [UV mapping](../uv-mapping.md) |
| Texturing | [PBR materials](../../texturing/pbr-materials.md) |
| Rigging & animation | [Rigging & skinning](../../rigging-animation/rigging-and-skinning.md) · [Animation](../../rigging-animation/animation.md) |
| Second Life delivery | [Export & upload](../../second-life/export-and-upload.md) |

Bundled add-ons such as Rigify are part of the baseline — see the
[add-on catalog](addon-catalog.md).

## Getting set up

1. [Install & setup](install-and-setup.md) — the right LTS build, units and viewport for Second Life scale.
2. [Interface & navigation](interface-and-navigation.md) — moving around before you model anything.

## Official learning

| Type | Resource |
|------|----------|
| Fundamentals course | [Blender Fundamentals](https://www.blender.org/support/tutorials/) |
| Full reference | [Blender Manual](https://docs.blender.org/manual/en/latest/) |
| Official channel | [@BlenderOfficial](https://www.youtube.com/@BlenderOfficial) |

## Community channels used across the wiki

| Channel | Why |
|---------|-----|
| [Blender Guru](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | The "Donut" series — the standard zero-to-competent intro |
| [Grant Abbitt](https://www.youtube.com/@grabbitt) | Game-asset, low-poly and creature work for beginners |
| [Ryan King Art](https://www.youtube.com/@RyanKingArt) | Shader and PBR material walkthroughs |

## Studio notes

- Rigify's Basic Quadruped is the rigging baseline — see [experiment E04](../../research/experiments.md#e04-rig-and-retarget-baseline).
- Blender's glTF and Collada exporters are the Second Life upload path.
- Registry lookup: `python -m librarian.cli show --query "blender"`

## Videos

**Beginner**

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/B0J27sf02NU" title="Blender 4.0 Beginner Tutorial — Part 1" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Blender 4.0 Beginner Tutorial — Part 1](https://www.youtube.com/watch?v=B0J27sf02NU)** — Official Blender Foundation intro to interface and basics

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/nIoXOplUvAw" title="Blender Guru — Donut (modeling)" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Blender Guru — Donut (modeling)](https://www.youtube.com/watch?v=nIoXOplUvAw)** — Canonical beginner modeling series

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/lP3G5jADgYo" title="Grant Abbitt — low-poly character" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Grant Abbitt — low-poly character](https://www.youtube.com/watch?v=lP3G5jADgYo)** — Game-ready creature/character base mesh

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/KeL21Eap1hE" title="Grant Abbitt — sculpting for beginners" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Grant Abbitt — sculpting for beginners](https://www.youtube.com/watch?v=KeL21Eap1hE)** — Organic sculpt fundamentals before retopo

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/h6E9N10rN5s" title="Royal Skies — retopology beginner" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Royal Skies — retopology beginner](https://www.youtube.com/watch?v=h6E9N10rN5s)** — Manual retopo over high-poly sculpt

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/mLuhL_vgGUE" title="Blender Official — UV basics" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Blender Official — UV basics](https://www.youtube.com/watch?v=mLuhL_vgGUE)** — UV unwrapping fundamentals

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/2XXH8M25sNM" title="Blender — weight painting basics" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Blender — weight painting basics](https://www.youtube.com/watch?v=2XXH8M25sNM)** — Deformation cleanup after auto weights

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/u6Q6LNDLJNQ" title="Blender — animation fundamentals" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Blender — animation fundamentals](https://www.youtube.com/watch?v=u6Q6LNDLJNQ)** — Keyframe loops for idle/walk cycles

**[Blender Official YouTube](https://www.youtube.com/@BlenderOfficial)** — Official feature overviews and release highlights

**[Grant Abbitt channel](https://www.youtube.com/@GrantAbbitt)** — Low-poly and game asset tutorials

**[Grant Abbitt — low-poly creatures](https://www.youtube.com/@grabbitt)** — Creature base meshes

**Intermediate**

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/4_xYiw1nL5M" title="Ryan King Art — PBR texturing" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Ryan King Art — PBR texturing](https://www.youtube.com/watch?v=4_xYiw1nL5M)** — Metallic/roughness workflow for game/SL assets

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/6Km2tRFTxvs" title="Darkfall — quadruped rigging intro" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

**[Darkfall — quadruped rigging intro](https://www.youtube.com/watch?v=6Km2tRFTxvs)** — Creature rig for breedables

**[FlippedNormals — Blender creature workflow](https://www.youtube.com/@FlippedNormals)** — Industry creature modeling content

---
