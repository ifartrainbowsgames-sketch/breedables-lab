---
title: "Blender add-on catalog"
section: modeling
type: topic
---
# Blender add-on catalog

A curated list of Blender add-ons that genuinely help the **Second Life breedables pipeline**, grouped by cost. For each: what it does, its relevance to breedables, and whether it is **Essential** or **Nice-to-have** for our workflow.

**Legend:** ⭐ Essential for the SL breedables pipeline · ◻ Nice-to-have.

Install built-ins via **Preferences → Add-ons** (search the name). Free/community add-ons install from a downloaded `.zip` (or, in Blender 4.2+, via the **Extensions** platform). Paid add-ons come from the developer or a marketplace (Superhive/Blender Market, Gumroad).

For learning *how* to use these in context, see the [Blender Foundations path](index.md) and the [tutorial arsenal](../../academy/index.md).

---

## Built-in (ships with Blender — just enable)

These are free, bundled, and stable across LTS releases. Enable them in [Lesson 1](install-and-setup.md).

| Add-on | Cost | What it does | Relevance to breedables | Priority |
|--------|------|--------------|--------------------------|----------|
| [Node Wrangler](https://docs.blender.org/manual/en/latest/addons/node_wrangler.html) | Free (built-in) | Keyboard-driven shader/geo node editing (Ctrl+T, Ctrl+Shift+click preview) | Massive speedup for the PBR node work in [Lesson 7](../../texturing/pbr-materials.md) and phenotype shader groups | ⭐ |
| [LoopTools](https://docs.blender.org/manual/en/latest/addons/mesh/looptools.html) | Free (built-in) | Extra mesh ops: Relax, Space, Circle, Bridge, Flatten | Cleans edge loops on organic bases ([Lesson 3](../mesh-modeling.md)) and retopo ([Lesson 5](../retopology.md)) | ⭐ |
| [Rigify](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) | Free (built-in) | Meta-rig → full rig generator, incl. Basic Quadruped | Studio rigging baseline for [Lesson 8](../../rigging-animation/rigging-and-skinning.md) / [Rig + animation](../../rigging-animation/projects/rig-and-animation.md) | ⭐ |
| glTF 2.0 importer/exporter | Free (built-in) | Import/export glTF/GLB with PBR materials | SL PBR material upload path ([Lesson 10](../../second-life/export-and-upload.md)) | ⭐ |
| Collada (.dae) exporter | Free (built-in) | Export COLLADA meshes, LODs, rigs | SL's mesh upload format ([Lesson 10](../../second-life/export-and-upload.md)) | ⭐ |
| [Bool Tool](https://docs.blender.org/manual/en/latest/addons/mesh/bool_tool.html) | Free (built-in) | Fast boolean union/difference shortcuts | Hard-surface accessories, tack, HUD props | ◻ |
| [Extra Objects (Add Mesh)](https://docs.blender.org/manual/en/latest/addons/add_mesh/mesh_extra_objects.html) | Free (built-in) | More primitive shapes to start from | Faster blockouts and prop bases | ◻ |
| [Extra Curve Objects](https://docs.blender.org/manual/en/latest/addons/add_curve/index.html) | Free (built-in) | Extra curve primitives | Leashes, vines, tails-as-curves, HUD elements | ◻ |
| [Copy Attributes Menu](https://docs.blender.org/manual/en/latest/addons/object/copy_attributes.html) | Free (built-in) | Ctrl+C to copy transforms/data between objects | Speeds repetitive setup across phenotype variants | ◻ |
| [Auto Mirror](https://docs.blender.org/manual/en/latest/addons/mesh/auto_mirror.html) | Free (built-in) | One-click cut-in-half + Mirror modifier | Symmetric creature modeling ([Lesson 3](../mesh-modeling.md)) | ◻ |
| [3D-Print Toolbox](https://docs.blender.org/manual/en/latest/addons/mesh/3d_print_toolbox.html) | Free (built-in) | Mesh checks: non-manifold, degenerate, intersecting | Pre-export sanity checks before SL upload | ◻ |

---

## Free / community

Free (some open-source, some free-tier). Verify license before shipping anything bundled — see the [tools registry](../../research/tool-registry.md).

| Add-on | Cost | What it does | Relevance to breedables | Priority |
|--------|------|--------------|--------------------------|----------|
| [RetopoFlow](https://github.com/CGCookie/retopoflow) | Free (GPL; also sold to support CG Cookie) | Dedicated retopology toolset (guided quad drawing) | Faster clean retopo for [Lesson 5](../retopology.md)/[Retopology](../projects/retopology-project.md); [registry](../software/retopoflow.md) | ⭐ |
| [Ucupaint](https://github.com/ucupumar/ucupaint) | Free (open-source) | Layer-based texture painting inside Blender | Phenotype variant layers in [Layered textures](../../texturing/projects/layered-textures.md); [registry](../../texturing/software/ucupaint.md) | ⭐ |
| [TexTools](https://github.com/franMarz/TexTools-Blender) | Free (open-source) | UV + texture utilities: align/rectify UVs, texel density, baking helpers | Even texel density and quick bakes for [Lesson 6](../uv-mapping.md)/[Lesson 7](../../texturing/pbr-materials.md) | ⭐ |
| [Poly Haven Assets](https://polyhaven.com/plugins/blender) ([GitHub](https://github.com/Poly-Haven/polyhavenassets)) | Free (assets are CC0) | Browse/download CC0 HDRIs, textures, models in the Asset Browser | CC0 reference materials + studio lighting; [registry](../../texturing/software/poly-haven.md) | ⭐ |
| [MACHIN3tools](https://machin3.io/MACHIN3tools/) | Free | Modeling QoL pie menus & smart tools | General modeling speed for [Lesson 3](../mesh-modeling.md) and hard-surface props | ◻ |

> Blender **4.2+ Extensions**: many of these are installable directly from the in-app Extensions browser or [extensions.blender.org](https://extensions.blender.org/). Prefer that channel where available for auto-updates.

---

## Paid — but worth it

Only adopt a paid add-on when it wins on measured evidence (see the [tool comparison rules](../../research/decision-model.md#writing-a-tool-comparison)). These are the ones that repeatedly justify their cost for SL work.

| Add-on | Cost | What it does | Relevance to breedables | Priority |
|--------|------|--------------|--------------------------|----------|
| [Avastar](https://www.avalab.org/avastar/) ([docs](https://blog.machinimatrix.org/avastar/)) | Paid | Blender add-on with the **exact Second Life avatar skeleton**, weighting, fitted-mesh and SL-native animation/mesh export | **The** SL rigging/Animesh bridge — provides SL bones and `.anim`/mesh export that hand-rigging struggles to match. Central to [Lesson 8](../../rigging-animation/rigging-and-skinning.md)/[Lesson 10](../../second-life/export-and-upload.md) for animated creatures | ⭐ |
| [Auto-Rig Pro](https://www.lucky3d.fr/auto-rig-pro/doc/) ([Superhive](https://superhivemarket.com/products/auto-rig-pro)) | Paid ($25 Lite / $50 Full) | Fast character rigging, retargeting, skinning helpers, FBX export | Speeds quadruped rigging & animation retarget for [Rig + animation](../../rigging-animation/projects/rig-and-animation.md); pair with SL-skeleton export | ◻ |
| [UVPackmaster](https://uvpackmaster.com/) | Paid (from ~$39) | GPU/CPU high-efficiency UV packing | Squeezes more texture resolution from one SL texture set ([Lesson 6](../uv-mapping.md)) — only after packing is a measured bottleneck | ◻ |
| [Zen UV](https://zenmastersteam.github.io/Zen-UV/latest/) | Paid | Full UV toolkit (marking, unwrap, stacking, texel density) | Faster, more consistent unwraps for [Lesson 6](../uv-mapping.md) | ◻ |
| [SimpleBake](https://superhivemarket.com/products/simplebake---simple-pbr-and-other-baking-in-blender-2) | Paid | One-click PBR + specialist map baking (AO, curvature, ID, etc.) | Streamlines the sculpt→low-poly bakes in [Lesson 7](../../texturing/pbr-materials.md); Blender's built-in bake also works for free | ◻ |
| [Hard Ops / Boxcutter](https://masterxeon1001.gumroad.com/l/hopscutter) ([site](https://masterxeon1001.com/)) | Paid (bundle) | Best-in-class hard-surface modeling & cutting | Accessories, collars, HUD hardware, mechanical props — not needed for the organic creature itself | ◻ |

---

## Choosing what to install (breedables shortlist)

**Minimum to complete the [Blender Foundations path](index.md):** the built-ins (Node Wrangler, LoopTools, Rigify, glTF, Collada) + free RetopoFlow, Ucupaint, TexTools, Poly Haven. That is a fully free stack.

**Add when producing animated creatures for sale:** **Avastar** (⭐) — the one paid add-on that is hard to replace for SL Animesh.

**Add only if measured pain justifies it:** UVPackmaster / Zen UV (UV throughput), SimpleBake (baking convenience), Auto-Rig Pro (rig speed), Hard Ops/Boxcutter (hard-surface accessories).

---

## Related

- [Blender Foundations path](index.md) · [Tutorial arsenal](../../academy/index.md) · [Wider software index](../../research/software-database.md)
- [Tools registry](../../research/tool-registry.md) — license/status detail for reviewers
- [Production line — tool comparison rules](../../research/decision-model.md#writing-a-tool-comparison)

## Videos

**Beginner**

**[Blender Bros Hard Ops & Boxcutter Tutorials](https://www.youtube.com/@BlenderBros/videos)** — Beginner-friendly breakdowns of common Hard Ops and Boxcutter operations in Blender.

**[Dikko Hard Ops for Beginners](https://www.youtube.com/@Dikko/videos)** — Clear introductory tutorials covering the Hard Ops UI and essential boolean modeling shortcuts.

**Intermediate**

**[Hard Ops — quick start](https://www.youtube.com/@HardOps)** — Hard-surface modeling add-on for props

**[Hard Ops Official Channel](https://www.youtube.com/@hardops)** — Official source for Hard Ops/Boxcutter updates and workflow demos from the add-on authors.

**[CGDive Hard Surface / Boxcutter Workflow](https://www.youtube.com/@CGDive/videos)** — Focused hard-surface modeling workflows using Boxcutter and Hard Ops in production.

**[Default Cube Hard Ops/Boxcutter Tips](https://www.youtube.com/@DefaultCube/videos)** — Concise tips and workflow tricks for speeding up hard-surface design with Hard Ops add-ons.

**Advanced**

**[Josh Gambrell Hard Surface Workflow](https://www.youtube.com/@JoshGambrell/videos)** — Professional hard-surface workflows that integrate Hard Ops/Boxcutter for game-ready assets.

---
