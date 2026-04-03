"""
TC-003 Wide Styling Comb
20-tooth wide comb for thick/textured hair
FreeCAD Parametric Rebuild Script
Generated: 2026-04-02 | Rev A
"""

import FreeCAD, Part
doc = FreeCAD.newDocument("TC_003")

# ── Parameters ──
spine_length = 95.0
spine_width = 10.0
spine_height = 5.5
tooth_count = 20
tooth_pitch = 2.0
tooth_length = 50.0
tooth_width = 1.2
recv_socket_dia = 12.5
recv_socket_depth = 15.0

# ── Spine ──
spine = Part.makeBox(spine_length, spine_width, spine_height)
spine.translate(FreeCAD.Vector(-spine_length/2, -spine_width/2, 0))

comb = spine
teeth_start = -((tooth_count - 1) * tooth_pitch) / 2
for i in range(tooth_count):
    x = teeth_start + i * tooth_pitch
    tooth = Part.makeBox(tooth_width, spine_width, tooth_length)
    tooth.translate(FreeCAD.Vector(x - tooth_width/2, -spine_width/2, spine_height))
    comb = comb.fuse(tooth)

socket = Part.makeCylinder(recv_socket_dia/2, recv_socket_depth)
socket.translate(FreeCAD.Vector(0, 0, -recv_socket_depth))
comb = comb.cut(socket)

obj = doc.addObject("Part::Feature", "Wide_Comb")
obj.Shape = comb
doc.recompute()
doc.saveAs("/tmp/TC_003.FCStd")
print("TC-003 Wide Styling Comb built successfully")
