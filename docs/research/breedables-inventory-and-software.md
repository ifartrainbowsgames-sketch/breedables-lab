# Breedables inventory & software

**Kimi updated:** 2026-08-24  
**Status:** RESEARCH — not a product plan  
**Date:** 2026-08-23  

**Companion pages:**

- [Breedables case studies](breedables-case-studies.md) — deep profiles of major lines
- [Breedables market study](breedables-market-study.md) — success/failure patterns
- [SL platform baseline](../secondlife/platform-baseline.md) — Animesh, PBR, Linkset Data
- [Blender add-on catalog](../academy/software/addon-catalog.md) — tools for *making* breedables

!!! note "Software disclosure is sparse"
    Breedable companies rarely publish their full 3D pipeline. Where no primary source exists, this page marks software as **inferred** (typical SL creator stack for that era) rather than confirmed. "Documented" means we found a direct source or a widely cited SL-specific tool.

---

## How breedables are actually built (software stack)

Every breedable line combines **3D art**, **SL upload**, and **LSL/Mono game logic**. The art side is what Academy teaches; the script side is almost always proprietary per company.

### 3D art & animation (documented industry patterns)

| Stage | Professional tools (inferred) | Free/OSS route (Academy) | SL export |
|-------|------------------------------|--------------------------|-----------|
| Reference | PureRef | PureRef / boards | — |
| Blockout / modeling | Maya, Blender | Blender | — |
| Organic sculpt | ZBrush, Blender | Blender sculpt | — |
| Retopology | Maya Quad Draw, TopoGun | Blender + RetopoFlow | Low-poly game mesh |
| UVs | Maya, RizomUV, Blender | Blender + TexTools | Texel density matters |
| Texturing | Substance Painter, Mari | Ucupaint, Krita, Material Maker | Diffuse → **PBR glTF** (new) |
| Rigging quadrupeds / Animesh | Maya + studio rigs | Blender + **Rigify** or **Avastar** | Collada (.dae) |
| Animation | Maya, Blender | Blender | BVH / SL animation |
| Lookdev | Marmoset Toolbag | Blender EEVEE/Cycles | In-world QA |

!!! note "Documented vs inferred"
    Maya, ZBrush, Substance Painter, TopoGun, Marmoset, and RizomUV are **inferred** for most breedable studios — they are standard in game/SL asset pipelines but individual companies have not published their toolchains. Blender, Avastar, Rigify, and built-in Collada/glTF exporters are **documented** as common SL creator tools.

### Documented SL-specific tools

