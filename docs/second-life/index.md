---
title: "Second Life Production"
section: second-life
type: index
question: "How do I get the finished asset into Second Life correctly?"
---
# Second Life Production

!!! abstract "This section answers one question"
    *How do I get the finished asset into Second Life correctly?*

Second Life is a delivery target with hard constraints — land impact,
LOD, physics shapes, texture cost, permissions and Animesh limits. Learn the
general professional workflow first in the subject sections; this section covers
only what must change to ship in-world.

## Topics

| Page | What it covers |
|------|----------------|
| [Platform baseline](platform-baseline.md) | Animesh, PBR, land impact, Linkset Data |
| [Export & upload](export-and-upload.md) | Mesh, LODs, physics and material upload |
| [Adapting professional work](adapting-professional-work.md) | What changes once the general 3D is good |
| [Viewer & creator tools](viewer-and-tools.md) | The viewer as a production tool |

## Software

| Tool | Licence & role |
|------|----------------|
| [Second Life viewer](viewer-and-tools.md) | Free — upload and in-world QA |

## Pipeline stages owned by this section

These are the production-line stages this section is responsible for.

### Stage 9 — Export & optimization

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
**Related pages** — [Lesson 10 — Export to SL](../second-life/export-and-upload.md)

### Stage 10 — Second Life upload & PBR verification

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
**Related pages** — [Lesson 10 — Export to SL](../second-life/export-and-upload.md) · [In-world fixture](../engineering/projects/in-world-fixture.md) · [Platform baseline](../second-life/platform-baseline.md)

### Stage 14 — In-world testing & QA

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
**Related pages** — [In-world fixture](../engineering/projects/in-world-fixture.md) · [Experiments](../research/experiments.md)
