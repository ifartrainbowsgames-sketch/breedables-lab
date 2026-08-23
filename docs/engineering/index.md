---
title: "Breedables Engineering"
section: engineering
type: index
question: "How does the breedable system actually work?"
---
# Breedables Engineering

!!! abstract "This section answers one question"
    *How does the breedable system actually work?*

The runtime system — LSL scripting, genetics and inheritance, lifecycle and
needs, persistence, movement and animation control, HUD and updater. This is the
software side of a breedable, not the art side.

## Topics

| Page | What it covers |
|------|----------------|
| [LSL & engine overview](lsl-engine.md) | Runtime architecture and state machines |

## How the runtime is split

A breedable is not one script. Keeping these separate is what lets a designer
retune rarity without a scripter touching the engine.

| Layer | Responsibility | Lives in |
|-------|----------------|----------|
| Engine | Lifecycle, needs, breeding, movement, updater | `scripts/` |
| Data | Traits, colours, rarity tables, mutation rates | `data/genes/`, `data/traits/` |
| HUD | Player-facing menus, status, breeding UI | `hud/` |
| Releases | Versioned packages and changelogs | `releases/`, `creatures/<species>/` |

The engine reads the data files; it does not embed them. A balance change should
be a data commit, not an engine rewrite.

## The platform primitives that matter

| Primitive | Why it decides the design |
|-----------|---------------------------|
| **Linkset Data** | The modern persistence store. State that does not survive a sim restart is not state. |
| **Animesh** | Animated mesh with its own bone and land-impact budget, which constrains the rig long before scripting starts. |
| **PBR materials** | Set via glTF, so appearance changes at runtime are limited to what the material system exposes. |

Canonical function signatures come from
[lsl-definitions](https://github.com/secondlife/lsl-definitions) — the studio
treats that repository as the reference, not forum posts.

## Studio position on existing breedables

Established products are worth studying and are not worth copying blindly. They
encode years of platform workarounds, some of which are obsolete now that
Linkset Data and Animesh exist. Read the
[case studies](../research/breedables-case-studies.md) for what they solved, then
decide independently whether their solution is still the right one.

## Prove it before you build it

The [in-world fixture lab](../projects/in-world-fixture.md) exists so the runtime
is validated on fake traits before any species-specific genetics are written. A
persistence bug found with three fake genes is cheap; the same bug found after a
full trait table is not.

**Evidence folders** — `scripts/`, `training/lsl/a05/`, `data/`

## Related

- [Platform baseline](../second-life/platform-baseline.md) — the limits the engine has to respect
- [Studio labs](../projects/index.md) — where the runtime gets tested
- [Roadmap](../roadmap.md) — what order this gets built in
