# RetopoFlow

!!! warning "Blender add-on — not Blender 101"
    **RetopoFlow is a retopology plugin.** You must already know high-poly/low-poly workflow and Edit Mode.

    Prerequisites: [B03–B05 Blender path](../../academy/software/blender/b03-mesh-modeling.md) → [B05 Retopology](../../academy/software/blender/b05-retopology.md)

| Field | Value |
|-------|-------|
| **Commercial type** | UNKNOWN (audit required) |
| **Code license** | GPL-3.0 |
| **Category** | Retopology |
| **Repository** | [CGCookie/retopoflow](https://github.com/CGCookie/retopoflow) |

## Role

Manual, animation-friendly organic retopology workflow inside Blender.

## Breedables use

Retopology benchmark for messy organic meshes before rigging ([E03](../experiments.md)).

## Risks

- Repository **code** is GPL; **non-code / bundled assets** may have separate restrictions
- Do not assume every bundled asset is freely redistributable

## Decision

Strong benchmark tool; complete commercial-type and asset audit before studio approval.

## Evidence

| Field | Link |
|-------|------|
| Primary video | [RetopoFlow 4 setup](https://www.youtube.com/watch?v=Ds5Soybs610) |
| Wiki lesson | [A03 Retopology](../../academy/tracks/a03-retopology.md) |
| Official docs | [docs.retopoflow.com](http://docs.retopoflow.com/) |
| License notes | This page + [E03](../experiments.md) |
| Academy track | A03 |
| Evidence folder | `training/modeling/a03/` |

Fill E03 measurement table and license audit before production approval.

## Librarian

```powershell
python -m librarian.cli show --query "retopoflow"
```
