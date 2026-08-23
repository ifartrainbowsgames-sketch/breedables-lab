---
title: "TripoSR"
section: research
type: candidate
---
# TripoSR

| Field | Value |
|-------|-------|
| **Commercial type** | OPEN_SOURCE |
| **Code license** | MIT |
| **Model license** | MIT (per upstream repo) |
| **Category** | 3D AI |
| **Repository** | [VAST-AI-Research/TripoSR](https://github.com/VAST-AI-Research/TripoSR) |

## Role

Fast single-image 3D reconstruction with optional texture baking.

## Breedables use

Concept / blockout / reference geometry generation — **never** assumed production-ready without cleanup and retopology.

## Decision

Cleanest image-to-3D baseline in Phase 0 survey; benchmark first in [E02](../experiments.md).

!!! warning "Output rights"
    Generated-output rights still need workflow-specific verification before commercial approval.

## Evidence

| Field | Link |
|-------|------|
| Primary video | [TripoSR image → 3D workflow](https://www.youtube.com/watch?v=e2UeHwzncHA) |
| Interactive demo | [Hugging Face Space](https://huggingface.co/spaces/stabilityai/TripoSR) |
| Official docs | [TripoSR GitHub](https://github.com/VAST-AI-Research/TripoSR) |
| Academy track | A-model (research) |
| Evidence folder | `training/modeling/triposr/` |

Complete E02 table before using outputs in breedables pipeline.

## Librarian

```powershell
python -m librarian.cli show --query "triposr"
```
