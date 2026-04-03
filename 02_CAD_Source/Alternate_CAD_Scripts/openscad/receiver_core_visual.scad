// TAYLKOMB corrected shared receiver core visual
slot_w = 5.18;
slot_h = 2.64;
slot_d = 46.0;
body_l = 55;
body_w = 16;
body_h = 20;
difference() {
    cube([body_l, body_w, body_h], center=false);
    translate([4, body_w/2 - slot_w/2, body_h/2 - slot_h/2]) cube([slot_d, slot_w, slot_h], center=false);
    translate([35, body_w/2, body_h/2]) rotate([90,0,0]) cylinder(h=8, r=1.25, $fn=40);
}
