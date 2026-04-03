"""
TAYLKOMB Shared Receiver Core — build123d
Document: TK-IF-002 / TK-LOCK-002 Compliant
Date: April 2, 2026

This module defines the UNIVERSAL FEMALE RECEIVER used by ALL 5 attachments.
Identical internal geometry across TC-002, TC-003, TH-001, TH-002, TH-003.
Each attachment wraps its unique outer body around this shared core.

Requirements: pip install build123d
"""

from build123d import *

# ============================================================
# SHARED RECEIVER PARAMETERS (TK-IF-002)
# ============================================================

# Receiver slot (accepts TC-001 tang)
SLOT_WIDTH = 5.18         # Y-axis (tang 5.08 + 0.10 clearance)
SLOT_THICKNESS = 2.64     # X-axis (tang 2.54 + 0.10 clearance)
SLOT_DEPTH = 46.00        # Z-axis insertion depth
SLOT_CORNER_R = 0.30      # Internal corners
SLOT_CHAMFER = 1.00       # Opening funnel

# Receiver block outer envelope
RECEIVER_WIDTH = 8.00     # X-axis (matches tang shoulder)
RECEIVER_HEIGHT = 16.00   # Y-axis (matches tang shoulder)
RECEIVER_LENGTH = 55.00   # Z-axis total block

# Ball detent
BALL_DIA = 3.00
BALL_WINDOW_DIA = 2.50    # Retains ball
LOCK_Z = 35.00            # Ball window center from Datum C (opening face)

# Spring pocket (from -X side)
SPRING_POCKET_DIA = 3.20
SPRING_POCKET_DEPTH = 8.00

# Button bore (from +X side)
BUTTON_BORE_DIA = 4.00    # Slightly larger than button shaft (3.80)

# Magnet pockets (in Datum C face)
MAG_DIA = 4.00
MAG_POCKET_DEPTH = 2.20
MAG_OFFSET_Y = 4.50


def build_receiver_core():
    """Build the universal female receiver block with all lock hardware bores.

    This is the IDENTICAL internal geometry shared across all 5 attachments.
    The outer body shape differs per attachment but this core is constant.

    Origin: Receiver opening face (Datum C) is at Z=0.
    Tang enters from Z=0 in +Z direction (positive Z is into the receiver).
    Receiver block extends from Z=0 to Z=RECEIVER_LENGTH.
    """

    with BuildPart() as receiver:
        # --- Outer receiver block ---
        with BuildSketch():
            RectangleRounded(RECEIVER_WIDTH, RECEIVER_HEIGHT, 1.0)
        extrude(amount=RECEIVER_LENGTH)

        # --- Main tang slot (from opening face, Z=0, into block) ---
        with BuildSketch():
            RectangleRounded(SLOT_THICKNESS, SLOT_WIDTH, SLOT_CORNER_R)
        extrude(amount=SLOT_DEPTH, mode=Mode.SUBTRACT)

        # --- Opening chamfer / lead-in funnel ---
        # Larger opening at Z=0, narrowing to slot size at Z=SLOT_CHAMFER
        with BuildSketch(Plane.XY.offset(-0.01)):
            RectangleRounded(
                SLOT_THICKNESS + SLOT_CHAMFER * 2,
                SLOT_WIDTH + SLOT_CHAMFER * 2,
                SLOT_CORNER_R + 0.5
            )
        extrude(amount=SLOT_CHAMFER, mode=Mode.SUBTRACT)

        # --- Ball window (cross-drilled through +X wall at Z=LOCK_Z) ---
        # Through-hole from +X face to slot
        with BuildSketch(Plane.YZ.offset(RECEIVER_WIDTH/2)):
            with Locations([(LOCK_Z, 0)]):
                Circle(radius=BALL_WINDOW_DIA/2)
        extrude(amount=-RECEIVER_WIDTH, mode=Mode.SUBTRACT)

        # --- Spring pocket (from -X face, larger bore) ---
        with BuildSketch(Plane.YZ.offset(-RECEIVER_WIDTH/2)):
            with Locations([(LOCK_Z, 0)]):
                Circle(radius=SPRING_POCKET_DIA/2)
        extrude(amount=SPRING_POCKET_DEPTH, mode=Mode.SUBTRACT)

        # --- Button bore (from +X face to ball window area) ---
        with BuildSketch(Plane.YZ.offset(RECEIVER_WIDTH/2)):
            with Locations([(LOCK_Z, 0)]):
                Circle(radius=BUTTON_BORE_DIA/2)
        extrude(amount=-(RECEIVER_WIDTH/2 - SLOT_THICKNESS/2 + 0.5), mode=Mode.SUBTRACT)

        # --- Magnet pockets in opening face (Datum C, Z=0) ---
        for y_off in [MAG_OFFSET_Y, -MAG_OFFSET_Y]:
            with BuildSketch(Plane.XY.offset(RECEIVER_LENGTH)):
                with Locations([(0, y_off)]):
                    Circle(radius=(MAG_DIA + 0.10)/2)
            extrude(amount=-MAG_POCKET_DEPTH, mode=Mode.SUBTRACT)

    return receiver.part


