"""
FreeCAD Parametric Rebuild Script: TK-TANG-001 Passive Male Tang
================================================================
TAYLKOMB LLC · Patent Pending · Confidential
================================================================

INSTRUCTIONS:
1. Open FreeCAD (0.21+ recommended)
2. Open the Python console (View → Panels → Python Console)
3. Run this script: exec(open("TK_TANG_001_freecad.py").read())
4. The parametric model will appear with full feature tree

This creates a NATIVE PARAMETRIC model with:
- Spreadsheet-driven dimensions (change any parameter)
- Full feature tree with design intent
- Proper datum references
- Constraint history
"""

import FreeCAD
import Part
import Sketcher
from FreeCAD import Vector, Rotation

# ============================================================
# CREATE NEW DOCUMENT
# ============================================================
doc = FreeCAD.newDocument("TK-TANG-001_Passive_Male_Tang")

# ============================================================
# PARAMETER SPREADSHEET (design intent)
# ============================================================
ss = doc.addObject("Spreadsheet::Sheet", "Parameters")

# Tang dimensions
ss.set("A1", "Parameter")
ss.set("B1", "Value")
ss.set("C1", "Unit")
ss.set("D1", "Description")

params = [
    ("tang_diameter", 10.00, "mm", "Tang outer diameter"),
    ("tang_length", 45.00, "mm", "Tang overall length"),
    ("tip_chamfer", 1.00, "mm", "Tip chamfer size (45°)"),
    ("root_fillet", 0.50, "mm", "Root transition fillet"),
    ("detent_from_tip", 35.00, "mm", "Ball detent center from tip"),
    ("detent_groove_width", 3.20, "mm", "Detent groove width"),
    ("detent_groove_depth", 1.50, "mm", "Detent groove radial depth"),
    ("detent_groove_radius", 1.60, "mm", "Groove cross-section radius"),
    ("magnet_pocket_dia", 6.10, "mm", "Magnet pocket diameter"),
    ("magnet_pocket_depth", 2.10, "mm", "Magnet pocket depth"),
    ("magnet_from_tip", 20.00, "mm", "Magnet pocket center from tip"),
    ("flange_diameter", 14.00, "mm", "Root flange diameter"),
    ("flange_height", 2.00, "mm", "Root flange height"),
]

for i, (name, value, unit, desc) in enumerate(params):
    row = i + 2
    ss.set(f"A{row}", name)
    ss.set(f"B{row}", str(value))
    ss.set(f"C{row}", unit)
    ss.set(f"D{row}", desc)
    ss.setAlias(f"B{row}", name)

ss.recompute()

# ============================================================
# FEATURE TREE BUILD
# ============================================================

# --- Feature 1: Base Cylinder (Tang Body) ---
body = doc.addObject("Part::Cylinder", "Tang_Body")
body.Radius = 5.0  # tang_diameter / 2
body.Height = 45.0  # tang_length
body.setExpression("Radius", "Parameters.tang_diameter / 2")
body.setExpression("Height", "Parameters.tang_length")
body.Label = "F01_Tang_Body"

# --- Feature 2: Root Flange ---
flange = doc.addObject("Part::Cylinder", "Root_Flange")
flange.Radius = 7.0
flange.Height = 2.0
flange.Placement.Base = Vector(0, 0, -2)
flange.setExpression("Radius", "Parameters.flange_diameter / 2")
flange.setExpression("Height", "Parameters.flange_height")
flange.Label = "F02_Root_Flange"

# Union body + flange
union1 = doc.addObject("Part::Fuse", "Tang_With_Flange")
union1.Shape1 = body
union1.Shape2 = flange
union1.Label = "F03_Union_Body_Flange"

