// ============================================================
// TC-002: Narrow Comb (Fine Teeth Only)
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Material: PA66-GF30 or PA12-CF (injection molded)
// Surface Finish: SPI B-2 mold texture
// Color: Black (RAL/Pantone TBD)
// ============================================================

include <TK_common.scad>;

$fn = 60;

// === PARAMETERS ===
comb_length         = 178.00;
comb_width          = 32.00;
comb_thickness      = 5.00;
spine_height        = 4.00;
fine_count          = 36;
fine_spacing        = 1.20;
fine_length         = 25.00;
fine_thickness      = 0.80;
recv_zone_length    = 22.00;

module tooth(length, thickness) {
    hull() {
        cube([thickness, 0.01, comb_thickness], center = true);
        translate([0, length, 0])
            cube([thickness * 0.5, 0.01, comb_thickness * 0.65], center = true);
    }
}

module comb_body() {
    cube([comb_length - recv_zone_length, spine_height, comb_thickness]);
    
    fine_start = 8;
    for (i = [0 : fine_count - 1]) {
        translate([fine_start + i * fine_spacing, -fine_length, comb_thickness/2])
            tooth(fine_length, fine_thickness);
    }
}

module receiver_housing() {
    translate([comb_length - recv_zone_length, 0, 0]) {
        difference() {
            hull() {
                cube([recv_zone_length * 0.3, recv_outer_dia + 4, comb_thickness]);
                translate([recv_zone_length * 0.7, (recv_outer_dia + 4)/2, comb_thickness/2])
                    rotate([0, 90, 0])
                        cylinder(d = recv_outer_dia + 2, h = recv_zone_length * 0.3);
            }
            translate([recv_zone_length + 0.01, (recv_outer_dia + 4)/2, comb_thickness/2])
                rotate([0, -90, 0])
                    cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall + 1);
        }
    }
}

union() {
    comb_body();
    receiver_housing();
    
    color("Silver", 0.5)
        translate([comb_length, (recv_outer_dia + 4)/2, comb_thickness/2])
            rotate([0, -90, 0])
                female_receiver_core(with_magnet = true);
}
