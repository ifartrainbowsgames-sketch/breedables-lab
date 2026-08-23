---
title: "Animation libraries and motion capture"
section: research
type: reference
---
# Animation libraries and motion capture

!!! info "About this page"
    **Canonical home** — sources of ready-made motion data and the tooling to retarget it  
    **Studio status** — none approved yet; every entry needs a licence audit before commercial use  
    **Prerequisites** — [Rigging & skinning](../tools/blender/rigging-and-skinning.md), then [Animation](../tools/blender/animation.md)

A breedable needs idle, walk, eat and play loops before it feels alive, and
hand-keying each one for each species does not scale. This page tracks where
motion data can come from and what its licence actually permits.

!!! warning "Licence first, animation second"
    Motion capture datasets carry wildly different terms — research-only,
    attribution-required, non-commercial. A dataset being free to download says
    nothing about whether you may ship it in a product sold for Linden dollars.
    Audit before use; record the finding in the [tool registry](tool-registry.md).

## The quadruped problem

Most free animation libraries are **humanoid**. Mixamo never supported
four-legged creatures, and its successors mostly inherit that limit. For a
quadruped breedable this means one of three routes:

1. **Hand-key the loops.** Slowest, no licence risk, full control. This is what
   the [rig + animation project](../projects/rig-and-animation.md) asks for.
2. **Retarget humanoid or generic motion** onto a quadruped rig. Cheap to try,
   usually looks wrong on four legs without heavy cleanup.
3. **Capture your own.** Highest setup cost, no licence question at all.

Route 1 is the studio default until an experiment shows otherwise.

## Motion data sources

| Source | Format | Licence | Note |
|--------|--------|---------|------|
| [CMU Graphics Lab Motion Capture Database](https://mocap.cs.cmu.edu/) | BVH | Free to use — confirm current terms | Thousands of clips; imports natively via File → Import → BVH. Humanoid |
| [Bandai Namco Research Motion Dataset](https://github.com/BandaiNamcoResearchInc/Bandai-Namco-Research-Motiondataset) | BVH | Repository states its own terms — **audit** | ~3,000 stylised moves with a Blender visualisation script |
| [Quaternius](https://quaternius.com/) | GLB, BVH | CC0 | Universal rig animations, **including quadrupeds**. The closest thing to a free non-humanoid library |

## Tooling

| Tool | Licence | What it does |
|------|---------|--------------|
| [Open Mocap](https://github.com/Larenju-Rai/open-mocap-blender) | Open source | AI pose tracking inside Blender — offline full-body and hand tracking, with retargeting to any rig. No external software |
| [Animation retargeting](candidates/animation-retargeting.md) | Under evaluation | Moves an existing action onto a different skeleton |
| [Rokoko Studio Live](candidates/rokoko-studio-live.md) | Under evaluation | Live capture streamed into Blender |

## Practice rigs

Rigging and animating are separate skills. These let you practise motion without
building a rig first.

| Rig | Licence | Good for |
|-----|---------|----------|
| [Rain](https://studio.blender.org/characters/rain/v3/) | CC-BY | A full production character rig, Blender 4.1+ |
| [Animation Fundamentals rigs](https://studio.blender.org/training/animation-fundamentals/) | Free | Ball, pendulum and character rigs — the classic exercises |

## What Second Life adds

Animation that looks correct in Blender can still fail in-world. Upload format,
priority, and Animesh limits all constrain what ships — see
[platform baseline](../second-life/platform-baseline.md) and
[export & upload](../tools/blender/export-and-upload.md).

## Related

- [Rigging & skinning](../tools/blender/rigging-and-skinning.md) — build the armature first
- [Animation](../tools/blender/animation.md) — keyframing idle and walk cycles
- [Rig + animation project](../projects/rig-and-animation.md) — the lab that proves it
- [Experiment E04](experiments.md#e04-rig-and-retarget-baseline) — the retarget benchmark these sources feed
