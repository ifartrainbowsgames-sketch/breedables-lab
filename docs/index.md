# Breedables Lab

Open-source-first production studio for building **Second Life breedables**.

!!! warning "Wiki-first"
    We are **building the complete wiki in this repo** first. Slack docs will be removed/archived; Slack will only **link** to the wiki later. See **[Wiki-first strategy](studio/wiki-first-strategy.md)**.

## Workflow

**Research → Learn → Experiment → Build → Test → Release**

This site is the studio wiki. Facts live in the [Librarian](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/tools/librarian) registry; readable specs and decisions live here.

## Quick links

| Resource | Description |
|----------|-------------|
| [Studio roadmap](studio-roadmap.md) | Phased plan and recommended open source stack |
| [Decision model](production/decision-model.md) | License + readiness classification |
| [Tool registry](production/tools/index.md) | Curated tools with links and status |
| **[Production line](academy/production-line.md)** | Full pipeline: model → texture → rig → SL |
| [Experiments](production/experiments.md) | E01–E05 benchmark plan |
| [Second Life baseline](secondlife/platform-baseline.md) | PBR, Animesh, Linkset Data, LSL |
| [Academy](academy/overview.md) | Training tracks tied to experiments |
| [Librarian](https://github.com/ifartrainbowsgames-sketch/breedables-lab/tree/feature/studio-librarian-v1/tools/librarian) | Python CLI + Slack bot (`/breedtool`, `/breedgaps`) |

## Local preview

```powershell
cd breedables-lab
py -3.11 -m venv .venv-docs
.venv-docs\Scripts\Activate.ps1
pip install -r requirements-docs.txt
mkdocs serve
```

Open http://127.0.0.1:8000

## Published site

After push to GitHub, the workflow [`.github/workflows/docs.yml`](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/feature/studio-librarian-v1/.github/workflows/docs.yml) deploys to:

**https://ifartrainbowsgames-sketch.github.io/breedables-lab/**

Enable once in GitHub: **Settings → Pages → Build and deployment → Source: Deploy from branch `gh-pages`**.

## Slack

With the Librarian bot running, use in a **channel** (not the bot DM):

- `/breedstatus` — registry counts by status
- `/breedtool Blender` — tool lookup
- `/breedgaps` — review queue
