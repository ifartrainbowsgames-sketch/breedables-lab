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

EVIDENCE_DEFAULTS: dict[str, dict] = {
    "Blender": {
        "primary_video_url": "https://www.youtube.com/watch?v=B0J27sf02NU",
        "doc_urls": [
            "https://docs.blender.org/manual/en/latest/",
            "https://docs.blender.org/manual/en/latest/render/shader_nodes/intro.html",
        ],
        "lesson_wiki_path": "docs/academy/software/blender/index.md",
        "evidence_path": "training/blender/",
        "academy_track": "A-model",
    },
    "Material Maker": {
        "primary_video_url": "https://www.youtube.com/watch?v=8MMSS2F5vtc",
        "doc_urls": [
            "https://github.com/RodZill4/material-maker/wiki",
            "https://docs.blender.org/manual/en/latest/files/import_export.html",
        ],
        "lesson_wiki_path": "docs/academy/tracks/a01-organic-pbr.md",
        "evidence_path": "training/texturing/a01/",
        "academy_track": "A01",
    },
    "Ucupaint": {
        "primary_video_url": "https://www.youtube.com/watch?v=d3KrMwAWJI0",
        "doc_urls": [
            "https://github.com/ucupumar/ucupaint",
            "https://docs.blender.org/manual/en/latest/sculpt_paint/texture_paint/index.html",
        ],
        "lesson_wiki_path": "docs/academy/tracks/a02-layered-textures.md",
        "evidence_path": "training/texturing/a02/",
        "academy_track": "A02",
    },
    "TripoSR": {
        "primary_video_url": "https://www.youtube.com/watch?v=e2UeHwzncHA",
        "doc_urls": [
            "https://github.com/VAST-AI-Research/TripoSR",
            "https://github.com/VAST-AI-Research/TripoSR/blob/main/LICENSE",
        ],
        "lesson_wiki_path": "docs/production/tools/triposr.md",
        "evidence_path": "training/modeling/triposr/",
        "academy_track": "A-model",
    },
    "RetopoFlow": {
        "primary_video_url": "https://www.youtube.com/watch?v=Ds5Soybs610",
        "doc_urls": [
            "https://github.com/CGCookie/retopoflow",
            "https://docs.blender.org/manual/en/latest/modeling/meshes/retopology.html",
        ],
        "lesson_wiki_path": "docs/academy/tracks/a03-retopology.md",
        "evidence_path": "training/modeling/a03/",
        "license_note_path": "docs/production/tools/retopoflow.md",
        "academy_track": "A03",
    },
    "Poly Haven": {
        "primary_video_url": "https://www.youtube.com/watch?v=ku_xv6WV6UE",
        "doc_urls": [
            "https://polyhaven.com/license",
            "https://docs.blender.org/manual/en/latest/files/asset_libraries/introduction.html",
        ],
        "lesson_wiki_path": "docs/production/tools/poly-haven.md",
        "evidence_path": "training/texturing/assets/",
    },
    "ambientCG": {
        "primary_video_url": "https://www.youtube.com/watch?v=fUZHyoeuwVI",
        "doc_urls": [
            "https://ambientcg.com/license",
            "https://docs.blender.org/manual/en/latest/files/import_export.html",
        ],
        "lesson_wiki_path": "docs/production/tools/ambientcg.md",
        "evidence_path": "training/texturing/assets/",
    },
}


def seed_baseline(db: LibrarianDB) -> dict:
    created = 0
    merged = 0
    evidence_updated = 0
    for item in BASELINE_RESOURCES:
        resource, was_created = db.add(**item, source_type="curated-baseline")
        created += int(was_created)
        merged += int(not was_created)
        defaults = EVIDENCE_DEFAULTS.get(resource.name)
        if defaults:
            db.update_evidence(resource.id, **defaults)
            evidence_updated += 1
    return {
        "seen": len(BASELINE_RESOURCES),
        "created": created,
        "merged": merged,
        "evidence_updated": evidence_updated,
    }
