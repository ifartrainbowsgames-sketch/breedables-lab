---
title: "Second Life Production"
section: second-life
type: index
question: "How do I get the finished asset into Second Life correctly?"
---
# Second Life Production

!!! abstract "This section answers one question"
    *How do I get the finished asset into Second Life correctly?*

Second Life is a delivery target with hard constraints — land impact, LOD,
physics shapes, texture cost, permissions and Animesh limits. Learn the general
professional workflow from the [tool that does the work](../tools/index.md);
this section covers only what must change to ship in-world.

## Topics

| Page | What it covers |
|------|----------------|
| [Platform baseline](platform-baseline.md) | Animesh, PBR, land impact, Linkset Data — the numbers you design against |
| [Adapting professional work](adapting-professional-work.md) | What changes once the general 3D is already good |
| [Viewer & creator tools](viewer-and-tools.md) | The viewer as a production tool, not just a game client |

Exporting *out of Blender* is Blender's job, so it is taught as
[lesson 10](../tools/blender/export-and-upload.md) rather than repeated here.

## The rule this section exists to enforce

**Blender agreeing with you is not evidence. Second Life agreeing with you is.**

Every studio lab that touches a surface, a rig or a script demands an in-world
capture for exactly this reason. Renders are made under lighting you chose;
the platform is not.

| Check it in-world | Because |
|-------------------|---------|
| PBR materials | Metallic and roughness respond to the region's lighting, not your HDRI |
| Land impact | Only the uploader can tell you the real number, and it decides your cost |
| LOD behaviour | Your model is judged at distance, where the viewer swaps meshes |
| Animesh playback | Frame rate, loop seams and bone limits differ from the timeline |
| Script persistence | A sim restart is the only honest test of Linkset Data |

Capture under consistent lighting, note the viewer version and the date, and
commit it. An undated screenshot proves nothing six months later.

## What to have ready before you upload

1. A mesh at a **known** triangle count, with LODs you generated deliberately rather than accepted by default.
2. A physics shape you chose — the automatic one is usually wrong and usually expensive.
3. Materials exported through the glTF 2.0 path, since that is what carries PBR into the platform.
4. Somewhere to test that is not a public sandbox, so failures are cheap and repeatable.

## Where the evidence goes

| Work | Folder |
|------|--------|
| Upload packages and export presets | `pipeline/export/` |
| In-world captures | `training/secondlife/` |
| QA runs and regression checks | `tests/`, `training/secondlife/qa/` |

## Related

- [In-world fixture lab](../projects/in-world-fixture.md) — the lab that proves the whole chain works
- [Breedables Engineering](../engineering/index.md) — what the creature does once it is in-world
- [Official mesh upload docs](https://create.secondlife.com/) · [PBR Materials on the SL wiki](https://wiki.secondlife.com/wiki/PBR_Materials)
