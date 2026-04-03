// ============================================================
// TK-ASM-001: Taylkomb System Assembly
// TAYLKOMB LLC · Patent Pending · Confidential
// ============================================================
// Shows all configurations of the modular system:
//   Comb + Tang mated with Handle + Receiver
// ============================================================

include <TK_common.scad>;

$fn = 60;

// === ASSEMBLY: Main Comb + Double Handle ===
// This shows TC-001 tang inserted into TH-001 receiver

// Tang (part of comb, shown at mate position)
color("DimGray")
    translate([0, 0, 0])
        passive_male_tang(with_magnet = true);

// Receiver (part of handle)
color("Silver")
    translate([0, 0, -5])  // receiver mouth aligns with tang root
        rotate([180, 0, 0])
            female_receiver_core(with_magnet = true);

// Ball/Detent assembly (in engaged position)
translate([0, 0, tang_length - tang_detent_from_tip])
    button_detent_assembly();

// === EXPLODED VIEW (offset) ===
translate([50, 0, 0]) {
    // Tang - pulled out
    color("DimGray")
        translate([0, 0, 30])
            passive_male_tang(with_magnet = true);
    
    // Ball
    color("Silver")
        translate([0, 0, 15])
            sphere(d = ball_dia);
    
    // Spring
    color("Gray")
        translate([0, 0, 5])
            cylinder(d = spring_od, h = spring_free_len);
    
    // Button
    color("DarkGray")
        translate([0, 0, -5])
            cylinder(d = button_dia, h = button_len);
    
    // Receiver
    color("Silver")
        translate([0, 0, -45])
            female_receiver_core(with_magnet = true);
}
