# Ucupaint

!!! warning "Blender add-on — not Blender 101"
    **Ucupaint is a plugin** for layer painting. You must already know Blender UVs, materials, and Edit Mode.

    Prerequisites: [B06–B07 Blender path](../../academy/software/blender/b06-uv-unwrapping.md) → complete [Organic PBR material](../../academy/tracks/a01-organic-pbr.md)

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_SOURCE |
| **License** | GPL-3.0 |
| **Category** | Textures |
| **Repository** | [ucupumar/ucupaint](https://github.com/ucupumar/ucupaint) |

## Role

Blender texture-layer management and hand painting inside Blender.

## Breedables use

Hand-painted refinement, masks, detail layers, phenotype variations, cleanup after procedural generation.

## Decision

Test **alongside** Material Maker — not a replacement. Compare in [E01](../experiments.md).

## Evidence

| Field | Link |
|-------|------|
| Primary video | [Ucupaint — Substance-like workflow](https://www.youtube.com/watch?v=d3KrMwAWJI0) |
| Wiki lesson | [A02 Layered Textures](../../academy/tracks/a02-layered-textures.md) |
| Official docs | [Ucupaint wiki](https://ucupumar.github.io/ucupaint-wiki/) |
| Academy track | A02 |
| Evidence folder | `training/texturing/a02/` |

GPL output considerations — document in E01 license row.

## Librarian

```powershell
python -m librarian.cli show --query "ucupaint"
```
