// TAYLKOMB corrected lock stack visual (attachment side)
button_d = 3.8;
ball_d = 3.0;
spring_len = 6.0;
translate([0,0,0]) cylinder(h=8, r=button_d/2, $fn=40);
translate([12,0,0]) sphere(r=ball_d/2, $fn=40);
translate([24,0,0]) cylinder(h=spring_len, r=1.4, $fn=30);
