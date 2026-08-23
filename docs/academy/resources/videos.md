# Curated training videos

Pinned videos for Academy tracks. **Slack should link here**, not embed long lists.

When adding a video:

1. Confirm it matches a [production line](../production-line.md) stage
2. Add tool version / date reviewed
3. Prefer official channels or long-standing tutorials
4. Run `/breedtool <name>` after updating Librarian `primary_video_url`

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
| *TBD — Ucupaint walkthrough* | — | Add when reviewed |

Lesson: [A02 Layered Textures](../tracks/a02-layered-textures.md)

---

## A03 — Retopology

| Title | URL | Notes |
|-------|-----|-------|
| *TBD — retopology walkthrough* | — | Add when reviewed |

Lesson: [A03 Retopology](../tracks/a03-retopology.md)

---

## A04 — Rig + animation

| Title | URL | Notes |
|-------|-----|-------|
| *TBD — rigging for game/SL* | — | Add when reviewed |

Lesson: [A04 Rig + Animation](../tracks/a04-rig-animation.md)

---

## A05 — SL fixture / LSL

| Title | URL | Notes |
|-------|-----|-------|
| *TBD — LSL basics* | — | Add when reviewed |

Lesson: [A05 SL Creature Fixture](../tracks/a05-sl-fixture.md)

---

## Maintainer commands

```bash
cd tools/librarian
python -m librarian.cli set-evidence <id> --video "https://..." --docs "https://...,https://..."
python -m librarian.cli content-gaps
```
