# Taylkomb FreeCAD Parametric Rebuild Scripts

## Overview
These Python scripts create **native parametric CAD models** in FreeCAD with:
- ✅ Spreadsheet-driven parameters (change any dimension)
- ✅ Full feature tree with design intent
- ✅ Constraint history
- ✅ STEP export capability
- ✅ Design history preserved in feature order

## Requirements
- FreeCAD 0.21 or later (free, open-source)
- Download: https://www.freecad.org/downloads.php

## How to Use
1. Open FreeCAD
2. Open the Python console: `View → Panels → Python Console`
3. Run a script: `exec(open("script_name.py").read())`
4. The model appears with full feature tree in the Model panel
5. Edit dimensions via the **Parameters** spreadsheet
6. Right-click any feature to suppress, modify, or reorder

## Scripts

| Script | Part Number | Description |
|--------|-------------|-------------|
| `TK_TANG_001_freecad.py` | TK-TANG-001 | Passive Male Tang (10 features) |
| `TK_RECV_001_freecad.py` | TK-RECV-001 | Female Receiver Core (7 features) |

### Additional parts (rebuild from scratch using these as templates):
- TC-001 Main Comb → Use `TK_TANG_001_freecad.py` as interface reference
- TC-002 Narrow Comb
- TC-003 Wide Comb
- TH-001 Double Handle
- TH-002 Flat Handle  
- TH-003 Round Handle

## Parametric Editing
Each script creates a **Parameters** spreadsheet. To modify:
1. Double-click "Parameters" in the Model tree
2. Change any value in column B
3. Press Enter, then `Ctrl+Shift+R` to recompute
4. All dependent features update automatically

## STEP Export
After building, export production STEP:
```
Part.export([final_part], "output.step")
```

## Design Intent Notes
- All features are built in manufacturing sequence
- Boolean operations preserve the design tree
- Datum references match the manufacturing drawing datums
- Interface geometry (tang OD, receiver bore) uses tolerance-class aliases

---
TAYLKOMB LLC · Patent Pending · Confidential Engineering Documentation
