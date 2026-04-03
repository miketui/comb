"""
TAYLKOMB Comb Family — CORRECTED — build123d
Document: TK-IF-002 / TK-LOCK-002 Compliant
Date: April 2, 2026

CORRECTED ARCHITECTURE:
  TC-001 Main Comb = SOLE MALE (passive tang, no lock hardware)
  TC-002 Narrow Comb = FEMALE RECEIVER (lock hardware inside)
  TC-003 Wide Comb = FEMALE RECEIVER (lock hardware inside)

TC-002 and TC-003 dock INVERTED onto TC-001, creating double-ended comb tools.

Requirements: pip install build123d
"""

from build123d import *

# ============================================================
# SHARED INTERFACE PARAMETERS (TK-IF-002)
# ============================================================

TANG_WIDTH = 5.08;  TANG_THICKNESS = 2.54;  TANG_LENGTH = 50.80
TANG_CORNER_R = 0.25;  TANG_CHAMFER = 0.50
SHOULDER_WIDTH = 8.00;  SHOULDER_HEIGHT = 16.00;  SHOULDER_DEPTH = 5.00
NOTCH_FROM_TIP = 35.00;  NOTCH_DEPTH = 0.80;  NOTCH_WIDTH_Z = 3.00
BALL_DIA = 3.00

SLOT_WIDTH = 5.18;  SLOT_THICKNESS = 2.64;  SLOT_DEPTH = 46.00
SLOT_CORNER_R = 0.30;  SLOT_CHAMFER = 1.00
RECEIVER_WIDTH = SHOULDER_WIDTH;  RECEIVER_HEIGHT = SHOULDER_HEIGHT
RECEIVER_LENGTH = 55.00

BALL_WINDOW_DIA = 2.50;  LOCK_Z = 35.00
SPRING_POCKET_DIA = 3.20;  SPRING_POCKET_DEPTH = 8.00
BUTTON_BORE_DIA = 4.00
MAG_DIA = 4.00;  MAG_POCKET_DEPTH = 2.20;  MAG_OFFSET_Y = 4.50

# Comb body envelopes
TC001_LENGTH = 228.81;  TC002_LENGTH = 223.67;  TC003_LENGTH = 223.23
SPINE_THICKNESS = 8.00;  COMB_HEIGHT = 50.80


def _add_receiver_features(part_builder):
    """Add universal receiver features (slot, lock bores, magnet pockets) to a part.
    Call this inside a BuildPart context after the receiver block is extruded."""
    # Tang slot
    with BuildSketch():
        RectangleRounded(SLOT_THICKNESS, SLOT_WIDTH, SLOT_CORNER_R)
    extrude(amount=SLOT_DEPTH, mode=Mode.SUBTRACT)
    # Opening chamfer
    with BuildSketch(Plane.XY.offset(-0.01)):
        RectangleRounded(SLOT_THICKNESS + SLOT_CHAMFER*2, SLOT_WIDTH + SLOT_CHAMFER*2, SLOT_CORNER_R+0.5)
    extrude(amount=SLOT_CHAMFER, mode=Mode.SUBTRACT)
    # Ball window
    with BuildSketch(Plane.YZ.offset(RECEIVER_WIDTH/2)):
        with Locations([(LOCK_Z, 0)]): Circle(radius=BALL_WINDOW_DIA/2)
    extrude(amount=-RECEIVER_WIDTH, mode=Mode.SUBTRACT)
    # Spring pocket
    with BuildSketch(Plane.YZ.offset(-RECEIVER_WIDTH/2)):
        with Locations([(LOCK_Z, 0)]): Circle(radius=SPRING_POCKET_DIA/2)
    extrude(amount=SPRING_POCKET_DEPTH, mode=Mode.SUBTRACT)
    # Button bore
    with BuildSketch(Plane.YZ.offset(RECEIVER_WIDTH/2)):
        with Locations([(LOCK_Z, 0)]): Circle(radius=BUTTON_BORE_DIA/2)
    extrude(amount=-(RECEIVER_WIDTH/2 - SLOT_THICKNESS/2 + 0.5), mode=Mode.SUBTRACT)
    # Magnet pockets
    for y_off in [MAG_OFFSET_Y, -MAG_OFFSET_Y]:
        with BuildSketch(Plane.XY.offset(RECEIVER_LENGTH)):
            with Locations([(0, y_off)]): Circle(radius=(MAG_DIA+0.10)/2)
        extrude(amount=-MAG_POCKET_DEPTH, mode=Mode.SUBTRACT)