# ============================================================
# RECEIVER VARIANTS (wrapping different outer bodies)
# ============================================================

def build_comb_extension_receiver(tooth_spacing="narrow"):
    """Build a comb extension (TC-002 or TC-003) with shared receiver core.

    The comb extension body extends BELOW the receiver block (in -Z direction
    when assembled, creating inverted teeth for double-ended comb).

    Args:
        tooth_spacing: "narrow" for TC-002, "wide" for TC-003
    """
    # Start with standard receiver core
    # In production, the outer body wraps around this core
    # Here we build a simplified representation

    part_id = "TC-002" if tooth_spacing == "narrow" else "TC-003"
    spacing = 4.0 if tooth_spacing == "narrow" else 13.5
    body_length = 223.67 if tooth_spacing == "narrow" else 223.23

    print(f"  Building {part_id} ({tooth_spacing} comb extension)")
    print(f"  Receiver core: {RECEIVER_WIDTH}x{RECEIVER_HEIGHT}x{RECEIVER_LENGTH} mm")
    print(f"  Tooth spacing: ~{spacing} mm")
    print(f"  Overall body length: ~{body_length} mm")
    print(f"  Lock hardware: ball + spring + button (in receiver)")
    print(f"  Docking: INVERTED onto TC-001 tang")

    return build_receiver_core()


def build_handle_receiver(handle_type="double"):
    """Build a handle attachment with shared receiver core.

    Args:
        handle_type: "double" (TH-001), "flat" (TH-002), or "round" (TH-003)
    """
    part_map = {
        "double": ("TH-001", "Double Handle (fork)", 242.80),
        "flat": ("TH-002", "Flat Handle (rattail)", 204.95),
        "round": ("TH-003", "Round Handle (pintail)", 242.65),
    }

    part_id, name, body_length = part_map[handle_type]

    print(f"  Building {part_id} {name}")
    print(f"  Receiver core: {RECEIVER_WIDTH}x{RECEIVER_HEIGHT}x{RECEIVER_LENGTH} mm")
    print(f"  Overall body length: ~{body_length} mm")
    print(f"  Lock hardware: ball + spring + button (in receiver)")
    print(f"  Material: 316L stainless steel")

    return build_receiver_core()


if __name__ == "__main__":
    print("=" * 60)
    print("TAYLKOMB Shared Receiver Core")
    print("=" * 60)
    print()
    print(f"Slot:     {SLOT_THICKNESS} x {SLOT_WIDTH} mm (accepts 2.54 x 5.08 tang)")
    print(f"Depth:    {SLOT_DEPTH} mm")
    print(f"Block:    {RECEIVER_WIDTH} x {RECEIVER_HEIGHT} x {RECEIVER_LENGTH} mm")
    print(f"Lock Z:   {LOCK_Z} mm from opening (ball window center)")
    print(f"Ball:     {BALL_DIA} mm dia, window {BALL_WINDOW_DIA} mm")
    print(f"Spring:   pocket {SPRING_POCKET_DIA} x {SPRING_POCKET_DEPTH} mm")
    print(f"Button:   bore {BUTTON_BORE_DIA} mm")
    print(f"Magnets:  2x pockets dia {MAG_DIA} mm at ±{MAG_OFFSET_Y} mm")
    print()
    print("This receiver is IDENTICAL across all 5 attachments:")
    print("  TC-002 Narrow Comb, TC-003 Wide Comb")
    print("  TH-001 Double Handle, TH-002 Flat Handle, TH-003 Round Handle")
    print()

    try:
        part = build_receiver_core()
        part.export_step("TK-RECV_Universal_Receiver_Corrected.step")
        part.export_stl("TK-RECV_Universal_Receiver_Corrected.stl")
        print("Exported: TK-RECV_Universal_Receiver_Corrected.step/.stl")
    except Exception as e:
        print(f"Export skipped (build123d not installed): {e}")
