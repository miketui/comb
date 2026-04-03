// ============================================================
// TK-FIT-001: Fit Coupon Set for Interface Validation
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Print these FIRST before full part prototyping.
// Test protocol: T-01 through T-08 per TK-FIT-001
// ============================================================

include <TK_common.scad>;

$fn = 120;

// === COUPON 1: Tang Test Piece ===
module coupon_tang() {
    union() {
        passive_male_tang(with_magnet = false);
        // Print base plate
        translate([0, 0, -4])
            cylinder(d = 30, h = 2);
        // Label
        translate([0, 0, -4])
            linear_extrude(height = 0.5)
                text("TANG", size = 4, halign = "center", valign = "center");
    }
}

// === COUPON 2: Nominal Receiver ===
module coupon_receiver_nominal() {
    difference() {
        union() {
            // Thick-wall test receiver
            cylinder(d = recv_outer_dia + 8, h = recv_bore_depth + recv_wall);
            // Print base
            translate([0, 0, -2])
                cylinder(d = 35, h = 2);
        }
        // Standard bore
        translate([0, 0, -0.01])
            cylinder(d = recv_bore_dia, h = recv_bore_depth + 0.01);
        // Ball bore
        translate([0, 0, recv_bore_depth - recv_ball_bore_pos])
            rotate([0, 90, 0])
                cylinder(d = recv_ball_bore_dia, h = 50, center = true);
    }
    translate([0, 0, -2])
        linear_extrude(height = 0.5)
            text("NOM", size = 4, halign = "center", valign = "center");
}

// === COUPON 3: Relief Receiver (+0.10mm clearance) ===
module coupon_receiver_relief() {
    relief = 0.10;
    difference() {
        union() {
            cylinder(d = recv_outer_dia + 8, h = recv_bore_depth + recv_wall);
            translate([0, 0, -2])
                cylinder(d = 35, h = 2);
        }
        translate([0, 0, -0.01])
            cylinder(d = recv_bore_dia + relief, h = recv_bore_depth + 0.01);
        translate([0, 0, recv_bore_depth - recv_ball_bore_pos])
            rotate([0, 90, 0])
                cylinder(d = recv_ball_bore_dia, h = 50, center = true);
    }
    translate([0, 0, -2])
        linear_extrude(height = 0.5)
            text("REL", size = 4, halign = "center", valign = "center");
}

// === COUPON 4: Lock Test Block ===
module coupon_lock_test() {
    difference() {
        union() {
            // Block with receiver bore + ball/spring/button bores
            cylinder(d = recv_outer_dia + 12, h = recv_bore_depth + recv_wall + 5);
            translate([0, 0, -2])
                cylinder(d = 40, h = 2);
        }
        // Main bore
        translate([0, 0, -0.01])
            cylinder(d = recv_bore_dia, h = recv_bore_depth + 0.01);
        // Ball bore
        translate([0, 0, recv_bore_depth - recv_ball_bore_pos])
            rotate([0, 90, 0])
                cylinder(d = recv_ball_bore_dia, h = 60, center = true);
        // Spring pocket
        translate([recv_bore_dia/2, 0, recv_bore_depth - recv_ball_bore_pos])
            rotate([0, 90, 0])
                cylinder(d = recv_spring_dia, h = recv_spring_depth);
        // Button bore
        translate([0, recv_bore_dia/2, recv_bore_depth - recv_ball_bore_pos])
            rotate([90, 0, 0])
                cylinder(d = recv_button_bore_dia, h = 40, center = true);
    }
    translate([0, 0, -2])
        linear_extrude(height = 0.5)
            text("LOCK", size = 4, halign = "center", valign = "center");
}

// === RENDER ALL COUPONS (spaced for print bed) ===
translate([-30, -30, 0]) coupon_tang();
translate([30, -30, 0])  coupon_receiver_nominal();
translate([-30, 30, 0])  coupon_receiver_relief();
translate([30, 30, 0])   coupon_lock_test();
