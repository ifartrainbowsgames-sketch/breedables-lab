# Build plan

!!! info "About this page"
    **Date** — 2026-08-23  
    **Status** — LIVING ROADMAP  
    **Owner** — Academy  
    **Related** — [Software & Tools](index.md) · [Blender Foundations](blender/index.md) · [Wiki concept audit](../../research/wiki-concept-audit.md)

This is the tracking document for the **Software & Tools** learning section — the guide teaching users how to learn Blender and the other software needed to make 3D models and textures for Second Life breedables. Update the checklist statuses honestly as pages land.

---

## 1. Goal & scope

**Goal:** a learner with zero 3D experience can, using only this wiki, go from installing Blender to uploading a **rigged, textured, SL-ready breedable creature**.

**In scope**

- A sequenced **Blender learning path** (B01–B10): install → interface → modeling → sculpting → retopology → UV → texturing/PBR → rigging → animation → SL export.
- A curated **add-on catalog** (built-in, free, paid).
- A **wider software index** (texturing, retopology, AI blockout, CC0 assets, SL-side tools).
- A large **tutorial arsenal** of verified videos/docs grouped by pipeline stage.

**Out of scope (covered elsewhere)**

- In-world scripting/genetics/HUD — see [In-world fixture](../tracks/a05-sl-fixture.md) and the [production line](../production-line.md).
- Tool license/approval detail — lives in the [tools registry](../../production/tools/index.md).

**Definition of done**

- [ ] Every B01–B10 page published with the full lesson template.
- [ ] Add-on catalog + software index + tutorial arsenal published, links verified.
- [ ] All pages wired into `mkdocs.yml` nav; `mkdocs build` passes with no broken internal links.
- [ ] A01–A05 tracks link to the relevant Blender lessons.
- [ ] At least one complete **evidence folder** exists (e.g. `training/blender/b01/`) proving a learner can follow a page end-to-end. *(Learner deliverable — see §6.)*

---

## 2. Lesson template (mandatory on every lesson page)

Every lesson page has:

1. **Outcome** — one-sentence skill gained
2. **Watch** — ≥1 verified tutorial video (table: topic, link, why chosen)
3. **Read** — ≥1 official doc link (Blender manual / SL wiki / tool docs)
4. **Explain** — our breedables-specific, numbered step-by-step guide
5. **Do** — hands-on lab (numbered)
6. **Produce** — exact artifacts + repo paths
7. **Completed when** — a checklist, not a status label

No lesson ships without at least one **Watch** and one **Read** link. No `GREEN`/`EXPERIMENTAL` on learner pages.

---

## 3. Full page inventory

Status key: **done** = published this run · **stub** = placeholder only · **planned** = not yet written.
"Evidence needed" = the artifacts/labs a learner must still produce to prove the page works (the page text is complete when marked done).

### Hub & roadmap

| Page | Purpose | Status | Evidence needed |
|------|---------|--------|-----------------|
| [software/index.md](index.md) | Software & Tools hub / start-here | done | — |
| [software/build-plan.md](build-plan.md) | This roadmap | done | keep statuses current |

### Blender Foundations path

| Page | Purpose | Status | Evidence needed |
|------|---------|--------|-----------------|
| [blender/index.md](blender/index.md) | Path overview + sequence | done | — |
| [B01 Install & setup](blender/b01-install-setup.md) | Right LTS + SL-scale config | done | `training/blender/b01/` startup blend + screenshots |
| [B02 Interface & navigation](blender/b02-interface-navigation.md) | Viewport, select, transform, editors | done | `training/blender/b02/` practice scene + cheat sheet |
| [B03 Mesh modeling](blender/b03-mesh-modeling.md) | Organic creature base | done | `training/blender/b03/` quadruped base + wire shots |
| [B04 Sculpting basics](blender/b04-sculpting.md) | Form + detail | done | `training/blender/b04/` sculpt + matcap render |
| [B05 Retopology](blender/b05-retopology.md) | Low-poly + LOD + land impact | done | `training/blender/b05/` retopo + LI screenshot |
| [B06 UV unwrapping](blender/b06-uv-unwrapping.md) | Seams + packed UVs | done | `training/blender/b06/` UV layout + checker shot |
| [B07 Texture painting & PBR](blender/b07-texture-painting-pbr.md) | Metallic/roughness + bake | done | `training/blender/b07/` maps + **in-world shot** |
| [B08 Rigging & weight painting](blender/b08-rigging-weight-painting.md) | Quadruped rig for Animesh | done | `training/blender/b08/` rig + pose/weight shots |
| [B09 Basic animation](blender/b09-animation.md) | Idle + walk, baked | done | `training/blender/b09/` playblasts |
| [B10 Export to Second Life](blender/b10-export-to-sl.md) | LODs, physics, upload | done | `training/blender/b10/` export pkg + LI + in-world shot |

### Catalog & indexes

| Page | Purpose | Status | Evidence needed |
|------|---------|--------|-----------------|
| [software/addon-catalog.md](addon-catalog.md) | Built-in/free/paid add-ons | done | periodic link re-check + version notes |
| [software/software-index.md](software-index.md) | Non-Blender tool hub | done | periodic link re-check |

### Tutorial arsenal (resources)

