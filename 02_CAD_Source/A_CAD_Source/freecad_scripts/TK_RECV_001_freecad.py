"""
FreeCAD Parametric Rebuild Script: TK-RECV-001 Female Receiver Core
===================================================================
TAYLKOMB LLC · Patent Pending · Confidential

INSTRUCTIONS:
1. Open FreeCAD (0.21+)
2. Run: exec(open("TK_RECV_001_freecad.py").read())
3. Edit Parameters spreadsheet to modify any dimension

Feature Tree:
  F01: Outer Cylinder
  F02: Main Bore (cut)
  F03: Mouth Chamfer (cut)
  F04: Ball Bore - radial through-hole (cut)
  F05: Spring Pocket - radial blind hole (cut)
  F06: Button Bore - radial through-hole (cut)
  F07: Magnet Pocket - axial blind hole (cut)
"""

import FreeCAD
import Part
from FreeCAD import Vector, Rotation, Placement
import math

doc = FreeCAD.newDocument("TK-RECV-001_Female_Receiver_Core")

# ============================================================
# PARAMETERS
# ============================================================
ss = doc.addObject("Spreadsheet::Sheet", "Parameters")
ss.set("A1", "Parameter"); ss.set("B1", "Value"); ss.set("C1", "Unit")

params = [
    ("bore_diameter", 10.10, "mm"),
    ("bore_depth", 40.00, "mm"),
    ("wall_thickness", 2.50, "mm"),
    ("outer_diameter", 15.10, "mm"),
    ("ball_bore_diameter", 3.30, "mm"),
    ("ball_bore_from_mouth", 10.00, "mm"),
    ("spring_pocket_dia", 3.60, "mm"),
    ("spring_pocket_depth", 10.00, "mm"),
    ("button_bore_dia", 4.20, "mm"),
    ("button_bore_depth", 12.00, "mm"),
    ("mouth_chamfer", 0.50, "mm"),
    ("magnet_pocket_dia", 6.10, "mm"),
    ("magnet_pocket_depth", 2.10, "mm"),
    ("total_length", 42.50, "mm"),  # bore_depth + wall
]

for i, (name, value, unit) in enumerate(params):
    row = i + 2
    ss.set(f"A{row}", name); ss.set(f"B{row}", str(value)); ss.set(f"C{row}", unit)
    ss.setAlias(f"B{row}", name)
ss.recompute()

# ============================================================
# FEATURE TREE
# ============================================================

# F01: Outer body
outer = doc.addObject("Part::Cylinder", "F01_Outer_Body")
outer.Radius = 7.55
outer.Height = 42.5
outer.setExpression("Radius", "Parameters.outer_diameter / 2")
outer.setExpression("Height", "Parameters.total_length")

# F02: Main bore
bore = doc.addObject("Part::Cylinder", "F02_Main_Bore")
bore.Radius = 5.05
bore.Height = 40.01
bore.Placement.Base = Vector(0, 0, -0.01)
bore.setExpression("Radius", "Parameters.bore_diameter / 2")
bore.setExpression("Height", "Parameters.bore_depth + 0.01")

bored = doc.addObject("Part::Cut", "Recv_Bored")
bored.Base = outer; bored.Tool = bore

# F03: Mouth chamfer
chamfer = doc.addObject("Part::Cone", "F03_Mouth_Chamfer")
chamfer.Radius1 = 5.55  # bore_dia/2 + chamfer
chamfer.Radius2 = 5.05  # bore_dia/2
chamfer.Height = 0.51
chamfer.Placement.Base = Vector(0, 0, -0.01)
chamfer.setExpression("Radius1", "Parameters.bore_diameter / 2 + Parameters.mouth_chamfer")
chamfer.setExpression("Radius2", "Parameters.bore_diameter / 2")
chamfer.setExpression("Height", "Parameters.mouth_chamfer + 0.01")

chamfered = doc.addObject("Part::Cut", "Recv_Chamfered")
chamfered.Base = bored; chamfered.Tool = chamfer

# F04: Ball bore (radial, at ball_bore_from_mouth position)
ball_bore = doc.addObject("Part::Cylinder", "F04_Ball_Bore")
ball_bore.Radius = 1.65
ball_bore.Height = 20  # through both walls
ball_bore.setExpression("Radius", "Parameters.ball_bore_diameter / 2")
# Position: rotate to be radial, at correct Z position
ball_z = 40.0 - 10.0  # bore_depth - ball_bore_from_mouth
ball_bore.Placement = Placement(
    Vector(0, 0, ball_z),
    Rotation(Vector(0, 1, 0), 90)
)
ball_bore.Placement.Base = Vector(-10, 0, ball_z)

ball_bored = doc.addObject("Part::Cut", "Recv_BallBored")
ball_bored.Base = chamfered; ball_bored.Tool = ball_bore

# F05: Spring pocket (radial, behind ball bore, 180° from button)
spring_pocket = doc.addObject("Part::Cylinder", "F05_Spring_Pocket")
spring_pocket.Radius = 1.80
spring_pocket.Height = 10.0
spring_pocket.setExpression("Radius", "Parameters.spring_pocket_dia / 2")
spring_pocket.setExpression("Height", "Parameters.spring_pocket_depth")
spring_pocket.Placement = Placement(
    Vector(5.05, 0, ball_z),  # starts at bore wall, goes outward
    Rotation(Vector(0, 1, 0), 90)
)

spring_cut = doc.addObject("Part::Cut", "Recv_SpringPocket")
spring_cut.Base = ball_bored; spring_cut.Tool = spring_pocket

# F06: Button bore (radial, 90° from ball bore)
button_bore = doc.addObject("Part::Cylinder", "F06_Button_Bore")
button_bore.Radius = 2.10
button_bore.Height = 20
button_bore.setExpression("Radius", "Parameters.button_bore_dia / 2")
button_bore.Placement = Placement(
    Vector(0, -10, ball_z),
    Rotation(Vector(1, 0, 0), 90)
)

button_cut = doc.addObject("Part::Cut", "Recv_ButtonBored")
button_cut.Base = spring_cut; button_cut.Tool = button_bore

# F07: Magnet pocket (axial, at bottom of bore)
magnet_pocket = doc.addObject("Part::Cylinder", "F07_Magnet_Pocket")
magnet_pocket.Radius = 3.05
magnet_pocket.Height = 2.10
magnet_pocket.Placement.Base = Vector(0, 0, 40.0 - 2.10)
magnet_pocket.setExpression("Radius", "Parameters.magnet_pocket_dia / 2")
magnet_pocket.setExpression("Height", "Parameters.magnet_pocket_depth")

final = doc.addObject("Part::Cut", "TK_RECV_001_Final")
final.Base = button_cut; final.Tool = magnet_pocket
final.Label = "TK-RECV-001 Female Receiver Core"

# Visibility
for obj in doc.Objects:
    if hasattr(obj, 'ViewObject') and obj.Label not in ["TK-RECV-001 Female Receiver Core", "Parameters"]:
        try: obj.ViewObject.Visibility = False
        except: pass

doc.recompute()
Part.export([final], "/tmp/TK-RECV-001.step")

print("TK-RECV-001 Female Receiver Core — parametric model created!")
print("Features: 7 | Parameters: 14 | Edit via 'Parameters' spreadsheet")
