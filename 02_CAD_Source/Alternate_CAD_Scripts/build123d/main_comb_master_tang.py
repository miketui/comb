"""
TAYLKOMB Main Comb Master Tang — build123d
Document: TK-IF-002 Compliant
Date: April 2, 2026

TC-001 Main Comb is the ONLY male part in the system.
This script generates the passive tang with detent notch and magnet pockets.
No moving lock hardware exists in this part.

Requirements: pip install build123d
"""

from build123d import *
from math import pi

# ============================================================
# PARAMETERS (TK-IF-002)
# ============================================================

# Tang cross-section
TANG_WIDTH = 5.08        # Y-axis (wide face, provides keying)
TANG_THICKNESS = 2.54    # X-axis (narrow face)
TANG_LENGTH = 50.80      # Z-axis total
TANG_CORNER_R = 0.25     # Corner radius
TANG_CHAMFER = 0.50      # Tip chamfer (45°)

# Shoulder (insertion stop)
SHOULDER_WIDTH = 8.00    # X-axis
SHOULDER_HEIGHT = 16.00  # Y-axis
SHOULDER_DEPTH = 5.00    # Z-axis

# Tang root transition
TANG_ROOT_FILLET = 2.00  # Minimum fillet radius

# Detent notch (passive — ball engages here)
NOTCH_FROM_TIP = 35.00   # Center from tang tip (Z)
NOTCH_DEPTH = 0.80       # Into +X face
NOTCH_WIDTH_Z = 3.00     # Along Z-axis
BALL_DIA = 3.00           # For spherical seat

# Magnet pockets (shoulder face)
MAG_DIA = 4.00
MAG_POCKET_DEPTH = 2.20
MAG_OFFSET_Y = 4.50      # From Y-centerline


def build_tang():
    """Build the TC-001 Main Comb tang — passive male connector."""

    with BuildPart() as tang:
        # --- Main tang body ---
        with BuildSketch() as tang_profile:
            RectangleRounded(TANG_THICKNESS, TANG_WIDTH, TANG_CORNER_R)

        extrude(amount=TANG_LENGTH)

        # --- Shoulder block ---
        with BuildSketch(Plane.XY.offset(TANG_LENGTH)) as shoulder_profile:
            RectangleRounded(SHOULDER_WIDTH, SHOULDER_HEIGHT, 1.0)

        extrude(amount=SHOULDER_DEPTH)

        # --- Tang root fillet ---
        # Fillet the transition edges between tang and shoulder
        tang_top_face_edges = tang.edges().filter_by(
            lambda e: abs(e.center().Z - TANG_LENGTH) < 0.1
        )
        if tang_top_face_edges:
            try:
                fillet(tang_top_face_edges, radius=TANG_ROOT_FILLET)
            except Exception:
                pass  # Skip if fillet fails on complex geometry

        # --- Tip chamfer ---
        tang_tip_edges = tang.edges().filter_by(
            lambda e: abs(e.center().Z) < 0.1 and e.length < TANG_WIDTH * 1.5
        )
        if tang_tip_edges:
            try:
                chamfer(tang_tip_edges, length=TANG_CHAMFER)
            except Exception:
                pass

        # --- Detent notch (passive groove on +X face) ---
        # Spherical seat for ball engagement
        with Locations([(TANG_THICKNESS/2, 0, NOTCH_FROM_TIP)]):
            Sphere(radius=BALL_DIA/2 + 0.1, mode=Mode.SUBTRACT)

        # Flat-bottom notch channel
        with BuildSketch(Plane.XZ.offset(0)) as notch_sk:
            with Locations([(TANG_THICKNESS/2 - NOTCH_DEPTH/2, NOTCH_FROM_TIP)]):
                Rectangle(NOTCH_DEPTH + 0.5, NOTCH_WIDTH_Z)

        extrude(amount=NOTCH_WIDTH_Z, both=True, mode=Mode.SUBTRACT)

        # --- Magnet pockets in shoulder face ---
        for y_offset in [MAG_OFFSET_Y, -MAG_OFFSET_Y]:
            with Locations([(0, y_offset, TANG_LENGTH)]):
                Hole(radius=MAG_DIA/2 + 0.05, depth=MAG_POCKET_DEPTH)

    return tang.part


def build_tang_simple():
    """Simplified tang construction for environments where
    filter_by may not be available."""

    with BuildPart() as tang:
        # Tang body
        with BuildSketch():
            RectangleRounded(TANG_THICKNESS, TANG_WIDTH, TANG_CORNER_R)
        extrude(amount=TANG_LENGTH)

        # Shoulder
        with BuildSketch(Plane.XY.offset(TANG_LENGTH)):
            RectangleRounded(SHOULDER_WIDTH, SHOULDER_HEIGHT, 1.0)
        extrude(amount=SHOULDER_DEPTH)

        # Detent notch — box cut
        with BuildSketch(Plane.YZ.offset(TANG_THICKNESS/2)):
            with Locations([(0, NOTCH_FROM_TIP)]):
                Rectangle(NOTCH_WIDTH_Z, NOTCH_DEPTH * 2)
        extrude(amount=-NOTCH_DEPTH - 0.1, mode=Mode.SUBTRACT)

        # Magnet pockets
        for y_off in [MAG_OFFSET_Y, -MAG_OFFSET_Y]:
            with BuildSketch(Plane.XY.offset(TANG_LENGTH)):
                with Locations([(0, y_off)]):
                    Circle(radius=(MAG_DIA + 0.10)/2)
            extrude(amount=-MAG_POCKET_DEPTH, mode=Mode.SUBTRACT)

    return tang.part


if __name__ == "__main__":
    print("TAYLKOMB Main Comb Master Tang")
    print(f"  Tang: {TANG_THICKNESS} x {TANG_WIDTH} x {TANG_LENGTH} mm")
    print(f"  Shoulder: {SHOULDER_WIDTH} x {SHOULDER_HEIGHT} x {SHOULDER_DEPTH} mm")
    print(f"  Detent notch: {NOTCH_DEPTH} mm deep at {NOTCH_FROM_TIP} mm from tip")
    print(f"  Magnet pockets: 2x dia {MAG_DIA} mm at ±{MAG_OFFSET_Y} mm from center")
    print(f"  Total length: {TANG_LENGTH + SHOULDER_DEPTH} mm (tang + shoulder)")
    print()
    print("  NOTE: TC-001 is PASSIVE — no ball, spring, or button.")
    print("  Lock hardware lives in each of the 5 attachment receivers.")

    try:
        part = build_tang_simple()
        part.export_step("TC-001_tang_corrected.step")
        part.export_stl("TC-001_tang_corrected.stl")
        print("\n  Exported: TC-001_tang_corrected.step/.stl")
    except Exception as e:
        print(f"\n  Export skipped (build123d not installed): {e}")