| Page | Purpose | Status | Evidence needed |
|------|---------|--------|-----------------|
| [resources/tutorials.md](../resources/tutorials.md) | Curated library by stage (incl. Shader & Geometry Nodes) | done | fill open per-track slots in [videos.md](../resources/videos.md) |
| [resources/videos.md](../resources/videos.md) | Per-track primary video picks | stub (A02–A05 slots open) | verified videos for A02, A03, A04, A05 |
| [resources/official-docs.md](../resources/official-docs.md) | Official doc index | done (pre-existing) | keep in sync with new pages |

---

## 4. Phased milestones

| Phase | Scope | Status |
|-------|-------|--------|
| **Phase 1** | Blender fundamentals path B01–B10 published with template + verified links | ✅ done this run |
| **Phase 2** | Add-on catalog (built-in/free/paid, essential vs nice-to-have) | ✅ done this run |
| **Phase 3** | Wider software index + tutorial arsenal (texturing, shader/geo nodes, AI, CC0 assets) | ✅ done this run |
| **Phase 4** | Link A01–A05 tracks to the matching B-lessons; cross-wire nav | ✅ done this run (B-lessons link to A-tracks; A-tracks to be back-linked — see §7) |
| **Phase 5** | Fill evidence folders — a real learner runs B01→B10 and commits artifacts | ⬜ open (learner deliverable) |
| **Phase 6** | Fill open [videos.md](../resources/videos.md) slots (A02–A05) with verified picks | ⬜ open |

---

## 5. Content standards

1. **Verified links only.** Every external URL is checked before inclusion. Prefer canonical sources: [Blender manual](https://docs.blender.org/manual/en/latest/), Blender's [official YouTube](https://www.youtube.com/@BlenderOfficial), long-standing tutorials (Blender Guru "Donut", Grant Abbitt, CG Cookie, Ryan King Art, Default Cube/CGMatter, CGDive), the [Second Life wiki](https://wiki.secondlife.com/) for SL specifics, and each tool's official site. If a specific video can't be verified, link the channel/playlist/official page instead — never invent a video ID.
2. **Evidence-first.** Watching ≠ completion. Every lesson produces committed artifacts under `training/…`.
3. **SL-specific correctness.** Get Animesh, land impact / LOD (LI = max of download/physics/server weight), metallic/roughness PBR + glTF 2.0, and Collada/DAE upload right — verified against the SL wiki, not from memory.
4. **No status theater.** No `GREEN`/`YELLOW`/`RED`/`EXPERIMENTAL` on learner pages (see the [audit](../../research/wiki-concept-audit.md)). Registry labels stay in the [registry](../../production/tools/index.md).
5. **Same voice/format** as existing docs; tables + admonitions + numbered steps.
6. **Free-first.** Present the free option first; recommend paid tools only with a reason (and ideally an experiment).

---

## 6. Mapping to Academy tracks

The [Academy tracks A01–A05](../overview.md) are **outcome labs**; the Blender path is the **skill layer** beneath them:

| B-lesson | Feeds track | Production stage |
|----------|-------------|------------------|
| B03, B04 | A-model (planned) | 2 Modeling |
| B05 | [A03 Retopology](../tracks/a03-retopology.md) | 3 Retopo/LOD |
| B06, B07 | [A01 Organic PBR](../tracks/a01-organic-pbr.md) / [A02 Layered textures](../tracks/a02-layered-textures.md) | 4–5 UV/Texturing |
| B08, B09 | [A04 Rig + animation](../tracks/a04-rig-animation.md) | 7–8 Rig/Animation |
| B10 | [A05 SL fixture](../tracks/a05-sl-fixture.md) | 9–10 Export/Upload |

This supplies the learning content the [audit](../../research/wiki-concept-audit.md) found missing — a new member can learn Blender and breedables production from this wiki alone.

---

## 7. Open questions & follow-ups

- **Back-link A-tracks → B-lessons.** The B-lessons link up to the A-tracks; adding a "prerequisite Blender lessons" line to each A0x page would close the loop. *(Deliberately left as a follow-up to avoid editing track pages another worker may own.)*
- **Fill evidence folders (Phase 5).** `training/blender/b01…b10/` are named in each lesson but not yet populated — needs a real run-through by a learner/studio member.
- **Verify A02–A05 primary videos.** [videos.md](../resources/videos.md) still has open slots; fill with verified picks.
- **Avastar vs manual SL skeleton.** Decide the studio's default Animesh export path (paid Avastar vs hand-built SL bones) and document it in B08/B10 once chosen.
- **Blender LTS pin.** Confirm which LTS (4.5 vs 5.2) the studio standardises on once paid add-on (Avastar) compatibility is checked; record in B01.
- **A-model / A-export tracks.** The production line lists planned A-model and A-export tracks; B03/B04 and B10 already cover the skills — decide whether to formalise those tracks or point them at these lessons.

---

## References

- [Software & Tools hub](index.md) · [Blender path](blender/index.md) · [Add-on catalog](addon-catalog.md) · [Software index](software-index.md) · [Tutorial arsenal](../resources/tutorials.md)
- [Software & Tools hub](index.md) · [Blender path](blender/index.md) · [Tutorial arsenal](../resources/tutorials.md) · [Wiki concept audit](../../research/wiki-concept-audit.md)
