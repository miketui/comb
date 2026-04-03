"""
TH-002 Flat Ergonomic Handle
160mm flat-profile handle with textured grip surface
FreeCAD Parametric Rebuild Script
Generated: 2026-04-02 | Rev A
"""

import FreeCAD, Part
doc = FreeCAD.newDocument("TH_002")

# ── Parameters ──
total_length = 160.0
width = 28.0
thickness = 12.0
tang_socket_dia = 12.5
tang_socket_depth = 15.0
grip_zone_start = 20.0
grip_zone_end = 140.0
texture_count = 16
texture_depth = 0.4
corner_r = 3.0

# ── Main Body (rounded rectangle profile) ──
body = Part.makeBox(width, thickness, total_length)
body.translate(FreeCAD.Vector(-width/2, -thickness/2, 0))
body = body.makeFillet(corner_r, body.Edges)

# ── Tang Socket ──
socket = Part.makeCylinder(tang_socket_dia/2, tang_socket_depth)
body = body.cut(socket)

# ── Grip Textures (transverse grooves on flat faces) ──
for i in range(texture_count):
    z = grip_zone_start + i * (grip_zone_end - grip_zone_start) / (texture_count - 1)
    groove = Part.makeBox(width + 2, texture_depth * 2, 1.0)
    groove.translate(FreeCAD.Vector(-width/2 - 1, thickness/2 - texture_depth, z - 0.5))
    body = body.cut(groove)
    groove2 = Part.makeBox(width + 2, texture_depth * 2, 1.0)
    groove2.translate(FreeCAD.Vector(-width/2 - 1, -thickness/2 - texture_depth, z - 0.5))
    body = body.cut(groove2)

obj = doc.addObject("Part::Feature", "Flat_Handle")
obj.Shape = body
doc.recompute()
doc.saveAs("/tmp/TH_002.FCStd")
print("TH-002 Flat Ergonomic Handle built successfully")
