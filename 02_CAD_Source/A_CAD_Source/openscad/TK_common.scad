// ============================================================
// TAYLKOMB COMMON INTERFACE LIBRARY
// TK-SCAD-LIB-001 Rev A
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// This file defines the shared interface geometry used by all
// combs and handles in the Taylkomb modular system.
// All dimensions in millimeters.
// ============================================================

$fn = 120; // High resolution for production geometry

// === TANG PARAMETERS ===
tang_diameter       = 10.00;
tang_length         = 45.00;
tang_tip_chamfer    = 1.00;
tang_root_fillet    = 0.50;
tang_detent_from_tip = 35.00;
tang_detent_width   = 3.20;
tang_detent_depth   = 1.50;  // radial depth
tang_detent_radius  = 1.60;  // groove cross-section radius
tang_magnet_from_tip = 20.00;

// === RECEIVER PARAMETERS ===
recv_bore_dia       = 10.10;
recv_bore_depth     = 40.00;
recv_wall           = 2.50;
recv_outer_dia      = recv_bore_dia + 2 * recv_wall; // 15.10
recv_ball_bore_dia  = 3.30;
recv_ball_bore_pos  = 10.00;  // from mouth (matches tang detent)
recv_spring_dia     = 3.60;
recv_spring_depth   = 10.00;
recv_button_bore_dia = 4.20;
recv_button_bore_depth = 12.00;
recv_mouth_chamfer  = 0.50;

// === DETENT HARDWARE ===
ball_dia            = 3.175;
spring_od           = 3.00;
spring_free_len     = 10.00;
button_dia          = 4.00;
button_len          = 8.00;
button_head_dia     = 6.00;
button_head_height  = 1.50;

// === MAGNET ===
magnet_dia          = 6.00;
magnet_thick        = 2.00;
magnet_pocket_dia   = 6.10;
magnet_pocket_depth = 2.10;

// ============================================================
// MODULE: passive_male_tang()
// Creates the passive male tang with ball detent groove
// and optional magnet pocket.
// ============================================================
module passive_male_tang(with_magnet = true) {
    difference() {
        union() {
            // Main tang body
            cylinder(d = tang_diameter, h = tang_length);
            
            // Root flange (for integration with comb/handle body)
            translate([0, 0, -2])
                cylinder(d = tang_diameter + 4, h = 2);
        }
        
        // Tip chamfer (45° cone cut)
        translate([0, 0, tang_length - tang_tip_chamfer])
            difference() {
                cylinder(d = tang_diameter + 2, h = tang_tip_chamfer + 0.1);
                cylinder(d1 = tang_diameter, d2 = tang_diameter - 2*tang_tip_chamfer, h = tang_tip_chamfer + 0.1);
            }
        
        // Ball detent groove (circumferential)
        detent_z = tang_length - tang_detent_from_tip;
        translate([0, 0, detent_z])
            rotate_extrude()
                translate([tang_diameter/2, 0, 0])
                    resize([tang_detent_depth * 2, tang_detent_width])
                        circle(d = tang_detent_width);
        
        // Magnet pocket (axial, at tip end)
        if (with_magnet) {
            translate([0, 0, tang_length - tang_magnet_from_tip])
                cylinder(d = magnet_pocket_dia, h = magnet_pocket_depth, center = true);
        }
    }
}

// ============================================================
// MODULE: female_receiver_core()
// Creates the female receiver socket with ball bore,
// spring pocket, button bore, and optional magnet pocket.
// ============================================================
module female_receiver_core(with_magnet = true) {
    difference() {
        // Outer body
        cylinder(d = recv_outer_dia, h = recv_bore_depth + recv_wall);
        
        // Main bore
        translate([0, 0, -0.01])
            cylinder(d = recv_bore_dia, h = recv_bore_depth + 0.01);
        
        // Mouth chamfer
        translate([0, 0, -0.01])
            cylinder(d1 = recv_bore_dia + 2*recv_mouth_chamfer, 
                     d2 = recv_bore_dia, 
                     h = recv_mouth_chamfer + 0.01);
        
        // Ball bore (radial, through outer wall into main bore)
        // Positioned so ball contacts tang at detent groove
        ball_bore_z = recv_bore_depth - recv_ball_bore_pos;
        translate([0, 0, ball_bore_z])
            rotate([0, 90, 0])
                cylinder(d = recv_ball_bore_dia, h = recv_outer_dia, center = true);
        
        // Spring pocket (radial, behind ball, opposite side from button)
        translate([0, 0, ball_bore_z])
            rotate([0, 90, 180])  // opposite side
                translate([0, 0, recv_bore_dia/2 - 0.5])
                    cylinder(d = recv_spring_dia, h = recv_spring_depth);
        
        // Button bore (radial, 90° from ball bore)
        translate([0, 0, ball_bore_z])
            rotate([0, 90, 90])
                translate([0, 0, -recv_outer_dia/2 - 0.01])
                    cylinder(d = recv_button_bore_dia, h = recv_outer_dia + 0.02);
        
        // Magnet pocket (at bottom of bore)
        if (with_magnet) {
            translate([0, 0, recv_bore_depth - magnet_pocket_depth])
                cylinder(d = magnet_pocket_dia, h = magnet_pocket_depth + 0.01);
        }
    }
}

// ============================================================
// MODULE: button_detent_assembly()
// Visual representation of the button/detent sub-assembly
// ============================================================
module button_detent_assembly() {
    // Ball
    color("Silver")
        sphere(d = ball_dia);
    
    // Spring (simplified as cylinder)
    color("Gray")
        translate([recv_bore_dia/2 + 1, 0, 0])
            rotate([0, 90, 0])
                cylinder(d = spring_od, h = spring_free_len);
    
    // Button
    color("DarkGray") {
        // Button shaft
        rotate([0, 90, 90])
            translate([0, 0, recv_bore_dia/2])
                cylinder(d = button_dia, h = button_len);
        // Button head
        rotate([0, 90, 90])
            translate([0, 0, recv_bore_dia/2 + button_len])
                cylinder(d = button_head_dia, h = button_head_height);
    }
}

// ============================================================
// MODULE: fit_coupon_tang()
// Simplified tang coupon for 3D print fit testing
// ============================================================
module fit_coupon_tang() {
    passive_male_tang(with_magnet = false);
    // Base plate for printing
    translate([0, 0, -4])
        cube([30, 30, 2], center = true);
}

// ============================================================
// MODULE: fit_coupon_receiver()
// Simplified receiver coupon for 3D print fit testing
// ============================================================
module fit_coupon_receiver(type = "nominal") {
    clearance_offset = (type == "relief") ? 0.10 : 0.00;
    
    difference() {
        union() {
            cylinder(d = recv_outer_dia + 10 + clearance_offset*2, h = recv_bore_depth + recv_wall);
            // Base plate
            translate([0, 0, -2])
                cube([35, 35, 2], center = true);
        }
        
        // Adjusted bore for testing
        translate([0, 0, -0.01])
            cylinder(d = recv_bore_dia + clearance_offset, h = recv_bore_depth + 0.01);
        
        // Ball bore
        ball_bore_z = recv_bore_depth - recv_ball_bore_pos;
        translate([0, 0, ball_bore_z])
            rotate([0, 90, 0])
                cylinder(d = recv_ball_bore_dia, h = recv_outer_dia + 20, center = true);
    }
}
