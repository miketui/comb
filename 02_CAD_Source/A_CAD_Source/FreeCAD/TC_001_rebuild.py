"""
TC-001 Main Styling Comb
32-tooth main comb with receiver socket and alignment ribs
FreeCAD Parametric Rebuild Script
Generated: 2026-04-02 | Rev A
"""

import FreeCAD, Part
doc = FreeCAD.newDocument("TC_001")

# ── Parameters ──
spine_length = 85.0
spine_width = 8.0
spine_height = 5.0
tooth_count = 32
tooth_pitch = 1.2     # mm center-to-center
tooth_length = 45.0
tooth_width = 0.8
tooth_taper = 0.6     # tip width
recv_socket_dia = 12.5
recv_socket_depth = 15.0
rib_width = 1.0
rib_height = 1.5
fillet_r = 0.2

# ── Spine ──
spine = Part.makeBox(spine_length, spine_width, spine_height)
spine.translate(FreeCAD.Vector(-spine_length/2, -spine_width/2, 0))

# ── Teeth ──
teeth_start_x = -((tooth_count - 1) * tooth_pitch) / 2
comb = spine
for i in range(tooth_count):
    x = teeth_start_x + i * tooth_pitch
    # Tapered tooth profile
    tooth = Part.makeBox(tooth_width, spine_width, tooth_length)
    tooth.translate(FreeCAD.Vector(x - tooth_width/2, -spine_width/2, spine_height))
    comb = comb.fuse(tooth)

# ── Receiver Socket (bottom center) ──
socket = Part.makeCylinder(recv_socket_dia/2, recv_socket_depth)
socket.translate(FreeCAD.Vector(0, 0, -recv_socket_depth))
comb = comb.cut(socket)

# ── Alignment Ribs ──
for offset in [-3.0, 3.0]:
    rib = Part.makeBox(rib_width, rib_height, recv_socket_depth * 0.8)
    rib.translate(FreeCAD.Vector(offset - rib_width/2, recv_socket_dia/2, -recv_socket_depth * 0.8))
    comb = comb.fuse(rib)

obj = doc.addObject("Part::Feature", "Main_Comb")
obj.Shape = comb
doc.recompute()
doc.saveAs("/tmp/TC_001.FCStd")
print("TC-001 Main Styling Comb built successfully")
