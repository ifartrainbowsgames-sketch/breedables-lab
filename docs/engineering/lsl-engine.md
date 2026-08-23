---
title: "LSL & breedables engine overview"
section: engineering
type: topic
---

# LSL & breedables engine overview

!!! info "About this page"
    **Prerequisites** — Basic LSL scripting and Second Life linkset concepts  
    **Evidence folder** — `training/lsl/a05/`

A Second Life breedables engine is an event-driven LSL system that coordinates state, genetics, and persistence inside a linkset. This page maps how the moving parts fit together—linkset layout, timers, Linkset Data, trait encoding, owner-facing HUDs, and QA workflows—without duplicating generic LSL tutorials.

## Read

| Source | Covers |
|---|---|
| [LSL Portal](https://wiki.secondlife.com/wiki/LSL_Portal) | Official Second Life scripting language and API reference |
| [LSL definitions](https://github.com/secondlife/lsl-definitions) | Language-server definitions and built-in function signatures |
| [In-world fixture](../projects/in-world-fixture.md) | Reusable test parcel and fixture for breedables QA |
| [Modern SL persistence fixture](../research/experiments.md#e05-modern-sl-persistence-fixture) | Evaluation of Linkset Data versus legacy persistence patterns |
| [Second Life platform baseline](../second-life/platform-baseline.md) | Platform constraints that drive persistence and update choices |

## What this page covers

This page documents how a breedables *engine* works in Second Life: the scripts that turn a static object into a living pet. It is not a generic LSL tutorial. Instead, it maps the architecture needed to store **state**, express **genetics**, and survive **persistence** across rez and region crossings. Use the links below for language syntax; use this page for how the pieces are wired together.

## Architecture at a glance

A breedable is usually a single linkset. The root prim typically hosts the main control script; child prims carry mesh/texture swap targets, animation controllers, or sensor scripts. For **Animesh** creatures, the root script drives `llStartAnimation`/`llStopAnimation` and meshes are rigged externally; for legacy rigged-mesh pets, child prims are swapped or retextured. Keep module boundaries explicit:

- **Controller** — state machine, timer owner, persistence layer.
- **Render** — mesh/texture/animation changes driven by phenotype.
- **Sensor/Chat** — listens for breeding partners, owner commands, or update broadcasts.
- **HUD relay** — talks to an external HUD over a private channel.

Because LSL is event-driven, every long-running process must be broken into timer ticks or listener callbacks, never blocking loops.

## State machine

The heart of the engine is a finite-state or enumerated-state loop. On each timer tick (set with `llSetTimerEvent`) the controller evaluates:

1. **Hunger** — decrement a stored value; if below threshold, trigger foraging request or health loss.
2. **Energy** — spent by movement, breeding, or aging; recovered by food or rest.
3. **Life stage** — age counter increments; thresholds trigger baby → adult → elder transitions.
4. **Breeding cooldown** — a timestamp or tick counter prevents immediate re-breeding.
5. **Mood/health flags** — sickness, pregnancy, hibernation.

State changes are kept in **Linkset Data** (or the chosen persistence store) and mirrored to the render module so the visible pet matches its internal state.

## Persistence strategy

Breedables must remember state across derez/rez, region crossings, and script resets. Modern engines should prefer **Linkset Data** (`llLinksetDataRead`, `llLinksetDataWrite`, `llLinksetDataDelete`) because it is script-local, fast, and survives inventory transfer. Compare it to the legacy patterns:

| Pattern | Pros | Cons |
|---|---|---|
| Linkset Data | Fast, no inventory bloat, survives take/rez | Limited per-linkset budget, no human-readable backup |
| Notecard lines | Readable, player-editable | Slow, requires inventory permissions, creates asset spam |
| Inventory items | Familiar | Heavy, slow to update, hard to version |
| External server | Unlimited storage | Requires HTTP-out, reliability and privacy concerns |

The final choice is recorded in the [modern SL persistence fixture](../research/experiments.md#e05-modern-sl-persistence-fixture) and must respect the [platform baseline](../second-life/platform-baseline.md).

## Genetics and trait system

Genetics turn stored strings into visible creatures. A minimal schema contains:

- **Genotype string(s)** — encoded dominant/recessive pairs for color, pattern, size, ears, tail, etc.
- **Breeding function** — combines two parent genotypes with mutation and crossover rules.
- **Phenotype resolver** — maps the resulting genotype to mesh UUIDs, texture UUIDs, animation overrides, and size/position offsets.
- **Visual mapper** — the render module applies the resolved UUIDs to child prims, changes face textures, or swaps meshes.

Keep genotype and phenotype separate: the engine only breeds genotypes; the renderer only reads phenotypes. This makes adding new visual parts possible without rewriting inheritance logic.

## HUD and owner UX

Owner interaction is usually mediated by `llDialog` menus and a private listener channel. A well-behaved engine:

- Uses a randomly offset or owner-key-derived channel to avoid crosstalk.
- Checks `llDetectedKey`/`llListen` origin before acting on commands.
- Offers actions: status, feed, breed, rename, info, update.
- Sends update notices on a known broadcast channel so the HUD can reflect state in real time.
- Respects permissions: only the owner or an allowed group can trigger high-value actions.

HUD scripts should be thin clients: they request state from the pet and display it, rather than storing authoritative state themselves.

## Debug and QA workflow

Test the engine inside the [in-world fixture](../projects/in-world-fixture.md) before any release. A typical QA pass:

1. Rez a fresh pet and verify initial state values.
2. Let one full timer cycle run and confirm hunger/energy/age tick correctly.
3. Trigger feed, breed, and life-stage events manually and observe state transitions.
4. Take the object into inventory and rez it again; confirm persistence restored.
5. Reset the root script and confirm state reloads from the persistence layer.
6. Run two pets side by side and verify breeding handshake, cooldown, and offspring genotype.
7. Capture an in-world screenshot for the evidence folder.

Log state to owner-only chat or a debug prim during development; remove or gate logs before shipping.

## Evidence and deliverables

When the lab produces working code, commit artifacts to the canonical evidence folder:

- `training/lsl/a05/scripts/` — the fixture script plus minimal engine modules (controller, render, sensor, HUD relay).
- `training/lsl/a05/notes.md` — architecture decisions, especially the persistence choice and genetics schema.
- `training/lsl/a05/inworld-test.png` — proof the engine runs on the test parcel.

Long-form engine documentation should live here, updated as each module lands in git.

## Current blockers

This page remains a planning stub until the following preconditions are met:

- [ ] The lab produces at least one working fixture script.
- [ ] A genetics schema is drafted, even as a markdown spec.
- [ ] The Linkset Data versus alternatives decision is recorded from the persistence experiment.

Do not author final engine docs outside git; add sections here as code and test evidence land.

## Do

1. Create or rez the test linkset on the in-world fixture parcel.
2. Place the controller script in the root prim and render/sensor/HUD scripts in child prims.
3. Configure Linkset Data keys for hunger, energy, age, life stage, and breeding cooldown.
4. Start the timer loop and verify state ticks on each cycle.
5. Manually trigger feed, breed, and stage-advance events; observe state transitions and visual updates.
6. Derez and rez the object; confirm persistence restores the previous state.
7. Run two pets through a breeding handshake and validate offspring genotype.
8. Capture an in-world screenshot and commit it to the evidence folder.

## Produce

| Artifact | Path |
|----------|------|
| Fixture and minimal engine modules | `training/lsl/a05/scripts/` |
| Architecture decision notes | `training/lsl/a05/notes.md` |
| In-world test proof | `training/lsl/a05/inworld-test.png` |

## Done when

- [ ] At least one working fixture script exists in the evidence folder.
- [ ] A genetics schema is drafted in markdown or code.
- [ ] The Linkset Data versus alternatives decision is recorded.
- [ ] State restores correctly after derez/rez and script reset.
- [ ] Breeding handshake, cooldown, and offspring generation are verified in-world.

## Related

- [In-world fixture](../projects/in-world-fixture.md)
- [Modern SL persistence fixture](../research/experiments.md#e05-modern-sl-persistence-fixture)
- [Second Life platform baseline](../second-life/platform-baseline.md)
