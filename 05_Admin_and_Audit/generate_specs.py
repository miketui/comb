#!/usr/bin/env python3
"""
TAYLKOMB Specification Document Generator
Generates:
  - TK-TOL-001: Tolerance Stack-Up Analysis
  - TK-HW-001: Hardware BOM & Specification
  - TK-MAT-001: Material & Finish Specification

TAYLKOMB LLC · Patent Pending · Confidential
"""

import os
import json
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, red, gray, lightgrey, white
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
from reportlab.lib import colors

OUT_DIR = "/tmp/taylkomb/D_Specifications"
os.makedirs(OUT_DIR, exist_ok=True)

with open("/tmp/taylkomb/A_CAD_Source/parameters.json") as f:
    P = json.load(f)

# ============================================================
# TK-TOL-001: TOLERANCE STACK-UP ANALYSIS
# ============================================================
def generate_tolerance_stackup():
    print("Generating TK-TOL-001: Tolerance Stack-Up Analysis...")
    
    doc = SimpleDocTemplate(
        os.path.join(OUT_DIR, "TK-TOL-001-Tolerance-Stack-Up.pdf"),
        pagesize=LETTER,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
        leftMargin=0.75*inch, rightMargin=0.75*inch,
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    # Title
    story.append(Paragraph("<b>TK-TOL-001 Rev A</b>", styles['Title']))
    story.append(Paragraph("TOLERANCE STACK-UP ANALYSIS", styles['Title']))
    story.append(Paragraph("TAYLKOMB Modular Hair Tool System — Tang/Receiver Interface", styles['Normal']))
    story.append(Paragraph("TAYLKOMB LLC · Patent Pending · Confidential", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # 1. Interface Fit Analysis
    story.append(Paragraph("<b>1. TANG / RECEIVER FIT ANALYSIS</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    tang = P["interface"]["tang"]
    recv = P["interface"]["receiver"]
    tol = P["tolerances"]
    
    tang_tol = tol["interface_tang_diameter"]
    recv_tol = tol["interface_receiver_bore"]
    
    tang_max = tang_tol["nominal"] + tang_tol["upper"]
    tang_min = tang_tol["nominal"] + tang_tol["lower"]
    recv_max = recv_tol["nominal"] + recv_tol["upper"]
    recv_min = recv_tol["nominal"] + recv_tol["lower"]
    
    min_clearance = recv_min - tang_max
    max_clearance = recv_max - tang_min
    
    fit_data = [
        ["DIMENSION", "NOMINAL", "UPPER", "LOWER", "MAX", "MIN", "CLASS"],
        ["Tang OD", f"Ø{tang_tol['nominal']:.2f}", f"{tang_tol['upper']:+.3f}", f"{tang_tol['lower']:+.3f}",
         f"Ø{tang_max:.3f}", f"Ø{tang_min:.3f}", tang_tol['class']],
        ["Receiver Bore", f"Ø{recv_tol['nominal']:.2f}", f"{recv_tol['upper']:+.3f}", f"{recv_tol['lower']:+.3f}",
         f"Ø{recv_max:.3f}", f"Ø{recv_min:.3f}", recv_tol['class']],
    ]
    
    t = Table(fit_data, colWidths=[90, 55, 50, 50, 55, 55, 40])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    
    story.append(Paragraph(f"<b>Minimum diametral clearance:</b> {min_clearance:.3f} mm", styles['Normal']))
    story.append(Paragraph(f"<b>Maximum diametral clearance:</b> {max_clearance:.3f} mm", styles['Normal']))
    story.append(Paragraph(f"<b>Fit type:</b> CLEARANCE FIT (Sliding)", styles['Normal']))
    story.append(Paragraph(f"<b>Assessment:</b> {'PASS — adequate clearance for smooth insertion' if min_clearance > 0.05 else 'REVIEW — clearance may be too tight'}", styles['Normal']))
    story.append(Spacer(1, 15))
    
    # 2. Ball Detent Position Stack
    story.append(Paragraph("<b>2. BALL DETENT POSITION STACK-UP</b>", styles['Heading2']))
    story.append(Spacer(1, 5))
    story.append(Paragraph("This analysis ensures the ball in the receiver aligns with the detent groove on the tang when fully inserted.", styles['Normal']))
    story.append(Spacer(1, 10))
    
    detent_pos = tol["ball_detent_groove_position"]
    ball_pos = tol["ball_bore_position"]
    
    position_data = [
        ["CONTRIBUTOR", "NOMINAL (mm)", "TOLERANCE (mm)", "DIRECTION"],
        ["Tang: detent groove from tip", f"{detent_pos['nominal']:.2f}", f"±{detent_pos['tolerance']:.2f}", "Along tang axis"],
        ["Receiver: ball bore from mouth", f"{ball_pos['nominal']:.2f}", f"±{ball_pos['tolerance']:.2f}", "Along bore axis"],
        ["Tang insertion depth", "40.00", "±0.10", "Controlled by receiver depth"],
        ["Receiver bore depth", "40.00", "±0.30", "Machining tolerance"],
    ]
    
    t2 = Table(position_data, colWidths=[150, 80, 80, 120])
    t2.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(t2)
    story.append(Spacer(1, 10))
    
    # Worst case stack
    worst_case = detent_pos['tolerance'] + ball_pos['tolerance'] + 0.10 + 0.30
    groove_width = tang["ball_detent_groove_width"]
    ball_dia = P["interface"]["detent"]["ball_diameter"]
    
    story.append(Paragraph(f"<b>Worst-case misalignment:</b> ±{worst_case:.2f} mm", styles['Normal']))
    story.append(Paragraph(f"<b>Groove width:</b> {groove_width:.2f} mm | <b>Ball diameter:</b> {ball_dia:.3f} mm", styles['Normal']))
    story.append(Paragraph(f"<b>Available float:</b> {groove_width - ball_dia:.3f} mm", styles['Normal']))
    story.append(Paragraph(f"<b>Assessment:</b> {'PASS — groove width accommodates stack-up' if (groove_width - ball_dia)/2 > worst_case else 'REVIEW — margin is tight'}", styles['Normal']))
    story.append(Spacer(1, 15))
    
    # 3. Concentricity Requirements
    story.append(Paragraph("<b>3. CONCENTRICITY & GEOMETRIC TOLERANCE SUMMARY</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    geo_data = [
        ["FEATURE", "TOLERANCE TYPE", "VALUE", "DATUM REF", "CTF?"],
        ["Tang OD", "Concentricity", f"Ø{tol['concentricity_tang']}", "A (tang axis)", "YES"],
        ["Receiver Bore", "Concentricity", f"Ø{tol['concentricity_receiver_bore']}", "A (bore axis)", "YES"],
        ["Tang Root Face", "Perpendicularity", str(tol['perpendicularity_tang_root']), "A (tang axis)", "YES"],
        ["Receiver Mouth", "Perpendicularity", str(tol['perpendicularity_receiver_mouth']), "A (bore axis)", "YES"],
        ["Tang OD Surface", "Profile of Surface", str(tol['surface_profile_tang']), "A, B", "YES"],
        ["Receiver Bore Surface", "Profile of Surface", str(tol['surface_profile_receiver']), "A, B", "YES"],
        ["Ball Bore to Main Bore", "True Position", "Ø0.05", "A (bore axis)", "YES"],
        ["Button Bore to Ball Bore", "True Position", "Ø0.08", "A, C", "NO"],
    ]
    
    t3 = Table(geo_data, colWidths=[110, 90, 55, 85, 35])
    t3.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (1, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (-1, 1), (-1, -1), colors.HexColor('#FFEEEE')),
    ]))
    story.append(t3)
    story.append(Spacer(1, 15))
    
    # 4. Surface Finish Requirements
    story.append(Paragraph("<b>4. SURFACE FINISH REQUIREMENTS</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    finish_data = [
        ["SURFACE", "Ra (μm)", "PROCESS", "REASON"],
        ["Tang OD", "0.8", "Grinding", "Smooth insertion, low friction"],
        ["Receiver Bore ID", "0.8", "Honing", "Smooth sliding fit with tang"],
        ["Receiver OD", "1.6", "Turning", "Insert interface with housing"],
        ["Ball Bore ID", "0.4", "Reaming", "Ball retention, consistent force"],
        ["Button Bore ID", "1.6", "Drilling + reaming", "Button travel"],
        ["Detent Groove", "0.8", "Grinding/EDM", "Ball engagement surface"],
        ["Handle Grip (Polished)", "0.2", "Polishing", "User comfort, aesthetics"],
        ["Handle Grip (Brushed)", "0.4", "Brushing", "User comfort, grip"],
        ["Handle Grip (Blasted)", "1.6", "Bead blasting", "Texture, grip"],
        ["Comb Body", "SPI B-2", "Mold texture", "Matte finish, aesthetics"],
        ["Comb Teeth", "SPI B-2", "Mold texture", "Hair glide, comfort"],
    ]
    
    t4 = Table(finish_data, colWidths=[110, 45, 100, 160])
    t4.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(t4)
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("TAYLKOMB LLC · Patent Pending · Confidential Engineering Documentation · TK-TOL-001 Rev A", styles['Normal']))
    
    doc.build(story)
    print(f"  Saved: {OUT_DIR}/TK-TOL-001-Tolerance-Stack-Up.pdf")


# ============================================================
# TK-HW-001: HARDWARE BOM & SPECIFICATION
# ============================================================
def generate_hardware_bom():
    print("Generating TK-HW-001: Hardware BOM & Specification...")
    
    doc = SimpleDocTemplate(
        os.path.join(OUT_DIR, "TK-HW-001-Hardware-BOM.pdf"),
        pagesize=LETTER,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    story.append(Paragraph("<b>TK-HW-001 Rev A</b>", styles['Title']))
    story.append(Paragraph("HARDWARE BOM & SPECIFICATION", styles['Title']))
    story.append(Paragraph("TAYLKOMB LLC · Patent Pending · Confidential", styles['Normal']))
    story.append(Spacer(1, 20))
    
    det = P["interface"]["detent"]
    mag = P["interface"]["magnet"]
    
    # Complete BOM
    story.append(Paragraph("<b>1. COMPLETE SYSTEM BOM</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    bom_data = [
        ["ITEM", "PART NO.", "DESCRIPTION", "QTY/SET", "MATERIAL", "SOURCE"],
        ["1", "TK-TANG-001", "Passive Male Tang", "3", "316L SS", "Custom CNC"],
        ["2", "TK-RECV-001", "Female Receiver Core", "4", "316L SS", "Custom CNC"],
        ["3", "TK-BTN-001-A", "Lock Button", "4", "POM (Delrin)", "Custom CNC/Mold"],
        ["4", "TK-BTN-001-B", f"Ball Ø{det['ball_diameter']:.3f}mm G25", "4", det['ball_material'], "Purchased"],
        ["5", "TK-BTN-001-C", "Compression Spring", "4", "302 SS Wire", "Custom/Catalog"],
        ["6", "TK-MAG-001", f"N52 Magnet Ø{mag['diameter']}×{mag['thickness']}mm", "8", "NdFeB Ni-Cu-Ni", "Purchased"],
        ["7", "TC-001", "Main Comb (Fine + Coarse)", "1", "PA66-GF30", "Injection Mold"],
        ["8", "TC-002", "Narrow Comb (Fine)", "1", "PA66-GF30", "Injection Mold"],
        ["9", "TC-003", "Wide Comb (Coarse)", "1", "PA66-GF30", "Injection Mold"],
        ["10", "TH-001", "Double Handle", "1", "316L SS", "Custom CNC"],
        ["11", "TH-002", "Flat Handle", "1", "316L SS", "Custom CNC"],
        ["12", "TH-003", "Round Handle", "1", "316L SS", "Custom CNC"],
    ]
    
    t = Table(bom_data, colWidths=[30, 65, 130, 45, 70, 80])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (0, 0), (0, -1), 'CENTER'),
        ('ALIGN', (3, 0), (3, -1), 'CENTER'),
    ]))
    story.append(t)
    story.append(Spacer(1, 20))
    
    # Hardware specifications
    story.append(Paragraph("<b>2. HARDWARE DETAIL SPECIFICATIONS</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    # Ball spec
    story.append(Paragraph("<b>2.1 Ball Bearing (TK-BTN-001-B)</b>", styles['Heading3']))
    ball_spec = [
        ["PARAMETER", "SPECIFICATION"],
        ["Diameter", f"{det['ball_diameter']:.3f} mm (1/8 inch)"],
        ["Grade", det['ball_grade']],
        ["Material", det['ball_material']],
        ["Surface Finish", "Mirror polish, Ra ≤ 0.025 μm"],
        ["Hardness", "60-67 HRC"],
        ["Sphericity", "≤ 0.000635 mm (per G25)"],
        ["Suggested Supplier", "Precision Balls Inc., BC Precision, or equiv."],
        ["Suggested P/N", "BC-0125-CS-G25 or equivalent"],
        ["Qty per Assembly", "1 per receiver"],
    ]
    t_ball = Table(ball_spec, colWidths=[120, 300])
    t_ball.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#444')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(t_ball)
    story.append(Spacer(1, 15))
    
    # Spring spec
    story.append(Paragraph("<b>2.2 Compression Spring (TK-BTN-001-C)</b>", styles['Heading3']))
    spring_spec = [
        ["PARAMETER", "SPECIFICATION"],
        ["Outer Diameter", f"{det['spring_outer_diameter']:.2f} mm"],
        ["Wire Diameter", f"{det['spring_wire_diameter']:.2f} mm"],
        ["Free Length", f"{det['spring_free_length']:.2f} mm"],
        ["Compressed Length (working)", f"{det['spring_compressed_length']:.2f} mm"],
        ["Spring Rate", f"{det['spring_rate_N_per_mm']} N/mm"],
        ["Preload at Compressed", f"{det['spring_rate_N_per_mm'] * (det['spring_free_length'] - det['spring_compressed_length']):.2f} N"],
        ["Material", "302 Stainless Steel Spring Wire"],
        ["Ends", "Closed and ground"],
        ["Finish", "Passivated"],
        ["Suggested Supplier", "Lee Spring, Century Spring, or equiv."],
        ["Suggested P/N", "TBD — select from catalog matching specs"],
        ["Qty per Assembly", "1 per receiver"],
    ]
    t_spring = Table(spring_spec, colWidths=[120, 300])
    t_spring.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#444')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(t_spring)
    story.append(Spacer(1, 15))
    
    # Magnet spec
    story.append(Paragraph("<b>2.3 Magnet (TK-MAG-001)</b>", styles['Heading3']))
    mag_spec = [
        ["PARAMETER", "SPECIFICATION"],
        ["Type", mag['type']],
        ["Diameter", f"{mag['diameter']:.2f} mm"],
        ["Thickness", f"{mag['thickness']:.2f} mm"],
        ["Coating", mag['coating']],
        ["Max Operating Temp", "80°C (176°F) — N52 grade"],
        ["Pull Force (approx)", "~1.2 kg per pair through 0.1mm gap"],
        ["Production Intent", "TBD — proto-only or production (DECISION REQUIRED)"],
        ["Suggested Supplier", "K&J Magnetics, SuperMagnetMan, or equiv."],
        ["Suggested P/N", "D41-N52 (K&J) or equivalent"],
        ["Qty per Joint", "2 (1 in tang + 1 in receiver)"],
    ]
    t_mag = Table(mag_spec, colWidths=[120, 300])
    t_mag.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#444')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(t_mag)
    story.append(Spacer(1, 15))
    
    # Button spec
    story.append(Paragraph("<b>2.4 Lock Button (TK-BTN-001-A)</b>", styles['Heading3']))
    btn_spec = [
        ["PARAMETER", "SPECIFICATION"],
        ["Shaft Diameter", f"{det['button_diameter']:.2f} mm"],
        ["Shaft Length", f"{det['button_length']:.2f} mm"],
        ["Head Diameter", f"{det['button_head_diameter']:.2f} mm"],
        ["Head Height", f"{det['button_head_height']:.2f} mm"],
        ["Travel", f"{det['button_travel']:.2f} mm"],
        ["Material Options", " / ".join(det['button_material_options'])],
        ["Process", "CNC turning (proto) / Injection molding (production)"],
        ["Surface Finish", "Ra 0.8 μm (shaft), smooth head"],
    ]
    t_btn = Table(btn_spec, colWidths=[120, 300])
    t_btn.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#444')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(t_btn)
    story.append(Spacer(1, 20))
    
    # 3. Force specs
    story.append(Paragraph("<b>3. FORCE SPECIFICATIONS</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    force_data = [
        ["PARAMETER", "TARGET", "TOLERANCE", "TEST METHOD"],
        ["Retention Force", f"{det['retention_force_target_N']} N", f"±{det['retention_force_tolerance_N']} N", "Push-pull gauge, axial pull"],
        ["Release Force (button)", f"{det['release_force_target_N']} N", "MAX", "Push-pull gauge, button push"],
        ["Insertion Force", f"{det['insertion_force_target_N']} N", "MAX", "Push-pull gauge, axial push"],
        ["Cycle Life", "5,000 cycles", "MINIMUM", "Automated cycling fixture"],
    ]
    
    t_force = Table(force_data, colWidths=[100, 60, 60, 180])
    t_force.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('ALIGN', (1, 0), (2, -1), 'CENTER'),
    ]))
    story.append(t_force)
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("TAYLKOMB LLC · Patent Pending · Confidential · TK-HW-001 Rev A", styles['Normal']))
    
    doc.build(story)
    print(f"  Saved: {OUT_DIR}/TK-HW-001-Hardware-BOM.pdf")


