# Rig + animation

![Blender](../../assets/inline/blender.png){ width="80" }

**Studio lab** · Quadruped rig, idle + walk cycles  
**Evidence folder:** `training/rigging/a04/` *(internal id A04)*

!!! danger "Prerequisites"
    Complete **[Blender lesson 8](../software/blender/b08-rigging-weight-painting.md)** (rigging) and **[lesson 9](../software/blender/b09-animation.md)** (animation) first.

**Production stage:** Rigging & animation  
**Experiment:** [E04 Rig and retarget baseline](../../production/experiments.md#e04-rig-and-retarget-baseline)  
**Primary tools:** [Blender](../../production/tools/blender.md), Rigify (bundled)

## Outcome

Rig a breedable-appropriate mesh and deliver **two loopable animations** (e.g. idle + eat/play) with export notes for Second Life Animesh upload.

---

## Watch

| Topic | Video | Notes |
|-------|-------|-------|
| Blender rigging intro | [Armatures introduction (manual)](https://docs.blender.org/manual/en/latest/animation/armatures/introduction.html) | Read + follow along in Blender |
| Quadruped rigging | [Darkfall — quadruped rigging intro](https://www.youtube.com/watch?v=6Km2tRFTxvs) | Creature rig for breedables |

→ [Video library — rigging](../resources/video-library.md#blender)

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/6Km2tRFTxvs" title="Darkfall quadruped rigging intro" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

## Read

| Source | Link |
|--------|------|
| Rigify manual | [Rigify add-on](https://docs.blender.org/manual/en/latest/addons/rigify/index.html) |
| NLA editor | [NLA documentation](https://docs.blender.org/manual/en/latest/editors/nla.html) |
| SL animation upload | [Uploading a rigged mesh](https://wiki.secondlife.com/wiki/Mesh/Uploading_and_wearing_a_rigged_mesh) · [How to create animations](https://wiki.secondlife.com/wiki/How_to_create_animations) |
| Animesh guide | [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) |

---

## Explain — Breedables workflow

1. Use mesh from A03 (or approved test mesh with similar topology).
2. Build Rigify quadruped (or documented manual rig) — **bone names map** saved for retargeting.
3. Create **idle loop** (2–4 s) and **second action** (eat, play, or locomotion stub).
4. Bake/export animations in SL-compatible format (document `.bvh` / upload path used).
5. Record retarget/cleanup effort for E04 — breedables often reuse animation libraries.

---

## Do — Hands-on lab

1. Rig test mesh; verify weight painting on deformation zones.
2. Keyframe idle + second loop; use NLA for organization if helpful.
3. Export animations to `training/rigging/a04/animations/`.
4. Render preview (viewport or MP4/GIF).
5. Optional: upload to SL test avatar/mesh and capture in-world screenshot.

---

## Produce — Required artifacts

| Artifact | Path |
|----------|------|
| Rigged scene | `training/rigging/a04/rigged.blend` |
| Bone mapping notes | `training/rigging/a04/bone-map.md` |
| Animation files | `training/rigging/a04/animations/` |
| Preview | `training/rigging/a04/preview.mp4` or `.gif` |
| Lab notes | `training/rigging/a04/notes.md` |

---

## Sign-off checklist

- [ ] Two distinct loopable animations exported
- [ ] Deformation acceptable on neck, legs, tail (if present)
- [ ] E04 measurement table filled
- [ ] SL upload path documented (even if blocked on permissions)

---

## Next track

[In-world fixture](a05-sl-fixture.md)
