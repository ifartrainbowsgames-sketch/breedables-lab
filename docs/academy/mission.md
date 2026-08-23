# Academy mission

**Status:** SOURCE OF TRUTH — read this before adding Academy pages  
**Last updated:** 2026-08-23

We are **not** eliminating the Academy. We are eliminating **meta-work** that does not serve production or education.

---

## Two equally important outputs

1. **Build** a real, reusable Second Life breedables production pipeline (Reference Creature vertical slice).
2. **Build** a genuinely useful professional 3D / texture Academy so a person can ask:

> *How do professional 3D creature artists actually work, what software do they use, what can I use for free, and where do I learn the entire workflow?*

…and get a **clickable curriculum**, not vague advice.

---

## What the Academy is NOT

- ❌ “Learn Blender” with no links  
- ❌ “Learn UV mapping” with no exercises  
- ❌ Registry status labels (`GREEN`, `EXPERIMENTAL`) on learner pages  
- ❌ Another AI dashboard, RAG bot, or crawler architecture  

Use the existing **Librarian + daily-wiki + webscreen + Kimi** stack to **populate** the Academy — do not replace it with new meta-systems.

---

## What the Academy IS

A **complete professional creature / 3D asset artist learning path** that:

1. Mirrors **real** current character/creature/game/VFX pipelines (validated against vendor docs, official training, schools like Gnomon, production breakdowns).
2. Shows **three routes** at every major stage when possible:
   - **A. Professional / studio route** (Maya, ZBrush, Substance, Mari, etc.)
   - **B. Free / open-source route** (Blender, Material Maker, Krita, etc.)
   - **C. Breedables Studio recommended route** (what we use now, and why — changes after experiments)
3. Provides **actual training**: official docs, beginner courses, verified video URLs, exercises, artifacts, PASS/FAIL criteria.
4. Teaches **correct general 3D production first**, then **Second Life adaptation** (LOD, PBR, Animesh, land impact, LSL) — not bad habits “because SL is limited.”

---

## Professional pipeline (validate & teach)

```text
REFERENCE / CONCEPT
  → BLOCKOUT
  → HIGH-POLY MODEL / SCULPT
  → RETOPOLOGY
  → UV
  → HIGH→LOW BAKING
  → TEXTURE / MATERIAL AUTHORING
  → LOOKDEV
  → RIGGING
  → SKINNING
  → ANIMATION
  → OPTIMIZATION / LOD
  → EXPORT
  → SECOND LIFE
  → IN-WORLD QA
```

Do **not** assume one program does everything. Show how **multi-tool** professional pipelines work.

→ [Pipeline stages (detail)](professional-workflow/pipeline-stages.md)  
→ [Role separation](professional-workflow/roles.md)  
→ [Software map by stage](professional-workflow/software-map.md)  
→ [Paid vs free matrix](professional-workflow/paid-vs-free-matrix.md)  
→ [Second Life adaptation](professional-workflow/second-life-adaptation.md)

---

## Training hard rule

A software page is **not complete** unless it provides an **actual learning route**:

| Required | Example |
|----------|---------|
| Official documentation | Blender Manual, Maya Help |
| Official beginner course | [Blender Fundamentals 4.5 LTS](https://www.blender.org/support/tutorials/) |
| Free video training | Direct playlist URL — never “search YouTube” |
| Beginner project | Named exercise + artifact path |
| Intermediate / production workflow | When available |
| Reference manual link | Searchable official docs |

→ [Software page standard](software/software-page-standard.md)  
→ [Complete workflow courses](resources/complete-courses.md)

---

## Artifact-based learning

**Every lesson produces something** in `training/`. Watching alone = incomplete.

| Stage | Example artifact |
|-------|------------------|
| Modeling | Clean blockout mesh |
| Sculpting | High-poly creature head |
| Retopology | Animation-ready low-poly |
| UV | Packed UV layout screenshot |
| Baking | Normal/AO maps without cage errors |
| Texturing | Base Color + Normal + Roughness (+ Metallic as needed) |
| Rigging | Deforming skeleton |
| Animation | Seamless idle or walk cycle |
| SL export | Upload-ready package + in-world screenshot |

Every practical lesson has **PASS / FAIL** criteria (see software pages and studio labs).

---

## Reference Creature = living laboratory

**BUILD → TEST → FAIL → SOLVE → DOCUMENT**

If the Reference Creature proves a tutorial is wrong, a tool exports badly, or a free alternative is inadequate — **update the Academy with evidence**. Academy and production reinforce each other.

---

## Learner journey (target)

```text
Enter knowing nothing
  → See what professional software exists
  → Understand what each tool is for
  → Choose free or paid with eyes open
  → Follow real videos + guides + exercises
  → Produce real artifacts
  → Learn the professional pipeline
  → Build a Second-Life-ready creature
```

---

## Where to start

| Audience | Page |
|----------|------|
| Complete beginner | [Start here](start-here.md) |
| “How pros work” | [Professional workflow](professional-workflow/index.md) |
| Free OSS path (our primary teach path) | [Blender Foundations](software/blender/index.md) |
| Tool-by-tool cards | [Software packages](software/packages/index.md) |
| Breedables proof projects | [Studio labs](start-here.md#layer-2-studio-labs-breedables-projects) |

---

## Related

- [Wiki concept audit](../research/wiki-concept-audit.md) — what went wrong before  
- [System build summary](../studio/system-build-summary.md) — automation vs Academy product  
- [Production line](production-line.md) — studio stage spec (maintainers)
