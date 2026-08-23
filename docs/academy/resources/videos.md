# Video index

!!! warning "Blender fundamentals live elsewhere"
    **Start here:** [Blender Foundations B01](../software/blender/b01-install-setup.md) — Donut / official beginner series in [tutorial arsenal](tutorials.md).

    This page lists **extra videos** for studio labs and add-ons. A handful of links does not equal learning Blender.

When adding a video: confirm production stage, note Blender/tool version, prefer official or long-standing tutorials.

---

## A01 — Organic PBR

| Title | URL | Notes |
|-------|-----|-------|
| Blender 4.0 Beginner Tutorial — Part 1 | https://www.youtube.com/watch?v=B0J27sf02NU | Blender Foundation |
| PBR Texturing in Blender | https://www.youtube.com/watch?v=4_xYiw1nL5M | Metallic/roughness workflow |
| Material Maker intro | https://www.youtube.com/watch?v=8MMSS2F5vtc | Procedural PBR |

Lesson: [A01 Organic PBR](../tracks/a01-organic-pbr.md)

---

## A02 — Layered textures

| Title | URL | Notes |
|-------|-----|-------|
| Ucupaint — Turn Blender Into Substance Painter | https://www.youtube.com/watch?v=d3KrMwAWJI0 | 3D From Zero; layer + PBR channels |
| More Ucupaint tutorials | https://ucupumar.github.io/ucupaint-wiki/video-tutorials/ | Official curated list |

Lesson: [A02 Layered Textures](../tracks/a02-layered-textures.md)

---

## A03 — Retopology

| Title | URL | Notes |
|-------|-----|-------|
| RetopoFlow 4 — Installation & setup | https://www.youtube.com/watch?v=Ds5Soybs610 | CG Cookie / Orange Turbine |
| RetopoFlow 4 course trailer | https://www.youtube.com/watch?v=ZE3gcVRR3Dk | Full free course on CG Cookie |

Lesson: [A03 Retopology](../tracks/a03-retopology.md)

---

## A04 — Rig + animation

| Title | URL | Notes |
|-------|-----|-------|
| Rigify documentation walkthrough | https://docs.blender.org/manual/en/latest/addons/rigify/index.html | Official manual (no single video) |
| *Add Rigify quadruped tutorial* | — | Match your Blender version; update when reviewed |

Lesson: [A04 Rig + Animation](../tracks/a04-rig-animation.md)

---

## A05 — SL fixture / LSL

| Title | URL | Notes |
|-------|-----|-------|
| LSL Portal | https://wiki.secondlife.com/wiki/LSL_Portal | Official examples |
| Animesh User Guide | https://wiki.secondlife.com/wiki/Animesh_User_Guide | In-world animated mesh |

Lesson: [A05 SL Creature Fixture](../tracks/a05-sl-fixture.md)

---

## Image-to-3D (E02 / tools)

| Title | URL | Notes |
|-------|-----|-------|
| TripoSR — 2D image to 3D mesh | https://www.youtube.com/watch?v=e2UeHwzncHA | Local inference + Blender import |
| TripoSR Colab overview | https://www.youtube.com/watch?v=_xy7OiEnDMc | Fast overview; links official repo |

Tool: [TripoSR](../../production/tools/triposr.md)

---

## Asset libraries (reference)

| Title | URL | Notes |
|-------|-----|-------|
| Poly Haven Blender add-on | https://www.youtube.com/watch?v=ku_xv6WV6UE | Official Poly Haven |
| PBR texture maps for beginners | https://www.youtube.com/watch?v=fUZHyoeuwVI | Generic Blender PBR setup (works with CC0 assets) |

Tools: [Poly Haven](../../production/tools/poly-haven.md) · [ambientCG](../../production/tools/ambientcg.md)

---

## Maintainer commands

```bash
cd tools/librarian
python -m librarian.cli seed-baseline
python -m librarian.cli content-gaps
```
