// ============================================================
// TAYLKOMB MODULAR COMB SYSTEM — CORRECTED LOCK MECHANISM
// ============================================================
// Document: TK-IF-002 / TK-LOCK-002 Compliant
// Status: SUPERSEDES TAYLKOMB_Lock_Mechanism.scad and RevB.scad
// Designer: TAYLKOMB LLC
// Date: April 2, 2026
// Units: Millimeters
//
// CRITICAL CORRECTION:
//   TC-001 Main Comb is the ONLY male part (passive tang + notch)
//   ALL 5 attachments have female receivers with integrated lock
//   Lock hardware (ball, spring, button) lives in EACH attachment
//
// This file contains:
//   1. Universal Tang (male, TC-001 ONLY) with magnet pockets
//   2. Universal Receiver (female, ALL 5 attachments) with lock + magnets
//   3. Lock sub-assembly (ball, spring, button)
//   4. Magnetic assist system (shoulder face N52 neodymium)
//   5. Assembly visualizations (open, closed, section)
//   6. Individual printable test/fit coupon parts
//   7. Comb extension docking demo (inverted orientation)
//
// HOW TO USE:
//   - Set 'show_mode' variable to choose what to display/export
//   - Render (F6) then export STL for 3D printing
// ============================================================

// === DISPLAY MODE ===
// "assembly_closed"     = fully assembled/locked position
// "assembly_open"       = exploded view showing all parts
// "assembly_section"    = cross-section through lock center
// "tang_only"           = export tang for printing
// "receiver_only"       = export receiver for printing
// "button_only"         = export release button for printing
// "fit_coupon_tang"     = tang coupon with handling plate
// "fit_coupon_receiver" = receiver coupon with handling plate
// "fit_test_pair"       = tang + receiver side by side
// "comb_extension_demo" = shows inverted comb docking onto main comb
// "five_up_demo"        = TC-001 + all 5 receivers arrayed

show_mode = "assembly_section";

// === MASTER PARAMETERS (TK-IF-002) ===

// --- Tang (male, TC-001 ONLY) ---
tang_width     = 5.08;    // Y-axis, wide face
tang_thickness = 2.54;    // X-axis, narrow face
tang_length    = 50.80;   // total tang length
tang_corner_r  = 0.25;    // corner radius
tang_chamfer   = 0.50;    // tip chamfer (45° all edges)
tang_neck_r    = 2.00;    // fillet at tang-to-body transition

// --- Shoulder (insertion stop) ---
shoulder_width  = 8.00;   // X-axis
shoulder_height = 16.00;  // Y-axis
shoulder_depth  = 5.00;   // Z-axis

// --- Detent Notch (in tang — passive feature) ---
notch_from_tip  = 35.00;  // center of notch from tang tip
notch_width_z   = 3.00;   // groove width along Z
notch_depth     = 0.80;   // groove depth into tang face (X-dir)

// --- Receiver (female, ALL 5 attachments — identical) ---
slot_width     = 5.18;    // Y-axis (tang_width + 0.10 clearance)
slot_thickness = 2.64;    // X-axis (tang_thickness + 0.10 clearance)
slot_depth     = 46.00;   // total slot depth
slot_corner_r  = 0.30;    // internal corner radius
slot_chamfer   = 1.00;    // opening chamfer
receiver_width  = shoulder_width;   // 8mm outer X
receiver_height = shoulder_height;  // 16mm outer Y
receiver_length = 55.00;  // Z-axis length of receiver block

// --- Detent Ball ---
ball_dia       = 3.00;    // precision Grade 25
ball_window    = 2.50;    // window hole diameter (retains ball)

// --- Spring Pocket ---
spring_pocket_dia   = 3.20;
spring_pocket_depth = 8.00;

// --- Release Button ---
button_dia        = 3.80;
button_length     = 5.00;
button_flange_dia = 4.50;
button_flange_t   = 0.50;

// --- Spring (visualization only) ---
spring_od       = 2.80;
spring_wire     = 0.40;
spring_free_len = 6.00;
spring_work_len = 4.00;

// --- Magnetic Assist (shoulder face) ---
mag_dia         = 4.00;
mag_thickness   = 2.00;
mag_pocket_depth= 2.20;
mag_offset_y    = 4.50;

// --- Cosmetic ---
$fn = 64;

// ============================================================
// MODULES
// ============================================================

module rounded_rect(w, h, r) {
    offset(r) offset(-r) square([w, h], center=true);
}

