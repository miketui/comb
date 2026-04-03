"""
TAYLKOMB Handle Family — CORRECTED — build123d
Document: TK-IF-002 / TK-LOCK-002 Compliant
Date: April 2, 2026

ALL THREE HANDLES are FEMALE RECEIVERS with integrated lock hardware.
Each shares the identical receiver core; only the outer body shape differs.

  TH-001 Double Handle (fork/two-prong) — stainless steel
  TH-002 Flat Handle (rattail/spatula) — stainless steel
  TH-003 Round Handle (pintail) — stainless steel

Requirements: pip install build123d
"""

from build123d import *

# ============================================================
# SHARED RECEIVER PARAMETERS (TK-IF-002)
# ============================================================

SLOT_WIDTH = 5.18;  SLOT_THICKNESS = 2.64;  SLOT_DEPTH = 46.00
SLOT_CORNER_R = 0.30;  SLOT_CHAMFER = 1.00
RECEIVER_WIDTH = 8.00;  RECEIVER_HEIGHT = 16.00;  RECEIVER_LENGTH = 55.00

BALL_WINDOW_DIA = 2.50;  LOCK_Z = 35.00
SPRING_POCKET_DIA = 3.20;  SPRING_POCKET_DEPTH = 8.00
BUTTON_BORE_DIA = 4.00
MAG_DIA = 4.00;  MAG_POCKET_DEPTH = 2.20;  MAG_OFFSET_Y = 4.50

# Handle body dimensions
TH001_BODY_LENGTH = 192.00   # Double handle body
TH001_FORK_WIDTH = 16.00
TH001_CROSS_W = 27.20
TH001_CROSS_H = 8.00

TH002_BODY_LENGTH = 204.95   # Flat handle body
TH002_TIP_WIDTH = 7.64
TH002_THICKNESS = 2.54

TH003_BODY_LENGTH = 187.20   # Round handle body
TH003_DIA = 3.11


def _build_receiver_block():
    """Build the universal receiver block with all lock hardware bores."""
    # Receiver outer block
    with BuildSketch():
        RectangleRounded(RECEIVER_WIDTH, RECEIVER_HEIGHT, 1.0)
    extrude(amount=RECEIVER_LENGTH)
    # Tang slot
    with BuildSketch():
        RectangleRounded(SLOT_THICKNESS, SLOT_WIDTH, SLOT_CORNER_R)
    extrude(amount=SLOT_DEPTH, mode=Mode.SUBTRACT)
    # Opening chamfer
    with BuildSketch(Plane.XY.offset(-0.01)):
        RectangleRounded(SLOT_THICKNESS + SLOT_CHAMFER*2,
                         SLOT_WIDTH + SLOT_CHAMFER*2, SLOT_CORNER_R+0.5)
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


def build_th001_double_handle():
    """TH-001 Double Handle (fork) — FEMALE RECEIVER.
    Two-prong fork for sectioning, weaving, and flat iron work.
    Material: 316L stainless steel with glue-resistant coating.
    """
    with BuildPart() as p:
        _build_receiver_block()
        # Transition zone
        with BuildSketch(Plane.XY.offset(-10)):
            RectangleRounded(TH001_CROSS_H, TH001_CROSS_W * 0.7, 1.5)
        extrude(amount=10)
        # Handle body (simplified as rectangle)
        with BuildSketch(Plane.XY.offset(-10 - TH001_BODY_LENGTH)):
            RectangleRounded(TH001_CROSS_H * 0.8, TH001_FORK_WIDTH, 1.0)
        extrude(amount=TH001_BODY_LENGTH)
    return p.part


def build_th002_flat_handle():
    """TH-002 Flat Handle (rattail/spatula) — FEMALE RECEIVER.
    Flat applicator for wig work, edge control, weft pressing.
    Material: 316L stainless steel with glue-resistant coating.
    """
    with BuildPart() as p:
        _build_receiver_block()
        # Transition zone
        with BuildSketch(Plane.XY.offset(-10)):
            RectangleRounded(TH002_THICKNESS * 2, RECEIVER_HEIGHT * 0.5, 1.0)
        extrude(amount=10)
        # Flat body (tapers from wider to narrower)
        with BuildSketch(Plane.XY.offset(-10 - TH002_BODY_LENGTH)):
            RectangleRounded(TH002_THICKNESS, TH002_TIP_WIDTH, 0.5)
        extrude(amount=TH002_BODY_LENGTH)
    return p.part


def build_th003_round_handle():
    """TH-003 Round Handle (pintail) — FEMALE RECEIVER.
    Long pointed rod for precision parting, foil work, extension manipulation.
    Material: 316L stainless steel with glue-resistant coating.
    """
    with BuildPart() as p:
        _build_receiver_block()
        # Transition zone
        with BuildSketch(Plane.XY.offset(-10)):
            Circle(radius=TH003_DIA * 1.5)
        extrude(amount=10)
        # Round body
        with BuildSketch(Plane.XY.offset(-10 - TH003_BODY_LENGTH)):
            Circle(radius=TH003_DIA / 2)
        extrude(amount=TH003_BODY_LENGTH)
    return p.part


if __name__ == "__main__":
    print("TAYLKOMB HANDLE FAMILY — CORRECTED")
    print("  All 3 handles: FEMALE RECEIVERS with integrated lock")
    print()
    handles = [
        ("TH-001", "Double Handle (fork)", build_th001_double_handle),
        ("TH-002", "Flat Handle (rattail)", build_th002_flat_handle),
        ("TH-003", "Round Handle (pintail)", build_th003_round_handle),
    ]
    for pid, name, fn in handles:
        print(f"  {pid} {name}")
        print(f"    Receiver: {RECEIVER_WIDTH}x{RECEIVER_HEIGHT}x{RECEIVER_LENGTH} mm")
        print(f"    Lock: ball detent + spring + button")
        print(f"    Material: 316L stainless steel")
        try:
            part = fn()
            part.export_step(f"{pid}_Corrected.step")
            part.export_stl(f"{pid}_Corrected.stl")
            print(f"    Exported: {pid}_Corrected.step/.stl")
        except Exception as e:
            print(f"    Skip: {e}")
        print()
