---
title: "RetopoFlow"
section: tools
type: software
---
# RetopoFlow

!!! warning "Blender add-on — not Blender 101"
    **RetopoFlow is a retopology plugin.** You must already know high-poly/low-poly workflow and Edit Mode.

    Prerequisites: [Blender lessons 3–5](../blender/mesh-modeling.md) → [Retopology](../blender/retopology.md)

| Field | Value |
|-------|-------|
| **Commercial type** | UNKNOWN (audit required) |
| **Code license** | GPL-3.0 |
| **Category** | Retopology |
| **Repository** | [CGCookie/retopoflow](https://github.com/CGCookie/retopoflow) |

## Role

Manual, animation-friendly organic retopology workflow inside Blender.

## Breedables use

Retopology benchmark for messy organic meshes before rigging ([Experiment E03](../../research/experiments.md)).

## Risks

- Repository **code** is GPL; **non-code / bundled assets** may have separate restrictions
- Do not assume every bundled asset is freely redistributable

## Decision

Strong benchmark tool; complete commercial-type and asset audit before studio approval.

## Evidence

!!! tip "Play it in Tutorials"
    The player lives on [More tool tutorials — RetopoFlow](../../tutorials/more-tools.md#retopoflow).

| Field | Link |
|-------|------|
| Primary video | [RetopoFlow 4 setup](https://www.youtube.com/watch?v=Ds5Soybs610) |
| Wiki lesson | [Retopology project](../../projects/retopology-project.md) |
| Official docs | [docs.retopoflow.com](http://docs.retopoflow.com/) |
| License notes | This page + [Experiment E03](../../research/experiments.md) |
| Academy track | A03 |
| Evidence folder | `training/modeling/a03/` |

Fill E03 measurement table and license audit before production approval.

## Librarian

```powershell
python -m librarian.cli show --query "retopoflow"
```
