from __future__ import annotations

from .db import LibrarianDB

BASELINE_RESOURCES = [
    {
        "name": "Blender",
        "url": "https://www.blender.org/",
        "category": "3d",
        "commercial_type": "OPEN_SOURCE",
        "code_license": "GPL-3.0-or-later",
        "status": "USE_NOW",
        "notes": "Primary modeling, sculpting, UV, baking, rigging and animation tool.",
    },
    {
        "name": "Material Maker",
        "url": "https://github.com/RodZill4/material-maker",
        "category": "textures",
        "commercial_type": "OPEN_SOURCE",
        "code_license": "MIT",
        "status": "EXPERIMENTAL",
        "notes": "Procedural PBR material authoring candidate.",
    },
    {
        "name": "Ucupaint",
        "url": "https://github.com/ucupumar/ucupaint",
        "category": "textures",
        "commercial_type": "OPEN_SOURCE",
        "code_license": "GPL-3.0",
        "status": "EXPERIMENTAL",
        "notes": "Layer-based texture painting workflow inside Blender.",
    },
    {
        "name": "TripoSR",
        "url": "https://github.com/VAST-AI-Research/TripoSR",
        "category": "3d-ai",
        "commercial_type": "OPEN_SOURCE",
        "code_license": "MIT",
        "model_license": "MIT",
        "status": "EXPERIMENTAL",
        "notes": "Image-to-3D baseline candidate. Generated-output rights still need workflow-specific verification.",
    },
    {
        "name": "RetopoFlow",
        "url": "https://github.com/CGCookie/retopoflow",
        "category": "retopology",
        "commercial_type": "UNKNOWN",
        "code_license": "GPL-3.0",
        "dependency_risk": "Repository code is GPL; non-code/bundled assets may have separate terms. Audit before studio approval.",
        "status": "REVIEWING",
        "notes": "Retopology workflow candidate with mixed licensing considerations.",
    },
    {
        "name": "Poly Haven",
        "url": "https://polyhaven.com/",
        "category": "assets",
        "commercial_type": "OPEN_CONTENT_CC0",
        "asset_license": "CC0",
        "status": "USE_NOW",
        "notes": "CC0 HDRIs, textures and models; record provenance per asset.",
    },
    {
        "name": "ambientCG",
        "url": "https://ambientcg.com/",
        "category": "assets",
        "commercial_type": "OPEN_CONTENT_CC0",
        "asset_license": "CC0",
        "status": "USE_NOW",
        "notes": "CC0 PBR assets; record provenance per asset.",
    },
]


def seed_baseline(db: LibrarianDB) -> dict:
    created = 0
    merged = 0
    for item in BASELINE_RESOURCES:
        _, was_created = db.add(**item, source_type="curated-baseline")
        created += int(was_created)
        merged += int(not was_created)
    return {"seen": len(BASELINE_RESOURCES), "created": created, "merged": merged}
