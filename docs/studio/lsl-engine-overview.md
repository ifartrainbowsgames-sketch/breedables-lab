# LSL & breedables engine overview

**Status:** Stub — expand when fixture scripts land in `training/lsl/a05/` and production repo modules exist.

---

## Purpose

Document how breedables **state**, **genetics**, and **persistence** work in Second Life — separate from generic LSL tutorials.

## Planned sections

1. **Architecture** — linkset layout, Animesh vs legacy rigged mesh, module boundaries  
2. **Persistence** — Linkset Data vs legacy notecard/inventory patterns ([platform baseline](../secondlife/platform-baseline.md))  
3. **State machine** — hunger, energy, breeding cooldowns, life stages  
4. **Genetics** — trait encoding, inheritance rules, phenotype → mesh/texture mapping  
5. **HUD & owner UX** — menus, permissions, update channel  
6. **Debug & QA** — in-world test checklist tied to [In-world fixture](../academy/tracks/a05-sl-fixture.md)

## Read first

- [LSL Portal (SL wiki)](https://wiki.secondlife.com/wiki/LSL_Portal)
- [LSL definitions (GitHub)](https://github.com/secondlife/lsl-definitions)
- [In-world fixture](../academy/tracks/a05-sl-fixture.md)
- [E05 persistence experiment](../production/experiments.md#e05-modern-sl-persistence-fixture)

## Evidence

When scripts exist, commit to:

- `training/lsl/a05/scripts/` — fixture + minimal engine modules  
- `training/lsl/a05/notes.md` — architecture decisions  
- `training/lsl/a05/inworld-test.png` — proof on test parcel  

## Blockers

This page stays a stub until:

- [ ] A05 lab produces at least one working fixture script  
- [ ] Genetics schema is drafted (even as markdown spec)  
- [ ] Linkset Data vs alternatives decision recorded from E05  

Do not author long-form engine docs outside git — add sections here as code lands.
