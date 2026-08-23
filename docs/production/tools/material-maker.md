# Material Maker

!!! warning "Not a Blender tutorial"
    **Material Maker is a separate app** for procedural textures. It does not teach Blender, UVs, or shader nodes.

    Prerequisites: [Blender B07 PBR](../../academy/software/blender/b07-texture-painting-pbr.md) → [A01 lab](../../academy/tracks/a01-organic-pbr.md)

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_SOURCE |
| **License** | MIT |
| **Category** | Textures |
| **Repository** | [RodZill4/material-maker](https://github.com/RodZill4/material-maker) |

## Role

Procedural PBR texture authoring and 3D painting.

## Breedables use

Reusable organic material generators for skin, fur-like surfaces, scales, shell, horn, eye surrounds, pads, claws, accessories, and environment props.

## Decision

First-choice open-source procedural material authoring candidate. Promote after [E01 PBR pipeline shootout](../experiments.md) passes with committed evidence.

## Evidence

| Field | Link |
|-------|------|
| Primary video | [Material Maker intro](https://www.youtube.com/watch?v=8MMSS2F5vtc) |
| Wiki lesson | [A01 Organic PBR](../../academy/tracks/a01-organic-pbr.md) |
| Official docs | [Material Maker wiki](https://github.com/RodZill4/material-maker/wiki) |
| Academy track | A01 |
| Evidence folder | `training/texturing/a01/` |

Run E01 measurements and commit SL screenshots before production use.

## Librarian

```powershell
python -m librarian.cli show --query "material maker"
```