def build_tc001():
    """TC-001 Main Comb — SOLE MALE, passive tang, no lock hardware."""
    with BuildPart() as p:
        # Tang
        with BuildSketch(): RectangleRounded(TANG_THICKNESS, TANG_WIDTH, TANG_CORNER_R)
        extrude(amount=TANG_LENGTH)
        # Shoulder
        with BuildSketch(Plane.XY.offset(TANG_LENGTH)):
            RectangleRounded(SHOULDER_WIDTH, SHOULDER_HEIGHT, 1.0)
        extrude(amount=SHOULDER_DEPTH)
        # Comb spine (simplified)
        spine_len = TC001_LENGTH - TANG_LENGTH - SHOULDER_DEPTH
        with BuildSketch(Plane.XY.offset(TANG_LENGTH + SHOULDER_DEPTH)):
            RectangleRounded(SPINE_THICKNESS, COMB_HEIGHT * 0.35, 0.5)
        extrude(amount=spine_len)
        # Detent notch
        with BuildSketch(Plane.YZ.offset(TANG_THICKNESS/2)):
            with Locations([(0, NOTCH_FROM_TIP)]): Rectangle(NOTCH_WIDTH_Z, NOTCH_DEPTH*2)
        extrude(amount=-NOTCH_DEPTH-0.1, mode=Mode.SUBTRACT)
        # Magnet pockets in shoulder
        for y_off in [MAG_OFFSET_Y, -MAG_OFFSET_Y]:
            with BuildSketch(Plane.XY.offset(TANG_LENGTH)):
                with Locations([(0, y_off)]): Circle(radius=(MAG_DIA+0.10)/2)
            extrude(amount=-MAG_POCKET_DEPTH, mode=Mode.SUBTRACT)
    return p.part


def build_tc002():
    """TC-002 Narrow Comb — FEMALE RECEIVER, docks inverted onto TC-001."""
    with BuildPart() as p:
        # Receiver block
        with BuildSketch(): RectangleRounded(RECEIVER_WIDTH, RECEIVER_HEIGHT, 1.0)
        extrude(amount=RECEIVER_LENGTH)
        _add_receiver_features(p)
        # Comb body below receiver
        body_len = TC002_LENGTH - RECEIVER_LENGTH
        with BuildSketch(Plane.XY.offset(-body_len)):
            RectangleRounded(SPINE_THICKNESS, COMB_HEIGHT * 0.35, 0.5)
        extrude(amount=body_len)
    return p.part


def build_tc003():
    """TC-003 Wide Comb — FEMALE RECEIVER, docks inverted onto TC-001."""
    with BuildPart() as p:
        # Receiver block
        with BuildSketch(): RectangleRounded(RECEIVER_WIDTH, RECEIVER_HEIGHT, 1.0)
        extrude(amount=RECEIVER_LENGTH)
        _add_receiver_features(p)
        # Comb body below receiver
        body_len = TC003_LENGTH - RECEIVER_LENGTH
        with BuildSketch(Plane.XY.offset(-body_len)):
            RectangleRounded(SPINE_THICKNESS, COMB_HEIGHT * 0.40, 0.5)
        extrude(amount=body_len)
    return p.part


if __name__ == "__main__":
    print("TAYLKOMB COMB FAMILY — CORRECTED")
    print("  TC-001 Main Comb:   MALE (passive tang)")
    print("  TC-002 Narrow Comb: FEMALE (receiver + lock)")
    print("  TC-003 Wide Comb:   FEMALE (receiver + lock)")
    for fn, name in [(build_tc001,"TC-001"),(build_tc002,"TC-002"),(build_tc003,"TC-003")]:
        try:
            part = fn()
            part.export_step(f"{name}_Corrected.step")
            part.export_stl(f"{name}_Corrected.stl")
            print(f"  Exported {name}")
        except Exception as e:
            print(f"  Skip {name}: {e}")
