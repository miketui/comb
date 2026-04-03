// ============================================================
// TH-003: Round Handle (Cylindrical)
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Material: 316L Stainless Steel
// Process: CNC turning
// Finish: Polished (Ra 0.2 μm)
// Grip: Straight knurl, 1.0mm pitch
// ============================================================

include <TK_common.scad>;

$fn = 120;

// === PARAMETERS ===
handle_length       = 108.00;
grip_diameter       = 16.00;
taper_length        = 12.00;
end_dome_height     = 6.00;
knurl_pitch         = 1.00;

// === GRIP SECTION ===
module round_grip() {
    grip_len = handle_length - recv_bore_depth - recv_wall - taper_length - end_dome_height;
    
    translate([0, 0, recv_bore_depth + recv_wall + taper_length]) {
        // Main cylinder
        cylinder(d = grip_diameter, h = grip_len);
        
        // Domed end cap
        translate([0, 0, grip_len])
            resize([grip_diameter, grip_diameter, end_dome_height * 2])
                sphere(d = grip_diameter);
    }
}

// === RECEIVER HOUSING ===
module receiver_end() {
    cylinder(d = recv_outer_dia + 2, h = recv_bore_depth + recv_wall);
    
    // Taper to grip diameter
    translate([0, 0, recv_bore_depth + recv_wall])
        cylinder(d1 = recv_outer_dia + 2, d2 = grip_diameter, h = taper_length);
}

// === COMPLETE HANDLE ===
difference() {
    union() {
        receiver_end();
        round_grip();
    }
    
    // Receiver bore
    translate([0, 0, -0.01])
        cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall);
}

// Show receiver insert
color("Silver", 0.3)
    female_receiver_core(with_magnet = true);
