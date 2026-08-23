---
title: "Breedables Engineering"
section: engineering
type: index
question: "How does the breedable system actually work?"
---
# Breedables Engineering

!!! abstract "This section answers one question"
    *How does the breedable system actually work?*

The runtime system — LSL scripting, genetics and inheritance, lifecycle
and needs, persistence, movement and animation control, HUD and updater. This is
the software side of a breedable, not the art side.

## Topics

| Page | What it covers |
|------|----------------|
| [LSL & engine overview](lsl-engine.md) | Runtime architecture and state machines |

## Software

| Tool | Licence & role |
|------|----------------|
| [Linden Scripting Language](lsl-engine.md) | Official LSL portal and reference |
| [Linkset Data](../second-life/platform-baseline.md) | Modern persistence primitive |

## Hands-on projects

Each project ends in committed evidence, not a watched video.

| Project | Outcome |
|---------|---------|
| [In-world fixture](projects/in-world-fixture.md) | Minimal rezzable breedable with a persistence test |

## Pipeline stages owned by this section

These are the production-line stages this section is responsible for.

### Stage 11 — LSL / breedables engine scripting

Runtime logic: breeding, aging, movement, food, persistence, updates — modular engine in `scripts/`.

!!! tip "Studio pick"
    **In-viewer + git** for script modules. No paid tool required.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **SL script editor** | in viewer | Deploy LSL |
    | **lsl-definitions** | GitHub | API accuracy |
    | **VS Code + LSL syntax** | community extensions | External editing |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | *(none required)* | | |

**How we use it**

- Modern patterns: **Linkset Data**, Animesh, PBR — study XS Pet for lessons, do not copy blindly  
- Canonical definitions: [lsl-definitions](https://github.com/secondlife/lsl-definitions)  
- Fake-trait fixture in E05 before species-specific genetics

**What to complete**

- Studio labs: [In-world fixture](../engineering/projects/in-world-fixture.md)  
- Experiments:   
- Produce: LSL modules + test harness in-world

**Evidence folder** — `scripts/`, `training/lsl/a05/`  
**Related pages** — [In-world fixture](../engineering/projects/in-world-fixture.md) · [LSL engine overview](../engineering/lsl-engine.md)

### Stage 12 — Genetics & data definitions

Data-driven **traits, colors, rarity, mutations** separate from code — enables balance without rewriting engine.

!!! tip "Studio pick"
    **Git-tracked data files** as source of truth; spreadsheets for draft only.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Git + text editor** | — | Schema and tables |
    | **Python validation scripts** | `pipeline/validation/` | Schema checks |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Spreadsheets** (Excel/Sheets) | — | Design-phase tuning — export to git |

**How we use it**

- JSON/YAML or similar in `data/genes/`, `data/traits/`, etc.  
- Engine reads definitions; designers tune tables

**What to complete**

- Read: `data/README.md`  
- Do: design fake-trait tables for E05 fixture

**Evidence folder** — `data/`  
**Related pages** — [Production line](../pipeline.md) · [Decision model](../research/decision-model.md)

### Stage 13 — HUD & player UI

In-world menus, breeding UI, status displays, updater flows — packaged in `hud/`.

!!! tip "Studio pick"
    Build custom HUD art in Blender + our PBR pipeline for consistency.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Blender** | — | HUD texture assets |
    | **SL UI primitives** | wiki | Buttons, dialogs |

=== "Paid tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **FUI designers** | various | Optional texture packs |

**How we use it**

- LSL + SL UI conventions  
- Separate from creature body scripts where possible

**What to complete**

- *(Track A-hud — to define after A05)*

**Evidence folder** — `hud/`  
**Related pages** — [Production line](../pipeline.md) *(A-hud track planned)*

### Stage 15 — Release & maintenance

Ship versioned packages to players; document changes; support updates via engine updater module.

!!! tip "Studio pick"
    Git tags + markdown release notes tied to test evidence.

=== "Free tools"

    | Tool | Link | Best for |
    |------|------|----------|
    | **Git tags** | GitHub | Version markers |
    | **MkDocs** | this wiki | Player-facing docs *(if public)* |

**How we use it**

- Release notes in `releases/`  
- Creature-specific packages in `creatures/<species>/`  
- Announce in `#releases` with links to evidence-tested builds

**Evidence folder** — `releases/`, `creatures/`  
**Related pages** — [Promotion rules](../research/promotion-rules.md) · [Studio roadmap](../roadmap.md)

---

## Academy track index (learning paths)

| Track | Stage(s) | Status |
|-------|----------|--------|
| **A01** Organic PBR Material | 4–5, 10 | Spec in production line — **fill videos next** |
| **A02** Layered Texture Refinement | 4–5 | Same |
| **A03** Organic Retopology | 3 | Same |
| **A04** Rig + Two Animations | 7–8 | Same |
| **A05** SL Creature Fixture | 10–11, 14 | Same |
| **A00** Concept *(planned)* | 1 | Template only |
| **A-model** Modeling *(planned)* | 2 | Template only |
| **A-export** SL export *(planned)* | 9 | Template only |
| **A-data** Genetics *(planned)* | 12 | Template only |
| **A-hud** HUD *(planned)* | 13 | Template only |

Every track page uses **Watch · Read · Explain · Do · Produce · Completed when** — see [Academy overview](index.md).

---

## Tool comparison rules (studio-wide)

When writing “which is better”:

1. State **breedables-specific** criterion (SL PBR, quadruped rig, commercial license, etc.)  
2. List **free option first**  
3. Paid only if it wins on measured evidence from an experiment  
4. Link to **E01–E05** or `research/experiments/` result  
5. **Never** use GREEN/YELLOW/RED in learner-facing text  

---

## Next actions (in order)

1. **Approve** this production line as the master map  
2. Create `docs/academy/resources/videos.md` — start curating real URLs per stage  
3. Build **A01 lesson page** first (full Watch/Read/Do/Produce)  
4. Update Librarian `/breedtool` to link lesson + evidence path  
5. Add E01 evidence folder with first complete artifact package  

---

## References

- [Software & Tools](index.md)  
- [Blender Foundations](../modeling/blender/index.md)  
- [Tutorial arsenal](index.md)  
- [Experiments](../research/experiments.md)  
- [Second Life baseline](../second-life/platform-baseline.md)  
- [Phase 0 survey](../research/index.md)

---

## For maintainers — stage template

??? note "Copy this skeleton when adding or updating a stage"

    Every stage answers the same five questions in the same order, so readers can
    scan any stage the way they scanned the last one. Use **bold labels**, not
    `###` headings — headings here would flood the table of contents.

    ```markdown
    ## Stage N — Name

    One paragraph: why this stage exists for Second Life breedables.

    !!! tip "Studio pick"
        What we chose and **why** — cite evidence when we have it.

    === "Free tools"

        | Tool | Link | Best for |
        |------|------|----------|

    === "Paid tools"

        | Tool | Link | Best for | Cost note |
        |------|------|----------|-----------|

    **How we use it**

    - Studio workflow rules

    **What to complete**

    - Watch / Read / Do / Produce

    **Evidence folder** — `path/in/repo/`
    **Related pages** — links to lessons and studio labs
    ```

    **Rule:** a studio pick is only valid with evidence behind it — a link, an
    artifact, or a measurement. See [Academy overview](index.md).
