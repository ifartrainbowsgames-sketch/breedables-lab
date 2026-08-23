---
title: "Lesson 1 — Install & setup"
section: tools
type: topic
---
# Lesson 1 — Install & setup

!!! abstract "Lesson 1 of 10 · [Blender foundations](index.md)"
    **Production stage** — Tooling  
    **Prerequisites** — none  
    **Evidence folder** — `training/blender/b01/` *(matches lesson number)*

## Outcome

You have the correct Blender **LTS** installed and configured with **units, scale, and viewport settings** sensible for Second Life work, and you can prove it with a screenshot of your preferences and a saved startup file.

Watching alone is not completion — you commit a configured startup `.blend` and a screenshot.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Blender beginner series (install + basics) | [Blender Guru — Donut series (Part 1)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | The standard zero-to-competent intro; Part 1 covers install and first launch |
| Official beginner intro | [Blender 4.0 Beginner Tutorial — Part 1](https://www.youtube.com/watch?v=B0J27sf02NU) | Blender Foundation channel; stable overview of install and interface |

---

## Read

| Source | Link |
|--------|------|
| Blender download (stable) | [blender.org/download](https://www.blender.org/download/) |
| Blender LTS releases | [blender.org/download/lts](https://www.blender.org/download/lts/) |
| System requirements | [blender.org/download/requirements](https://www.blender.org/download/requirements/) |
| Manual — Units & scene properties | [Scene units](https://docs.blender.org/manual/en/latest/scene_layout/scene/properties.html) |
| Manual — Saving & startup file | [Blend files / defaults](https://docs.blender.org/manual/en/latest/files/blend/index.html) |

Full index: [Official docs](../../research/software-database.md).

---

## Explain — which version and settings, step by step

### Pick the LTS, not the newest

Blender ships a new feature release roughly every quarter and marks two of them per cycle as **LTS (Long Term Support)** — patched for two years. For a studio pipeline, always run an **LTS**: add-ons and export behaviour stay stable.

- As of 2026 the current LTS lines are **Blender 5.2 LTS** (July 2026, supported to 2028) and **Blender 4.5 LTS** (July 2025, supported to 2027).
- **Studio pick:** standardise the whole team on **one** LTS. Use **4.5 LTS** if any paid add-on you rely on (e.g. Avastar) has not yet certified 5.x; otherwise use **5.2 LTS**. Record the chosen version in your lab notes so everyone matches.
- Prefer the installer/portable build from [blender.org](https://www.blender.org/download/) over Steam or OS package managers so version and add-on paths are predictable.

### Configure once, for SL scale

Second Life is a **1 metre = 1 metre** world. Match Blender to it so your creature imports at the right size and you don't have to rescale on upload.

1. Open Blender. Delete the default cube (`X` → Delete) — start clean.
2. **Properties editor → Scene properties → Units:** set **Unit System = Metric**, **Unit Scale = 1.0**, **Length = Meters**. This is the default, but confirm it — mismatched unit scale is the most common cause of "my mesh uploaded tiny/huge".
3. **Overlays:** in the viewport header, open the **Overlays** dropdown and enable **Scale** on the floor grid so 1 grid square reads as 1 m.
4. **Add a size reference:** add a plane or cube scaled to a known SL creature footprint (e.g. a 0.5 m cube for a small pet) and keep it on a hidden collection called `ref`. Model against it.
5. **Viewport clipping:** press `N` for the sidebar → **View** tab → set **Clip Start** to `0.01 m` and **End** to `1000 m`. Small creatures otherwise disappear when you zoom in.
6. **Preferences (`Edit → Preferences`):**
   - **Interface → Display:** leave tooltips + Python tooltips on while learning.
   - **Input:** enable **Emulate Numpad** only if your keyboard has no numpad (affects navigation shortcuts in B02).
   - **Save & Load:** turn on **Auto Save** (every 2–5 min) and **Save Versions** ≥ 1.
   - **Add-ons:** enable the built-ins you'll need soon — **Node Wrangler**, **LoopTools**, **Extra Objects**, and the **glTF 2.0** / **Collada** exporters (these ship with Blender). See the [add-on catalog](addon-catalog.md).
7. **Save your defaults:** with units, clipping, and add-ons set, choose **File → Defaults → Save Startup File**. Every new file now opens SL-ready.

### Why this matters for breedables

Getting scale and export add-ons right on day one prevents the two most common upload failures later ([Lesson 10](export-and-upload.md)): wrong size in-world, and a missing Collada/glTF exporter when you try to export.

---

## Do — hands-on lab

1. Install your chosen Blender LTS from [blender.org](https://www.blender.org/download/).
2. Apply the units, clipping, auto-save, and add-on settings above.
3. Add a 0.5 m reference cube on a `ref` collection.
4. **Save Startup File** so it becomes your default.
5. Save the file to `training/blender/b01/sl-startup.blend`.
6. Screenshot **Preferences → Add-ons** (showing the enabled exporters) → `training/blender/b01/addons.png`.
7. Screenshot the viewport with the grid scale overlay + reference cube → `training/blender/b01/scale-check.png`.
8. Write `training/blender/b01/notes.md`: Blender version + build hash, OS, and why you picked that LTS.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| SL-ready startup file | `training/blender/b01/sl-startup.blend` |
| Add-ons screenshot | `training/blender/b01/addons.png` |
| Scale check screenshot | `training/blender/b01/scale-check.png` |
| Lab notes (version + rationale) | `training/blender/b01/notes.md` |

---

## Completed when

- [ ] Running a current **LTS** (version recorded in notes)
- [ ] Metric units, Unit Scale 1.0, grid scale overlay verified against a 0.5 m cube
- [ ] Clipping start/end adjusted; auto-save on
- [ ] glTF **and** Collada exporters enabled
- [ ] Startup file saved as default and committed

---

## Next

[Lesson 2 — Interface & navigation](interface-and-navigation.md)
