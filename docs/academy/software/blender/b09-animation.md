# Lesson 9 — Basic animation

!!! abstract "Lesson 9 of 10 · [Blender foundations](index.md)"
    **Production stage** — 8 Animation  
    **Prerequisites** — [Lesson 8](b08-rigging-weight-painting.md)  
    **Feeds studio lab** — [Rig + animation](../../tracks/a04-rig-animation.md)  
    **Evidence folder** — `training/blender/b09/` (mirror to `training/animation/a04/`)

## Outcome

You can keyframe an **idle** and a **walk cycle** on your quadruped rig using the Dope Sheet, Graph Editor, and NLA, and bake them into clips ready for Second Life upload.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Animation fundamentals | [Blender Guru — Donut series (animation part)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | Keyframes, timeline, and the graph editor in context |
| Character/creature animation | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Beginner walk-cycle and posing tutorials |

> Add a verified quadruped walk-cycle video to the [videos index](../../resources/videos.md#a04-rig-animation).

---

## Read

| Source | Link |
|--------|------|
| Manual — Animation & rigging | [Animation](https://docs.blender.org/manual/en/latest/animation/index.html) |
| Manual — Keyframes | [Keyframes](https://docs.blender.org/manual/en/latest/animation/keyframes/index.html) |
| Manual — Graph Editor | [Graph Editor](https://docs.blender.org/manual/en/latest/editors/graph_editor/index.html) |
| Manual — NLA (actions) | [Nonlinear Animation](https://docs.blender.org/manual/en/latest/editors/nla/index.html) |
| SL — Uploading & animating a model | [Uploading a rigged mesh](https://wiki.secondlife.com/wiki/Mesh/Uploading_and_wearing_a_rigged_mesh) · [How to create animations](https://wiki.secondlife.com/wiki/How_to_create_animations) |

---

## Explain — idle and walk, step by step

### The tools

- **Timeline** — playback, current frame, frame range.
- **Dope Sheet** — every keyframe as a dot; move/copy/scale timing here.
- **Graph Editor** — the curves between keys; controls easing (ease-in/out) that makes motion feel alive.
- **Action Editor / NLA** — each animation is an **Action**; SL wants **one action per clip** (idle, walk).

### Keyframing basics

1. In **Pose Mode**, set the frame, pose the bones, then `I` → **Insert Keyframe** (choose LocRot, or use **Auto Keying** to key automatically as you pose).
2. Move to the next key frame, adjust the pose, key again. Blender interpolates between.
3. Set **interpolation** to Bézier and shape easing in the Graph Editor; use **Constant** only for holds.

### An idle (subtle, loops)

1. Frame range e.g. 1–48 at 24 fps (a ~2 s loop).
2. Keys: a gentle breathing rise/fall of the chest, tiny head sway, tail drift. Keep amplitude small.
3. Make it **loop**: the last frame's pose = the first frame's pose. Copy frame 1's keys to the last frame.

### A walk cycle (the four contact poses)

1. Frame range e.g. 1–24 for one cycle. Quadruped gaits are typically diagonal (a "trot"-like walk is easiest to start).
2. Block the key poses: **contact**, **down/passing**, **lift**, **passing** — for the diagonal leg pairs, offset in time.
3. Add secondary motion: spine flex, head bob, tail counter-sway.
4. Loop it: first and last poses match. Test playback on a loop.

### Bake for export

1. **Bake** the action to plain bone keyframes if you used constraints/Rigify controls (Pose → Animation → Bake Action, **Visual Keying**, **Clear Constraints** on a copy). SL needs baked bone motion, not rig-control dependencies.
2. Keep idle and walk as **separate actions**, clearly named.
3. SL animation upload accepts **BVH** or (via Avastar) **.anim**; you'll finalize the export format in [Lesson 10](b10-export-to-sl.md). Note SL priority, loop in/out points, and hand/ease settings there.

### Why this matters for breedables

Idle + walk are the minimum believable life for an Animesh creature. Baked, well-named, looping clips are what the [A05 in-world fixture](../../tracks/a05-sl-fixture.md) triggers via script. Good easing is the difference between "alive" and "robotic".

---

## Do — hands-on lab

1. On the B08 rig, animate a looping **idle** and a looping **walk cycle**.
2. Refine easing in the Graph Editor; confirm both loop seamlessly.
3. Bake each to a clean, separate, named Action.
4. Render a viewport playblast of each (`.mp4` or image sequence) → `training/blender/b09/idle.mp4`, `walk.mp4`.
5. Save `.blend` → `training/blender/b09/animated.blend`; mirror to `training/animation/a04/`.
6. `training/blender/b09/notes.md`: frame ranges, fps, gait choice, bake settings.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Animated source | `training/blender/b09/animated.blend` |
| Idle + walk playblasts | `training/blender/b09/idle.mp4`, `walk.mp4` |
| Notes (ranges, fps, gait, bake) | `training/blender/b09/notes.md` |
| A04 mirror | `training/animation/a04/` |

---

## Completed when

- [ ] Idle and walk both loop seamlessly
- [ ] Easing shaped in the Graph Editor (not linear/robotic)
- [ ] Each clip baked to a separate, named Action
- [ ] Playblasts + notes committed

---

## Next

[Lesson 10 — Exporting to Second Life](b10-export-to-sl.md)