- **[Avastar](https://www.avalab.org/avastar/)** (Blender, paid) — quadruped/Animesh rigging, SL skeleton, Collada export; widely used by SL mesh creators ([Avastar quadruped docs](https://avalab.org/avastar/300/reference/usermanual/advanced/non-human-rigging/)).
- **Built-in Collada + glTF exporters** (Blender) — mesh and PBR material upload ([B10 export lesson](../academy/software/blender/b10-export-to-sl.md)).
- **Rigify** (Blender, free) — alternative rig path; Teulu-style Animesh still needs SL-compatible bone mapping.

### Runtime / game logic (rarely public)

| Layer | Typical tech | Notes |
|-------|--------------|-------|
| Genetics engine | Custom LSL/Mono | Dominant/recessive traits (Ozimals onward); server-side or object-side |
| Feeding / upkeep | LSL + external DB | BioBreeds shutdown showed backend ownership risk |
| Breeding UI | LSL + web portal | KittyCatS Cattery, Wild Kajaera portal, Nixsy website |
| Movement | Pathfinding, Animesh | Mossms early adopter; Teulu/WK/Nixsy use Animesh |
| Persistence | LSL, Linkset Data | Modern lines should evaluate [Linkset Data](../secondlife/platform-baseline.md) |

**Documented script vendor:** Ozimals partnered with **Akimeta Metaverse Development Services** for bunny scripts before the 2017 cease-and-desist ([SL Newser](http://slnewser.blogspot.com/2022/05/looking-back-end-of-ozimals.html)).

---

## Master inventory — what has been produced

Sources: [SL Wiki — Breedables Guide](https://wiki.secondlife.com/wiki/Breedables_Guide_For_Second_Life), [case studies](breedables-case-studies.md), official sites checked 2026-08-23.

**Status key:**  
**Active** = current listings/site activity · **Discontinued** = official shutdown · **Niche** = exists but not mainstream · **Legacy** = supported but little new content

### Historical / discontinued (still culturally important)

| Company | Product | Species / theme | Era | Tech | Status |
|---------|---------|-----------------|-----|------|--------|
| Sion | Chickens | Chickens | ~2008–2009 | Prim/script AI | Discontinued |
| Ozimals | Bunnies | Rabbits | 2010 | Sculpt/mesh + genetics | Discontinued 2017 |
| Ozimals | Pufflings | Stylized birds | post-2010 | Mesh + genetics | Discontinued 2017 |
| Ozimals / successor | Fables | Bunnies (successor) | post-2017 | — | Separate company; verify before citing |
| BioBreeds | Dogs | Realistic dogs | Feb 2011 | Mesh | Discontinued 2023 |
| BioBreeds | Pal Ponies | Ponies | Nov 2011 | Mesh, ridable | Discontinued 2023 |
| BioBreeds | Exotics | Fantasy ridables | — | Cross-breed w/ ponies | Discontinued 2023 |
| BioBreeds | Wild Ones | Wolf, fox, coyote, tiger | Feb 2014 | Mesh + animations | Discontinued 2023 |

### Long-running active majors

| Company | Product | Species / theme | Era | Tech | Status |
|---------|---------|-----------------|-----|------|--------|
| Amaretto | Horses | Horses (ride, race, stud) | Sep 2010 | Mesh → Animesh migration unclear | **Active** (Teulu ownership 2024) |
| Amaretto | K-9s | Dogs | Aug 2011 | Mesh | **Active** |
| Amaretto | Barnyard Birds | Birds | May 2012 | Mesh | **Active** |
| KittyCatS | Cats | Cats | ~2011 | Mesh; off-grid Cattery | **Active** |
| Teulu | Furbs | Fantasy creatures | Mar 2020 | **Animesh** | **Active** |
| Teulu | Horses | Horses | Nov 2021–22 | **Animesh**, ridable | **Active** |
| Teulu | Dogs | Dogs | Apr 2023 | **Animesh** | **Active** |
| Teulu | Ludens | Animesh creatures | Sep 2023 | **Animesh** | **Active** |
| Teulu | JingJings | (legacy line) | 2012 | Not Animesh | **Active** |
| Wild Kajaera | Big Cats | Lions, tigers, cougars… | mid-2012 | Animated mesh/Animesh | **Active** |
| Wild Kajaera | Wild Dogs | Wolves, dire wolves… | — | Animated | **Active** |
| Wild Kajaera | Little Varmints | Ferrets, etc. | — | Animated | **Active** |
| Wild Kajaera | Wild Mustangs | Horses | — | Animated | **Active** |
| oYo | Dodos, Fuzzy Buzzies, Pigs | Mixed cute | 2014 (from InWorldz) | Mesh; **Animesh Ele** (2026 news) | **Active** |
| Foxtrot | Many species | 72+ classified species per wiki | long-running | Low-LI mesh; legacy + active | **Active** |
| Nixsy | Cross-species pets | Bears, wolves, etc. | 2020s | **Animesh** + token server | **Active** |
| Kreatures | Cubs | Bear, lion, wolf cross-breed | Apr 2022 | Mesh/Animesh | **Active** |
| Snuffles | Snuffles | Squirrel-like | 2020s | Genetics + **Solana token** | **Active** |
| PlantPets | Plants | Flowers, orchids, etc. | 2007 | Interactive flora | **Active** |
| DFS | Digital Farm System | Crops + farm animals | Oct 2016 | Farming sim, not classic pet | **Active** |
| Krafties | Fantasy MMORPG | Many creature types | — | Game + breeding | **Active** |

!!! note "Tooling is mostly inferred"
    None of the companies above have published a primary-source pipeline breakdown. The "Tech" column reflects **documented platform capabilities** (mesh, Animesh, token server, Solana integration) and **inferred** art tools based on era and visual style.

### Niche / long-tail / mixed activity

| Company | Product | Species / theme | Status |
|---------|---------|-----------------|--------|
| Fennux | Foxes | Foxes + dueling/crafting | Niche |
| Meeroos | Meeroos | Fantasy meerkat-like | Niche |
| Fawns | Fawns | Dueling, racing deer-like | Active (market exists) |
| Mossms | Mossms | Space creatures | Niche; early mesh/pathfinding |
| BattleBeast | Dragons, Kitsune | Fantasy combat breeding | Active (RP/combat niche) |
| AEON Pets | Many mini-lines | Hamsters, elephants, spiders… | Active (breadth over depth) |
| EVO Breeding Co | Fairies, hammies, fish… | Mixed fantasy/farm | Active |
| Papillon | Butterflies, dragonflies | Insect ecosystem | Active |
| Pet Peddlers | Fish, seahorses | Aquatic | Active |
| Stray Cats | Cats | Pathfinding cats | Active |
| Buildables | Robots | Sci-fi bots | Active (different genre) |
| Unique Breedables | Various | Generic brand | Active |
| ADS | Shubbies | Fish Hunt companions | Active |

### Marketplaces (not producers)

| Name | Role |
|------|------|
| Sweetflowers Breedables | Auction/rental market for many brands |
| Fennux Market / Fawns Market | Secondary markets for those lines |

---

## Software by era — what creators likely used

| Era | Approx. years | Mesh tech | Inferred 3D tools | Documented examples |
|-----|---------------|-----------|-------------------|---------------------|
| Prim/sculpt | 2008–2011 | Sculpties, prims | Photoshop, optional Blender | Sion chickens, early Ozimals |
| Mesh | 2011–2019 | Collada mesh, low LI | Blender, Maya, ZBrush, Photoshop | Amaretto, BioBreeds, KittyCatS, WK |
| Mesh + pathfinding | 2013+ | Mesh + pathfinding | Same + SL pathfinding navmesh | Mossms, Stray Cats |
| Animesh | 2020+ | Rigged Collada Animesh | **Blender + Avastar** or Maya; Bento skeleton | Teulu, Nixsy, oYo Ele, Ludens |
| PBR / glTF | 2023+ | Metallic-roughness materials | Substance Painter or Blender PBR → glTF | **No major breedable line documented as PBR-native yet** |

**Takeaway for Breedables Lab:** Teulu proved Animesh breedables work commercially. **PBR-native genetics** (coat roughness/metalness as traits) is still a documented open gap ([market study §3](breedables-market-study.md)).

---

## What could still be available to make

This is **opportunity analysis**, not a go decision. Market room in 2026 is **not verified** here.

### Species / themes with weak or no Animesh-native leader

| Gap | Why it may be open | Caveat |
|-----|-------------------|--------|
| **Reptiles** (snakes, lizards, turtles) | Few dedicated modern lines vs cats/dogs/horses | WK/Foxtrot may cover some |
| **Birds** as primary Animesh breedables | Ozimals Pufflings dead; Amaretto Barnyard Birds older tech | Niche audience |
| **Aquatic mammals** (otters, seals) | Pet Peddlers owns fish; not same niche | Art + rig cost |
| **Farm mammals** (goats, sheep, cows) | DFS has farming sim; not classic collect-and-breed pets | DFS overlap |
| **Insects** beyond Papillon | Papillon exists but ecosystem-style | Different mechanic |

### Mechanics combinations not seen together in researched evidence

| Combination | Who has pieces | Gap |
|-------------|----------------|-----|
| Deep genetics + utility (ride/race/duel) + **Animesh** + **low LI** | Amaretto (utility), Teulu (Animesh), Fennux (duel) | No line documented with all four at AAA polish |
| **PBR trait genetics** (roughness/metalness/normal variants) | None in case studies | Platform-new; visual differentiator |
| **Discoverable hidden traits** + modern Animesh | Meeroos (hidden), Teulu (modern) | Meeroos not Animesh-native |
| Cross-species breeding + Animesh | Kreatures, Nixsy | Crowded for “cute crossbreed” |
| Blockchain payout | Snuffles only | Polarizing; not proven long-term |

### Production niches for *new studios* (Breedables Lab angle)

Using the **free/OSS Academy stack** (Blender, Material Maker, Ucupaint, RetopoFlow, Avastar):

1. **Animesh creature MVP** — one species, low LI, 3–5 genetic coat traits, feeding loop — validates B01–B10 + LSL integration before scaling.
2. **PBR showcase breedable** — first line marketed on glTF PBR coats (even one species) — differentiates from 2010-era diffuse-only pets.
3. **Backend-resilient design** — document open ownership model up front (lesson from BioBreeds 2023).
4. **Original genetics script** — avoid Ozimals/Amaretto-style IP exposure ([case law summary](breedables-case-studies.md#ozimals-bunnies)).

### Probably *not* open (saturated or legally risky)

- Generic **cats**, **horses**, **dogs** without a sharp twist (KittyCatS, Amaretto/Teulu, WK, BioBreeds legacy crowd)
- **Bunnies** (Ozimals trauma + Fables successor space)
- **Clone mechanics** of an active line’s trait tables or UI
- **Blockchain-first** monetization unless you explicitly want that audience split

---

## Recommended 3D plugin shortlist for *making* a new breedable

From [add-on catalog](../academy/software/addon-catalog.md) — minimum viable art pipeline:

**Free:** Node Wrangler, LoopTools, Rigify, Collada/glTF exporters, RetopoFlow, Ucupaint, TexTools, Poly Haven

**Paid when selling SL Animesh:** **Avastar** (SL skeleton, quadruped rig, export)

**Paid optional:** Auto-Rig Pro, UVPackmaster, SimpleBake — only if measured bottlenecks

---

## Refresh with Kimi

Kimi writes **directly to this wiki page** (subscription OAuth — `kimi login --region global`):

```powershell
cd tools/librarian
python -m librarian.cli breedables-research
```

A dated audit copy is also saved under `research/discoveries/daily-YYYY-MM-DD/breedables-inventory-kimi.md`. If Kimi fails, this page is **not** overwritten.

---

## References

- [Breedables Guide For Second Life (SL Wiki)](https://wiki.secondlife.com/wiki/Breedables_Guide_For_Second_Life)
- [Breedables case studies — References](breedables-case-studies.md#references)
- [Teulu Breedables portal](https://portal7.teulubreedables.com/)
- [Wild Kajaera portal](https://www.portal.wildkajaera.com/)
- [oYo Breedables](https://oyobreedables.org/)
- [Foxtrot Breedables wiki](https://wiki.foxtrotbreedables.com/)
- [Nixsy Breedables](https://nixsybreedables.com/)
- [PlantPets about](https://plantpets.dejapi.com/?q=about)
- [Avastar — Non-human rigging](https://avalab.org/avastar/300/reference/usermanual/advanced/non-human-rigging/)
- [SL Community — Are breedables still a thing?](https://community.secondlife.com/forums/topic/501746-are-breedables-still-a-thing-which-one-is-the-most-popular-right-now/)
