# Second Life adaptation — after good general 3D

**Rule:** Teach **correct professional 3D production first**. Then teach what **changes for Second Life delivery** — do not teach bad modeling habits “because SL.”

---

## Two layers

| Layer | What it covers |
|-------|----------------|
| **General professional workflow** | Reference → sculpt → retopo → UV → bake → texture → rig → anim → optimize → export |
| **SL delivery requirements** | Upload limits, LOD, materials, Animesh, land impact, LSL, performance |

---

## What adapts for SL (not “what to skip”)

| Topic | General practice | SL adaptation |
|-------|------------------|---------------|
| Poly budget | Game engine draw calls | **Land impact**, upload limits, Animesh cost |
| LODs | Engine LOD chains | SL **mesh LOD** upload requirements |
| Textures | 4K common in film | **Cost-aware** resolutions; PBR metallic/roughness in viewer |
| Rigging | Engine-specific | **Animesh** vs uploaded rig; joint limits |
| Animation | FBX to Unity/Unreal | SL **animation** upload + priority |
| Materials | Engine shaders | SL **PBR** material model — verify in-world |
| QA | In-engine | **In-world** rez, lighting, script loop |

---

## Academy placement

| General skill | SL-specific lesson |
|---------------|-------------------|
| Lessons 1–9 (Blender) | Professional creature skills |
| [Lesson 10 — Export to SL](../software/blender/b10-export-to-sl.md) | Upload package |
| [In-world fixture lab](../tracks/a05-sl-fixture.md) | LSL, persistence, Animesh test |
| [Platform baseline](../../secondlife/platform-baseline.md) | Rules & viewer behavior |

---

## Reference Creature loop

When the Reference Creature hits an SL-specific wall (bad export, PBR surprise, land impact):

1. Document in `research/experiments/` or `training/secondlife/`
2. Update this page + affected lesson **with evidence**
3. Do not silently patch tutorials without proof

→ [Pipeline stages](pipeline-stages.md) · [Mission](../mission.md)
