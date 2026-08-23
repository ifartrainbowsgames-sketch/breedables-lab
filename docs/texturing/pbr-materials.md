---
title: "Lesson 7 — Texture painting & PBR materials"
section: texturing
type: topic
---
# Lesson 7 — Texture painting & PBR materials

!!! abstract "Lesson 7 of 10 · [Blender foundations](../modeling/blender/index.md)"
    **Production stage** — 5 Texturing  
    **Prerequisites** — [Lesson 6](../modeling/uv-mapping.md)  
    **Feeds studio lab** — [Organic PBR material](projects/organic-pbr-material.md) / [Layered textures](projects/layered-textures.md)  
    **Evidence folder** — `training/blender/b07/` (mirror to `training/texturing/a01/`)

## Outcome

You can build a **metallic/roughness PBR material**, bake your B04 sculpt detail into a normal map, paint/refine surface colour, and export the map set so it uploads correctly as **Second Life glTF PBR**.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Blender shader/PBR basics | [PBR Texturing in Blender (Ryan King Art)](https://www.youtube.com/watch?v=4_xYiw1nL5M) | Practical metallic/roughness node setup |
| Shader node fundamentals | [Ryan King Art — YouTube channel](https://www.youtube.com/@RyanKingArt) | Deep, topic-by-topic node tutorials (see the [tutorial arsenal](#shader-nodes)) |
| Procedural PBR alternative | [Material Maker intro](https://www.youtube.com/watch?v=8MMSS2F5vtc) | Procedural generators for skin/fur variants |

---

## Read

| Source | Link |
|--------|------|
| Manual — Texture Paint | [Texture painting](https://docs.blender.org/manual/en/latest/sculpt_paint/texture_paint/index.html) |
| Manual — Shader nodes | [Shader nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/introduction.html) |
| Manual — Baking | [Render baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html) |
| SL — PBR materials | [PBR Materials (SL wiki)](https://wiki.secondlife.com/wiki/PBR_Materials) |
| Studio — platform baseline | [Platform baseline](../second-life/platform-baseline.md) |

---

## Explain — PBR for Second Life, step by step

### What SL expects

Second Life uses **glTF 2.0 metallic/roughness PBR**. Your material resolves to these channels:

- **Base Color** (albedo) — the flat colour, no baked lighting/shadows.
- **Metallic** — 0 for organic surfaces (skin, fur, scales); 1 only for actual metal.
- **Roughness** — how matte/glossy; skin is fairly rough, wet eyes/claws smoother.
- **Normal** — surface detail from your sculpt, so the low-poly mesh looks detailed.
- Optionally **Emissive** and **Occlusion**. (SL packs occlusion/roughness/metallic into one ORM-style texture on upload; author them cleanly and let the uploader combine.)

Legacy spec/gloss is **not** PBR — always author metallic/roughness.

### Bake the sculpt detail down

1. Keep both meshes: high-poly B04 sculpt + low-poly B06 unwrapped mesh, aligned.
2. In the low-poly material, add an **Image Texture** node, new image (e.g. 2048², 32-bit float for normal), and **do not connect it** — just keep it selected as the bake target.
3. Render properties → engine **Cycles** → **Bake** panel → **Bake Type: Normal**, enable **Selected to Active** (select high-poly, then shift-select low-poly last), set a small **Extrusion/Ray Distance**, **Bake**.
4. Repeat for **Ambient Occlusion** and, if you want, **Curvature** — these help drive wear/dirt masks in A02.
5. Save each baked image (`Image → Save As`) to `training/blender/b07/maps/`.

### Build the material

1. In the **Shading** workspace, set up a **Principled BSDF**:
   - Base Color ← your painted/procedural colour texture.
   - Roughness ← roughness map (or a constant while learning).
   - Normal ← **Normal Map** node ← baked normal texture. Set the Normal Map node's space to **Tangent**.
2. **Paint colour** in Texture Paint mode directly on the model (or generate a procedural base in Material Maker and refine with [Ucupaint](software/ucupaint.md) layers — this is the A02 workflow).
3. Preview in **Material Preview** / **Rendered** shading. Remember Blender's viewport and SL's renderer differ — the real test is in-world.

### Export the map set

- Export each channel as **PNG** at a power-of-two resolution (1024 or 2048; document the choice). Base Color usually sRGB; Normal/Roughness/Metallic as **Non-Color** data.
- For upload you can either apply the individual maps in SL's material editor or export the whole material as **glTF** ([Lesson 10](../second-life/export-and-upload.md)).

### Validate in-world (required)

Upload the maps to SL, apply to a test prim/mesh, and screenshot under a known environment/EEP setting. Compare to your Blender preview and note differences. **A Blender render is not proof; the in-world screenshot is.**

### Why this matters for breedables

This is the visible product. Correct metallic/roughness authoring is the difference between a creature that looks plastic or washed-out in-world and one that reads as living skin/fur/scale. The baked normal map is what lets a cheap low-poly mesh (B05) look sculpted.

---

## Do — hands-on lab

1. Bake Normal + AO from the B04 sculpt onto the B06 low-poly UVs.
2. Build a Principled BSDF metallic/roughness material using the baked maps + a painted or procedural base colour.
3. Export the full map set to `training/blender/b07/maps/` (correct colour spaces).
4. Upload to SL, apply, screenshot in-world with EEP/viewer noted.
5. Screenshots: Blender rendered view → `training/blender/b07/blender-render.png`; in-world → `training/blender/b07/sl-inworld.png`.
6. Save `.blend` → `training/blender/b07/textured.blend`; mirror maps + shots to `training/texturing/a01/`.
7. `training/blender/b07/notes.md`: resolutions, colour spaces, metallic/roughness values, EEP used.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Textured source | `training/blender/b07/textured.blend` |
| Baked + painted map set | `training/blender/b07/maps/` |
| Blender render + in-world proof | `training/blender/b07/blender-render.png`, `sl-inworld.png` |
| Notes | `training/blender/b07/notes.md` |
| A01 mirror | `training/texturing/a01/` |

---

## Completed when

- [ ] Normal (and AO) baked from sculpt to low-poly
- [ ] Metallic/roughness material (not spec/gloss), correct colour spaces
- [ ] Map set exported at documented power-of-two resolution
- [ ] **In-world screenshot** committed with EEP/viewer noted

---

## Next

[Lesson 8 — Rigging & weight painting](../rigging-animation/rigging-and-skinning.md)

## More tutorials

Lesson: [Lesson 7 — Texture painting & PBR materials](pbr-materials.md) · Tracks: [Organic PBR material](projects/organic-pbr-material.md)/[Layered textures](projects/layered-textures.md)

**Beginner**
- **PBR Texturing in Blender** (Ryan King Art) — metallic/roughness setup. [Video](https://www.youtube.com/watch?v=4_xYiw1nL5M)
- **Grant Abbitt** — texture painting fundamentals. [Channel](https://www.youtube.com/@grabbitt)
- Manual — [Texture painting](https://docs.blender.org/manual/en/latest/sculpt_paint/texture_paint/index.html) · [Baking](https://docs.blender.org/manual/en/latest/render/cycles/baking.html)

**Intermediate**
- **Material Maker intro** — procedural PBR generators for skin/fur variants. [Video](https://www.youtube.com/watch?v=8MMSS2F5vtc) · [Material Maker](https://www.materialmaker.org/)
- Tool: [Ucupaint](https://github.com/ucupumar/ucupaint) (layer painting) — [registry](software/ucupaint.md)

### Advanced / SL-specific
- **SL — PBR Materials** (metallic/roughness, glTF 2.0). [SL wiki](https://wiki.secondlife.com/wiki/PBR_Materials) · [platform baseline](../second-life/platform-baseline.md)
- CC0 inputs: [Poly Haven](https://polyhaven.com/) · [ambientCG](https://ambientcg.com/) — record provenance.

---

## Shader nodes

Lesson: [Lesson 7 — Texture painting & PBR materials](pbr-materials.md) (shader section)

The material node editor is its own skill — procedural masks, mix shaders, and node groups power breedable **phenotype variation** without repainting.

**Beginner**
- **Ryan King Art** — the most complete free node-by-node library (Mix, ColorRamp, Noise, Voronoi, Bump/Normal, node groups). [Channel](https://www.youtube.com/@RyanKingArt)
- **Blender Guru — Donut series** (shading parts) introduces the shader editor gently. [Playlist](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z)
- Manual — [Shader nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/index.html) · [Introduction](https://docs.blender.org/manual/en/latest/render/shader_nodes/introduction.html)

**Intermediate**
- **Ryan King Art** — procedural material series (skin, scales, fur-like surfaces). [Channel](https://www.youtube.com/@RyanKingArt) · [Gumroad (Paid extras)](https://ryankingart.gumroad.com/)
- Manual — [Principled BSDF](https://docs.blender.org/manual/en/latest/render/shader_nodes/shader/principled.html) · [Texture nodes](https://docs.blender.org/manual/en/latest/render/shader_nodes/textures/index.html)
- Add-on: [Node Wrangler](https://docs.blender.org/manual/en/latest/addons/node_wrangler.html) (built-in) — essential node-editing speedups.

**Advanced**
- **Default Cube / CGMatter** — deep procedural/node techniques. [Default Cube](https://www.youtube.com/channel/UCdpWKLNfbROyoGPV46-zaUQ) · [@CGMatter](https://www.youtube.com/@CGMatter)
- Manual — [Shader nodes overview](https://docs.blender.org/manual/en/latest/render/shader_nodes/index.html) for masks and phenotype logic.

---
