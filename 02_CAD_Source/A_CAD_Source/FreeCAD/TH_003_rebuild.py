"""
TH-003 Round Comfort Handle
150mm round barrel handle with single tang receptacle
FreeCAD Parametric Rebuild Script
Generated: 2026-04-02 | Rev A
"""

import FreeCAD, Part
doc = FreeCAD.newDocument("TH_003")

# ── Parameters ──
total_length = 150.0
barrel_dia = 28.0
tang_socket_dia = 12.5
tang_socket_depth = 15.0
end_cap_height = 5.0
end_cap_dia = 30.0
grip_groove_count = 20
grip_groove_depth = 0.4

# ── Main Barrel ──
barrel = Part.makeCylinder(barrel_dia/2, total_length)

# ── End Cap (slightly wider, decorative) ──
cap = Part.makeCylinder(end_cap_dia/2, end_cap_height)
cap.translate(FreeCAD.Vector(0, 0, total_length - end_cap_height))
handle = barrel.fuse(cap)

# ── Tang Socket ──
socket = Part.makeCylinder(tang_socket_dia/2, tang_socket_depth)
handle = handle.cut(socket)

# ── Circumferential Grip Grooves ──
for i in range(grip_groove_count):
    z = 20 + i * (total_length - 45) / (grip_groove_count - 1)
    groove = Part.makeTorus(barrel_dia/2, grip_groove_depth)
    groove.translate(FreeCAD.Vector(0, 0, z))
    handle = handle.cut(groove)

# ── Fillet exposed edges ──
try:
    handle = handle.makeFillet(1.0, handle.Edges[:4])
except:
    pass  # Skip if fillet fails on complex geometry

obj = doc.addObject("Part::Feature", "Round_Handle")
obj.Shape = handle
doc.recompute()
doc.saveAs("/tmp/TH_003.FCStd")
print("TH-003 Round Comfort Handle built successfully")
