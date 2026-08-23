---
title: "ambientCG"
section: tools
type: software
---

# ambientCG

!!! info "About this page"
    **Evidence folder** — `training/texturing/assets/`

ambientCG is a public-domain (CC0) library of PBR materials and reference assets. This page documents how the studio sources, validates and imports those assets into Blender for breedables look development while recording provenance.

!!! tip "Studio pick"
    Approved CC0 source for PBR materials and reference assets. CC0 waives attribution, but we still record provenance per asset used in shipping content so we can defend originality and rebuild materials later.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | ambientCG | [ambientCG](https://ambientcg.com/) | CC0 PBR materials and reference assets for look development, benchmarks and temporary placeholders. |

## Watch

!!! tip "Play it in Tutorials"
    The player lives on [Tutorials](../../tutorials/more-tools.md#ambientcg). Titles below stay so you can see what we picked.


| Topic | Video | Why this one |
|---|---|---|
| PBR texture maps in Blender | [PBR texture maps in Blender](https://www.youtube.com/watch?v=fUZHyoeuwVI) | Demonstrates how to wire color, roughness, metallic, normal and displacement maps in Blender, matching the map sets ambientCG distributes. |

## Read

| Source | Covers |
|---|---|
| [ambientCG license](https://ambientcg.com/license) | CC0 public-domain dedication and the legal terms that apply to every asset on the site. |
| [AmbientCG Material Importer](https://extensions.blender.org/add-ons/ambientcg-material-importer/) | Official Blender extension that downloads and configures ambientCG materials with the correct node graph. |

## Tool facts

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_CONTENT_CC0 |
| **Asset license** | CC0 |
| **Category** | Assets |
| **Site** | [ambientcg.com](https://ambientcg.com/) |

## What ambientCG provides

ambientCG hosts a curated library of PBR material sets and reference assets released under CC0. Each material usually ships as a ZIP archive containing the maps needed for a metal/roughness workflow: color (albedo), roughness, metallic, normal, ambient occlusion, displacement and opacity where relevant. Many entries offer multiple resolutions and map variants. Because the license is public domain, you may remix, redistribute and use the assets in commercial content without attribution, although the studio still records provenance for every asset that ships.

## License and provenance

All assets on ambientCG are released under CC0 1.0 Universal, meaning the creator has waived copyright and related rights to the extent allowed by law. See [ambientCG license](https://ambientcg.com/license) for the full legal text. For the lab, CC0 does not remove the engineering need to trace sources. Record the asset ID, download date, resolution and map names for any texture used in a shipping breedable or promotional render. This defends against accidental duplicate licensing and lets us rebuild the material later.

## Breedables use

ambientCG supplies base PBR materials and reference assets during look development. We use it for quick material tests on new sculpts, benchmarking fur, feather or scale looks against high-quality CC0 scans, placeholder meshes when designing body proportions, and background or environment assets for promotional screenshots. It is not a substitute for original hand-painted textures or species-specific surface design, but it accelerates early iterations before proprietary art takes over.

## Blender import workflow

The fastest path is the [AmbientCG Material Importer](https://extensions.blender.org/add-ons/ambientcg-material-importer/) extension, which fetches and configures materials automatically. To set up manually, download the ZIP, extract the maps into the project asset folder, create a new material on your mesh, then add an Image Texture node for each map. Connect color to Base Color, roughness to Roughness, metallic to Metallic, normal through a Normal Map node to Normal, displacement through a Displacement node, and ambient occlusion to a multiply or dedicated mix as desired. Set color maps to sRGB and data maps (roughness, metallic, normal, displacement, AO) to Non-Color. Use the [PBR texture maps in Blender](https://www.youtube.com/watch?v=fUZHyoeuwVI) video as a visual reference.

## Second Life considerations

Second Life's PBR render pipeline uses a metal/roughness material model. Import the texture maps and assign them to the appropriate Second Life material channels: base color, roughness, metallic, normal and emissive. Prefer 1K or 2K resolutions for in-world body parts unless the detail justifies 4K, because texture memory and upload costs affect performance. Keep opacity maps only where transparency is required, since alpha blending increases draw calls and can cause sorting issues in crowded breedable scenes.

## Provenance log

Every ambientCG asset used in shipping content must be tracked. Create a row per asset with: asset ID (for example `Rock035`), category, downloaded resolution, license URL or timestamp, local path under `training/texturing/assets/`, and the project or model that consumes it. Store the actual ZIPs and extracted maps in the same evidence folder so the material can be rebuilt months later.

## Librarian lookup

The lab's librarian can query the ambientCG entry and related notes from the command line:

```powershell
python -m librarian.cli show --query "ambientcg"
```

## Do

1. Search ambientCG for a material or reference asset that matches the current concept.
2. Download the ZIP and copy the asset ID and license URL into the provenance log.
3. Extract the maps into `training/texturing/assets/<assetID>/`.
4. Import the material into Blender using the AmbientCG Material Importer or a manual node setup.
5. Test under studio lighting; adjust scale, tiling and values for the breedable.
6. Mark the asset as consumed in the provenance log when it enters shipping content.

## Produce

| Artifact | Path |
|----------|------|
| PBR material zip | `training/texturing/assets/` |
| Provenance log | `training/texturing/assets/provenance.csv` |
| Material preview render | `training/texturing/assets/previews/` |

## Done when

- [ ] Asset ID, category and resolution recorded.
- [ ] CC0 license confirmed from the asset page or license page.
- [ ] Maps connected with correct color spaces: sRGB for color, Non-Color for data.
- [ ] Material previewed under the same lighting as final screenshots.
- [ ] Usage noted in the shipping content's provenance row.

## Related

- [Lesson 7 — Texture painting & PBR materials](../blender/pbr-materials.md)
- [Poly Haven](../poly-haven/index.md)
- [Material Maker](../material-maker/index.md)
- [Krita](../krita/index.md)
