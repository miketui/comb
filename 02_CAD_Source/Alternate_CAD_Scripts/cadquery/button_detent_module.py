"""TAYLKOMB corrected receiver-side button + detent module baseline."""
from pathlib import Path
import cadquery as cq
from cadquery import exporters

BUTTON_D = 3.80
BUTTON_L = 8.0
BUTTON_HEAD_D = 6.0
BUTTON_HEAD_T = 1.2
BALL_D = 3.0

shaft = cq.Workplane("XY").circle(BUTTON_D/2).extrude(BUTTON_L)
head = cq.Workplane("XY").circle(BUTTON_HEAD_D/2).extrude(BUTTON_HEAD_T)
button = head.union(shaft.translate((0,0,BUTTON_HEAD_T)))

ball = cq.Workplane("XY").sphere(BALL_D/2)

if __name__ == "__main__":
    out = Path(__file__).resolve().parents[2] / "02_working" / "exports"
    (out / "step").mkdir(parents=True, exist_ok=True)
    exporters.export(button, str(out / "step" / "button_module.step"))
    exporters.export(ball, str(out / "step" / "detent_ball.step"))
