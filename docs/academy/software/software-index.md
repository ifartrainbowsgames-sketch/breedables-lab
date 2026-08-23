# Wider software index

Blender is the hub, but a breedables studio touches other tools for texturing, retopology, AI blockouts, and CC0 assets. This page is the **map** of that wider stack, with learning pointers. Where the studio already maintains a [tools registry](../../production/tools/index.md) page, this links there instead of re-describing the tool.

**Legend:** Free / Paid / **CC0** (public-domain assets). ⭐ = studio-default for its job.

---

## Texturing & materials

| Tool | Cost | What it's for | Studio note |
|------|------|---------------|-------------|
| **Blender** (shader editor, texture paint, bake) ⭐ | Free | The default texturing environment | Core path — see [Lesson 7](blender/b07-texture-painting-pbr.md); [registry](../../production/tools/blender.md) |
| [Material Maker](https://www.materialmaker.org/) ⭐ | Free (open-source) | Node-based **procedural** PBR generator (standalone) | Procedural skin/scale/fur bases for phenotype variants; [registry](../../production/tools/material-maker.md) |
| [Ucupaint](https://github.com/ucupumar/ucupaint) ⭐ | Free (open-source) | Layer-based painting **inside Blender** | Variant layers & wear for [Layered textures](../tracks/a02-layered-textures.md); [registry](../../production/tools/ucupaint.md) |
| [Krita](https://krita.org/) | Free (open-source) | 2D painting; texture touch-ups, hand-painted maps, concept art | Great for hand-painted markings and HUD art |
| [GIMP](https://www.gimp.org/) | Free (open-source) | 2D image editing; map tweaks, channel packing | Utility editor when you don't need a full painter |
| **Substance 3D (Painter/Designer)** | Paid (subscription) | Industry-standard texturing/material authoring | Optional; overlaps Material Maker + Ucupaint. Only adopt with an [E01](../../production/experiments.md) comparison — the free stack covers breedables |

**Substance alternatives (free/open):** Material Maker (≈ Substance Designer) and Ucupaint + Blender texture paint (≈ Substance Painter for our needs) cover breedables. Other tools in this space (ArmorPaint/Armor Lab, Quixel Mixer, etc.) exist but are not studio-supported — evaluate as research before relying on them.

Learn: [Texturing/PBR](../resources/tutorials.md#texturing-pbr) and [Shader nodes](../resources/tutorials.md#shader-nodes) in the arsenal.

---

## Retopology tools

| Tool | Cost | What it's for | Studio note |
|------|------|---------------|-------------|
| **Blender manual retopo** ⭐ | Free | Full-control retopology for deforming meshes | Primary path for creatures; [Lesson 5](blender/b05-retopology.md) |
| **QuadriFlow** (built into Blender) | Free | Automatic quad remesh for a fast base | Clean-up still required; good starting cage |
| [RetopoFlow](https://github.com/CGCookie/retopoflow) | Free (GPL) | Guided retopology toolset | Speed benchmark; [registry](../../production/tools/retopoflow.md) / [catalog](addon-catalog.md#free-community) |

SL context you must know for retopo decisions: [Mesh & LOD](https://wiki.secondlife.com/wiki/Mesh_and_LOD), [land impact / download weight](https://wiki.secondlife.com/wiki/Mesh/Download_Weight).

---

## AI & 3D scanning (concept/blockout only)

Use these for **concept geometry**, never as ship-ready meshes — always retopologise and audit licenses. See the [production line stage 6](../production-line.md#stage-6-image-to-3d-research-blockout).

| Tool | Cost | What it's for | Studio note |
|------|------|---------------|-------------|
| [TripoSR](https://github.com/VAST-AI-Research/TripoSR) | Free (open, local) | Single-image → 3D blockout mesh | First baseline; [registry](../../production/tools/triposr.md) / experiment [E02](../../production/experiments.md) |
| Hosted image-to-3D (Tripo3D, Meshy, etc.) | Paid (SaaS) | Faster hosted generation | **Audit commercial ToS** before any production use |

Rule: AI output is a **concept blockout**. It enters the pipeline at modeling/sculpt ([Lesson 4](blender/b04-sculpting.md)), then goes through retopo/UV/texture/rig like any other mesh.

---

## Asset libraries (CC0)

Public-domain (CC0) assets you can use commercially — **record provenance per file** in `assets/cc0/provenance.md`.

| Library | Cost | What it's for | Studio note |
|---------|------|---------------|-------------|
| [Poly Haven](https://polyhaven.com/) ⭐ | **CC0** | HDRIs (studio lighting), textures, models | Use the [Blender add-on](addon-catalog.md#free-community); [registry](../../production/tools/poly-haven.md) |
| [ambientCG](https://ambientcg.com/) ⭐ | **CC0** | PBR material scans, textures, HDRIs | Reference/base materials; [registry](../../production/tools/ambientcg.md) |

Licenses: [Poly Haven license](https://polyhaven.com/license) · [ambientCG license](https://ambientcg.com/license). CC0 = no attribution required, but we still log provenance for auditability.

---

## Second Life-side tools (not Blender)

| Tool | Cost | What it's for | Studio note |
|------|------|---------------|-------------|
| Second Life viewer (official or Firestorm) | Free | Upload mesh/materials, in-world testing | Required for the in-world proofs in [Lesson 7](blender/b07-texture-painting-pbr.md)/[Lesson 10](blender/b10-export-to-sl.md) |
| [lsl-definitions](https://github.com/secondlife/lsl-definitions) | Free (open) | Canonical LSL/SLua definitions | Scripting accuracy for [In-world fixture](../tracks/a05-sl-fixture.md); [platform baseline](../../secondlife/platform-baseline.md) |
| [create.secondlife.com](https://create.secondlife.com/) | Free (docs) | Official creator documentation | LSL reference, upload guidance |

---

## The fully-free breedables stack (recommended)

You can build and sell breedables end-to-end without paid software:

**Blender** (model/sculpt/retopo/UV/rig/animate/export) + **Material Maker** & **Ucupaint** (texturing) + **Krita/GIMP** (2D) + **Poly Haven / ambientCG** (CC0 inputs) + **RetopoFlow** (retopo speed) + **Second Life viewer** (upload/test).

The one paid tool most breedables studios eventually add is **[Avastar](addon-catalog.md#paid-but-worth-it)** for SL-native rigging/Animesh export.

---

## Related

- [Blender Foundations path](blender/index.md) · [Add-on catalog](addon-catalog.md) · [Tutorial arsenal](../resources/tutorials.md)
- [Production line](../production-line.md) · [Tools registry](../../production/tools/index.md)
- [Second Life platform baseline](../../secondlife/platform-baseline.md)