// --- Tang (male — TC-001 ONLY, passive: no moving parts) ---
module tang() {
    color("SaddleBrown", 0.85)
    difference() {
        union() {
            // Main tang body
            linear_extrude(height=tang_length)
                rounded_rect(tang_thickness, tang_width, tang_corner_r);

            // Shoulder block
            translate([0, 0, tang_length])
            linear_extrude(height=shoulder_depth)
                rounded_rect(shoulder_width, shoulder_height, 1.0);
        }

        // Tip chamfer — cut 45° on all four long edges at Z=0
        for (rx = [-1, 1]) for (ry = [-1, 1]) {
            translate([rx * tang_thickness/2, ry * tang_width/2, 0])
            translate([-tang_chamfer*1.5, -tang_chamfer*1.5, -0.1])
                cube([tang_chamfer*3, tang_chamfer*3, tang_chamfer + 0.1]);
        }

        // Detent notch — half-round groove on +X face
        translate([tang_thickness/2 - notch_depth, -notch_width_z/2, notch_from_tip - notch_width_z/2])
            cube([notch_depth + 0.5, notch_width_z, notch_width_z]);

        // Spherical detent seat in notch (better ball engagement)
        translate([tang_thickness/2 - notch_depth + 0.2, 0, notch_from_tip])
            sphere(d=ball_dia + 0.2, $fn=32);

        // Magnet pockets in shoulder face (facing attachment)
        for (my = [-1, 1]) {
            translate([0, my * mag_offset_y, tang_length - 0.01])
            cylinder(d=mag_dia + 0.10, h=mag_pocket_depth + 0.01, $fn=32);
        }
    }
}

// --- Detent Ball ---
module detent_ball() {
    color("Silver", 0.95)
        sphere(d=ball_dia, $fn=48);
}

// --- Compression Spring (visualization) ---
module spring(length=spring_work_len) {
    color("LightGray", 0.7) {
        coils = 6;
        for (i = [0:coils-1]) {
            translate([0, 0, i * length/coils])
            rotate_extrude($fn=24)
            translate([spring_od/2 - spring_wire/2, 0, 0])
                circle(d=spring_wire, $fn=12);
        }
    }
}

// --- Release Button ---
module release_button() {
    color("DimGray", 0.9)
    union() {
        // Retention flange (inner end)
        cylinder(d=button_flange_dia, h=button_flange_t, $fn=32);
        // Main shaft
        cylinder(d=button_dia, h=button_length, $fn=32);
        // Domed cap (outer end)
        translate([0, 0, button_length])
            intersection() {
                sphere(d=button_dia * 1.2, $fn=32);
                translate([0, 0, 0])
                    cylinder(d=button_dia * 1.5, h=button_dia, $fn=32);
            }
    }
}

// --- Magnet ---
module magnet(polarity="N") {
    c = (polarity == "N") ? [0.2, 0.4, 0.8] : [0.8, 0.2, 0.2];
    color(c, 0.9)
    cylinder(d=mag_dia, h=mag_thickness, $fn=24);
}

// --- Universal Receiver (female — shared across ALL 5 attachments) ---
module receiver() {
    color("LightSteelBlue", 0.6)
    difference() {
        // Outer block
        linear_extrude(height=receiver_length)
            rounded_rect(receiver_width, receiver_height, 1.0);

        // Main slot (tang cavity)
        translate([0, 0, -0.1])
        linear_extrude(height=slot_depth + 0.1)
            rounded_rect(slot_thickness, slot_width, slot_corner_r);

        // Opening chamfer / lead-in funnel
        translate([0, 0, -0.1])
        linear_extrude(height=slot_chamfer + 0.1, scale=[
            slot_thickness / (slot_thickness + slot_chamfer*2),
            slot_width / (slot_width + slot_chamfer*2)
        ])
            rounded_rect(slot_thickness + slot_chamfer*2, slot_width + slot_chamfer*2, slot_corner_r + 0.5);

        // Lock hardware bores — all at Z = lock_z
        lock_z = receiver_length - shoulder_depth - tang_length + notch_from_tip;

        // Ball window (through +X wall)
        translate([0, 0, lock_z])
        rotate([0, 90, 0])
        translate([0, 0, -receiver_width/2 - 0.1])
            cylinder(d=ball_window, h=receiver_width + 0.2, $fn=32);

        // Spring pocket (from −X side, larger bore)
        translate([-receiver_width/2 - 0.1, 0, lock_z])
        rotate([0, 90, 0])
            cylinder(d=spring_pocket_dia, h=spring_pocket_depth + 0.1, $fn=32);

        // Button bore (from +X side)
        translate([slot_thickness/2 + 0.5, 0, lock_z])
        rotate([0, 90, 0])
        rotate([0, 0, 180])
            cylinder(d=button_dia + 0.2, h=receiver_width, $fn=32);

        // Magnet pockets in receiver face (Datum C)
        for (my = [-1, 1]) {
            translate([0, my * mag_offset_y, receiver_length - mag_pocket_depth])
            cylinder(d=mag_dia + 0.10, h=mag_pocket_depth + 0.1, $fn=32);
        }
    }
}

