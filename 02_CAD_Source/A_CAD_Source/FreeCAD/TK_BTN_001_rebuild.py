"""
TK-BTN-001 Button/Detent Assembly
Push-button release with spring bore, ball pocket, and snap-fit clip
FreeCAD Parametric Rebuild Script
Generated: 2026-04-02 | Rev A
"""

import FreeCAD, Part, Sketcher
doc = FreeCAD.newDocument("TK_BTN_001")

# ── Parameters ──
btn_dia = 8.0        # Button head diameter (mm)
btn_height = 5.0     # Button head height
shaft_dia = 4.0      # Shaft diameter
shaft_len = 12.0     # Shaft length
spring_bore_dia = 4.5  # Spring bore diameter
spring_bore_depth = 8.0
ball_pocket_dia = 4.85  # Slightly larger than 4.763mm ball
ball_pocket_depth = 3.5
clip_width = 1.5     # Snap-fit clip width
clip_depth = 0.8     # Clip engagement depth
fillet_r = 0.3

# ── Button Head ──
head = Part.makeCylinder(btn_dia/2, btn_height)
head_fillet = head.makeFillet(fillet_r, head.Edges)

# ── Shaft ──
shaft = Part.makeCylinder(shaft_dia/2, shaft_len)
shaft.translate(FreeCAD.Vector(0, 0, -shaft_len))

# ── Spring Bore (into shaft) ──
bore = Part.makeCylinder(spring_bore_dia/2, spring_bore_depth)
bore.translate(FreeCAD.Vector(0, 0, -(shaft_len)))

# ── Ball Pocket (end of shaft) ──
pocket = Part.makeSphere(ball_pocket_dia/2)
pocket.translate(FreeCAD.Vector(0, 0, -(shaft_len - ball_pocket_depth)))

# ── Combine ──
button = head_fillet.fuse(shaft)
button = button.cut(bore)
button = button.cut(pocket)

# ── Snap-fit Clip (2x opposing) ──
for angle in [0, 180]:
    import math
    rad = math.radians(angle)
    clip_box = Part.makeBox(clip_width, clip_depth, 3.0)
    clip_box.translate(FreeCAD.Vector(
        shaft_dia/2 * math.cos(rad) - clip_width/2,
        shaft_dia/2 * math.sin(rad),
        -(shaft_len * 0.7)
    ))
    button = button.fuse(clip_box)

obj = doc.addObject("Part::Feature", "Button_Detent")
obj.Shape = button

# ── Feature Tree Labels ──
doc.recompute()
doc.saveAs("/tmp/TK_BTN_001.FCStd")
print("TK-BTN-001 Button/Detent Assembly built successfully")
