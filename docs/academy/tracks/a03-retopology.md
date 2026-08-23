# Retopology

![Blender](../../assets/inline/blender.png){ width="80" }

**Studio lab** · Animation-ready mesh for breedables  
**Evidence folder:** `training/modeling/a03/` *(internal id A03)*

!!! danger "Prerequisites"
    Complete **[Blender lessons 3–5](../software/blender/b03-mesh-modeling.md)** (modeling through retopology) first.

**Production stage:** Retopology & LOD  
**Experiment:** [E03 Organic retopology benchmark](../../production/experiments.md#e03-organic-retopology-benchmark)  
**Primary tools:** Blender, [RetopoFlow](../../production/tools/retopoflow.md) (license audit required)

## Outcome

Retopologize a high-poly sculpt into **animation-ready topology** with a documented poly budget suitable for breedables (Animesh / uploaded mesh limits).

---

## Watch

| Topic | Video | Notes |
|-------|-------|-------|
| RetopoFlow 4 setup | [Installation & RetopoFlow mode](https://www.youtube.com/watch?v=Ds5Soybs610) | CG Cookie / Orange Turbine |
| Blender retopo concepts | [Blender manual — retopology](https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html) | Native tools baseline |

→ [Video library — retopo (all tools)](../resources/video-library.md#blender)

<div class="wiki-video" markdown="0">
<iframe src="https://www.youtube-nocookie.com/embed/Ds5Soybs610" title="RetopoFlow installation and mode" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

---

## Read

| Source | Link |
|--------|------|
| RetopoFlow docs | [docs.retopoflow.com](http://docs.retopoflow.com/) |
| RetopoFlow GitHub | [CGCookie/retopoflow](https://github.com/CGCookie/retopoflow) |
| License notes | [RetopoFlow tool page](../../production/tools/retopoflow.md) |

---

## Explain — Breedables workflow

1. Start from a high-poly organic sculpt (creature head/body block — studio test asset OK).
2. Set **target poly count** before retopo (document in notes — e.g. 5k / 10k / 15k tiers).
3. Retopo with edge flow for mouth, eyes, limb joints if present.
4. Verify deformation with a quick bone test or shape keys before calling done.
5. Hand off clean mesh to UV + texturing (A01) or rigging (A04).

**License:** RetopoFlow repo is GPL; bundled assets may differ — read tool page before production approval.

---

## Do — Hands-on lab

1. Import or open high-poly source in Blender.
2. Retopo to target poly budget (RetopoFlow or native — document tool used).
3. Save retopo mesh + reference sculpt in `source/`.
4. Export wireframe renders from front/side.
5. Fill E03 measurement table (time, poly count, deformation notes).

---

## Produce — Required artifacts

| Artifact | Path |
|----------|------|
| High-poly reference | `training/modeling/a03/source/sculpt.blend` |
| Retopo result | `training/modeling/a03/retopo.blend` |
| Wireframe proof | `training/modeling/a03/wireframe.png` |
| Lab notes (poly count, time, tool) | `training/modeling/a03/notes.md` |

---

## Sign-off checklist

- [ ] Poly count documented and within studio target
- [ ] Edge flow checked at deformation points
- [ ] E03 row completed in experiments doc
- [ ] License note reviewed if RetopoFlow used

---

## Next track

[Rig + animation](a04-rig-animation.md)
