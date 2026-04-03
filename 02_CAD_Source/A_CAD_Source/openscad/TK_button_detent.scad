// ============================================================
// TK-BTN-001: Button/Detent Sub-Assembly
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Assembly: Spring-loaded ball detent + push-button release
// Components:
//   - Ball: 3.175mm (1/8") G25 AISI 52100 Chrome Steel
//   - Spring: 3mm OD, 0.3mm wire, 10mm free length
//   - Button: 4mm shaft, 6mm head, POM (Delrin)
// ============================================================

include <TK_common.scad>;

$fn = 120;

// === BUTTON BODY ===
module button_body() {
    union() {
        // Shaft
        cylinder(d = button_dia, h = button_len);
        // Head (mushroom cap)
        translate([0, 0, button_len])
            cylinder(d = button_head_dia, h = button_head_height);
        // Internal cam ramp (pushes ball outward)
        translate([0, 0, 0])
            cylinder(d1 = button_dia, d2 = button_dia - 1.0, h = 3);
    }
}

// === COMPRESSION SPRING (visual) ===
module compression_spring(od, wire_d, free_len, coils = 8) {
    pitch = free_len / coils;
    for (i = [0 : coils - 1]) {
        translate([0, 0, i * pitch])
            rotate_extrude($fn = 60)
                translate([od/2 - wire_d/2, 0])
                    circle(d = wire_d, $fn = 12);
    }
}

// === FULL ASSEMBLY VISUALIZATION ===
// Ball
color("Silver")
    sphere(d = ball_dia, $fn = 60);

// Spring (along X axis, behind ball)
color([0.5, 0.5, 0.5])
    translate([ball_dia/2 + 0.5, 0, 0])
        rotate([0, 90, 0])
            compression_spring(spring_od, 0.30, spring_free_len);

// Button (along Y axis)
color([0.3, 0.3, 0.3])
    translate([0, recv_bore_dia/2, 0])
        rotate([-90, 0, 0])
            button_body();
