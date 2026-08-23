# Second Life platform baseline

Runtime and scripting assumptions for breedables production. All material and animation experiments should ultimately be judged **in Second Life**, not only in Blender renders.

## PBR materials — USE NOW

- [PBR Materials (SL wiki)](https://wiki.secondlife.com/wiki/PBR_Materials)
- Second Life uses **Metallic/Roughness** PBR and **glTF 2.0** material upload
- Studio rule: judge [E01 PBR experiments](../production/experiments.md) with in-world screenshots

## Animesh — USE NOW

- [Animesh User Guide](https://wiki.secondlife.com/wiki/Animesh_User_Guide)
- Runtime target for independent animated creature objects
- Part of pre-species rigging/animation curriculum ([E04](../production/experiments.md))

## Linkset Data — USE NOW / architecture test

- [`llLinksetDataWrite` reference](https://create.secondlife.com/script/lsl-reference/functions/lllinksetdatawrite/)
- Persistent state at linkset level
- Test in [E05](../production/experiments.md) before finalizing persistence architecture

!!! tip
    Do not copy older breedable persistence patterns without comparing Linkset Data, Animesh, and PBR capabilities.

## Canonical LSL definitions — USE NOW

- [secondlife/lsl-definitions](https://github.com/secondlife/lsl-definitions)
- Authoritative LSL/SLua definition source for tooling and validation

## Historical reference — research only

- [XS Pet / breedable scripts (Outworldz)](https://outworldz.com/Secondlife/Posts/Breedable-pet/)
- Study modular concerns: aging, breeding, eating, movement, food, eggs, homes, transport, updating, debugging
- **Modernize** around current SL capabilities; do not treat as drop-in production code

## Tools

| Tool | Link |
|------|------|
| SL wiki | [wiki.secondlife.com](https://wiki.secondlife.com/) |
| Creator docs | [create.secondlife.com](https://create.secondlife.com/) |
| LSL definitions | [GitHub](https://github.com/secondlife/lsl-definitions) |
