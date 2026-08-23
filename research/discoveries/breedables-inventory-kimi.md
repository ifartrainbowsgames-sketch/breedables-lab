```markdown
---
title: Breedables inventory and software pipeline research
date: 2026-08-23
kimi_generation_date: 2026-08-23
status: RESEARCH — inventory and pipeline survey, not a product plan
path: docs/research/breedables-inventory-and-software.md
---

# Breedables inventory and software pipeline research

**Date:** 2026-08-23  
**Kimi generation date:** 2026-08-23  
**Status:** RESEARCH — inventory and pipeline survey, not a product plan

This document consolidates what is known about Second Life breedable-pet lines, the software pipelines used (or inferred) to produce them, and where openings may exist for a new entrant. It is intended as reference material for Breedables Lab and should be read alongside the [Breedables case studies](breedables-case-studies.md) and [Breedables market & design study](breedables-market-study.md).

!!! note "Sourcing limits"
    Claims about real companies and products are hedged where sourcing is thin ("reportedly," "widely regarded as," "unverified"). No URLs or product names are invented; anything not independently verified is marked as such or omitted.

---

## 1. Master inventory

The table below lists documented Second Life breedable producers and product lines. Status labels are approximate and based on web research, not live in-world verification. "Tech era" describes the rendering/animation technology the line launched with or is currently marketed around, based on available sources.

| Company | Product line | Species/theme | Launch era | Status (as researched) | Tech era |
|---|---|---|---|---|---|
| Sion Zaius (individual creator) | Sion Chickens | Chickens | ~2008–2009 | Discontinued | Prim/sculpt-era |
| Ozimals, Inc. | Ozimals | Bunnies; later Pufflings | Jan 2010 | Discontinued (2017) | Prim/sculpt-era |
| Ozimals, Inc. / successor | Fables | Bunnies (successor to Ozimals) | post-2017 | Active? unverified | Unverified |
| Amaretto Ranch Breedables, LLC (now under Teulu ownership) | Amaretto Ranch Breedables | Horses, K-9s, Barnyard Birds | Sep 2010 (horses); Aug 2011 (K-9s); May 2012 (Barnyard Birds) | Active | Prim/sculpt-era legacy; current stack unverified |
| BioBreeds | BioBreeds | Dogs, Ponies, Wild Ones (wolf, fox, coyote, tiger) | Feb 2011 (dogs); Feb 2014 (Wild Ones) | Discontinued (2023) | Sculpt/mesh-era (inferred from era and realism claims); specific tools unverified |
| KittyCatS | KittyCatS | Cats | ~2011 | Active | Prim/sculpt-era legacy; current stack unverified |
| Fennux | Fennux | Foxes | ~2011 | Niche / long-tail | Prim/sculpt-era legacy |
| Wonderful World of Meeroos | Meeroos | Fantasy meerkat-like creatures | ~2012–2013 | Niche / long-tail | Prim/sculpt-era legacy |
| Teulu Breedables | Teulu Originals / Teulu Horses / Teulu Dogs / Amaretto Ranch (acquired) | Original fantasy species, horses, dogs | Mar 2020 (first line); Nov 2022 (horses); Apr 2023 (dogs); Mar 2024 (Amaretto acquisition) | Active | Mesh / Animesh (documented as first Animesh breedables in SL) |
| Snuffles / Goldtokens | Snuffles | Fantasy creatures | 2020s | Active | Mesh-era or later (unverified in sources) |
| Various (Wild Kajaera cited) | Wild Kajaera | Big cats, wild dogs, wild mustangs | Unverified | Mentioned only; status unverified | Unverified |
| Various | Fawns, Kreatures, oYo Breedables, Foxtrot Breedables, Nixsy Breedables | Various | Unverified | Mentioned only; status unverified | Unverified |

!!! note "Marketplace hosts vs. producers"
    **Sweetflowers** is frequently referenced in Second Life breedables community discussion as a third-party auction/marketplace host for reselling breedables, not as a breedable producer. The rows above list product creators. Specific producer relationships with Sweetflowers were not independently verified in this research pass, so it is not included as a sourced product line.

---

## 2. Software & pipeline

This section separates what is **documented** in available sources from what is **inferred** from the era, technology, or standard Second Life workflows. Where a tool or pipeline is not documented for a specific line, it is marked as unknown.

### 2.1 Documented

- **LSL (Linden Scripting Language)** — Used as the in-world runtime layer for breeding logic, genetics, feeding timers, movement/AI state, and interaction. This is documented by the nature of the products and by the [SL Wiki Breedables Guide](https://wiki.secondlife.com/wiki/Breedables_Guide_For_Second_Life).
- **Off-world / server-side backend** — Used by multiple lines for genetics databases, web dashboards, and remote state management. The BioBreeds shutdown demonstrates that backend ownership can be a single point of failure.
- **Animesh** — Documented as the core animation/rendering technology for Teulu Breedables (marketed as the first Animesh breedables in Second Life).
- **Solana blockchain / token integration** — Documented for Snuffles, tying in-world breeding output to an external cryptocurrency-adjacent asset ("Baby Poo").

### 2.2 Inferred (not documented per line)

- **Blender + Avastar** — The de-facto standard pipeline for rigging and animating SL-compatible mesh and Animesh creatures. Inferred for modern lines such as Teulu, but not explicitly documented in their public sources.
- **Maya, 3ds Max, or Modo** — Possible alternatives to Blender in professional or legacy workflows, but no specific line documents their use.
- **ZBrush or equivalent high-detail sculpting tool** — Inferred for BioBreeds' realistic animal models, given the level of organic detail described, but not documented.
- **Substance Painter / Substance Designer, Photoshop, GIMP** — Inferred for texture authoring, especially PBR material work, but not documented for any specific line.
- **Standard Second Life mesh upload path (with LODs)** — Inferred for any post-2010 mesh-era breedable aiming at low land impact.

### 2.3 Unknown / unverified

- The specific 3D modeling, sculpting, texturing, and rigging tools used by Sion Chickens, Ozimals, Amaretto Ranch, KittyCatS, Fennux, and Meeroos.
- Whether any major legacy line has been rebuilt around Second Life's newer PBR/glTF 2.0 material pipeline.
- The exact backend technologies (database, hosting provider, cloud architecture) used by active or defunct lines.

### 2.4 Breedables Lab's documented pipeline

Internal studio lessons already cover the tools that would likely be used for an Animesh/PBR-native breedable:

- [B05 Retopology / LOD generation](../academy/software/blender/b05-retopology.md)
- [B07 Texture painting & PBR](../academy/software/blender/b07-texture-painting-pbr.md)
- [B08 Rigging & weight painting](../academy/software/blender/b08-rigging-weight-painting.md)
- [A01 Organic PBR track](../academy/tracks/a01-organic-pbr.md)
- [A04 Rig + animation track](../academy/tracks/a04-rig-animation.md)

These are internal production-ready resources, not evidence of what existing competitors used.

---

## 3. What is still available to make

This section identifies species, mechanics, and technology combinations that appear underserved by currently active lines. It is **not** a product recommendation; it is a map of gaps, with caveats.

### 3.1 Species / theme gaps

No active, well-documented line currently dominates these spaces:

- **Aquatic / marine life** — fish, cetaceans, cephalopods, seals, etc.
- **Insects / arachnids** — butterflies, beetles, spiders, etc.
- **Reptiles / amphibians** — dragons, lizards, snakes, frogs, salamanders.
- **Birds beyond barnyard birds** — raptors, parrots, songbirds, fantasy birds.
- **Realistic farm livestock** — pigs, goats, sheep, cattle (Amaretto Barnyard Birds is the closest, but limited).
- **Small domestic mammals** — rabbits (Ozimals/Fables legacy leaves room, though Fables successor exists unverified), rodents, ferrets, etc.

### 3.2 Mechanics / technology gaps

No researched active line combines all of the following:

- **PBR-native genetics** — coat/skin variation driven by roughness, metalness, normal, or subsurface material properties rather than diffuse recoloring alone.
- **Animesh-native from day one** — Teulu proved the concept, but most species categories remain untouched by Animesh.
- **Strong genetics + utility/competitive layer + modern tech** — Amaretto had utility; Ozimals/KittyCatS had genetics; Teulu has modern tech; no documented line combines all three strongly.
- **Discoverable hidden traits / lore-driven breeding** — Meeroos explored this, but with legacy tech.
- **Backend-resilient architecture** — open-source, self-hostable, or multi-operator continuity planning as a design requirement, not an afterthought (lesson from BioBreeds' 2023 shutdown).
- **Low land-impact as a headline feature** — mesh-era optimization is marketable but not documented as a core genetics feature in any line.

### 3.3 Caveats: market saturation and risk

- **Historical market fatigue is documented.** The Ozimals bubble (2010) and Fennux secondary-market decline (~2013) show that breedables economies can saturate and crash when supply outpaces demand or upkeep costs exceed returns.
- **Current market size in 2026 is unverified** in this research. Whether there is room for a new entrant is an open question requiring current-state discovery (marketplace activity, active-community size, land-use patterns).
- **Established communities and secondary markets** (KittyCatS, Amaretto/Teulu) represent real competition for attention and breeder time.
- **IP/legal exposure** is a documented risk: the *Amaretto Ranch Breedables, LLC v. Ozimals, Inc.* litigation shows that genetics-engine originality and aggressive IP enforcement can both become costly.
- **Monetization is unsettled** — Snuffles' blockchain token layer is a live experiment whose audience impact is not yet verdict-ready; the Linden-dollar-only model remains the proven default.

---

## 4. Sources

- [Breedables case studies](breedables-case-studies.md) (Breedables Lab internal research)
- [Breedables market & design study](breedables-market-study.md) (Breedables Lab internal research)
- [Breedables Guide For Second Life (SL Wiki)](https://wiki.secondlife.com/wiki/Breedables_Guide_For_Second_Life)
- [Ozimals (SL Wiki)](https://wiki.secondlife.com/wiki/Ozimals)
- [Amaretto Ranch Breedables, LLC v. Ozimals, Inc. (Wikipedia)](https://en.wikipedia.org/wiki/Amaretto_Ranch_Breedables,_LLC_v._Ozimals,_Inc.)
- [Vice — "Thousands of Second Life Bunnies Are Going to Starve to Death This Weekend"](https://www.vice.com/en/article/kzekmv/thousands-of-second-life-bunnies-are-going-to-starve-to-death-this-weekend)
- [Boing Boing — "All the Second Life rabbits are doomed, thanks to DRM"](https://boingboing.net/2017/05/20/breedables-vs-drm.html)
- [SL Newser — "Goodbye Yellow Brick Road" Ozimals closure](http://slnewser.blogspot.com/2017/05/goodbye-yellow-brick-road-ozimal.html)
- [SL Newser — Update on Ozimals: New "Fables" Bunnies](http://slnewser.blogspot.com/2017/06/update-on-ozimals-new-fables-bunnies-on.html)
- [Kittywitchin — "The Battle of the Breedables"](https://kittywitchin.com/2010/12/16/ozimals-v-amaretto/)
- [SL Destinations — Amaretto Ranch](https://secondlife.com/destination/amaretto-ranch)
- [breedables.wordpress.com — Amaretto Horses category](https://breedables.wordpress.com/category/sl-breedables/amaretto-horses/)
- [SL Newser — BioBreeds Breedable Pets Shut Down](http://slnewser.blogspot.com/2023/02/biobreeds-breedable-pets-shut-down.html)
- [SL Community forum — "No Bio Breeds store or on Marketplace is Gone Help!"](https://community.secondlife.com/forums/topic/499376-no-bio-breeds-store-or-on-marketplace-is-gone-help/)
- [SL Destinations — KittyCatS](https://secondlife.com/destination/kittycats)
- [kittycats.ws](https://kittycats.ws/login_form4.php)
- [SL Community forum — "How much $ have you made via KittyCats, PlantPets, DFS, other breedables?"](https://community.secondlife.com/forums/topic/435130-how-much-have-you-made-via-kittycats-plantpets-dfs-other-breedables/)
- [Fennux official site](http://www.fennux.com/features)
- [SL Destinations — Meeroos](https://secondlife.com
