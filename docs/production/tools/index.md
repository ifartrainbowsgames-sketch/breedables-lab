# Tool registry

Curated tools in the Breedables Studio Librarian. Status reflects **our workflow**, not GitHub popularity.

| Tool | Category | Status | License | Link |
|------|----------|--------|---------|------|
| [Blender](blender.md) | 3D | USE NOW | GPL-3.0-or-later | [blender.org](https://www.blender.org/) |
| [Material Maker](material-maker.md) | Textures | EXPERIMENTAL | MIT | [GitHub](https://github.com/RodZill4/material-maker) |
| [Ucupaint](ucupaint.md) | Textures | EXPERIMENTAL | GPL-3.0 | [GitHub](https://github.com/ucupumar/ucupaint) |
| [TripoSR](triposr.md) | 3D AI | EXPERIMENTAL | MIT | [GitHub](https://github.com/VAST-AI-Research/TripoSR) |
| [RetopoFlow](retopoflow.md) | Retopology | REVIEWING | GPL-3.0 | [GitHub](https://github.com/CGCookie/retopoflow) |
| [Poly Haven](poly-haven.md) | Assets | USE NOW | CC0 | [polyhaven.com](https://polyhaven.com/) |
| [ambientCG](ambientcg.md) | Assets | USE NOW | CC0 | [ambientcg.com](https://ambientcg.com/) |

## CLI

```powershell
cd tools\librarian
.venv\Scripts\Activate.ps1
python -m librarian.cli list
python -m librarian.cli show --query "material"
python -m librarian.cli gaps
```

## Slack

```
/breedtool Material Maker
/breedstatus
/breedgaps
```

## More candidates

Ten additional tools from Phase 0 (not yet in the Librarian seed): **[Research candidates](research-candidates.md)** — DiffusedTexture, InstantMesh, Rigify, retargeting add-ons, and more.

Full survey: [Phase 0 report](../../research/phase-0-survey.md)
