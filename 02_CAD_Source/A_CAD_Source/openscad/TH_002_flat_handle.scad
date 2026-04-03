// ============================================================
// TH-002: Flat Handle (Paddle Style)
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Material: 316L Stainless Steel
// Process: CNC milling from billet
// Finish: Bead-blasted (Ra 1.6 μm)
// ============================================================

include <TK_common.scad>;

$fn = 120;

// === PARAMETERS ===
handle_length       = 105.00;
body_width          = 20.00;
body_height         = 8.00;
corner_radius       = 2.00;
taper_length        = 12.00;
end_cap_radius      = 4.00;

// === FLAT GRIP BODY ===
module flat_grip() {
    grip_len = handle_length - recv_bore_depth - recv_wall - taper_length - end_cap_radius;
    
    translate([0, 0, recv_bore_depth + recv_wall + taper_length]) {
        // Rounded rectangle cross-section extruded
        linear_extrude(height = grip_len) {
            offset(r = corner_radius)
                offset(delta = -corner_radius)
                    square([body_width, body_height], center = true);
        }
        
        // Rounded end cap
        translate([0, 0, grip_len])
            resize([body_width, body_height, end_cap_radius * 2])
                sphere(d = body_width);
    }
}

// === RECEIVER HOUSING ===
module receiver_end() {
    cylinder(d = recv_outer_dia + 2, h = recv_bore_depth + recv_wall);
    
    // Transition: round to flat
    translate([0, 0, recv_bore_depth + recv_wall])
        hull() {
            cylinder(d = recv_outer_dia + 2, h = 0.01);
            translate([0, 0, taper_length])
                linear_extrude(height = 0.01)
                    offset(r = corner_radius)
                        offset(delta = -corner_radius)
                            square([body_width, body_height], center = true);
        }
}

// === COMPLETE HANDLE ===
difference() {
    union() {
        receiver_end();
        flat_grip();
    }
    
    // Receiver bore
    translate([0, 0, -0.01])
        cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall);
}

// Show receiver insert
color("Silver", 0.3)
    female_receiver_core(with_magnet = true);
