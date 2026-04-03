// ============================================================
// TH-001: Double Handle (Dual-Receiver)
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Material: 316L Stainless Steel
// Process: CNC turning + CNC milling
// Finish: Brushed (Ra 0.4 μm grip area)
// Grip: Diamond knurl, 0.8mm pitch
// ============================================================

include <TK_common.scad>;

$fn = 120;

// === PARAMETERS ===
handle_length       = 125.00;
grip_diameter       = 14.00;
knurl_pitch         = 0.80;
knurl_depth         = 0.30;
taper_length        = 15.00;  // transition from grip to receiver housing

// === GRIP SECTION ===
module grip_section() {
    // Main cylindrical grip
    grip_len = handle_length - 2 * (recv_bore_depth + recv_wall + taper_length);
    
    translate([0, 0, recv_bore_depth + recv_wall + taper_length])
        cylinder(d = grip_diameter, h = grip_len);
    
    // Knurl texture (simplified as faceted surface)
    // In production: specified on drawing as diamond knurl 0.8mm pitch
}

// === RECEIVER HOUSING (each end) ===
module receiver_end() {
    // Receiver outer housing
    cylinder(d = recv_outer_dia + 2, h = recv_bore_depth + recv_wall);
    
    // Taper transition to grip
    translate([0, 0, recv_bore_depth + recv_wall])
        cylinder(d1 = recv_outer_dia + 2, d2 = grip_diameter, h = taper_length);
}

// === COMPLETE HANDLE ===
difference() {
    union() {
        // Bottom receiver housing
        receiver_end();
        
        // Grip
        grip_section();
        
        // Top receiver housing (mirrored)
        translate([0, 0, handle_length])
            rotate([180, 0, 0])
                receiver_end();
    }
    
    // Bottom receiver bore
    translate([0, 0, -0.01])
        cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall);
    
    // Top receiver bore
    translate([0, 0, handle_length + 0.01])
        rotate([180, 0, 0])
            cylinder(d = recv_outer_dia + 0.05, h = recv_bore_depth + recv_wall);
}

// Show receiver inserts (context)
color("Silver", 0.3) {
    female_receiver_core(with_magnet = true);
    translate([0, 0, handle_length])
        rotate([180, 0, 0])
            female_receiver_core(with_magnet = true);
}
