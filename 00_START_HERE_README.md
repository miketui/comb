# TAYLKOMB Designer Handoff — Curated Package
Date: 2026-04-03

## What this package is
This is a cleaned, designer-facing handoff built from the uploaded ZIP. It removes duplicate "final" folders, backup bundles, archive layers, and Mac metadata so the designer can work from one package.

## Recommended source of truth
Use these folders in this order:
1. `01_Project_Brief/` — product intent, architecture, revision matrix, handoff checklist
2. `02_CAD_Source/` — source scripts and parametric references
3. `03_Reference_Geometry/` — STEP/STL/glTF reference geometry
4. `04_Drawings/` — drawing PDFs
5. `05_Specs_and_Testing/` — tolerance, hardware, material, fit, inspection, and testing docs
6. `06_Concept_References/` — original concept PDFs/renders for visual context only

## What I removed from the original ZIP
- duplicate package copies (`final_zip`, `Finalized/final_zip`, backup packages)
- nested archives
- `__MACOSX` junk files
- repeated copies of the same STEP/STL/script assets

## Important designer note
The current package is strong for handoff, but it still appears to require a **native parametric rebuild in the target CAD system** before tooling release. Treat the supplied STEP files as reference geometry unless the receiving engineer validates them as production-usable.

## Folder map
- `01_Project_Brief/` — PRD, architecture, ergonomics, revision matrix, architecture SVG
- `02_CAD_Source/` — OpenSCAD, FreeCAD, alternate Build123d/CadQuery scripts
- `03_Reference_Geometry/` — STEP parametric, STEP converted, STL, glTF
- `04_Drawings/` — PDF drawings for tang, receiver, button, parts, assembly, interface
- `05_Specs_and_Testing/` — BOM/spec docs, test forms, fit coupons, inspection docs, output plans
- `06_Concept_References/` — original visual/context files
- `05_Admin_and_Audit/` — package README from source, gap analysis, generator scripts

## Package stats
- Total files: 136
- File types: .csv:1, .gltf:9, .json:1, .md:16, .mp4:1, .pdf:35, .png:2, .py:22, .scad:16, .sh:1, .step:19, .stl:11, .svg:2

See also:
- `00_FILE_INDEX.csv`
- `00_NEXT_STEPS_FOR_DESIGNER.md`
- `00_MISSING_OR_PENDING_ITEMS.md`
- `00_ORIGINAL_ZIP_ANALYSIS.md`
