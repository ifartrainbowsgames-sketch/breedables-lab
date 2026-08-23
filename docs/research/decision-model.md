---
title: "Decision model"
section: research
type: reference
---
# Decision model

Every candidate tool or asset is classified on **two independent axes**.

## License / commercial safety

| Rating | Meaning |
|--------|---------|
| **GREEN** | Clearly commercial-friendly for our intended use |
| **YELLOW** | Useful, but dependencies, model weights, assets, or territorial terms need review |
| **RED** | Not suitable for commercial production under current terms |

!!! warning "Separate audits required"
    Open-source **code**, **model weights**, **bundled assets**, **generated outputs**, and **dependency licenses** must be audited separately. A GitHub license field is evidence, not a full commercial-rights audit.

## Readiness

| Status | Meaning |
|--------|---------|
| **USE NOW** | Species-independent and practical today |
| **EXPERIMENT** | Requires measured testing before approval |
| **USE LATER** | Depends on eventual species or product design |
| **RESEARCH ONLY** | Learning value only; not a production dependency |

## Librarian mapping

The [Studio Librarian](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/tools/librarian) uses related enums:

**Commercial type:** `OPEN_SOURCE`, `FREE_CLOSED_SOURCE`, `FREEMIUM`, `PAID_COMMERCIAL`, `RESEARCH_ONLY`, `OPEN_CONTENT_CC0`, `UNKNOWN`

**Workflow status:** `DISCOVERED`, `REVIEWING`, `EXPERIMENTAL`, `USE_NOW`, `USE_LATER`, `APPROVED`, `REJECTED`, `SUPERSEDED`

Commercial type and workflow status are **intentionally separate**. A project can be open source while still experimental for our pipeline.

## Source

Extracted from the [Phase 0 toolbox survey](index.md).

## Writing a tool comparison

Whenever a page says one tool is better than another:

1. State the **breedables-specific** criterion — SL PBR support, quadruped rig,
   commercial licence, land impact, and so on. Not general praise.
2. List the **free option first**.
3. Recommend the paid option **only** when it wins on measured evidence.
4. Link the [experiment](experiments.md) or result folder that evidence came from.
5. Never use GREEN / YELLOW / RED status colours in learner-facing text — those
   belong in the maintainer [tool registry](tool-registry.md).

