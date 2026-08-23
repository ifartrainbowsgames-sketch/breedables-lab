# Start here — how this Academy works

**New question we answer:** *How do professional 3D creature artists work, what software do they use, what can I use for free, and where do I learn the whole workflow?*

→ Read [Academy mission](mission.md) first if you are building or editing pages.

Internal codes like **A01** or **B07** are only for folders — [cheat sheet below](#for-maintainers-only-code-cheat-sheet). Navigation uses plain names.

---

## The whole picture

```text
┌─────────────────────────────────────────────────────────────────┐
│  PROFESSIONAL PIPELINE (how the industry works)                  │
│  Reference → sculpt → retopo → UV → bake → texture → rig →    │
│  anim → optimize → export                                        │
│  See: Professional workflow + Paid vs Free matrix                │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  FREE / OSS TEACH PATH (what we walk you through)               │
│  10 Blender lessons → artifacts in training/blender/            │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  BREEDABLES STUDIO LABS + SECOND LIFE                           │
│  Prove breedables skills → in-world fixture                     │
└─────────────────────────────────────────────────────────────────┘
```

**Three routes at each stage:** professional (Maya/ZBrush/Substance…) · free/OSS (Blender/Krita/Material Maker…) · **what we recommend today** — [software map](professional-workflow/software-map.md).

---

## I want to…

| Goal | Go here |
|------|---------|
| Understand how pros work | [Professional workflow](professional-workflow/index.md) |
| Compare paid vs free tools | [Paid vs free matrix](professional-workflow/paid-vs-free-matrix.md) |
| Pick a program and learn it | [Software packages](software/packages/index.md) |
| **All training videos by stage** | [Training videos index](resources/training-videos-by-stage.md) |
| Follow our free Blender path | [Lesson 1 — Install](software/blender/b01-install-setup.md) |
| Full end-to-end courses | [Complete workflow courses](resources/complete-courses.md) |
| SL-specific rules after good 3D | [Second Life adaptation](professional-workflow/second-life-adaptation.md) |
| Do a breedables project lab | [Studio labs](#layer-2-studio-labs-breedables-projects) |

---

## Layer 1 — Blender lessons (free OSS path)

| # | What you learn | Open |
|---|----------------|------|
| 1 | Install & setup | [Lesson 1](software/blender/b01-install-setup.md) |
| 2 | Interface & navigation | [Lesson 2](software/blender/b02-interface-navigation.md) |
| 3 | Mesh modeling for creatures | [Lesson 3](software/blender/b03-mesh-modeling.md) |
| 4 | Sculpting basics | [Lesson 4](software/blender/b04-sculpting.md) |
| 5 | Retopology | [Lesson 5](software/blender/b05-retopology.md) |
| 6 | UV unwrapping | [Lesson 6](software/blender/b06-uv-unwrapping.md) |
| 7 | Texture painting & PBR | [Lesson 7](software/blender/b07-texture-painting-pbr.md) |
| 8 | Rigging & weight painting | [Lesson 8](software/blender/b08-rigging-weight-painting.md) |
| 9 | Basic animation | [Lesson 9](software/blender/b09-animation.md) |
| 10 | Export to Second Life | [Lesson 10](software/blender/b10-export-to-sl.md) |

Aligned with [Blender Fundamentals 4.5 LTS](https://www.blender.org/support/tutorials/) · [Blender package card](software/packages/blender.md)

Each lesson: **Watch · Read · Do · artifact · PASS criteria**. Watching alone is not completion.

---

## Layer 2 — Studio labs (breedables projects)

| Project | What you prove | Blender lessons first |
|---------|----------------|------------------------|
| [Organic PBR textures](tracks/a01-organic-pbr.md) | SL-ready PBR | 6 + 7 |
| [Layered textures](tracks/a02-layered-textures.md) | Multi-layer skins | Organic PBR + 7 |
| [Retopology](tracks/a03-retopology.md) | Animation-ready mesh | 3–5 |
| [Rig + animation](tracks/a04-rig-animation.md) | Quadruped + cycles | 8 + 9 |
| [In-world fixture](tracks/a05-sl-fixture.md) | Upload + LSL | 10 + earlier labs |

---

## Reference Creature

Our practical lab: **BUILD → TEST → FAIL → SOLVE → DOCUMENT**. When production proves a tutorial wrong, we update the Academy with evidence — see [mission](mission.md).

---

## For maintainers only — code cheat sheet

| Code | Plain name | Folder |
|------|------------|--------|
| B01–B10 | Blender lessons 1–10 | `training/blender/b01/` … `b10/` |
| A01–A05 | Studio labs | `training/texturing/a01/` … `training/lsl/a05/` |

Daily automation: `scripts/daily-wiki.ps1` → `report-human.md` + `wiki-evolution.md`

---

## Related

- [Academy overview](overview.md)  
- [Software page standard](software/software-page-standard.md)
