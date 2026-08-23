---
title: "Lesson 2 — Interface & navigation"
section: modeling
type: topic
---
# Lesson 2 — Interface & navigation

!!! abstract "Lesson 2 of 10 · [Blender foundations](index.md)"
    **Production stage** — 0 Tooling  
    **Prerequisites** — [Lesson 1](install-and-setup.md)  
    **Evidence folder** — `training/blender/b02/`

## Outcome

You can navigate the 3D viewport, select and transform objects, switch between the editors and workspaces you'll use every day, and read Blender's mode/header system — fast enough that the interface stops slowing you down.

---

## Watch

| Topic | Video | Why this one |
|-------|-------|--------------|
| Interface + navigation | [Blender Guru — Donut series (Parts 1–2)](https://www.youtube.com/playlist?list=PLjEaoINr3zgEPv5y--4MKpciLaoQYZB1Z) | Walks through viewport navigation and the interface hands-on |
| Beginner-friendly overview | [Grant Abbitt — YouTube channel](https://www.youtube.com/@grabbitt) | Short, clear beginner explainers on getting around Blender |

---

## Read

| Source | Link |
|--------|------|
| Manual — Interface | [User interface](https://docs.blender.org/manual/en/latest/interface/index.html) |
| Manual — Navigating the 3D viewport | [Navigation](https://docs.blender.org/manual/en/latest/editors/3dview/navigate/index.html) |
| Manual — Selecting | [Selecting objects](https://docs.blender.org/manual/en/latest/scene_layout/object/selecting.html) |
| Manual — Transform (move/rotate/scale) | [Basic transformations](https://docs.blender.org/manual/en/latest/scene_layout/object/editing/transform/introduction.html) |
| Manual — Editors & workspaces | [Editors](https://docs.blender.org/manual/en/latest/editors/index.html) |

---

## Explain — the interface, step by step

### Navigating the viewport

1. **Orbit:** hold **Middle Mouse Button (MMB)** and drag. No middle button? Enable *Emulate 3-Button Mouse* in Preferences (then `Alt`+LMB orbits).
2. **Pan:** **Shift + MMB** drag.
3. **Zoom:** scroll wheel, or **Ctrl + MMB** drag.
4. **Numpad views:** `1` front, `3` right, `7` top, `Ctrl` + those for the opposite side, `5` toggles perspective/orthographic, `` ` `` (backtick) opens the view pie menu. Ortho views are essential for precise modeling.
5. **Frame selected:** press `.` (numpad period) to snap the camera to whatever is selected — use this constantly.

### Selecting and transforming

1. **Select:** left click. `A` selects all, `Alt`+`A` deselects all, `B` box-select, `C` circle-select, `L` selects a linked island (in edit mode).
2. **Move / Rotate / Scale:** `G` / `R` / `S`. Constrain to an axis by tapping `X`, `Y`, or `Z` after; type a number for exact values (e.g. `G` `Z` `0.1` `Enter`). `Esc` or right-click cancels.
3. **The 3D cursor** (the red/white ring) is the default spawn point for new objects and a pivot option. `Shift`+right-click moves it; `Shift`+`C` resets it to the origin.
4. **Pivot & orientation:** the header dropdowns control what transforms pivot around (Median Point, 3D Cursor, Individual Origins) — you'll switch these often when modeling.

### Modes and the header

- The mode dropdown (top-left of the viewport) switches **Object Mode** (move whole objects) and **Edit Mode** (`Tab`, edit the mesh itself). Sculpt, Texture Paint, Weight Paint, and Pose modes appear here too — you'll use each later in this path.
- In Edit Mode, `1` / `2` / `3` switch **vertex / edge / face** select.

### Editors and workspaces

- The tabs across the very top (**Layout, Modeling, Sculpting, UV Editing, Texture Paint, Shading, Animation…**) are **workspaces** — preset editor arrangements. This path uses almost all of them; get comfortable clicking between them.
- Any panel corner can be dragged to split/join editors. The **Outliner** (top-right) lists your scene; the **Properties** editor (bottom-right) holds object, modifier, material, and render settings.

### Why this matters for breedables

Speed here compounds. Every later lesson — modeling, sculpting, rigging — is just these navigation and transform habits applied in a different mode. Invest now.

---

## Do — hands-on lab

1. Open your `sl-startup.blend` from [Lesson 1](install-and-setup.md).
2. Add three primitives (`Shift`+`A`): a cube, a UV sphere, a cylinder. Space them out.
3. Practise: orbit, pan, zoom; frame each with `.`; jump to front/side/top ortho views.
4. Move the sphere exactly `1 m` up (`G` `Z` `1` `Enter`), rotate the cylinder `90°` on X (`R` `X` `90` `Enter`), scale the cube to half (`S` `0.5` `Enter`).
5. Enter Edit Mode on the cube (`Tab`), select one face, extrude it (`E`), then return to Object Mode.
6. Cycle through the Layout, Modeling, and Shading workspaces.
7. Screenshot the result with the Outliner visible → `training/blender/b02/navigation-practice.png`.
8. Save as `training/blender/b02/practice.blend`.

---

## Produce — required artifacts

| Artifact | Path |
|----------|------|
| Practice scene | `training/blender/b02/practice.blend` |
| Screenshot with Outliner | `training/blender/b02/navigation-practice.png` |
| Shortcut notes (your own cheat sheet) | `training/blender/b02/shortcuts.md` |

---

## Completed when

- [ ] Can orbit/pan/zoom and reach front/side/top ortho without hunting
- [ ] Can `G`/`R`/`S` with axis constraint and typed values
- [ ] Comfortable toggling Object ↔ Edit mode and vertex/edge/face select
- [ ] Cheat sheet committed with your most-used shortcuts

---

## Next

[Lesson 3 — Mesh modeling for organic creatures](../mesh-modeling.md)
