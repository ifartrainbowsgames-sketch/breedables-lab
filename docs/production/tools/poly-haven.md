# Poly Haven

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_CONTENT_CC0 |
| **Asset license** | CC0 |
| **Category** | Assets |
| **Site** | [polyhaven.com](https://polyhaven.com/) |

## Role

HDRIs, textures, and 3D models under CC0.

## Breedables use

Lighting environments, material references, props, benchmark assets.

## Decision

Approved CC0 source — **record provenance per asset** used in shipping content (asset ID + URL in lab notes).

## Evidence

| Field | Link |
|-------|------|
| Primary video | [Poly Haven Blender add-on](https://www.youtube.com/watch?v=ku_xv6WV6UE) |
| Official docs | [Poly Haven license](https://polyhaven.com/license) · [Blender add-on guide](https://docs.polyhaven.com/en/guides/blender-addon) |
| Evidence folder | `training/texturing/assets/` |

Log each downloaded asset in `training/texturing/assets/provenance.md` when used in A01+ labs.

## Librarian

```powershell
python -m librarian.cli show --query "poly haven"
```