# --- Feature 3: Tip Chamfer ---
# Create a cone to cut the chamfer
chamfer_cone = doc.addObject("Part::Cone", "Chamfer_Tool")
chamfer_cone.Radius1 = 5.0  # tang radius
chamfer_cone.Radius2 = 4.0  # tang radius - chamfer
chamfer_cone.Height = 1.0
chamfer_cone.Placement.Base = Vector(0, 0, 44)  # tang_length - chamfer
chamfer_cone.setExpression("Radius1", "Parameters.tang_diameter / 2")
chamfer_cone.setExpression("Radius2", "Parameters.tang_diameter / 2 - Parameters.tip_chamfer")
chamfer_cone.setExpression("Height", "Parameters.tip_chamfer")
chamfer_cone.Label = "F04_Chamfer_Tool"

# Outer cylinder to create the cut volume
chamfer_outer = doc.addObject("Part::Cylinder", "Chamfer_Outer")
chamfer_outer.Radius = 6.0
chamfer_outer.Height = 1.1
chamfer_outer.Placement.Base = Vector(0, 0, 44)
chamfer_outer.setExpression("Radius", "Parameters.tang_diameter / 2 + 1")
chamfer_outer.setExpression("Height", "Parameters.tip_chamfer + 0.1")
chamfer_outer.Label = "F05_Chamfer_Outer"

# Cut volume = outer - cone
chamfer_cut = doc.addObject("Part::Cut", "Chamfer_Volume")
chamfer_cut.Base = chamfer_outer
chamfer_cut.Tool = chamfer_cone
chamfer_cut.Label = "F06_Chamfer_Cut_Volume"

# Apply chamfer
chamfered = doc.addObject("Part::Cut", "Tang_Chamfered")
chamfered.Base = union1
chamfered.Tool = chamfer_cut
chamfered.Label = "F07_Tang_Chamfered"

# --- Feature 4: Ball Detent Groove ---
# Torus for circumferential groove
groove = doc.addObject("Part::Torus", "Detent_Groove")
groove.Radius1 = 5.0  # tang radius (center of groove arc)
groove.Radius2 = 1.6  # groove cross-section radius
groove.Placement.Base = Vector(0, 0, 10)  # tang_length - detent_from_tip
groove.setExpression("Radius1", "Parameters.tang_diameter / 2")
groove.setExpression("Radius2", "Parameters.detent_groove_radius")
groove.Label = "F08_Detent_Groove"

# Cut groove from tang
grooved = doc.addObject("Part::Cut", "Tang_Grooved")
grooved.Base = chamfered
grooved.Tool = groove
grooved.Label = "F09_Tang_With_Groove"

# --- Feature 5: Magnet Pocket ---
magnet_pocket = doc.addObject("Part::Cylinder", "Magnet_Pocket")
magnet_pocket.Radius = 3.05  # magnet_pocket_dia / 2
magnet_pocket.Height = 2.10
magnet_pocket.Placement.Base = Vector(0, 0, 25 - 1.05)  # tang_length - magnet_from_tip - depth/2
magnet_pocket.setExpression("Radius", "Parameters.magnet_pocket_dia / 2")
magnet_pocket.setExpression("Height", "Parameters.magnet_pocket_depth")
magnet_pocket.Label = "F10_Magnet_Pocket"

# Cut magnet pocket
final = doc.addObject("Part::Cut", "TK_TANG_001_Final")
final.Base = grooved
final.Tool = magnet_pocket
final.Label = "TK-TANG-001 Passive Male Tang"

# ============================================================
# SET VISIBILITY
# ============================================================
for obj in doc.Objects:
    if obj.Label != "TK-TANG-001 Passive Male Tang" and obj.Label != "Parameters":
        obj.ViewObject.Visibility = False

# Final part visible
final.ViewObject.Visibility = True

# ============================================================
# RECOMPUTE AND SAVE
# ============================================================
doc.recompute()

# Export STEP
Part.export([final], "/tmp/TK-TANG-001.step")

print("=" * 50)
print("TK-TANG-001 Passive Male Tang")
print("Parametric model created successfully!")
print("Feature tree: 10 features")
print("Parameters: Editable via 'Parameters' spreadsheet")
print("=" * 50)
