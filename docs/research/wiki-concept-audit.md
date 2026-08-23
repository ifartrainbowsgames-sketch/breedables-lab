# Wiki & Academy Concept Audit — What Went Wrong

**Date:** 2026-08-23  
**Status:** DIAGNOSTIC — read this before any more wiki or tooling work  
**Author intent:** Stop building on a broken concept. Name the mistake. Redesign from truth.

---

## Executive summary

We built a **tool compliance registry** and labeled it an **Academy wiki**. Those are not the same product.

The MkDocs site looks like documentation, but it does not teach anything. It does not link to courses, videos, official manuals, or step-by-step paths. It mostly repeats license colors (`GREEN`, `YELLOW`, `EXPERIMENTAL`, `USE NOW`) that mean something to an internal R&D survey — not to a human trying to learn how to make breedables.

**The mistake is conceptual, not cosmetic.** Adding more tool pages will not fix it.

---

## What you asked for (actual goal)

You want a system that:

1. **Teaches** — training videos, curated links, “start here” paths per subject  
2. **Improves daily** — AI + Python research feeds the wiki, not just a static table  
3. **Is usable** — open the wiki, know where to learn Blender texturing, SL scripting, rigging, etc.  
4. **Connects to production** — what you learned maps to tools you use and experiments you run  

An **Academy wiki** is a **learning hub**. A **Librarian** is a **catalog robot**. We merged them without designing the learning layer.

---

## What we actually built

| Layer | What it is | What it gives you |
|-------|------------|-------------------|
| **Phase 0 survey** | Internal R&D license/readiness report | Good research for *which tools to approve* |
| **Librarian (SQLite + Slack)** | Tool registry + link checker + gaps queue | `/breedtool`, `/breedgaps` — lookup, not teaching |
| **MkDocs wiki (Phase 1)** | Markdown copy of survey + registry fields | Tables of status labels; almost no learning URLs |

The wiki home page says “Academy” and “Workflow” but **clicking Academy shows five track names and zero lessons**.

---

## Symptom 1: `GREEN / EXPERIMENTAL / USE NOW` feels wrong

### Why it feels weird

We are showing **two different classification systems at once**, often contradicting each other:

| Tool | Survey says | Librarian says | Wiki shows both |
|------|-------------|----------------|-----------------|
| Material Maker | GREEN / **USE NOW** | **EXPERIMENTAL** | Confusing |
| Ucupaint | GREEN / USE NOW | EXPERIMENTAL | Confusing |
| RetopoFlow | YELLOW / EXPERIMENT | REVIEWING + UNKNOWN | Confusing |

**Survey axis:** “Is this legally/technically safe and ready for our studio?” (GREEN/YELLOW/RED × USE NOW/EXPERIMENT/…)  

**Librarian axis:** “Where is this in *our approval workflow*?” (DISCOVERED → … → APPROVED)

These are **internal engineering labels**. They belong in a **registry admin view**, not on the front page of an Academy.

### The mistake

We copied R&D survey vocabulary into user-facing wiki pages without translation. A learner does not care about `GREEN`; they care about **“Watch this → do this exercise → you’re done with A01.”**

---

## Symptom 2: “Academy” with no training content

### Current `docs/academy/overview.md`

- Lists A01–A05 track **names**
- Says deliverables exist
- Points to empty `training/` folders in the repo
- **No YouTube links**
- **No Blender manual deep links**
- **No Poly Haven / ambientCG “how to use” guides**
- **No Second Life creator docs per topic**
- **No ordered lesson list**

### What an Academy page must contain (minimum)

For each track, e.g. **A01 Organic PBR Material**:

| Section | Example content |
|---------|-----------------|
| **Outcome** | “You can author one reusable skin material and upload PBR to SL.” |
| **Prerequisites** | Blender basics, SL PBR wiki page |
| **Learn** | 2–5 curated videos (title, URL, why this one) |
| **Read** | Official docs + our notes (Material Maker docs, SL PBR wiki) |
| **Do** | Step-by-step lab (E01 exercise) |
| **Submit** | What files to commit / demo in-world |
| **Tools used** | Link to registry entry (secondary, not primary) |

We have **none of the Learn / Read / Do structure** — only “Tools wiki → start with registry.”

### The mistake

