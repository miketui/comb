"""
TAYLKOMB Button Detent Module — build123d
Document: TK-LOCK-002 Compliant
Date: April 2, 2026

Lock hardware components: ball, spring, button.
These are assembled INTO each of the 5 attachment receivers.
TC-001 Main Comb has NONE of these parts.

Requirements: pip install build123d
"""

from build123d import *

# ============================================================
# LOCK COMPONENT PARAMETERS
# ============================================================

# Detent Ball
BALL_DIA = 3.00           # AISI 52100 chrome steel, Grade 25
BALL_TOLERANCE = 0.0025   # ±0.0025 mm

# Compression Spring
SPRING_OD = 2.80          # Outer diameter
SPRING_WIRE = 0.40        # Wire diameter
SPRING_FREE_LEN = 6.00    # Free (uncompressed) length
SPRING_WORK_LEN = 4.00    # Compressed working length
SPRING_SOLID_HT = 2.80    # Solid height (max compression)
SPRING_RATE = 0.75        # N/mm (approximate)

# Release Button
BUTTON_SHAFT_DIA = 3.80   # Main shaft
BUTTON_SHAFT_LEN = 5.00   # Shaft length
BUTTON_FLANGE_DIA = 4.50  # Internal flange (prevents push-through)
BUTTON_FLANGE_T = 0.50    # Flange thickness
BUTTON_CAP_R = 2.00       # Domed cap radius


def build_detent_ball():
    """Build the precision detent ball."""
    with BuildPart() as ball:
        Sphere(radius=BALL_DIA/2)
    return ball.part


def build_release_button():
    """Build the release button with flange and domed cap."""
    with BuildPart() as button:
        # Internal flange (retention, prevents push-through)
        with BuildSketch():
            Circle(radius=BUTTON_FLANGE_DIA/2)
        extrude(amount=BUTTON_FLANGE_T)

        # Main shaft
        with BuildSketch(Plane.XY.offset(BUTTON_FLANGE_T)):
            Circle(radius=BUTTON_SHAFT_DIA/2)
        extrude(amount=BUTTON_SHAFT_LEN)

        # Domed cap (external, user-facing)
        with BuildSketch(Plane.XY.offset(BUTTON_FLANGE_T + BUTTON_SHAFT_LEN)):
            Circle(radius=BUTTON_SHAFT_DIA/2)
        extrude(amount=BUTTON_SHAFT_DIA/4)

    return button.part


def build_spring_visualization():
    """Build a simplified spring representation for visualization.
    Not for manufacturing — use spring spec for ordering.
    """
    with BuildPart() as spring:
        # Simplified as a cylinder with hollow core
        with BuildSketch():
            Circle(radius=SPRING_OD/2)
            Circle(radius=SPRING_OD/2 - SPRING_WIRE, mode=Mode.SUBTRACT)
        extrude(amount=SPRING_WORK_LEN)
    return spring.part


# ============================================================
# LOCK ASSEMBLY INFO
# ============================================================

def print_lock_bom():
    """Print the bill of materials for one lock assembly."""
    print("=" * 55)
    print("TAYLKOMB LOCK ASSEMBLY BOM (per attachment)")
    print("=" * 55)
    print()
    print("Qty  Part                    Spec")
    print("---  ----------------------  ----------------------------")
    print(f" 1   Detent ball             {BALL_DIA} mm, 52100 steel, Gr 25")
    print(f" 1   Compression spring      {SPRING_OD} OD x {SPRING_WIRE} wire x {SPRING_FREE_LEN} FL")
    print(f" 1   Release button          {BUTTON_SHAFT_DIA} shaft, {BUTTON_FLANGE_DIA} flange")
    print(f" 2   N52 magnet (optional)   4.00 x 2.00 mm disc, NiCuNi")
    print()
    print("TOTAL per system (5 attachments):")
    print(f" 5   Detent balls")
    print(f" 5   Compression springs")
    print(f" 5   Release buttons")
    print(f" 10  N52 magnets (optional)")
    print()
    print("Assembly order: spring → ball → button")
    print("Function test: press button, ball retracts; release, ball returns")
    print()
    print("CRITICAL: These components go ONLY in the 5 attachments.")
    print("TC-001 Main Comb has NO lock hardware — passive tang only.")


def print_spring_spec():
    """Print detailed spring specification for ordering."""
    force_at_work = SPRING_RATE * (SPRING_FREE_LEN - SPRING_WORK_LEN)
    print()
    print("SPRING SPECIFICATION")
    print("-" * 40)
    print(f"  Material:        302 stainless steel")
    print(f"  Wire diameter:   {SPRING_WIRE} mm")
    print(f"  Outer diameter:  {SPRING_OD} mm")
    print(f"  Free length:     {SPRING_FREE_LEN} mm")
    print(f"  Working length:  {SPRING_WORK_LEN} mm")
    print(f"  Solid height:    {SPRING_SOLID_HT} mm")
    print(f"  Rate:            ~{SPRING_RATE} N/mm")
    print(f"  Force at work:   ~{force_at_work:.1f} N")
    print(f"  End type:        Closed and ground")
    print(f"  Total coils:     ~8")
    print(f"  Active coils:    ~6")


if __name__ == "__main__":
    print_lock_bom()
    print_spring_spec()

    try:
        ball = build_detent_ball()
        ball.export_step("TK-BALL_Detent_Ball.step")
        ball.export_stl("TK-BALL_Detent_Ball.stl")
        print("\nExported: TK-BALL_Detent_Ball.step/.stl")

        button = build_release_button()
        button.export_step("TK-BTN_Release_Button_Corrected.step")
        button.export_stl("TK-BTN_Release_Button_Corrected.stl")
        print("Exported: TK-BTN_Release_Button_Corrected.step/.stl")
    except Exception as e:
        print(f"\nExport skipped (build123d not installed): {e}")
