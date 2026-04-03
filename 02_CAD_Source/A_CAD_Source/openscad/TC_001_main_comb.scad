// ============================================================
// TC-001: Main Comb (Dual-Tooth — Fine + Coarse)
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Material: PA66-GF30 or PA12-CF (injection molded)
// Surface Finish: SPI B-2 mold texture (matte)
// Color: Black (RAL/Pantone TBD)
// Receiver: Molded-in 316L stainless insert
// ============================================================

include <TK_common.scad>;

$fn = 60;

// === COMB PARAMETERS ===
comb_length         = 192.00;
comb_width          = 40.00;
comb_thickness      = 6.00;
spine_height        = 5.00;

// Fine teeth (one side)
fine_count          = 28;
fine_spacing        = 1.80;
fine_length         = 28.00;
fine_thickness      = 1.00;
fine_taper          = 3;       // degrees

// Coarse teeth (other side)
coarse_count        = 14;
coarse_spacing      = 3.60;
coarse_length       = 22.00;
coarse_thickness    = 1.60;
coarse_taper        = 3;

// Receiver integration zone
recv_zone_length    = 25.00;   // length of receiver housing in comb body
recv_zone_width     = 20.00;

// === SINGLE TOOTH MODULE ===
module tooth(length, thickness, taper_deg) {
    // Tapered rectangular tooth
    hull() {
        cube([thickness, 0.01, comb_thickness], center = true);
        translate([0, length, 0])
            cube([thickness * 0.6, 0.01, comb_thickness * 0.7], center = true);
    }
}

// === COMB BODY ===
module comb_body() {
    // Main spine
    translate([0, 0, 0])
        cube([comb_length - recv_zone_length, spine_height, comb_thickness]);
    
    // Fine teeth
    fine_start = 10;
    for (i = [0 : fine_count - 1]) {
        translate([fine_start + i * fine_spacing, -fine_length, comb_thickness/2])
            rotate([0, 0, 0])
                tooth(fine_length, fine_thickness, fine_taper);
    }
    
    // Coarse teeth (opposite side)
    coarse_start = 10;
    for (i = [0 : coarse_count - 1]) {
        translate([coarse_start + i * coarse_spacing, spine_height, comb_thickness/2])
            rotate([180, 0, 0])
                translate([0, -coarse_length, 0])
                    tooth(coarse_length, coarse_thickness, coarse_taper);
    }
}

// === RECEIVER HOUSING ===
module receiver_housing() {
    // Transition zone from comb body to receiver
    translate([comb_length - recv_zone_length, 0, 0]) {
        // Housing block
        difference() {
            hull() {
                cube([recv_zone_length * 0.3, recv_zone_width, comb_thickness]);
                translate([recv_zone_length * 0.7, (recv_zone_width - recv_outer_dia)/2, (comb_thickness - recv_outer_dia)/2])
                    rotate([0, 90, 0])
                        cylinder(d = recv_outer_dia + 2, h = recv_zone_length * 0.3);
            }
            
            // Receiver bore (for insert)
            translate([recv_zone_length, recv_zone_width/2, comb_thickness/2])
                rotate([0, -90, 0])
                    cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall + 1);
        }
    }
}

// === COMPLETE TC-001 ===
union() {
    comb_body();
    receiver_housing();
    
    // Receiver insert (shown in context)
    color("Silver", 0.5)
        translate([comb_length, (comb_width > 20 ? 20 : comb_width/2) , comb_thickness/2])
            rotate([0, -90, 0])
                female_receiver_core(with_magnet = true);
}