Phase 0 survey **mentions** academy mapping (A01→E01) as a **one-line table**. We treated that table as if it were a curriculum. It was always a **placeholder intent**, never designed content.

---

## Symptom 3: Tool pages are not learning pages

### Current tool page pattern (e.g. Material Maker)

```
Survey rating | Librarian status | License | Repository
Role (one paragraph)
Breedables use (one paragraph)
Gap: /breedgaps may show...
Slack: /breedtool
```

### What’s missing

- Install / setup walkthrough  
- Link to official documentation  
- Link to best beginner tutorial (video or written)  
- Link to our academy lab that uses this tool  
- Example output screenshots / files  
- “Common mistakes” for breedables context  

A tool page in an **Academy** wiki should answer: **“How do I learn this for our project?”**  
We answered: **“What’s the license and approval status?”**

### The mistake

We used **DataHub / catalog page** template for **Udemy / wiki** content.

---

## Symptom 4: Three products collapsed into one nav tree

```
Home → Production → Tools → Material Maker (license table)
     → Academy → (empty tracks)
     → Research → (pointer to survey)
```

A learner opens **Production** expecting lessons. They get **compliance metadata**.

A researcher opens **Academy** expecting curriculum. They get **experiment IDs**.

### The mistake

**Single MkDocs nav** serves three audiences without separating:

1. **Learners** (Academy — videos, paths, labs)  
2. **Operators** (Librarian/Slack — lookup, gaps)  
3. **Reviewers** (R&D — licenses, promotion, experiments)  

---

## Symptom 5: “Daily AI + Python improvement” is not wired

The roadmap promised:

> discover → research → approve → publish → repeat

What runs daily today:

- Slack bot **if you keep PowerShell open**
- Manual `/breedgaps`
- **No** auto-export to wiki
- **No** research queue for AI
- **No** video/link ingestion
- **No** Canvas or wiki sync

The **automation story** was Phase 2+. The **Academy content story** was never Phase 1 — but we shipped Phase 1 *looking* like an Academy. That’s the bait-and-switch feeling.

---

## Root cause — where the mistake happened

### Timeline of the error

1. **Phase 0** correctly produced an **internal tool survey** (license + readiness). Good artifact for R&D.  
2. **Librarian V1** correctly implemented **registry + Slack lookup**. Good artifact for ops.  
3. **Phase 1 wiki** incorrectly assumed: *“Split the survey into pages = usable wiki.”*  
4. We added **Academy** and **Roadmap** nav labels without **any learning content model**.  
5. User expectation: **“Wiki for Academy with training videos and links.”**  
6. Delivered: **“Registry status pages with GREEN/EXPERIMENTAL.”**

**The fork in the road:** We optimized for **approval workflow documentation** when the user needed **learning pathway documentation**. Same repo, wrong product.

---

## What is NOT wrong (keep these)

Do **not** throw away:

| Asset | Keep because |
|-------|----------------|
| Phase 0 survey | Solid R&D source of truth for tool *evaluation* |
| Librarian + Slack | Works; good for `/breedtool`, `/breedgaps`, discovery queue |
| MkDocs infrastructure | Good *publisher* — wrong *content model* so far |
| Experiment definitions E01–E05 | Good lab *ideas* — need to become academy *labs* |
| Promotion rules | Good for *reviewers* — hide from learners |

Separate **content** from **delivery**. Delivery (MkDocs, GitHub Pages, Python) is fine. Content model is broken.

---

## Design principles for the redesign

### Principle 1: Two wikis, one repo (or two nav roots)

| Wiki | Audience | Top-level nav |
|------|----------|----------------|
| **Academy** | Humans learning | Tracks → Lessons → Labs |
| **Studio registry** | Ops + R&D | Tools → License → Status → Gaps |

Learners never see `GREEN/EXPERIMENTAL` on lesson pages. Reviewers get a registry view without video clutter.

### Principle 2: Lesson page schema (mandatory fields)

Every lesson `.md` must include:

```markdown
## Outcome
## Prerequisites
## Watch (videos with URLs)
## Read (official docs + our notes)
## Do (hands-on steps)
## Produce (artifacts)
## Tools (links to registry — optional footer)
```

No lesson ships without at least **one Watch** and **one Read** link.

### Principle 3: Registry labels stay in the registry

