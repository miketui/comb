"""
TH-001 Double-Ended Handle
185mm handle with tang receptacle at both ends
FreeCAD Parametric Rebuild Script
Generated: 2026-04-02 | Rev A
"""

import FreeCAD, Part
doc = FreeCAD.newDocument("TH_001")

# ── Parameters ──
total_length = 185.0
grip_dia = 22.0
waist_dia = 18.0
tang_socket_dia = 12.5
tang_socket_depth = 15.0
grip_texture_depth = 0.5
grip_texture_width = 1.0
grip_texture_count = 24
fillet_r = 1.0

import math

# ── Main barrel (ergonomic profile with waist) ──
pts = []
for i in range(100):
    z = i * total_length / 99
    t = z / total_length
    # Sinusoidal ergonomic profile: wider at ends, narrower at center
    r = waist_dia/2 + (grip_dia/2 - waist_dia/2) * abs(math.cos(math.pi * t))
    pts.append(FreeCAD.Vector(r, 0, z))

# Build as simple cylinder with boolean ops for reliability
barrel = Part.makeCylinder(grip_dia/2, total_length)

# ── Tang Sockets (both ends) ──
socket_bottom = Part.makeCylinder(tang_socket_dia/2, tang_socket_depth)
socket_top = Part.makeCylinder(tang_socket_dia/2, tang_socket_depth)
socket_top.translate(FreeCAD.Vector(0, 0, total_length - tang_socket_depth))

handle = barrel.cut(socket_bottom).cut(socket_top)

# ── Grip Texture (circumferential grooves) ──
for i in range(grip_texture_count):
    z = 25 + i * (total_length - 50) / (grip_texture_count - 1)
    groove = Part.makeTorus(grip_dia/2, grip_texture_depth)
    groove.translate(FreeCAD.Vector(0, 0, z))
    handle = handle.cut(groove)

obj = doc.addObject("Part::Feature", "Double_Handle")
obj.Shape = handle
doc.recompute()
doc.saveAs("/tmp/TH_001.FCStd")
print("TH-001 Double-Ended Handle built successfully")
