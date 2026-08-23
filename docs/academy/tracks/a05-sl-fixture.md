# In-world fixture

![Second Life](../../assets/inline/second-life.png){ width="80" }

**Studio lab** · Upload, LSL, and persistence test in Second Life  
**Evidence folder:** `training/lsl/a05/` *(internal id A05)*

!!! danger "Prerequisites"
    Complete **[Blender lesson 10](../software/blender/b10-export-to-sl.md)** (export) and the **[earlier studio labs](a01-organic-pbr.md)** first.

**Production stage:** LSL, persistence, in-world test  
**Experiment:** [E05 Modern SL persistence fixture](../../production/experiments.md#e05-modern-sl-persistence-fixture)  
**Primary tools:** Second Life viewer, LSL, [platform baseline](../../secondlife/platform-baseline.md)

## Outcome

Deploy a **minimal breedable fixture** in-world: rezzable mesh + animations + simple state script proving a hunger/energy (or similar) loop with persistence test.

---

## Watch

| Topic | Video | Notes |
|-------|-------|-------|
| LSL basics | [LSL Portal tutorials](https://wiki.secondlife.com/wiki/LSL_Portal) | Start with Hello Avatar examples |
| Animesh in SL | [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) | Required for animated creature target |
| Mesh upload | [Gaia Clift — SL mesh upload](https://www.youtube.com/watch?v=uZ5KyLvivkw) | Pair with [platform baseline](../../secondlife/platform-baseline.md) |

→ [Video library — Second Life creator](../resources/video-library.md#second-life)

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/uZ5KyLvivkw" title="Gaia Clift SL mesh upload" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

## Read

| Source | Link |
|--------|------|
| LSL reference | [create.secondlife.com/script](https://create.secondlife.com/script/lsl-reference/) |
| Linkset Data | [`llLinksetDataWrite`](https://create.secondlife.com/script/lsl-reference/functions/lllinksetdatawrite/) |
| PBR upload | [PBR Materials wiki](https://wiki.secondlife.com/wiki/PBR_Materials) |
| Engine overview (stub) | [LSL engine overview](../../studio/lsl-engine-overview.md) |
| Production line — LSL stage | [Production line](../production-line.md) |

---

## Explain — Breedables workflow

1. Upload mesh + PBR materials from A01–A04 pipeline (subset OK for fixture).
2. Upload animations from A04; configure Animesh if used.
3. Write **minimal LSL** — states: e.g. `IDLE`, `HUNGRY`, `EATING` with timer transitions.
4. Test **Linkset Data** write/read across script reset and re-rez (E05).
5. Capture in-world proof on studio test parcel — no production genetics yet.

**Do not** copy legacy XS Pet scripts wholesale — use as architectural reference only ([platform baseline](../../secondlife/platform-baseline.md)).

---

## Do — Hands-on lab

1. Package linkset: mesh + textures + animations + scripts.
2. Implement fixture script with debug chat or hover text for state visibility.
3. Run E05 test matrix: reset, rez, region restart simulation if possible.
4. Screenshot + short notes on persistence outcome.
5. File follow-ups for [LSL engine overview](../../studio/lsl-engine-overview.md).

---

## Produce — Required artifacts

| Artifact | Path |
|----------|------|
| LSL scripts | `training/lsl/a05/scripts/` |
| Object setup notes | `training/lsl/a05/notes.md` |
| In-world screenshot | `training/lsl/a05/inworld-test.png` |
| Optional screen recording | `training/lsl/a05/inworld-test.mp4` |
| E05 results | Copy summary into [experiments](../../production/experiments.md#e05-modern-sl-persistence-fixture) |

---

## Sign-off checklist

- [ ] Fixture rezzes and animates at least one loop from A04
- [ ] State machine visible to tester (chat/HUD/debug)
- [ ] Linkset Data test results documented
- [ ] E05 table filled
- [ ] Capstone: A01–A05 evidence paths linked in notes

---

## Graduation

Completing A05 with evidence means the **Academy Phase 0 path** is done. Next: species-specific production or A-model / A-export tracks on the [production line](../production-line.md).