- Slack + Librarian: keep `EXPERIMENTAL`, `USE_NOW`, commercial type  
- Academy tool footer: plain language — “Studio status: under evaluation”  
- Survey GREEN/YELLOW/RED: **reviewer docs only** (`research/licenses/` or registry admin)

### Principle 4: Videos are first-class data

Not prose mentions — structured records:

| field | example |
|-------|---------|
| `title` | “Blender PBR basics for game assets” |
| `url` | YouTube / Blender official |
| `subject` | A01, texturing, rigging |
| `level` | beginner |
| `curated_by` | human / AI-assisted |
| `last_checked` | date |

Librarian V1.1 “YouTube registry” exists in roadmap — should be **Phase 1b**, not Phase 4, if Academy is the goal.

### Principle 5: AI daily loop targets *lesson gaps*, not only *tool gaps*

| Old gaps command | New gaps command |
|------------------|------------------|
| “Material Maker not approved” | “A01 has zero videos” |
| “RetopoFlow license unknown” | “A03 lab steps missing” |
| “HTTP 200” | “SL PBR wiki link broken” |

Python finds **missing learning content**. AI fills drafts. Human approves. Git publishes.

---

## Proposed information architecture (replacement)

```
docs/
  academy/                    ← PRIMARY for humans
    index.md                  ← “Start here” by role
    tracks/
      a01-organic-pbr/
        index.md              ← track overview
        lesson-01-watch.md
        lesson-02-lab-e01.md
    resources/
      videos.md               ← master video index by subject
      official-docs.md        ← SL wiki, Blender manual, etc.

  studio/                     ← SECONDARY for ops (rename from production/)
    registry/                 ← tool entries (license, status) — NOT lesson pages
    experiments/              ← E01–E05 specs for reviewers
    promotion-rules.md

  secondlife/                 ← platform reference (keep)

research/
  reports/                    ← deep R&D (Phase 0 stays here)
  licenses/                   ← reviewer-only license notes
```

**Delete or demote:** tool pages that look like academy content but only show status tables.

---

## Immediate actions (before writing more pages)

1. **Freeze** current tool-page template — no more `Survey rating | Librarian status` on learner paths.  
2. **Approve this audit** — agree the product is Academy-first, registry-second.  
3. **Pick one track** — implement **A01 end-to-end** as the template (videos, links, lab, produce).  
4. **Redesign MkDocs nav** — Academy tab first; Studio/Registry hidden under “For maintainers”.  
5. **Extend Librarian or new `academy.yaml`** — structured video/link records, not only SQLite tools.  
6. **Rewrite `/breedgaps`** — optional future: content gaps, not only approval gaps.

---

## Success criteria for the redesign

We know the redesign worked when:

- [ ] A new team member opens the wiki and finds **watch + read + do** for A01 without asking in Slack  
- [ ] No `GREEN/EXPERIMENTAL` on academy lesson pages  
- [ ] Every track has ≥3 curated external links (video or official doc)  
- [ ] Tool registry is reachable from lessons but is not the main nav  
- [ ] `/breedgaps` or equivalent can report **“A04 missing lab steps”**  
- [ ] Phase 0 survey remains available for **reviewers**, not confused with **curriculum**

---

## Decision required

**Question for the studio:**

> Is Breedables Lab primarily a **learning academy with a tool catalog attached**, or a **tool catalog with academy aspirations**?

Everything built so far assumes the second. Your feedback says you need the **first**.

**Recommended answer:** Academy-first. Registry serves the academy; not the reverse.

---

## Next document (after this audit is accepted)

Create: `research/reports/2026-08-23-academy-redesign-spec.md`

Contents:

- Final nav structure  
- Lesson template (copy-paste)  
- A01 full curriculum draft (real URLs)  
- Librarian vs Academy data split  
- Migration plan for existing markdown  

**Do not implement until this audit is agreed.**

---

## References

- [Phase 0 survey](phase-0-survey.md) — good R&D; wrong shape for Academy  
- [Studio roadmap](../studio-roadmap.md) — phases assume registry-first; needs revision  
- [Academy overview (current)](../academy/overview.md) — empty shell  
- [Librarian README](https://github.com/ifartrainbowsgames-sketch/breedables-lab/blob/feature/studio-librarian-v1/tools/librarian/README.md) — working ops layer  
