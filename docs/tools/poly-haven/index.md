---
title: "Poly Haven"
section: tools
type: software
---

# Poly Haven

!!! info "About this page"
    **Evidence folder** — `training/texturing/assets/`

Poly Haven is a public library of CC0 HDRIs, PBR textures, and 3D models maintained by a community of artists. This page records how the lab uses it as an approved source for lighting environments, material baselines, props, and benchmark assets, and it defines the provenance workflow required before any asset ships in a breedable or lab deliverable.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Poly Haven | [Poly Haven](https://polyhaven.com/) | CC0 HDRIs, PBR texture sets, and 3D models for look-dev and scene building |
    | Poly Haven Blender Add-on | [Poly Haven Blender Add-on](https://docs.polyhaven.com/en/guides/blender-addon) | Importing HDRIs and PBR materials directly inside Blender without manual download |

## Watch

| Topic | Video | Why this one |
|---|---|---|
| Blender add-on | [Poly Haven Blender add-on](https://www.youtube.com/watch?v=ku_xv6WV6UE) | Demonstrates the one-click HDRI and material import workflow that matches the lab's Blender pipeline. |

## Read

| Source | Covers |
|---|---|
| [Poly Haven license](https://polyhaven.com/license) | CC0 terms, public-domain dedication, and what commercial use is allowed |
| [Blender add-on guide](https://docs.polyhaven.com/en/guides/blender-addon) | Installation, asset resolution choices, and import settings for Blender projects |

## Role

Poly Haven hosts high-quality, CC0-licensed HDRIs, PBR textures, and 3D models. Because the license is CC0, every asset can be used commercially, modified, and redistributed without attribution. The lab still records provenance so any asset that ships with a creature, prop, or scene can be audited later.

## Metadata

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_CONTENT_CC0 |
| **Asset license** | CC0 |
| **Category** | Assets |
| **Site** | [polyhaven.com](https://polyhaven.com/) |

## Breedables use

- **Lighting environments** — HDRIs for accurate reflections and soft, natural lighting in Blender look-dev.
- **Material references** — PBR texture sets to sanity-check fur, skin, scale, or fabric materials before Second Life export.
- **Props and set dressing** — CC0 models for benchmark scenes, scale references, and marketing renders.
- **Benchmark assets** — standard geometry and materials used to compare topology, UV, and bake pipelines across lab tools.

## Download and inspect workflow

Browse by asset type — HDRIs, Textures, or Models — then inspect the individual asset page. Confirm the CC0 badge is present and note the asset slug or exact name. Download only the resolution you need; 1K–2K texture sets are usually enough for Second Life preview work, while 4K–8K may be used for offline renders or detail studies. Keep the original archive untouched in the evidence folder so the source can be reconstructed.

## Blender add-on workflow

Install the add-on from the [official guide](https://docs.polyhaven.com/en/guides/blender-addon). In Blender, open the Poly Haven side panel to browse and import HDRIs and materials directly. Choose the smallest resolution that still looks correct to keep file sizes manageable. For Second Life prep, bake or export textures at the target size after import; do not upload raw 8K maps to the viewer.

## Provenance and lab compliance

Poly Haven is an approved CC0 source, but **record provenance per asset** used in shipping content. The provenance entry must include the asset ID, exact title, source URL, license, and download date in `training/texturing/assets/provenance.md`. Before committing an asset to a project, verify the license page has not changed and that the asset is still marked CC0. Store the original resolution and file names in the evidence folder so any later dispute can be traced.

## Decision

Approved CC0 source — provenance is required for every asset used in lab or shipping content.

## Evidence and references

| Field | Link |
|-------|------|
| Primary video | [Poly Haven Blender add-on](https://www.youtube.com/watch?v=ku_xv6WV6UE) |
| Official docs | [Poly Haven license](https://polyhaven.com/license) · [Blender add-on guide](https://docs.polyhaven.com/en/guides/blender-addon) |
| Evidence folder | `training/texturing/assets/` |

## Librarian

Query the lab librarian for the current Poly Haven record and any project references:

```powershell
python -m librarian.cli show --query "poly haven"
```

Log each downloaded asset in `training/texturing/assets/provenance.md` before using it in lab work.

## Do

1. Open https://polyhaven.com/ and locate the asset type: HDRIs, Textures, or Models.
2. Read the asset page to confirm CC0 license and note the asset slug or name.
3. Download the resolution you need; keep the original archive in `training/texturing/assets/`.
4. If using Blender, install the Poly Haven add-on and import the asset via the 3D viewport side panel.
5. Record the asset ID, title, URL, license, and download date in `training/texturing/assets/provenance.md`.
6. Use the asset as a lighting environment, material reference, prop, or benchmark model; reduce resolution before Second Life export.

## Produce

| Artifact | Path |
|----------|------|
| download archive | `training/texturing/assets/` |
| provenance log | `training/texturing/assets/provenance.md` |

## Done when

- [ ] Asset license is confirmed as CC0 on the Poly Haven asset page.
- [ ] Provenance entry includes asset ID, title, URL, license, and download date.
- [ ] Downloaded archive is stored in `training/texturing/assets/` before being used in a project.
- [ ] Texture resolution is reduced to Second Life-appropriate sizes before export.
- [ ] Librarian query `python -m librarian.cli show --query "poly haven"` returns the expected record.

## Related

- [Tools](../index.md)
- [Lesson 7 — Texture painting & PBR materials](../blender/pbr-materials.md)
- [Blender add-on catalog](../blender/addon-catalog.md)
- [Software database](../../research/software-database.md)
- [ambientCG](../ambientcg/index.md)
