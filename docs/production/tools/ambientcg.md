# ambientCG

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_CONTENT_CC0 |
| **Asset license** | CC0 |
| **Category** | Assets |
| **Site** | [ambientcg.com](https://ambientcg.com/) |

## Role

PBR materials and reference assets under CC0.

## Breedables use

PBR materials and reference assets for look development and benchmarks.

## Decision

Approved CC0 source — **record provenance per asset** used in shipping content.

## Evidence

| Field | Link |
|-------|------|
| Primary video | [PBR texture maps in Blender](https://www.youtube.com/watch?v=fUZHyoeuwVI) |
| Official docs | [ambientCG license](https://ambientcg.com/license) |
| Blender extension | [AmbientCG Material Importer](https://extensions.blender.org/add-ons/ambientcg-material-importer/) |
| Evidence folder | `training/texturing/assets/` |

Log asset IDs (e.g. `Rock035`) in lab notes when used.

## Librarian

```powershell
python -m librarian.cli show --query "ambientcg"
```
