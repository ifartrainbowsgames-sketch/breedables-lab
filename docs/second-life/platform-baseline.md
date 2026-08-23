---
title: "Second Life platform baseline"
section: second-life
type: topic
---

# Second Life platform baseline

Runtime, rendering and scripting assumptions every Breedables Lab species build must satisfy. The page anchors production decisions to current Second Life capabilities—PBR materials, Animesh, Linkset Data, and authoritative LSL references—and warns against copy-pasting legacy breedable patterns without modernization.

=== "Free tools"

    | Tool | Link | Best for |
    |---|---|---|
    | Second Life Wiki | [Second Life Wiki](https://wiki.secondlife.com/) | Platform feature documentation and release notes |
    | Second Life Creator Docs | [Second Life Creator Docs](https://create.secondlife.com/) | Official creator tutorials and LSL references |
    | LSL Definitions | [LSL Definitions](https://github.com/secondlife/lsl-definitions) | Authoritative LSL/SLua types and constants for tooling |
    | Outworldz XS Pet scripts | [Outworldz XS Pet scripts](https://outworldz.com/Secondlife/Posts/Breedable-pet/) | Historical breedables architecture study |

## Read

| Source | Covers |
|---|---|
| [PBR Materials](https://wiki.secondlife.com/wiki/PBR_Materials) | Metallic/Roughness upload, glTF 2.0, texture conventions |
| [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) | Rigged animated objects, land impact, skeleton requirements |
| [llLinksetDataWrite](https://create.secondlife.com/script/lsl-reference/functions/lllinksetdatawrite/) | Persistent linkset key-value storage API |
| [LSL Portal](https://wiki.secondlife.com/wiki/LSL_Portal) | Language syntax and runtime behavior |
| [Creator Documentation](https://create.secondlife.com/) | Official building, scripting and upload workflows |

## Judge assets in-world, not only in Blender

Breedables are consumed inside the Second Life viewer under real constraints: level-of-detail (LOD) switches, texture memory budgets, region windlight, physics cost, and script time. A beautiful Blender render is only a preview. Every material, mesh, rig and animation must be re-evaluated after upload using in-world screenshots and performance measurements. Use the [Creator Docs](https://create.secondlife.com/) for the current build and upload workflow, and always test on a mainland-style region rather than only in an empty sandbox.

## PBR materials — USE NOW

Second Life uses **Metallic/Roughness** PBR with **glTF 2.0** material upload. The [PBR Materials wiki page](https://wiki.secondlife.com/wiki/PBR_Materials) defines the supported texture channels and upload format. In production, export a glTF bundle from Blender with separate `.bin` and texture files, then upload through the build floater. Verify that normal maps use OpenGL orientation, that roughness and metallic are packed as expected, and that emissive strength behaves under the viewer's environment. Judge the [PBR experiments page](../research/experiments.md) with side-by-side Blender and in-world screenshots, not renders alone.

## Animesh — USE NOW

Animesh is the runtime target for independent, animated creature objects. The [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide) covers rigging requirements, land impact behavior, and how the viewer treats an Animesh object as a single animated agent. Before committing a species rig, confirm the mesh is weighted to a compatible skeleton, that animations use appropriate priorities, and that LOD0/LOD1/LOD2 models stay within acceptable land impact at expected rez densities. This belongs in the pre-species rigging and animation curriculum covered by the [experiments page](../research/experiments.md).

## Linkset Data — USE NOW / architecture test

[`llLinksetDataWrite`](https://create.secondlife.com/script/lsl-reference/functions/lllinksetdatawrite/) provides persistent key-value storage at the linkset level, surviving script resets and object rerez until the object is deleted. Treat it as the default persistence layer for new breedables, but prototype the architecture in the [experiments page](../research/experiments.md) before finalizing. Plan which keys are required, set a memory budget, clean stale keys with the matching delete API, and write a recovery path for region restarts. **Do not copy older breedable persistence patterns without comparing Linkset Data, Animesh, and PBR capabilities.** Many legacy systems rely on notecards or per-prim memory because those were the only options available at the time.

## Canonical LSL definitions — USE NOW

The [secondlife/lsl-definitions](https://github.com/secondlife/lsl-definitions) repository is the authoritative source for LSL and SLua constants, types, and function signatures. Use it to validate autocomplete data in your editor, generate lint rules, and cross-check any hard-coded constants. Keeping tooling aligned with this repo prevents drift when Linden Lab adds new functions or renames constants.

## Historical reference — research only

The [XS Pet / breedable scripts on Outworldz](https://outworldz.com/Secondlife/Posts/Breedable-pet/) are valuable as a historical case study. Read them to understand how older systems split concerns such as aging, breeding, eating, movement, food, eggs, homes, transport, updating, and debugging across separate scripts. Then **modernize** around current SL capabilities; treat the XS scripts as an architecture reference, not drop-in production code.

## Platform limits that shape design

Second Life imposes limits that directly affect breedables economics and reliability: land impact per parcel, script memory per script and per region, maximum link counts, region-crossing delays for physical objects, and restrictions on chat/channel usage. Evaluate each species feature against these limits early. A creature that looks good as a single Animesh may still need to split accessories into a static linkset; a complex AI loop may need to yield time or move to off-sim services. Document the trade-off decisions on the species design page.

## Evaluating a species build

Use this workflow before calling any species milestone complete:

1. Export the creature model and PBR glTF bundle from Blender.
2. Upload to Second Life and compare the in-world screenshot against the Blender reference.
3. Rez the Animesh version and verify skeleton, animation priority, and land impact at multiple distances.
4. Write, read, and delete Linkset Data keys; simulate a region restart and confirm state recovery.
5. Audit LSL constants and function signatures against the official definitions repo.
6. Compare memory and persistence behavior to the legacy pattern being replaced.
7. Document the rationale for any modernized design choice.

## Tools and reference

- [Second Life Wiki](https://wiki.secondlife.com/) — platform feature and release documentation
- [Creator Docs](https://create.secondlife.com/) — building, scripting, and upload guides
- [LSL Definitions on GitHub](https://github.com/secondlife/lsl-definitions) — authoritative LSL/SLua definitions

## Do

1. Export a creature model + PBR glTF bundle and upload it to Second Life, then capture an in-world screenshot for comparison.
2. Rez an Animesh rig and verify skeleton, animation priority, and land impact across LOD distances.
3. Write, read, and delete Linkset Data keys, then simulate a region restart to confirm persistence.
4. Compare memory use and complexity against older notecard or per-prim storage patterns.
5. Audit all LSL constants and function signatures against the lsl-definitions repository.

## Produce

| Artifact | Path |
|----------|------|
| In-world screenshot set | `` |
| Linkset Data test harness script | `` |
| Land impact and LOD report | `` |

## Done when

- [ ] Asset renders match an in-world screenshot taken under default environment settings.
- [ ] Animesh moves with the correct skeleton and priority; land impact is acceptable at target rez density.
- [ ] Linkset Data survives object rerez and region restart without data loss.
- [ ] LSL constants validate against the official lsl-definitions source.
- [ ] Any legacy pattern has been modernized with a documented rationale.

## Related

- [Experiments](../research/experiments.md)