// --- Simplified body extensions for visualization ---
module comb_body_main() {
    // TC-001 Main Comb body (above shoulder)
    color("SaddleBrown", 0.3)
    translate([0, 0, tang_length + shoulder_depth]) {
        // Spine
        linear_extrude(height=80)
            rounded_rect(shoulder_width, shoulder_height * 0.5, 1.0);
        // Teeth (upward)
        for (i = [0:15]) {
            translate([0, -shoulder_height * 0.3, i * 5 + 3])
            linear_extrude(height=2)
                rounded_rect(shoulder_width * 0.12, 12, 0.1);
        }
        // Crown
        translate([0, shoulder_height * 0.35, 0])
        linear_extrude(height=80)
            rounded_rect(shoulder_width, 4, 0.5);
    }
}

module comb_body_extension() {
    // TC-002 or TC-003 comb body (below receiver, teeth pointing DOWN = inverted)
    color("Peru", 0.3)
    translate([0, 0, -85]) {
        // Spine
        linear_extrude(height=85)
            rounded_rect(receiver_width, receiver_height * 0.5, 1.0);
        // Teeth (downward from extension)
        for (i = [0:12]) {
            translate([0, -receiver_height * 0.3, i * 6 + 3])
            linear_extrude(height=2.5)
                rounded_rect(receiver_width * 0.15, 14, 0.1);
        }
    }
}

module handle_body() {
    // Generic handle extension (below receiver)
    color("LightSteelBlue", 0.4)
    translate([0, 0, -140])
    linear_extrude(height=140)
        rounded_rect(receiver_width, receiver_height * 0.5, 2.0);
}

// ============================================================
// ASSEMBLY MODES
// ============================================================

lock_z_in_receiver = receiver_length - shoulder_depth - tang_length + notch_from_tip;
tang_base_z = receiver_length - shoulder_depth - tang_length;

if (show_mode == "assembly_closed") {
    // Receiver at origin, tang inserted and locked
    receiver();

    // Tang fully seated
    translate([0, 0, tang_base_z])
        tang();

    translate([0, 0, tang_base_z])
        comb_body_main();

    // Lock hardware (in receiver)
    translate([tang_thickness/2 + ball_dia/2 - notch_depth*0.7, 0, lock_z_in_receiver])
        detent_ball();

    translate([-slot_thickness/2 - 2, 0, lock_z_in_receiver])
    rotate([0, 90, 0])
        spring(spring_work_len);

    translate([receiver_width/2 - 1.5, 0, lock_z_in_receiver])
    rotate([0, -90, 0])
        release_button();

    // Magnets
    for (my = [-1, 1]) {
        translate([0, my * mag_offset_y, tang_base_z + tang_length - mag_pocket_depth])
            magnet("N");
        translate([0, my * mag_offset_y, receiver_length - mag_thickness])
            magnet("S");
    }

    // Show handle body below receiver
    handle_body();
}

if (show_mode == "assembly_open") {
    explode = 25;

    receiver();
    handle_body();

    translate([0, 0, receiver_length + explode])
        tang();

    translate([0, 0, receiver_length + explode])
        comb_body_main();

    // Lock components exploded to side
    translate([explode * 1.2, explode * 0.8, lock_z_in_receiver])
        detent_ball();

    translate([explode * 1.5, -explode * 0.5, lock_z_in_receiver])
    rotate([0, 90, 0])
        spring(spring_free_len);

    translate([receiver_width/2 + explode, 0, lock_z_in_receiver])
    rotate([0, -90, 0])
        release_button();

    // Assembly arrow
    color("Red", 0.5) {
        translate([0, 0, receiver_length + explode * 0.3])
        cylinder(d=0.5, h=explode * 1.5, $fn=8);
    }

    // Labels
    color("White") {
        translate([explode * 1.5, explode * 1.2, lock_z_in_receiver])
        linear_extrude(0.5)
            text("BALL", size=2, halign="center", $fn=16);

        translate([explode * 1.8, -explode * 0.8, lock_z_in_receiver])
        linear_extrude(0.5)
            text("SPRING", size=2, halign="center", $fn=16);

        translate([receiver_width/2 + explode + 5, -3, lock_z_in_receiver])
        linear_extrude(0.5)
            text("BUTTON", size=2, halign="center", $fn=16);

        translate([0, -12, receiver_length + explode + tang_length/2])
        linear_extrude(0.5)
            text("TC-001 TANG (passive)", size=2, halign="center", $fn=16);

        translate([0, -12, receiver_length/2])
        linear_extrude(0.5)
            text("RECEIVER (lock inside)", size=2, halign="center", $fn=16);
    }
}

