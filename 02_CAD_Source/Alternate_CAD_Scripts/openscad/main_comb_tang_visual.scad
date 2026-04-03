// TAYLKOMB corrected main comb passive tang visual
tang_w = 5.08;
tang_h = 2.54;
tang_l = 50.8;
shoulder_t = 6;
shoulder_w = 8;
shoulder_h = 16;
difference() {
    union() {
        cube([shoulder_t, shoulder_w, shoulder_h], center=false);
        translate([shoulder_t, (shoulder_w - tang_w)/2, (shoulder_h - tang_h)/2]) cube([tang_l, tang_w, tang_h], center=false);
    }
    translate([shoulder_t + 35, shoulder_w/2, shoulder_h/2 + tang_h/2 - 0.4]) sphere(r=1.5, $fn=40);
}