# ============================================================
# TK-MAT-001: MATERIAL & FINISH SPECIFICATION
# ============================================================
def generate_material_spec():
    print("Generating TK-MAT-001: Material & Finish Specification...")
    
    doc = SimpleDocTemplate(
        os.path.join(OUT_DIR, "TK-MAT-001-Material-Finish-Spec.pdf"),
        pagesize=LETTER,
        topMargin=0.75*inch, bottomMargin=0.75*inch,
    )
    
    styles = getSampleStyleSheet()
    story = []
    
    story.append(Paragraph("<b>TK-MAT-001 Rev A</b>", styles['Title']))
    story.append(Paragraph("MATERIAL & FINISH SPECIFICATION", styles['Title']))
    story.append(Paragraph("TAYLKOMB LLC · Patent Pending · Confidential", styles['Normal']))
    story.append(Spacer(1, 20))
    
    # Material decision matrix
    story.append(Paragraph("<b>1. MATERIAL DECISION MATRIX</b>", styles['Heading2']))
    story.append(Paragraph("Status: DECISION REQUIRED — Material freeze must be signed off before tooling commitment.", styles['Normal']))
    story.append(Spacer(1, 10))
    
    # Comb body materials
    story.append(Paragraph("<b>1.1 Comb Body Material</b>", styles['Heading3']))
    comb_mat = [
        ["PROPERTY", "PA66-GF30", "PA12-CF", "NOTES"],
        ["Tensile Strength", "185 MPa", "140 MPa", "PA66-GF30 higher strength"],
        ["Flexural Modulus", "10 GPa", "14 GPa", "PA12-CF stiffer"],
        ["Heat Deflection (1.8 MPa)", "255°C", "175°C", "PA66-GF30 better heat resistance"],
        ["Water Absorption (24h)", "1.3%", "0.3%", "PA12-CF better for wet use"],
        ["Chemical Resistance", "Good", "Excellent", "PA12-CF better vs hair chemicals"],
        ["UV Resistance", "Fair", "Good", "Both need UV stabilizer additive"],
        ["Cost (relative)", "1.0×", "2.5×", "PA12-CF significantly more expensive"],
        ["Moldability", "Excellent", "Good", "PA66-GF30 easier to mold, lower warp"],
        ["Surface Finish", "Good", "Excellent", "PA12-CF smoother tooth surfaces"],
        ["RECOMMENDATION", "PRIMARY", "PREMIUM OPTION", "PA66-GF30 for V1, PA12-CF for premium SKU"],
    ]
    
    t_comb = Table(comb_mat, colWidths=[100, 80, 80, 160])
    t_comb.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#FFFFDD')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(t_comb)
    story.append(Spacer(1, 15))
    
    # Handle/receiver material
    story.append(Paragraph("<b>1.2 Handle & Receiver Material (Stainless Steel)</b>", styles['Heading3']))
    ss_mat = [
        ["PROPERTY", "316L", "304", "NOTES"],
        ["Corrosion Resistance", "Excellent", "Good", "316L better for salon chemicals"],
        ["Tensile Strength", "485 MPa", "505 MPa", "304 slightly stronger"],
        ["Machinability", "Good", "Good", "Similar CNC performance"],
        ["Cost (relative)", "1.3×", "1.0×", "316L ~30% premium"],
        ["Biocompatibility", "Excellent", "Good", "316L surgical grade"],
        ["Magnetic Response", "Non-magnetic", "Slightly magnetic", "316L preferred if magnets used"],
        ["RECOMMENDATION", "PRIMARY", "COST OPTION", "316L for all production"],
    ]
    
    t_ss = Table(ss_mat, colWidths=[100, 80, 80, 160])
    t_ss.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#FFFFDD')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(t_ss)
    story.append(Spacer(1, 15))
    
    # Button material
    story.append(Paragraph("<b>1.3 Lock Button Material</b>", styles['Heading3']))
    btn_mat = [
        ["PROPERTY", "POM (DELRIN)", "PA66-GF15", "NOTES"],
        ["Coefficient of Friction", "0.20", "0.35", "POM much lower friction"],
        ["Wear Resistance", "Excellent", "Good", "POM superior for sliding"],
        ["Stiffness", "Good", "Higher", "PA66-GF15 stiffer"],
        ["Chemical Resistance", "Excellent", "Good", "Both adequate"],
        ["Cost", "Low", "Low", "Similar cost"],
        ["RECOMMENDATION", "PRIMARY", "ALTERNATE", "POM for lower friction button action"],
    ]
    
    t_btn = Table(btn_mat, colWidths=[110, 80, 80, 160])
    t_btn.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#FFFFDD')),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
    ]))
    story.append(t_btn)
    story.append(Spacer(1, 20))
    
    # 2. Finish specifications
    story.append(Paragraph("<b>2. FINISH SPECIFICATIONS</b>", styles['Heading2']))
    story.append(Spacer(1, 10))
    
    finish_data = [
        ["COMPONENT", "FINISH", "PROCESS", "COLOR / SPEC"],
        ["Tang (316L SS)", "Ground, passivated", "Centerless grinding → passivation", "Natural SS"],
        ["Receiver (316L SS)", "Honed bore, turned OD", "CNC → hone bore → passivate", "Natural SS"],
        ["TH-001 Double Handle", "Brushed", "CNC → brush finish → passivate", "Ra 0.4 μm, natural SS"],
        ["TH-002 Flat Handle", "Bead-blasted", "CNC → glass bead blast → passivate", "Ra 1.6 μm, matte SS"],
        ["TH-003 Round Handle", "Polished", "CNC → progressive polish → passivate", "Ra 0.2 μm, mirror SS"],
        ["TC-001 Main Comb", "Mold texture", "SPI B-2 mold finish", "BLACK — RAL/Pantone TBD"],
        ["TC-002 Narrow Comb", "Mold texture", "SPI B-2 mold finish", "BLACK — RAL/Pantone TBD"],
        ["TC-003 Wide Comb", "Mold texture", "SPI B-2 mold finish", "BLACK — RAL/Pantone TBD"],
        ["Button (POM)", "As-machined", "CNC turning", "Natural white/black POM"],
    ]
    
    t_finish = Table(finish_data, colWidths=[95, 75, 140, 120])
    t_finish.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#333')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 6.5),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ]))
    story.append(t_finish)
    
    story.append(Spacer(1, 20))
    
    # Action items
    story.append(Paragraph("<b>3. OPEN DECISIONS (MATERIAL FREEZE REQUIRED)</b>", styles['Heading2']))
    story.append(Spacer(1, 5))
    
    decisions = [
        "☐ Freeze comb body material: PA66-GF30 or PA12-CF",
        "☐ Freeze handle body material: 316L or 304 Stainless",
        "☐ Freeze button material: POM (Delrin) or PA66-GF15",
        "☐ Freeze magnet decision: production-intent or proto-only",
        "☐ Freeze surface finish specs (mold texture, metal finish)",
        "☐ Select comb color: RAL number or Pantone reference",
        "☐ Complete chemical resistance validation per test plan",
        "☐ Complete heat resistance validation per test plan",
        "☐ Define UV resistance requirement",
        "☐ Specify plating/coating for metal handles (if any beyond passivation)",
    ]
    
    for d in decisions:
        story.append(Paragraph(d, styles['Normal']))
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("TAYLKOMB LLC · Patent Pending · Confidential · TK-MAT-001 Rev A", styles['Normal']))
    
    doc.build(story)
    print(f"  Saved: {OUT_DIR}/TK-MAT-001-Material-Finish-Spec.pdf")


# ============================================================
# MAIN
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TAYLKOMB Specification Document Generator")
    print("=" * 60)
    
    generate_tolerance_stackup()
    generate_hardware_bom()
    generate_material_spec()
    
    print("")
    print("=" * 60)
    print(f"Generated 3 specification documents in {OUT_DIR}")
    print("=" * 60)
