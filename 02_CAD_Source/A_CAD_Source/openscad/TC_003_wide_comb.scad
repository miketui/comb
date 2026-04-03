// ============================================================
// TC-003: Wide Comb (Coarse Teeth — Detangling)
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Material: PA66-GF30 or PA12-CF (injection molded)
// Surface Finish: SPI B-2 mold texture
// Color: Black (RAL/Pantone TBD)
// ============================================================

include <TK_common.scad>;

$fn = 60;

// === PARAMETERS ===
comb_length         = 205.00;
comb_width          = 55.00;
comb_thickness      = 7.00;
spine_height        = 6.00;
coarse_count        = 18;
coarse_spacing      = 5.00;
coarse_length       = 30.00;
coarse_thickness    = 1.80;
recv_zone_length    = 28.00;

module tooth(length, thickness) {
    hull() {
        cube([thickness, 0.01, comb_thickness], center = true);
        translate([0, length, 0])
            cube([thickness * 0.65, 0.01, comb_thickness * 0.7], center = true);
    }
}

module comb_body() {
    cube([comb_length - recv_zone_length, spine_height, comb_thickness]);
    
    coarse_start = 10;
    for (i = [0 : coarse_count - 1]) {
        translate([coarse_start + i * coarse_spacing, -coarse_length, comb_thickness/2])
            tooth(coarse_length, coarse_thickness);
    }
}

module receiver_housing() {
    translate([comb_length - recv_zone_length, 0, 0]) {
        difference() {
            hull() {
                cube([recv_zone_length * 0.3, recv_outer_dia + 6, comb_thickness]);
                translate([recv_zone_length * 0.7, (recv_outer_dia + 6)/2, comb_thickness/2])
                    rotate([0, 90, 0])
                        cylinder(d = recv_outer_dia + 3, h = recv_zone_length * 0.3);
            }
            translate([recv_zone_length + 0.01, (recv_outer_dia + 6)/2, comb_thickness/2])
                rotate([0, -90, 0])
                    cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall + 1);
        }
    }
}

union() {
    comb_body();
    receiver_housing();
    
    color("Silver", 0.5)
        translate([comb_length, (recv_outer_dia + 6)/2, comb_thickness/2])
            rotate([0, -90, 0])
                female_receiver_core(with_magnet = true);
}
