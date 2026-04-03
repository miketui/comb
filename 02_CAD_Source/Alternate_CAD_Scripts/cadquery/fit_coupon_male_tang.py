from pathlib import Path
import cadquery as cq
from cadquery import exporters
from main_comb_master_tang import part as tang_part
coupon = tang_part
if __name__ == "__main__":
    out = Path(__file__).resolve().parents[2] / "02_working" / "exports"
    (out / "step").mkdir(parents=True, exist_ok=True)
    (out / "stl").mkdir(parents=True, exist_ok=True)
    exporters.export(coupon, str(out / "step" / "fit_coupon_male_tang.step"))
    exporters.export(coupon, str(out / "stl" / "fit_coupon_male_tang.stl"))
