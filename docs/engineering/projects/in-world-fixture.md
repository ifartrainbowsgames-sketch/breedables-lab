---
title: "In-world fixture"
section: engineering
type: project
---

# In-world fixture

!!! info "About this page"
    **Prerequisites** — Lesson 10 — Exporting to Second Life and earlier studio labs  
    **Evidence folder** — `training/lsl/a05/`

Deploy a minimal breedable fixture in Second Life: a rezzable mesh plus a simple LSL state machine that proves a hunger/energy loop with a persistence test. This revision sharpens the project because the evidence folder training/lsl/a05/ is currently empty: the first artifact, exact filenames, and pass conditions are now explicit.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Second Life Viewer | [Second Life Viewer](https://secondlife.com/support/downloads/) | Uploading mesh, rezzing the fixture, and running LSL scripts in-world |
    | VS Code | [VS Code](https://code.visualstudio.com/) | Editing LSL scripts with syntax highlighting |

## Watch

| Topic | Video | Why this one |
|---|---|---|
| LSL basics | [LSL Portal tutorials](https://wiki.secondlife.com/wiki/LSL_Portal) | Start with the Hello Avatar and timer/state examples before writing the fixture script |
| Animesh in SL | [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) | Required background if the fixture uses an animated creature target |
| Mesh upload | [Gaia Clift — SL mesh upload](https://www.youtube.com/watch?v=uZ5KyLvivkw) | Pair with the platform baseline for a clean upload workflow |

## Read

| Source | Covers |
|---|---|
| [LSL reference](https://create.secondlife.com/script/lsl-reference/) | Syntax and built-in functions for state machines, timers, and Linkset Data |
| [Linkset Data write](https://create.secondlife.com/script/lsl-reference/functions/lllinksetdatawrite/) | How to persist a key/value pair across script resets |
| [Second Life platform baseline](https://ifartrainbowsgames-sketch.github.io/breedables-lab/second-life/platform-baseline/) | Technical limits and naming conventions for breedables in SL |

## Evidence folder status

The evidence folder `training/lsl/a05/` is **currently empty**. Do not invent screenshots, scripts, or test results. Use this page to create the first artifact, then commit only what you actually produce.

## First artifact: minimal state machine script

Before adding mesh or animations, prove that an LSL object can store and recover a simple numeric value across a script reset. The first artifact is a single script named `fixture-state-machine.lsl` inside `training/lsl/a05/scripts/`.

Required behavior:
- On rez, read a stored `hunger` value from Linkset Data using `llLinksetDataRead`.
- If no value exists, initialize `hunger` to `0`.
- On a timer, increment `hunger` by `1` every 30 seconds.
- When `hunger` reaches `5`, transition to a `HUNGRY` state and say so on channel 0.
- When `hunger` is reset to `0` via chat command `/5 reset`, save the value with `llLinksetDataWrite` and announce the new state.
- After a manual script reset, the object must remember the last saved `hunger` value.

Keep debug output visible in local chat or hover text so the tester can verify each transition without guessing.

## Do — hands-on lab

Follow these exact steps. Record the observed behavior in `training/lsl/a05/notes.md`; do not predict the result.

## Produce — required artifacts

Commit only files you actually create. Place every artifact under `training/lsl/a05/`.

## Sign-off checklist

Tick an item only when you have evidence in the folder above. Every box needs a matching filename.

## Graduation

When the checklist above is complete, the Phase 0 engineering fixture is proven. The next decision is either a species-specific production track or the [LSL & breedables engine overview](../lsl-engine.md) design pass.

## Do

1. Create `training/lsl/a05/scripts/fixture-state-machine.lsl` with the required hunger/energy state machine and Linkset Data persistence.
2. Create a simple SL object (one or more prims, or a basic mesh cube) and drop the script into the root prim. Name the object `BreedablesLab-A05-Fixture` in your inventory.
3. Rez the object in a sandbox or studio test parcel. Record the local-chat output for the first 5 timer ticks in `training/lsl/a05/notes.md`.
4. Send the chat command `/5 reset` and record the resulting local-chat output.
5. Open the script editor, click Reset, close the editor, and record whether the object restored the saved `hunger` value or restarted from `0`.
6. If the value was not restored, capture the exact error or behavior in `training/lsl/a05/notes.md` and file a follow-up issue against [LSL & breedables engine overview](../lsl-engine.md).
7. Take a screenshot of the rezzed object showing hover text or local chat proving the current state. Save it as `training/lsl/a05/inworld-test.png`.

## Produce

| Artifact | Path |
|----------|------|
| LSL state machine script | `training/lsl/a05/scripts/fixture-state-machine.lsl` |
| Object setup and test notes | `training/lsl/a05/notes.md` |
| In-world test screenshot | `training/lsl/a05/inworld-test.png` |
| Optional screen recording | `training/lsl/a05/inworld-test.mp4` |
| Experiment E05 summary | `training/lsl/a05/e05-results.md` |

## Done when

- [ ] `training/lsl/a05/scripts/fixture-state-machine.lsl` exists and compiles without errors.
- [ ] `training/lsl/a05/notes.md` contains the exact local-chat output for the first 5 timer ticks.
- [ ] The `/5 reset` command output is recorded in `training/lsl/a05/notes.md`.
- [ ] After a manual script reset, the object either restores the saved hunger value or the failure is documented with an exact repro step.
- [ ] `training/lsl/a05/inworld-test.png` shows the rezzed object and a visible state indicator (hover text or chat).
- [ ] `training/lsl/a05/e05-results.md` exists and links to [Experiment E05](../../research/experiments.md#e05-modern-sl-persistence-fixture).

## Related

- [LSL & breedables engine overview](../lsl-engine.md)
- [Experiment E05 — Modern SL persistence fixture](../../research/experiments.md)
- [Lesson 10 — Exporting to Second Life](../../second-life/export-and-upload.md)
- [Second Life platform baseline](../../second-life/platform-baseline.md)
- [Production pipeline](../../pipeline.md)
- [Rig + animation](../../rigging-animation/projects/rig-and-animation.md)
