"""TAYLKOMB corrected main-comb passive tang baseline.
Main Comb is the sole male connector. This script creates the passive tang +
shoulder baseline for fit-coupon and integration work.
"""
from pathlib import Path
import cadquery as cq
from cadquery import exporters

# Provisional baseline dimensions (mm)
TANG_W = 5.08
TANG_T = 2.54
TANG_L = 50.80
SHOULDER_W = 8.00
SHOULDER_H = 16.00
SHOULDER_T = 6.00
NOTCH_CENTER = 35.00
NOTCH_WIDTH = 3.00
NOTCH_DEPTH = 0.80
TIP_CHAMFER = 0.50

# Build orientation:
# X = tang length, Y = width, Z = height (body/face)
shoulder = cq.Workplane("YZ").box(SHOULDER_T, SHOULDER_W, SHOULDER_H, centered=(False, True, True))
tang = (
    cq.Workplane("YZ")
    .workplane(offset=SHOULDER_T)
    .box(TANG_L, TANG_W, TANG_T, centered=(False, True, True))
)

part = shoulder.union(tang)

# Half-round style notch approximated by subtracting a sphere from the tang top side.
notch_x = SHOULDER_T + NOTCH_CENTER
part = part.cut(
    cq.Workplane("XZ")
    .center(notch_x, TANG_T / 2.0 - NOTCH_DEPTH/2)
    .sphere(NOTCH_WIDTH / 2.0)
)

# Tip chamfer
part = part.edges("|Y and >X").chamfer(TIP_CHAMFER)

if __name__ == "__main__":
    out = Path(__file__).resolve().parents[2] / "02_working" / "exports"
    (out / "step").mkdir(parents=True, exist_ok=True)
    (out / "stl").mkdir(parents=True, exist_ok=True)
    exporters.export(part, str(out / "step" / "main_comb_master_tang.step"))
    exporters.export(part, str(out / "stl" / "main_comb_master_tang.stl"))