if (show_mode == "assembly_section") {
    difference() {
        union() {
            receiver();
            handle_body();

            translate([0, 0, tang_base_z])
                tang();

            // Lock hardware
            translate([tang_thickness/2 + ball_dia/2 - notch_depth*0.7, 0, lock_z_in_receiver])
                detent_ball();

            translate([-slot_thickness/2 - 2, 0, lock_z_in_receiver])
            rotate([0, 90, 0])
                spring(spring_work_len);

            translate([receiver_width/2 - 1.5, 0, lock_z_in_receiver])
            rotate([0, -90, 0])
                release_button();
        }

        // Section cut — remove +Y half
        translate([-50, 0, -200])
            cube([100, 50, 500]);
    }

    // Section annotations
    color("Red", 0.8) {
        translate([receiver_width/2 + 2, -1, lock_z_in_receiver])
        linear_extrude(0.5)
            text("LOCK", size=1.5, halign="center", $fn=24);

        translate([0, -tang_width/2 - 3, tang_base_z + tang_length/2])
        linear_extrude(0.5)
            text("5.08mm", size=1.2, halign="center", $fn=24);
    }
}

if (show_mode == "tang_only") {
    tang();
}

if (show_mode == "receiver_only") {
    receiver();
}

if (show_mode == "button_only") {
    release_button();
}

if (show_mode == "fit_coupon_tang") {
    // Tang coupon with handling plate
    tang();
    // Back plate for easier handling
    translate([0, 0, tang_length + shoulder_depth])
    color("SaddleBrown", 0.5)
    linear_extrude(height=5)
        rounded_rect(20, 20, 2.0);
}

if (show_mode == "fit_coupon_receiver") {
    // Receiver coupon with handling plate
    receiver();
    // Back plate
    translate([0, 0, receiver_length])
    color("LightSteelBlue", 0.5)
    linear_extrude(height=5)
        rounded_rect(20, 20, 2.0);
}

if (show_mode == "fit_test_pair") {
    translate([-15, 0, 0]) {
        tang();
        translate([0, 0, tang_length + shoulder_depth])
        color("SaddleBrown", 0.5)
        linear_extrude(height=5)
            rounded_rect(20, 20, 2.0);
    }
    translate([15, 0, 0]) {
        receiver();
        translate([0, 0, receiver_length])
        color("LightSteelBlue", 0.5)
        linear_extrude(height=5)
            rounded_rect(20, 20, 2.0);
    }
}

if (show_mode == "comb_extension_demo") {
    // Demo: TC-001 (Main Comb) with TC-002/TC-003 docked INVERTED
    // Main comb body + tang at top
    translate([0, 0, tang_base_z])
        tang();
    translate([0, 0, tang_base_z])
        comb_body_main();

    // Receiver (comb extension) at bottom — teeth point DOWN
    receiver();
    comb_body_extension();

    // Lock hardware in receiver
    translate([tang_thickness/2 + ball_dia/2 - notch_depth*0.7, 0, lock_z_in_receiver])
        detent_ball();
    translate([-slot_thickness/2 - 2, 0, lock_z_in_receiver])
    rotate([0, 90, 0])
        spring(spring_work_len);
    translate([receiver_width/2 - 1.5, 0, lock_z_in_receiver])
    rotate([0, -90, 0])
        release_button();

    // Label
    color("White") {
        translate([12, 0, receiver_length + 20])
        linear_extrude(0.5)
            text("TC-001 teeth UP", size=2, halign="left", $fn=16);

        translate([12, 0, -40])
        linear_extrude(0.5)
            text("TC-002/003 teeth DOWN", size=2, halign="left", $fn=16);

        translate([12, 0, lock_z_in_receiver])
        linear_extrude(0.5)
            text("LOCK (in extension)", size=2, halign="left", $fn=16);
    }
}

if (show_mode == "five_up_demo") {
    // TC-001 tang in center, 5 receivers arrayed around it
    // Center: tang
    tang();

    // 5 receivers spaced around
    for (i = [0:4]) {
        angle = i * 72;
        translate([cos(angle) * 30, sin(angle) * 30, 0])
        receiver();
    }

    // Labels
    labels = ["TC-002", "TC-003", "TH-001", "TH-002", "TH-003"];
    color("White")
    for (i = [0:4]) {
        angle = i * 72;
        translate([cos(angle) * 30, sin(angle) * 30 - 12, receiver_length + 2])
        linear_extrude(0.5)
            text(labels[i], size=2, halign="center", $fn=16);
    }

    translate([0, -12, tang_length + shoulder_depth + 2])
    color("Yellow")
    linear_extrude(0.5)
        text("TC-001 (sole male)", size=2.5, halign="center", $fn=16);
}

// ============================================================
// END OF FILE
// ============================================================
