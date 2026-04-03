#!/usr/bin/env python3
"""
TAYLKOMB Manufacturing Drawing Generator
Generates formal engineering drawings with GD&T per ASME Y14.5-2018
Output: PDF drawings for all parts in the Taylkomb system

TAYLKOMB LLC · Patent Pending · Confidential Engineering Documentation
"""

import os
import math
import json
from reportlab.lib.pagesizes import LETTER, landscape
from reportlab.lib.units import inch, mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black, white, red, gray, lightgrey

# Output directory
OUT_DIR = "/tmp/taylkomb/C_Drawings/PDF"
os.makedirs(OUT_DIR, exist_ok=True)

# Load parameters
with open("/tmp/taylkomb/A_CAD_Source/parameters.json") as f:
    PARAMS = json.load(f)

# ============================================================
# DRAWING UTILITIES
# ============================================================

class EngineeringDrawing:
    """Creates a formal manufacturing drawing on ANSI D size (landscape letter for now)"""
    
    def __init__(self, filename, title, part_number, material, rev="A"):
        self.filename = os.path.join(OUT_DIR, filename)
        self.page_w, self.page_h = landscape(LETTER)
        self.c = canvas.Canvas(self.filename, pagesize=landscape(LETTER))
        self.title = title
        self.part_number = part_number
        self.material = material
        self.rev = rev
        self.drawing_number = ""
        self.scale = "2:1"
        self.sheet = "1 OF 1"
        
        # Drawing area margins
        self.margin = 0.5 * inch
        self.border_x = self.margin
        self.border_y = self.margin
        self.draw_w = self.page_w - 2 * self.margin
        self.draw_h = self.page_h - 2 * self.margin
        
    def draw_border(self):
        """Draw drawing border and zone markers"""
        c = self.c
        c.setStrokeColor(black)
        c.setLineWidth(2)
        c.rect(self.border_x, self.border_y, self.draw_w, self.draw_h)
        
        # Inner border
        c.setLineWidth(0.5)
        inner = 0.15 * inch
        c.rect(self.border_x + inner, self.border_y + inner,
               self.draw_w - 2*inner, self.draw_h - 2*inner)
    
    def draw_title_block(self):
        """Draw ASME Y14.100 compliant title block"""
        c = self.c
        tb_w = 4.5 * inch
        tb_h = 1.8 * inch
        tb_x = self.border_x + self.draw_w - tb_w - 0.2*inch
        tb_y = self.border_y + 0.2*inch
        
        c.setLineWidth(1.5)
        c.rect(tb_x, tb_y, tb_w, tb_h)
        
        # Horizontal dividers
        row_h = tb_h / 6
        for i in range(1, 6):
            y = tb_y + i * row_h
            c.setLineWidth(0.5)
            c.line(tb_x, y, tb_x + tb_w, y)
        
        # Vertical divider for right column
        mid_x = tb_x + tb_w * 0.6
        c.line(mid_x, tb_y, mid_x, tb_y + 4*row_h)
        
        c.setFont("Helvetica-Bold", 7)
        pad = 4
        
        # Row 1 (bottom): Scale / Sheet
        c.setFont("Helvetica", 6)
        c.drawString(tb_x + pad, tb_y + pad + 2, f"SCALE: {self.scale}")
        c.drawString(mid_x + pad, tb_y + pad + 2, f"SHEET: {self.sheet}")
        
        # Row 2: Drawing number
        c.setFont("Helvetica", 6)
        c.drawString(tb_x + pad, tb_y + row_h + pad + 2, "DWG NO.")
        c.setFont("Helvetica-Bold", 10)
        c.drawString(tb_x + pad + 50, tb_y + row_h + pad, self.part_number)
        c.setFont("Helvetica", 6)
        c.drawString(mid_x + pad, tb_y + row_h + pad + 2, f"REV: {self.rev}")
        
        # Row 3: Material
        c.setFont("Helvetica", 6)
        c.drawString(tb_x + pad, tb_y + 2*row_h + pad + 2, "MATERIAL:")
        c.setFont("Helvetica-Bold", 7)
        c.drawString(tb_x + pad + 55, tb_y + 2*row_h + pad + 2, self.material)
        c.setFont("Helvetica", 6)
        c.drawString(mid_x + pad, tb_y + 2*row_h + pad + 2, "FINISH: SEE NOTES")
        
        # Row 4: Weight / Units
        c.setFont("Helvetica", 6)
        c.drawString(tb_x + pad, tb_y + 3*row_h + pad + 2, "ALL DIMS IN MM")
        c.drawString(mid_x + pad, tb_y + 3*row_h + pad + 2, "ANGLES IN DEGREES")
        
        # Row 5: Title
        c.setFont("Helvetica-Bold", 11)
        c.drawString(tb_x + pad, tb_y + 4*row_h + pad + 4, self.title)
        
        # Row 6 (top): Company
        c.setFont("Helvetica-Bold", 9)
        c.drawString(tb_x + pad, tb_y + 5*row_h + pad + 4, "TAYLKOMB LLC")
        c.setFont("Helvetica", 6)
        c.drawString(tb_x + pad + 80, tb_y + 5*row_h + pad + 6, "Patent Pending · Confidential")
        
        # Date
        c.setFont("Helvetica", 6)
        c.drawString(tb_x + tb_w - 80, tb_y + 5*row_h + pad + 4, "DATE: 2026-04-02")
        
    def draw_tolerance_block(self):
        """Draw general tolerance block"""
        c = self.c
        tol = PARAMS["tolerances"]
        
        tb_x = self.border_x + 0.3*inch
        tb_y = self.border_y + 0.3*inch
        tb_w = 3.2 * inch
        tb_h = 1.5 * inch
        
        c.setLineWidth(1)
        c.rect(tb_x, tb_y, tb_w, tb_h)
        
        c.setFont("Helvetica-Bold", 7)
        c.drawString(tb_x + 5, tb_y + tb_h - 12, "GENERAL TOLERANCES (UNLESS OTHERWISE SPECIFIED)")
        
        c.setFont("Helvetica", 6)
        lines = [
            f"LINEAR:  0-6mm: ±{tol['general_linear_0_6mm']}  |  6-30mm: ±{tol['general_linear_6_30mm']}  |  30-120mm: ±{tol['general_linear_30_120mm']}  |  120-400mm: ±{tol['general_linear_120_400mm']}",
            f"ANGULAR: ±{tol['general_angular']}°",
            "",
            "BREAK ALL SHARP EDGES 0.2 MAX",
            "REMOVE ALL BURRS",
            "SURFACE FINISH: Ra 3.2 μm UNLESS OTHERWISE SPECIFIED",
            "INTERPRET PER ASME Y14.5-2018",
            "THIRD ANGLE PROJECTION",
            "DO NOT SCALE DRAWING"
        ]
        
        y = tb_y + tb_h - 25
        for line in lines:
            c.drawString(tb_x + 5, y, line)
            y -= 10
    
    def draw_gdt_frame(self, x, y, symbol, tolerance, datums=None, modifier=None):
        """Draw a GD&T feature control frame"""
        c = self.c
        
        frame_h = 14
        cell_w = 28
        num_cells = 2  # symbol + tolerance
        if datums:
            num_cells += len(datums)
        total_w = cell_w * num_cells
        
        c.setLineWidth(0.8)
        c.rect(x, y, total_w, frame_h)
        
        # Symbol cell
        c.line(x + cell_w, y, x + cell_w, y + frame_h)
        c.setFont("Helvetica", 8)
        
        # GD&T symbols
        symbols = {
            "⌖": "⌖",  # Position
            "⏥": "⏥",  # Flatness
            "○": "○",  # Circularity
            "⌭": "⌭",  # Cylindricity
            "∥": "∥",  # Parallelism
            "⊥": "⊥",  # Perpendicularity
            "⊘": "⊘",  # Diameter
            "◎": "◎",  # Concentricity
            "⌓": "⌓",  # Profile of surface
            "⌒": "⌒",  # Profile of line
            "↗": "↗",  # Runout
            "POS": "⌖",
            "FLAT": "⏥",
            "CIRC": "○",
            "CYL": "⌭",
            "PAR": "∥",
            "PERP": "⊥",
            "CONC": "◎",
            "PROF_S": "⌓",
            "PROF_L": "⌒",
            "RUN": "↗",
        }
        
        sym_char = symbols.get(symbol, symbol)
        c.drawCentredString(x + cell_w/2, y + 3, sym_char)
        
        # Tolerance cell
        c.line(x + 2*cell_w, y, x + 2*cell_w, y + frame_h)
        tol_str = f"Ø{tolerance}" if modifier == "DIA" else str(tolerance)
        c.drawCentredString(x + cell_w + cell_w/2, y + 3, tol_str)
        
        # Datum cells
        if datums:
            for i, datum in enumerate(datums):
                cx = x + (2+i)*cell_w
                if i < len(datums) - 1:
                    c.line(cx + cell_w, y, cx + cell_w, y + frame_h)
                c.drawCentredString(cx + cell_w/2, y + 3, datum)
    
    def draw_datum_target(self, x, y, label):
        """Draw a datum feature symbol"""
        c = self.c
        c.setLineWidth(1)
        r = 8
        c.circle(x, y, r)
        c.line(x - r, y, x + r, y)  # horizontal divider
        c.setFont("Helvetica-Bold", 7)
        c.drawCentredString(x, y + 1, label)
        c.drawCentredString(x, y - 7, label)
    
    def draw_surface_finish(self, x, y, ra_value):
        """Draw surface finish symbol with Ra value"""
        c = self.c
        c.setLineWidth(0.5)
        # V-shaped surface finish symbol
        c.line(x, y, x + 5, y + 10)
        c.line(x + 5, y + 10, x + 10, y)
        c.line(x + 5, y + 10, x + 5, y + 16)
        c.line(x + 5, y + 16, x + 18, y + 16)
        c.setFont("Helvetica", 5)
        c.drawString(x + 6, y + 11, f"Ra {ra_value}")
    
    def draw_dimension(self, x1, y1, x2, y2, text, offset=15, above=True):
        """Draw a dimension with leader lines"""
        c = self.c
        c.setLineWidth(0.3)
        c.setStrokeColor(black)
        
        # Extension lines
        if abs(y1 - y2) < 2:  # Horizontal dimension
            dy = offset if above else -offset
            c.line(x1, y1, x1, y1 + dy)
            c.line(x2, y2, x2, y2 + dy)
            # Dimension line
            dim_y = y1 + dy
            c.line(x1, dim_y, x2, dim_y)
            # Arrows
            c.setLineWidth(0.5)
            # Left arrow
            c.line(x1, dim_y, x1 + 4, dim_y + 2)
            c.line(x1, dim_y, x1 + 4, dim_y - 2)
            # Right arrow
            c.line(x2, dim_y, x2 - 4, dim_y + 2)
            c.line(x2, dim_y, x2 - 4, dim_y - 2)
            # Text
            c.setFont("Helvetica", 7)
            c.drawCentredString((x1 + x2)/2, dim_y + 2, text)
        else:  # Vertical dimension
            dx = offset if above else -offset
            c.line(x1, y1, x1 + dx, y1)
            c.line(x2, y2, x2 + dx, y2)
            dim_x = x1 + dx
            c.line(dim_x, y1, dim_x, y2)
            c.setLineWidth(0.5)
            c.line(dim_x, y1, dim_x + 2, y1 + 4)
            c.line(dim_x, y1, dim_x - 2, y1 + 4)
            c.line(dim_x, y2, dim_x + 2, y2 - 4)
            c.line(dim_x, y2, dim_x - 2, y2 - 4)
            c.setFont("Helvetica", 7)
            c.saveState()
            c.translate(dim_x + 3, (y1 + y2)/2)
            c.rotate(90)
            c.drawCentredString(0, 0, text)
            c.restoreState()
    
    def draw_ctf_flag(self, x, y, text="CTF"):
        """Draw Critical-to-Function flag"""
        c = self.c
        c.setFillColor(red)
        c.setFont("Helvetica-Bold", 5)
        # Triangle flag
        c.setStrokeColor(red)
        c.setLineWidth(0.5)
        path = c.beginPath()
        path.moveTo(x, y)
        path.lineTo(x + 12, y + 4)
        path.lineTo(x, y + 8)
        path.close()
        c.drawPath(path, fill=1)
        c.setFillColor(white)
        c.drawString(x + 2, y + 2, text)
        c.setFillColor(black)
        c.setStrokeColor(black)
    
    def draw_inspection_point(self, x, y, point_id):
        """Draw inspection point callout"""
        c = self.c
        c.setLineWidth(0.8)
        c.circle(x, y, 6)
        c.setFont("Helvetica-Bold", 6)
        c.drawCentredString(x, y - 2, str(point_id))
    
    def draw_notes(self, notes, x=None, y=None):
        """Draw notes section"""
        c = self.c
        if x is None:
            x = self.border_x + 3.8*inch
        if y is None:
            y = self.border_y + 0.3*inch
        
        c.setFont("Helvetica-Bold", 7)
        c.drawString(x, y + len(notes)*10 + 5, "NOTES:")
        c.setFont("Helvetica", 6)
        for i, note in enumerate(notes):
            c.drawString(x + 5, y + (len(notes) - 1 - i)*10, f"{i+1}. {note}")
    
    def save(self):
        self.c.save()
        print(f"  Saved: {self.filename}")


# ============================================================
# DRAWING: TK-TANG-001 Passive Male Tang
# ============================================================
def draw_tang():
    print("Generating DWG-001: Passive Male Tang...")
    p = PARAMS["interface"]["tang"]
    t = PARAMS["tolerances"]
    
    dwg = EngineeringDrawing(
        "DWG-001-Tang.pdf",
        "PASSIVE MALE TANG",
        "TK-TANG-001",
        "316L STAINLESS STEEL (PREFERRED) / 304 SS",
    )
    dwg.drawing_number = "DWG-001"
    dwg.scale = "5:1"
    
    dwg.draw_border()
    dwg.draw_title_block()
    dwg.draw_tolerance_block()
    
    c = dwg.c
    
    # === FRONT VIEW (side profile of tang) ===
    # Scale: 5:1 for detail
    sc = 5.0
    cx = 3.5 * inch  # center x
    cy = 4.5 * inch  # center y
    
    tang_d = p["diameter"]
    tang_l = p["length"]
    detent_pos = p["ball_detent_center_from_tip"]
    detent_w = p["ball_detent_groove_width"]
    detent_depth = p["ball_detent_groove_depth"]
    chamfer = p["tip_chamfer"]
    
    # Draw tang profile (side view as rectangle with features)
    x0 = cx - (tang_l * sc / 2)
    y0 = cy - (tang_d * sc / 4)
    
    c.setLineWidth(1.5)  # visible edges
    
    # Main body outline
    r = tang_d * sc / 2
    body_w = tang_l * sc
    
    # Top edge
    c.line(x0 + chamfer*sc, y0 + r, x0 + body_w, y0 + r)
    # Bottom edge
    c.line(x0 + chamfer*sc, y0 - r, x0 + body_w, y0 - r)
    # Right end (root)
    c.line(x0 + body_w, y0 - r, x0 + body_w, y0 + r)
    # Tip chamfer
    c.line(x0, y0, x0 + chamfer*sc, y0 + r)
    c.line(x0, y0, x0 + chamfer*sc, y0 - r)
    
    # Ball detent groove (from tip)
    groove_start = tang_l - detent_pos - detent_w/2
    gx = x0 + groove_start * sc
    gw = detent_w * sc
    gd = detent_depth * sc
    
    # Groove on top
    c.setLineWidth(0.8)
    c.line(gx, y0 + r, gx, y0 + r - gd)
    c.line(gx, y0 + r - gd, gx + gw, y0 + r - gd)
    c.line(gx + gw, y0 + r - gd, gx + gw, y0 + r)
    # Groove on bottom
    c.line(gx, y0 - r, gx, y0 - r + gd)
    c.line(gx, y0 - r + gd, gx + gw, y0 - r + gd)
    c.line(gx + gw, y0 - r + gd, gx + gw, y0 - r)
    
    # Center line
    c.setLineWidth(0.2)
    c.setDash(6, 3)
    c.line(x0 - 10, y0, x0 + body_w + 15, y0)
    c.setDash()
    
    # Magnet pocket (hidden lines)
    mag = PARAMS["interface"]["magnet"]
    mag_pos = p["length"] - mag["pocket_position_from_tip"]
    mag_x = x0 + mag_pos * sc
    mag_d = mag["pocket_diameter"] * sc
    c.setDash(3, 2)
    c.setLineWidth(0.3)
    c.line(mag_x - mag_d/4, y0 - mag_d/4, mag_x - mag_d/4, y0 + mag_d/4)
    c.line(mag_x + mag_d/4, y0 - mag_d/4, mag_x + mag_d/4, y0 + mag_d/4)
    c.setDash()
    
    # === DIMENSIONS ===
    c.setLineWidth(0.3)
    
    # Overall length
    dwg.draw_dimension(x0, y0 + r + 5, x0 + body_w, y0 + r + 5,
                       f"{tang_l:.2f}", offset=25)
    
    # Diameter
    dwg.draw_dimension(x0 + body_w/2, y0 - r, x0 + body_w/2, y0 + r,
                       f"Ø{tang_d:.2f} {t['interface_tang_diameter']['class']}",
                       offset=body_w/2 + 30)
    
    # Ball detent position from tip
    dwg.draw_dimension(x0, y0 - r - 5, gx + gw/2, y0 - r - 5,
                       f"{detent_pos:.2f} ±{t['ball_detent_groove_position']['tolerance']}",
                       offset=20, above=False)
    
    # Detent groove width
    dwg.draw_dimension(gx, y0 + r - gd - 3, gx + gw, y0 + r - gd - 3,
                       f"{detent_w:.2f}", offset=12)
    
    # Detent groove depth  
    c.setFont("Helvetica", 6)
    c.drawString(gx + gw + 5, y0 + r - gd/2, f"GROOVE DEPTH: {detent_depth:.2f}")
    
    # Chamfer
    c.drawString(x0 - 5, y0 + r + 8, f"{chamfer:.1f} × 45°")
    
    # === CROSS SECTION VIEW (A-A) ===
    cs_cx = 7.5 * inch
    cs_cy = 5 * inch
    cs_r = tang_d * sc / 2
    
    c.setFont("Helvetica-Bold", 8)
    c.drawCentredString(cs_cx, cs_cy + cs_r + 20, "SECTION A-A")
    
    c.setLineWidth(1.5)
    c.circle(cs_cx, cs_cy, cs_r)
    
    # Magnet pocket in cross section
    mp_r = mag["pocket_diameter"] * sc / 4
    c.setLineWidth(0.5)
    c.setDash(3, 2)
    c.circle(cs_cx, cs_cy, mp_r)
    c.setDash()
    
    # Cross section hatching
    c.setLineWidth(0.2)
    for i in range(-int(cs_r), int(cs_r) + 1, 3):
        x_off = i
        y_range = math.sqrt(max(0, cs_r**2 - x_off**2))
        mp_y_range = math.sqrt(max(0, mp_r**2 - x_off**2)) if abs(x_off) < mp_r else 0
        
        if y_range > 0:
            c.line(cs_cx + x_off, cs_cy - y_range, cs_cx + x_off + 2, cs_cy + y_range)
    
    # === GD&T CALLOUTS ===
    
    # Datum A - tang axis
    dwg.draw_datum_target(x0 + body_w + 20, y0, "A")
    c.setLineWidth(0.5)
    c.line(x0 + body_w, y0, x0 + body_w + 12, y0)
    
    # Datum B - tang root face
    dwg.draw_datum_target(x0 + body_w, y0 - r - 25, "B")
    
    # Concentricity of tang OD to datum A
    dwg.draw_gdt_frame(x0 + body_w/3, y0 + r + 50, "CONC", f"Ø{t['concentricity_tang']}", ["A"])
    c.setLineWidth(0.3)
    c.line(x0 + body_w/3 + 42, y0 + r + 50, x0 + body_w/3 + 42, y0 + r + 3)
    
    # Perpendicularity of root face to datum A
    dwg.draw_gdt_frame(x0 + body_w + 25, y0 + r + 30, "PERP", str(t['perpendicularity_tang_root']), ["A"])
    
    # Surface profile of tang OD
    dwg.draw_gdt_frame(x0 + body_w/2 - 40, y0 - r - 35, "PROF_S", str(t['surface_profile_tang']), ["A", "B"])
    
    # Surface finish callouts
    dwg.draw_surface_finish(x0 + body_w * 0.7, y0 + r + 5, f"{p['surface_finish_Ra']} μm")
    
    # CTF flags
    dwg.draw_ctf_flag(gx - 15, y0 - r - 20)  # Detent groove position
    dwg.draw_ctf_flag(x0 + body_w/2 + 20, y0 + r + 55)  # Tang diameter
    
    # Inspection points
    dwg.draw_inspection_point(gx + gw/2, y0 + r + 45, "IP-1")  # Groove position
    dwg.draw_inspection_point(x0 + body_w*0.3, y0 + r + 65, "IP-2")  # OD
    dwg.draw_inspection_point(x0 + body_w, y0 + r + 45, "IP-3")  # Root face
    
    # === NOTES ===
    notes = [
        "MATERIAL: 316L STAINLESS STEEL PER ASTM A276",
        "HEAT TREAT: SOLUTION ANNEALED",
        f"SURFACE FINISH: Ra {p['surface_finish_Ra']} μm ON TANG OD (GROUND)",
        "BREAK ALL SHARP EDGES 0.2mm MAX",
        f"BALL DETENT GROOVE: R{p['ball_detent_groove_radius']} FULL RADIUS",
        "MAGNET POCKET: N52 NdFeB, 6.00 × 2.00mm, Ni-Cu-Ni COAT",
        "INTERPRET DIMENSIONS AND TOLERANCES PER ASME Y14.5-2018",
        "CRITICAL TO FUNCTION (CTF) DIMS FLAGGED - 100% INSPECTION",
    ]
    dwg.draw_notes(notes)
    
    dwg.save()


# ============================================================
# DRAWING: TK-RECV-001 Female Receiver Core
# ============================================================
def draw_receiver():
    print("Generating DWG-002: Female Receiver Core...")
    p = PARAMS["interface"]["receiver"]
    t = PARAMS["tolerances"]
    det = PARAMS["interface"]["detent"]
    
    dwg = EngineeringDrawing(
        "DWG-002-Receiver.pdf",
        "FEMALE RECEIVER CORE",
        "TK-RECV-001",
        "316L STAINLESS STEEL",
    )
    dwg.scale = "5:1"
    dwg.draw_border()
    dwg.draw_title_block()
    dwg.draw_tolerance_block()
    
    c = dwg.c
    sc = 5.0
    cx = 3.5 * inch
    cy = 4.5 * inch
    
    bore_d = p["bore_diameter"]
    od = p["outer_diameter"]
    depth = p["bore_depth"]
    wall = p["wall_thickness"]
    
    # Side view (cross-section)
    x0 = cx - (depth + wall) * sc / 2
    
    # Outer rectangle
    c.setLineWidth(1.5)
    outer_h = od * sc / 2
    inner_h = bore_d * sc / 2
    body_len = (depth + wall) * sc
    
    # Outer profile
    c.rect(x0, cy - outer_h, body_len, outer_h * 2)
    
    # Bore (shown as sectioned)
    c.setLineWidth(0.8)
    c.line(x0, cy - inner_h, x0 + depth*sc, cy - inner_h)
    c.line(x0, cy + inner_h, x0 + depth*sc, cy + inner_h)
    c.line(x0 + depth*sc, cy - inner_h, x0 + depth*sc, cy + inner_h)
    
    # Section hatching
    c.setLineWidth(0.15)
    for i in range(0, int(body_len), 4):
        ix = x0 + i
        # Top wall
        c.line(ix, cy + inner_h, ix + 2, cy + outer_h)
        # Bottom wall
        c.line(ix, cy - inner_h, ix + 2, cy - outer_h)
    
    # Ball bore (radial)
    bb_pos = depth - p["ball_bore_position_from_mouth"]
    bb_x = x0 + bb_pos * sc
    bb_d = p["ball_bore_diameter"]
    c.setLineWidth(0.8)
    c.line(bb_x - bb_d*sc/4, cy + inner_h, bb_x - bb_d*sc/4, cy + outer_h)
    c.line(bb_x + bb_d*sc/4, cy + inner_h, bb_x + bb_d*sc/4, cy + outer_h)
    c.line(bb_x - bb_d*sc/4, cy - inner_h, bb_x - bb_d*sc/4, cy - outer_h)
    c.line(bb_x + bb_d*sc/4, cy - inner_h, bb_x + bb_d*sc/4, cy - outer_h)
    
    # Button bore (perpendicular, shown as hidden)
    btn_d = p["button_bore_diameter"]
    c.setDash(3, 2)
    c.setLineWidth(0.4)
    c.line(bb_x - btn_d*sc/4, cy + outer_h, bb_x - btn_d*sc/4, cy - outer_h)
    c.line(bb_x + btn_d*sc/4, cy + outer_h, bb_x + btn_d*sc/4, cy - outer_h)
    c.setDash()
    
    # Spring pocket (shown as hidden, behind ball bore)
    sp_d = p["spring_pocket_diameter"]
    sp_depth = p["spring_pocket_depth"]
    c.setDash(3, 2)
    c.line(bb_x, cy + outer_h, bb_x, cy + outer_h + sp_depth*sc/2)
    c.setDash()
    
    # Center line
    c.setLineWidth(0.2)
    c.setDash(6, 3)
    c.line(x0 - 15, cy, x0 + body_len + 20, cy)
    c.setDash()
    
    # Mouth chamfer
    ch = p["mouth_chamfer"]
    c.setLineWidth(0.5)
    c.line(x0, cy + inner_h, x0 + ch*sc, cy + inner_h + ch*sc/2)
    c.line(x0, cy - inner_h, x0 + ch*sc, cy - inner_h - ch*sc/2)
    
    # === DIMENSIONS ===
    # Bore diameter
    dwg.draw_dimension(x0 + depth*sc/2, cy - inner_h, x0 + depth*sc/2, cy + inner_h,
                       f"Ø{bore_d:.2f} {t['interface_receiver_bore']['class']}",
                       offset=depth*sc/2 + 40)
    
    # Outer diameter
    dwg.draw_dimension(x0 + body_len/2, cy - outer_h, x0 + body_len/2, cy + outer_h,
                       f"Ø{od:.2f}",
                       offset=body_len/2 + 60)
    
    # Bore depth
    dwg.draw_dimension(x0, cy + outer_h + 5, x0 + depth*sc, cy + outer_h + 5,
                       f"{depth:.2f}", offset=20)
    
    # Ball bore diameter & position
    c.setFont("Helvetica", 6)
    c.drawString(bb_x + bb_d*sc/2 + 5, cy + outer_h + 10, 
                 f"BALL BORE Ø{p['ball_bore_diameter']:.2f}")
    c.drawString(bb_x + bb_d*sc/2 + 5, cy + outer_h + 0, 
                 f"@ {p['ball_bore_position_from_mouth']:.2f} FROM MOUTH")
    
    # Button bore
    c.drawString(bb_x + btn_d*sc/2 + 5, cy - outer_h - 15,
                 f"BUTTON BORE Ø{p['button_bore_diameter']:.2f} THRU")
    
    # Spring pocket
    c.drawString(bb_x + 10, cy + outer_h + sp_depth*sc/4,
                 f"SPRING POCKET Ø{sp_d:.2f} × {sp_depth:.1f} DEEP")
    
    # === GD&T ===
    # Datum A - bore axis
    dwg.draw_datum_target(x0 - 20, cy, "A")
    c.setLineWidth(0.5)
    c.line(x0, cy, x0 - 12, cy)
    
    # Datum B - mouth face
    dwg.draw_datum_target(x0, cy - outer_h - 20, "B")
    
    # Concentricity
    dwg.draw_gdt_frame(x0 + body_len/3, cy + outer_h + 40, "CONC", 
                       f"Ø{t['concentricity_receiver_bore']}", ["A"])
    
    # Perpendicularity of mouth face
    dwg.draw_gdt_frame(x0 - 10, cy - outer_h - 40, "PERP",
                       str(t['perpendicularity_receiver_mouth']), ["A"])
    
    # Surface profile
    dwg.draw_gdt_frame(x0 + depth*sc/2, cy - inner_h - 25, "PROF_S",
                       str(t['surface_profile_receiver']), ["A", "B"])
    
    # Surface finish
    dwg.draw_surface_finish(x0 + depth*sc * 0.3, cy + inner_h + 3,
                           f"{p['surface_finish_bore_Ra']} μm")
    dwg.draw_surface_finish(x0 + body_len * 0.8, cy + outer_h + 3,
                           f"{p['surface_finish_outer_Ra']} μm")
    
    # CTF flags
    dwg.draw_ctf_flag(x0 + depth*sc/2 + 30, cy + outer_h + 42)
    dwg.draw_ctf_flag(bb_x - 20, cy + outer_h + 12)
    
    # Inspection points
    dwg.draw_inspection_point(x0 + depth*sc/4, cy + outer_h + 55, "IP-1")
    dwg.draw_inspection_point(bb_x, cy + outer_h + 25, "IP-2")
    dwg.draw_inspection_point(x0, cy - outer_h - 30, "IP-3")
    
    # Notes
    notes = [
        "MATERIAL: 316L STAINLESS STEEL PER ASTM A276",
        f"BORE FINISH: Ra {p['surface_finish_bore_Ra']} μm (HONED)",
        f"OUTER FINISH: Ra {p['surface_finish_outer_Ra']} μm",
        "BALL BORE AND BUTTON BORE PERPENDICULAR TO MAIN BORE AXIS",
        f"BALL: {det['ball_diameter']}mm {det['ball_grade']} {det['ball_material']}",
        f"SPRING POCKET CONCENTRIC TO BALL BORE WITHIN Ø0.05",
        "CHAMFER MOUTH 0.5 × 45°",
        "CTF DIMS: 100% INSPECTION REQUIRED",
    ]
    dwg.draw_notes(notes)
    
    dwg.save()


# ============================================================
# DRAWING: TK-BTN-001 Button/Detent Sub-Assembly
# ============================================================
def draw_button():
    print("Generating DWG-003: Button/Detent Sub-Assembly...")
    det = PARAMS["interface"]["detent"]
    
    dwg = EngineeringDrawing(
        "DWG-003-Button-Detent.pdf",
        "BUTTON / DETENT SUB-ASSEMBLY",
        "TK-BTN-001",
        "SEE BOM",
    )
    dwg.scale = "10:1"
    dwg.draw_border()
    dwg.draw_title_block()
    dwg.draw_tolerance_block()
    
    c = dwg.c
    sc = 10.0
    
    # === BUTTON DETAIL ===
    bx = 2.5 * inch
    by = 5 * inch
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(bx - 30, by + det['button_length']*sc/2 + 25, "DETAIL: BUTTON (TK-BTN-001-A)")
    
    c.setLineWidth(1.5)
    # Button shaft
    shaft_h = det['button_length'] * sc
    shaft_w = det['button_diameter'] * sc
    c.rect(bx - shaft_w/2, by - shaft_h/2, shaft_w, shaft_h)
    
    # Button head
    head_w = det['button_head_diameter'] * sc
    head_h = det['button_head_height'] * sc
    c.rect(bx - head_w/2, by + shaft_h/2, head_w, head_h)
    
    # Dimensions
    dwg.draw_dimension(bx - shaft_w/2, by - shaft_h/2, bx - shaft_w/2, by + shaft_h/2,
                       f"{det['button_length']:.2f}", offset=-35)
    dwg.draw_dimension(bx - shaft_w/2 - 5, by - shaft_h/2, bx + shaft_w/2 + 5, by - shaft_h/2,
                       f"Ø{det['button_diameter']:.2f}", offset=-15, above=False)
    dwg.draw_dimension(bx - head_w/2 - 5, by + shaft_h/2, bx + head_w/2 + 5, by + shaft_h/2,
                       f"Ø{det['button_head_diameter']:.2f}", offset=head_h + 12)
    
    c.setFont("Helvetica", 6)
    c.drawString(bx + head_w/2 + 10, by + shaft_h/2 + head_h/2, 
                 f"HEAD HT: {det['button_head_height']:.2f}")
    c.drawString(bx + shaft_w/2 + 10, by,
                 f"TRAVEL: {det['button_travel']:.2f}")
    
    # === BALL DETAIL ===
    ball_cx = 5.5 * inch
    ball_cy = 5 * inch
    ball_r = det['ball_diameter'] * sc / 2
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(ball_cx - 30, ball_cy + ball_r + 20, "DETAIL: BALL (TK-BTN-001-B)")
    
    c.setLineWidth(1.5)
    c.circle(ball_cx, ball_cy, ball_r)
    
    c.setFont("Helvetica", 6)
    c.drawString(ball_cx + ball_r + 10, ball_cy + 5, f"Ø{det['ball_diameter']:.3f}")
    c.drawString(ball_cx + ball_r + 10, ball_cy - 5, f"GRADE: {det['ball_grade']}")
    c.drawString(ball_cx + ball_r + 10, ball_cy - 15, f"MATERIAL: {det['ball_material']}")
    
    # === SPRING DETAIL ===
    sp_cx = 8 * inch
    sp_cy = 5 * inch
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(sp_cx - 30, sp_cy + 40, "DETAIL: SPRING (TK-BTN-001-C)")
    
    sp_h = det['spring_free_length'] * sc / 2
    sp_w = det['spring_outer_diameter'] * sc
    
    # Spring visual (zigzag)
    c.setLineWidth(1)
    coils = 8
    coil_h = sp_h / coils
    for i in range(coils):
        y_base = sp_cy - sp_h/2 + i * coil_h
        c.line(sp_cx - sp_w/2, y_base, sp_cx + sp_w/2, y_base + coil_h/2)
        c.line(sp_cx + sp_w/2, y_base + coil_h/2, sp_cx - sp_w/2, y_base + coil_h)
    
    c.setFont("Helvetica", 6)
    c.drawString(sp_cx + sp_w + 5, sp_cy + 10, f"OD: {det['spring_outer_diameter']:.2f}")
    c.drawString(sp_cx + sp_w + 5, sp_cy, f"WIRE: {det['spring_wire_diameter']:.2f}")
    c.drawString(sp_cx + sp_w + 5, sp_cy - 10, f"FREE LEN: {det['spring_free_length']:.2f}")
    c.drawString(sp_cx + sp_w + 5, sp_cy - 20, f"COMP LEN: {det['spring_compressed_length']:.2f}")
    c.drawString(sp_cx + sp_w + 5, sp_cy - 30, f"RATE: {det['spring_rate_N_per_mm']} N/mm")
    
    # === ASSEMBLY BOM TABLE ===
    table_x = 1.5 * inch
    table_y = 1.5 * inch
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(table_x, table_y + 80, "ASSEMBLY BOM")
    
    c.setFont("Helvetica-Bold", 6)
    headers = ["ITEM", "PART NO.", "DESCRIPTION", "QTY", "MATERIAL"]
    col_w = [30, 70, 120, 25, 120]
    
    c.setLineWidth(0.5)
    y = table_y + 65
    x = table_x
    for i, (h, w) in enumerate(zip(headers, col_w)):
        c.drawString(x + 3, y + 3, h)
        c.rect(x, y, w, 14)
        x += w
    
    rows = [
        ["1", "TK-BTN-001-A", "BUTTON", "1", "POM (DELRIN) / PA66-GF15"],
        ["2", "TK-BTN-001-B", f"BALL Ø{det['ball_diameter']:.3f}", "1", f"{det['ball_grade']} {det['ball_material']}"],
        ["3", "TK-BTN-001-C", "COMPRESSION SPRING", "1", "302 STAINLESS SPRING WIRE"],
    ]
    
    c.setFont("Helvetica", 6)
    for row in rows:
        y -= 14
        x = table_x
        for val, w in zip(row, col_w):
            c.drawString(x + 3, y + 3, val)
            c.rect(x, y, w, 14)
            x += w
    
    # Force specifications
    c.setFont("Helvetica-Bold", 7)
    c.drawString(table_x, table_y - 10, "FORCE SPECIFICATIONS:")
    c.setFont("Helvetica", 6)
    c.drawString(table_x, table_y - 22, 
                 f"RETENTION: {det['retention_force_target_N']} ±{det['retention_force_tolerance_N']} N")
    c.drawString(table_x, table_y - 34, 
                 f"RELEASE: {det['release_force_target_N']} N MAX")
    c.drawString(table_x, table_y - 46, 
                 f"INSERTION: {det['insertion_force_target_N']} N MAX")
    
    notes = [
        "BUTTON MATERIAL: POM (DELRIN) PREFERRED, PA66-GF15 ALTERNATE",
        "BALL: PURCHASED, PRECISION GROUND",
        "SPRING: CUSTOM OR SELECT FROM CATALOG — VERIFY RATE",
        "ASSEMBLY: BALL + SPRING IN POCKET, BUTTON RETAINS",
        "LUBRICATE BALL WITH LIGHT MACHINE OIL AT ASSEMBLY",
        "CYCLE LIFE TARGET: 5,000 INSERTIONS MINIMUM",
    ]
    dwg.draw_notes(notes, x=5*inch, y=1.5*inch)
    
    dwg.save()


# ============================================================
# DRAWING: Comb Drawing (template for TC-001, TC-002, TC-003)
# ============================================================
def draw_comb(comb_id, comb_key, dwg_num):
    comb = PARAMS["combs"][comb_key]
    print(f"Generating DWG-{dwg_num:03d}: {comb_id} {comb['name']}...")
    
    dwg = EngineeringDrawing(
        f"DWG-{dwg_num:03d}-{comb_id}.pdf",
        f"{comb_id}: {comb['name'].upper()}",
        comb_id,
        f"{comb['material_options'][0]} (INJECTION MOLDED)",
    )
    dwg.scale = "1:1"
    dwg.draw_border()
    dwg.draw_title_block()
    dwg.draw_tolerance_block()
    
    c = dwg.c
    sc = 2.5  # Scale for drawing
    
    # Top view of comb
    cx = 4.5 * inch
    cy = 5 * inch
    
    length = comb['overall_length']
    width = comb.get('body_width', 40)
    thickness = comb['body_thickness']
    spine = comb.get('spine_height', 5)
    
    # Simplified top view: spine + teeth
    x0 = cx - length * sc / 3
    y0 = cy
    
    c.setLineWidth(1.5)
    
    # Spine body
    spine_len = length * 0.85
    c.rect(x0, y0, spine_len * sc / 3, spine * sc)
    
    # Receiver housing zone (thicker end)
    recv_zone = 25 * sc / 3
    c.setLineWidth(1)
    c.rect(x0 + spine_len * sc / 3, y0 - 3*sc, recv_zone, spine*sc + 6*sc)
    
    # Teeth (simplified)
    if 'tooth_count_fine' in comb:
        fine_count = comb['tooth_count_fine']
        fine_len = comb.get('tooth_length_fine', 25)
        fine_spacing = comb.get('tooth_spacing_fine', 1.5)
        
        c.setLineWidth(0.3)
        tooth_sc = sc / 3
        for i in range(min(fine_count, 30)):
            tx = x0 + 5*tooth_sc + i * fine_spacing * tooth_sc
            c.line(tx, y0, tx, y0 - fine_len * tooth_sc)
    
    if 'tooth_count_coarse' in comb:
        coarse_count = comb['tooth_count_coarse']
        coarse_len = comb.get('tooth_length_coarse', 22)
        coarse_spacing = comb.get('tooth_spacing_coarse', 3.5)
        
        c.setLineWidth(0.4)
        tooth_sc = sc / 3
        for i in range(min(coarse_count, 20)):
            tx = x0 + 5*tooth_sc + i * coarse_spacing * tooth_sc
            c.line(tx, y0 + spine*sc, tx, y0 + spine*sc + coarse_len * tooth_sc)
    
    # === DIMENSIONS ===
    c.setFont("Helvetica", 7)
    
    # Overall length
    total_w = spine_len * sc / 3 + recv_zone
    dwg.draw_dimension(x0, y0 + spine*sc + 5, x0 + total_w, y0 + spine*sc + 5,
                       f"{length:.2f}", offset=30 if 'tooth_count_coarse' in comb else 15)
    
    # Body width
    c.drawString(x0 + total_w + 10, y0 + spine*sc/2, f"WIDTH: {width:.2f}")
    
    # Thickness
    c.drawString(x0 + total_w + 10, y0 + spine*sc/2 - 12, f"THICK: {thickness:.2f}")
    
    # Tooth details
    y_notes = cy - 80
    c.setFont("Helvetica-Bold", 7)
    c.drawString(x0, y_notes, "TOOTH SPECIFICATIONS:")
    c.setFont("Helvetica", 6)
    
    note_y = y_notes - 12
    if 'tooth_spacing_fine' in comb:
        c.drawString(x0, note_y, f"FINE: {comb['tooth_count_fine']} teeth @ {comb['tooth_spacing_fine']}mm spacing, {comb.get('tooth_length_fine', 25)}mm length")
        note_y -= 10
    if 'tooth_spacing_coarse' in comb:
        c.drawString(x0, note_y, f"COARSE: {comb['tooth_count_coarse']} teeth @ {comb['tooth_spacing_coarse']}mm spacing, {comb.get('tooth_length_coarse', 22)}mm length")
        note_y -= 10
    c.drawString(x0, note_y, f"TOOTH THICKNESS: {comb.get('tooth_thickness', 1.0)}mm, TAPER: {comb.get('tooth_taper_angle', 3)}°")
    
    # === GD&T ===
    # Datum A - receiver bore axis
    recv_x = x0 + spine_len * sc / 3 + recv_zone/2
    dwg.draw_datum_target(recv_x, y0 - 20, "A")
    
    # Profile of surface for tooth plane
    dwg.draw_gdt_frame(x0 + 30, y0 + spine*sc + 50, "PROF_S", "0.15", ["A"])
    
    # CTF flag on receiver interface
    dwg.draw_ctf_flag(recv_x + 10, y0 + spine*sc + 10)
    
    # Surface finish
    dwg.draw_surface_finish(x0 + 10, y0 + spine*sc + 5, "SPI B-2")
    
    # Notes
    notes = [
        f"MATERIAL: {comb['material_options'][0]} / {comb['material_options'][1]}",
        "PROCESS: INJECTION MOLDING",
        f"COLOR: {comb['color']}",
        "SURFACE: SPI B-2 MOLD TEXTURE (MATTE)",
        f"RECEIVER: MOLDED-IN 316L SS INSERT (TK-RECV-001)",
        "DRAFT ANGLE: 1° MIN ALL VERTICAL SURFACES",
        "WALL THICKNESS: 1.5mm MINIMUM THROUGHOUT",
        "GATE LOCATION: ON SPINE (NON-COSMETIC SIDE)",
        "WELD LINE: NOT PERMITTED ON TEETH",
        "CTF: RECEIVER BORE CONCENTRICITY TO BODY DATUM",
    ]
    dwg.draw_notes(notes, x=5.5*inch, y=1.2*inch)
    
    dwg.save()


# ============================================================
# DRAWING: Handle Drawing (template for TH-001, TH-002, TH-003)
# ============================================================
def draw_handle(handle_id, handle_key, dwg_num):
    handle = PARAMS["handles"][handle_key]
    print(f"Generating DWG-{dwg_num:03d}: {handle_id} {handle['name']}...")
    
    dwg = EngineeringDrawing(
        f"DWG-{dwg_num:03d}-{handle_id}.pdf",
        f"{handle_id}: {handle['name'].upper()}",
        handle_id,
        handle["material"],
    )
    dwg.scale = "2:1"
    dwg.draw_border()
    dwg.draw_title_block()
    dwg.draw_tolerance_block()
    
    c = dwg.c
    sc = 3.0
    
    cx = 4 * inch
    cy = 5 * inch
    length = handle['overall_length']
    
    # Side view
    x0 = cx - length * sc / 4
    body_len = length * sc / 2
    
    if handle_key == "TH-001":
        # Double handle - cylindrical with receivers at both ends
        grip_d = handle['grip_diameter']
        grip_h = grip_d * sc / 3
        recv_h = 15.10 * sc / 3  # receiver OD
        
        c.setLineWidth(1.5)
        # Left receiver housing
        c.rect(x0, cy - recv_h/2, body_len * 0.2, recv_h)
        # Taper left
        taper_w = body_len * 0.1
        c.line(x0 + body_len*0.2, cy + recv_h/2, x0 + body_len*0.3, cy + grip_h/2)
        c.line(x0 + body_len*0.2, cy - recv_h/2, x0 + body_len*0.3, cy - grip_h/2)
        # Grip
        c.rect(x0 + body_len*0.3, cy - grip_h/2, body_len * 0.4, grip_h)
        # Taper right
        c.line(x0 + body_len*0.7, cy + grip_h/2, x0 + body_len*0.8, cy + recv_h/2)
        c.line(x0 + body_len*0.7, cy - grip_h/2, x0 + body_len*0.8, cy - recv_h/2)
        # Right receiver housing
        c.rect(x0 + body_len*0.8, cy - recv_h/2, body_len * 0.2, recv_h)
        
    elif handle_key == "TH-002":
        # Flat handle
        body_w = handle['cross_section_width']
        body_h_dim = handle['cross_section_height']
        flat_h = body_h_dim * sc / 2
        recv_h = 15.10 * sc / 3
        
        c.setLineWidth(1.5)
        c.rect(x0, cy - recv_h/2, body_len * 0.25, recv_h)
        # Taper
        c.line(x0 + body_len*0.25, cy + recv_h/2, x0 + body_len*0.35, cy + flat_h/2)
        c.line(x0 + body_len*0.25, cy - recv_h/2, x0 + body_len*0.35, cy - flat_h/2)
        # Flat body
        c.rect(x0 + body_len*0.35, cy - flat_h/2, body_len * 0.60, flat_h)
        # Rounded end
        c.arc(x0 + body_len*0.95 - flat_h/2, cy - flat_h/2, 
              x0 + body_len*0.95 + flat_h/2, cy + flat_h/2, -90, 180)
        
    else:
        # Round handle
        grip_d = handle['grip_diameter']
        grip_h = grip_d * sc / 3
        recv_h = 15.10 * sc / 3
        
        c.setLineWidth(1.5)
        c.rect(x0, cy - recv_h/2, body_len * 0.25, recv_h)
        c.line(x0 + body_len*0.25, cy + recv_h/2, x0 + body_len*0.35, cy + grip_h/2)
        c.line(x0 + body_len*0.25, cy - recv_h/2, x0 + body_len*0.35, cy - grip_h/2)
        c.rect(x0 + body_len*0.35, cy - grip_h/2, body_len * 0.55, grip_h)
        # Dome end
        c.arc(x0 + body_len*0.9 - grip_h/2, cy - grip_h/2,
              x0 + body_len*0.9 + grip_h/2, cy + grip_h/2, -90, 180)
    
    # Center line
    c.setLineWidth(0.2)
    c.setDash(6, 3)
    c.line(x0 - 10, cy, x0 + body_len + 15, cy)
    c.setDash()
    
    # Dimensions
    dwg.draw_dimension(x0, cy + recv_h/2 + 5 if handle_key != "TH-002" else cy + flat_h/2 + 5,
                       x0 + body_len, cy + recv_h/2 + 5 if handle_key != "TH-002" else cy + flat_h/2 + 5,
                       f"{length:.2f}", offset=25)
    
    # Grip dimension
    if 'grip_diameter' in handle:
        c.setFont("Helvetica", 7)
        c.drawString(x0 + body_len + 10, cy + 5, f"GRIP: Ø{handle['grip_diameter']:.2f}")
    elif 'cross_section_width' in handle:
        c.setFont("Helvetica", 7)
        c.drawString(x0 + body_len + 10, cy + 5, f"GRIP: {handle['cross_section_width']}×{handle['cross_section_height']}")
    
    # Receiver info
    c.setFont("Helvetica", 6)
    c.drawString(x0, cy - recv_h/2 - 15 if handle_key != "TH-002" else cy - flat_h/2 - 15,
                 f"RECEIVER: TK-RECV-001 ({handle['receiver_count']}× {handle['receiver_position']})")
    
    # GD&T
    dwg.draw_datum_target(x0 - 15, cy, "A")
    dwg.draw_gdt_frame(x0 + body_len * 0.4, cy + 50, "CONC", "Ø0.03", ["A"])
    
    # Surface finish
    dwg.draw_surface_finish(x0 + body_len * 0.5, cy + recv_h/2 + 3, handle['finish'].split('(')[1].rstrip(')'))
    
    # Notes
    notes = [
        f"MATERIAL: {handle['material']} PER ASTM A276",
        f"FINISH: {handle['finish']}",
        f"GRIP TEXTURE: {handle['grip_texture']}",
        f"RECEIVER INSERT: TK-RECV-001 (PRESS-FIT OR BRAZED)",
        f"RECEIVER COUNT: {handle['receiver_count']}",
        "OVERALL WEIGHT: TBD (WEIGH AFTER MACHINING)",
        "BALANCE POINT: CENTER OF GRIP ±5mm",
        "CTF: RECEIVER BORE AXIS COLINEAR WITH HANDLE AXIS",
    ]
    dwg.draw_notes(notes, x=5.5*inch, y=1.2*inch)
    
    dwg.save()


# ============================================================
# DRAWING: System Assembly
# ============================================================
def draw_assembly():
    print("Generating DWG-010: System Assembly...")
    
    dwg = EngineeringDrawing(
        "DWG-010-System-Assembly.pdf",
        "TAYLKOMB SYSTEM ASSEMBLY",
        "TK-ASM-001",
        "SEE BOM",
    )
    dwg.scale = "1:1"
    dwg.draw_border()
    dwg.draw_title_block()
    
    c = dwg.c
    
    # Assembly exploded view description
    c.setFont("Helvetica-Bold", 10)
    c.drawString(1*inch, 6.5*inch, "TAYLKOMB MODULAR HAIR TOOL SYSTEM — ASSEMBLY OVERVIEW")
    
    c.setFont("Helvetica", 8)
    c.drawString(1*inch, 6.2*inch, "The Taylkomb system consists of interchangeable combs and handles")
    c.drawString(1*inch, 6.0*inch, "connected via a spring-loaded ball detent tang/receiver interface.")
    
    # System BOM table
    table_x = 1 * inch
    table_y = 4.8 * inch
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(table_x, table_y + 15, "SYSTEM BILL OF MATERIALS")
    
    headers = ["ITEM", "PART NO.", "DESCRIPTION", "QTY", "MATERIAL", "PROCESS"]
    col_w = [30, 75, 140, 25, 120, 100]
    
    c.setFont("Helvetica-Bold", 6)
    c.setLineWidth(0.5)
    x = table_x
    for h, w in zip(headers, col_w):
        c.drawString(x + 2, table_y + 3, h)
        c.rect(x, table_y, w, 13)
        x += w
    
    rows = [
        ["1", "TK-TANG-001", "PASSIVE MALE TANG", "1/comb", "316L SS", "CNC TURNING"],
        ["2", "TK-RECV-001", "FEMALE RECEIVER CORE", "1/handle end", "316L SS", "CNC TURNING + MILLING"],
        ["3", "TK-BTN-001", "BUTTON/DETENT SUB-ASSY", "1/receiver", "SEE DWG-003", "ASSEMBLY"],
        ["4", "TC-001", "MAIN COMB (FINE + COARSE)", "1", "PA66-GF30", "INJECTION MOLDING"],
        ["5", "TC-002", "NARROW COMB (FINE)", "1", "PA66-GF30", "INJECTION MOLDING"],
        ["6", "TC-003", "WIDE COMB (COARSE)", "1", "PA66-GF30", "INJECTION MOLDING"],
        ["7", "TH-001", "DOUBLE HANDLE", "1", "316L SS", "CNC TURNING"],
        ["8", "TH-002", "FLAT HANDLE", "1", "316L SS", "CNC MILLING"],
        ["9", "TH-003", "ROUND HANDLE", "1", "316L SS", "CNC TURNING"],
        ["10", "TK-MAG-001", "N52 MAGNET Ø6×2mm", "2/joint", "NdFeB Ni-Cu-Ni", "PURCHASED"],
    ]
    
    c.setFont("Helvetica", 6)
    y = table_y
    for row in rows:
        y -= 13
        x = table_x
        for val, w in zip(row, col_w):
            c.drawString(x + 2, y + 3, val)
            c.rect(x, y, w, 13)
            x += w
    
    # Interface diagram (simplified)
    diag_x = 1.5 * inch
    diag_y = 1.5 * inch
    
    c.setFont("Helvetica-Bold", 8)
    c.drawString(diag_x, diag_y + 100, "INTERFACE DIAGRAM — TANG IN RECEIVER (LOCKED)")
    
    c.setLineWidth(1.5)
    # Simplified cross-section showing tang inside receiver
    # Tang
    c.setFillColor(lightgrey)
    c.rect(diag_x + 20, diag_y + 20, 200, 30, fill=1)
    c.setFillColor(white)
    
    # Receiver (around tang)
    c.setLineWidth(2)
    c.rect(diag_x + 10, diag_y + 10, 180, 50)
    
    # Ball in groove
    c.setFillColor(gray)
    c.circle(diag_x + 120, diag_y + 50, 5, fill=1)
    c.setFillColor(white)
    
    # Labels
    c.setFont("Helvetica", 6)
    c.drawString(diag_x + 230, diag_y + 40, "← TANG (TK-TANG-001)")
    c.drawString(diag_x + 230, diag_y + 25, "← RECEIVER (TK-RECV-001)")
    c.drawString(diag_x + 130, diag_y + 55, "← BALL IN DETENT GROOVE")
    c.drawString(diag_x + 50, diag_y + 65, "BUTTON (TK-BTN-001) →")
    
    # Configuration table
    c.setFont("Helvetica-Bold", 8)
    c.drawString(5.5*inch, diag_y + 100, "VALID CONFIGURATIONS")
    
    c.setFont("Helvetica", 6)
    configs = [
        "TC-001 Main Comb + TH-001 Double Handle",
        "TC-001 Main Comb + TH-002 Flat Handle", 
        "TC-001 Main Comb + TH-003 Round Handle",
        "TC-002 Narrow Comb + TH-001 Double Handle",
        "TC-002 Narrow Comb + TH-002 Flat Handle",
        "TC-002 Narrow Comb + TH-003 Round Handle",
        "TC-003 Wide Comb + TH-001 Double Handle",
        "TC-003 Wide Comb + TH-002 Flat Handle",
        "TC-003 Wide Comb + TH-003 Round Handle",
        "TH-001: Comb on both ends (any combination)",
    ]
    for i, cfg in enumerate(configs):
        c.drawString(5.5*inch, diag_y + 85 - i*10, f"• {cfg}")
    
    dwg.save()


# ============================================================
# DRAWING: Interface Section Detail
# ============================================================
def draw_interface_detail():
    print("Generating DWG-011: Interface Section Detail...")
    
    dwg = EngineeringDrawing(
        "DWG-011-Interface-Detail.pdf",
        "TANG/RECEIVER INTERFACE — SECTION DETAIL",
        "TK-INT-001",
        "SEE COMPONENT DRAWINGS",
    )
    dwg.scale = "10:1"
    dwg.draw_border()
    dwg.draw_title_block()
    dwg.draw_tolerance_block()
    
    c = dwg.c
    sc = 8.0  # 8:1 scale for detail
    
    t = PARAMS["interface"]["tang"]
    r = PARAMS["interface"]["receiver"]
    d = PARAMS["interface"]["detent"]
    tol = PARAMS["tolerances"]
    
    # Cross-section through the lock engagement
    cx = 4 * inch
    cy = 4.5 * inch
    
    tang_r = t["diameter"] * sc / 2
    recv_inner_r = r["bore_diameter"] * sc / 2
    recv_outer_r = r["outer_diameter"] * sc / 2
    
    c.setFont("Helvetica-Bold", 9)
    c.drawString(cx - 80, cy + recv_outer_r + 35, "SECTION X-X: LOCK ENGAGEMENT DETAIL")
    
    # Receiver outer
    c.setLineWidth(2)
    c.circle(cx, cy, recv_outer_r)
    
    # Receiver bore
    c.setLineWidth(1)
    c.circle(cx, cy, recv_inner_r)
    
    # Tang (inside receiver)
    c.setLineWidth(1.5)
    c.circle(cx, cy, tang_r)
    
    # Ball (protruding into tang groove)
    ball_r = d["ball_diameter"] * sc / 2
    ball_y = cy + tang_r - d["ball_diameter"]*sc/4  # partially in groove
    c.setFillColor(gray)
    c.circle(cx, ball_y, ball_r, fill=1)
    c.setFillColor(white)
    
    # Ball bore
    bb_r = r["ball_bore_diameter"] * sc / 2
    c.setLineWidth(0.5)
    c.line(cx - bb_r, cy + recv_inner_r, cx - bb_r, cy + recv_outer_r)
    c.line(cx + bb_r, cy + recv_inner_r, cx + bb_r, cy + recv_outer_r)
    
    # Button bore (90° from ball)
    btn_r = r["button_bore_diameter"] * sc / 2
    c.setDash(3, 2)
    c.line(cx + recv_inner_r, cy - btn_r, cx + recv_outer_r, cy - btn_r)
    c.line(cx + recv_inner_r, cy + btn_r, cx + recv_outer_r, cy + btn_r)
    c.setDash()
    
    # Hatching for receiver wall
    c.setLineWidth(0.15)
    for angle in range(0, 360, 8):
        rad = math.radians(angle)
        x1 = cx + recv_inner_r * math.cos(rad)
        y1 = cy + recv_inner_r * math.sin(rad)
        x2 = cx + recv_outer_r * math.cos(rad)
        y2 = cy + recv_outer_r * math.sin(rad)
        # Only draw hatching away from bores
        if abs(angle - 90) > 20 and abs(angle - 0) > 15 and abs(angle - 180) > 15:
            c.line(x1, y1, x2, y2)
    
    # === CLEARANCE ANNOTATIONS ===
    c.setFont("Helvetica", 6)
    c.setLineWidth(0.3)
    
    # Tang-receiver clearance
    gap = (r["bore_diameter"] - t["diameter"]) / 2
    c.drawString(cx + recv_inner_r + 10, cy - 30, f"DIAMETRAL CLEARANCE:")
    c.drawString(cx + recv_inner_r + 10, cy - 40, f"{r['bore_diameter']:.2f} - {t['diameter']:.2f} = {gap:.2f}mm")
    
    # Ball protrusion
    c.drawString(cx + recv_outer_r + 10, ball_y, f"BALL Ø{d['ball_diameter']:.3f}")
    c.drawString(cx + recv_outer_r + 10, ball_y - 10, f"PROTRUSION: ~{d['ball_diameter']/2 - gap:.2f}mm")
    
    # GD&T
    dwg.draw_gdt_frame(cx - recv_outer_r - 80, cy + recv_outer_r + 5, "CONC", 
                       f"Ø{tol['concentricity_receiver_bore']}", ["A"])
    
    dwg.draw_gdt_frame(cx - recv_outer_r - 80, cy - recv_outer_r - 20, "CONC",
                       f"Ø{tol['concentricity_tang']}", ["A"])
    
    # Fit callouts
    c.setFont("Helvetica-Bold", 7)
    c.drawString(1*inch, 2.5*inch, "FIT ANALYSIS:")
    c.setFont("Helvetica", 6)
    
    tang_tol = tol['interface_tang_diameter']
    recv_tol = tol['interface_receiver_bore']
    
    fit_lines = [
        f"TANG:     Ø{tang_tol['nominal']:.2f} {tang_tol['class']} ({tang_tol['upper']:+.3f} / {tang_tol['lower']:+.3f})",
        f"RECEIVER: Ø{recv_tol['nominal']:.2f} {recv_tol['class']} ({recv_tol['upper']:+.3f} / {recv_tol['lower']:+.3f})",
        f"MIN CLEARANCE: {recv_tol['nominal'] + recv_tol['lower'] - tang_tol['nominal'] - tang_tol['upper']:.3f}mm",
        f"MAX CLEARANCE: {recv_tol['nominal'] + recv_tol['upper'] - tang_tol['nominal'] - tang_tol['lower']:.3f}mm",
        f"FIT TYPE: CLEARANCE FIT (SLIDING)",
        "",
        f"BALL BORE: Ø{r['ball_bore_diameter']:.2f} (BALL Ø{d['ball_diameter']:.3f} = {r['ball_bore_diameter'] - d['ball_diameter']:.3f}mm clearance)",
        f"BUTTON BORE: Ø{r['button_bore_diameter']:.2f} (BUTTON Ø{d['button_diameter']:.2f} = {r['button_bore_diameter'] - d['button_diameter']:.2f}mm clearance)",
    ]
    
    for i, line in enumerate(fit_lines):
        c.drawString(1*inch, 2.3*inch - i*10, line)
    
    # Notes
    notes = [
        "THIS DRAWING SHOWS THE LOCKED ENGAGEMENT CONDITION",
        "BALL MUST PROTRUDE INTO TANG GROOVE FOR RETENTION",
        "BUTTON DEPRESSION RETRACTS BALL TO RELEASE TANG",
        "SPRING MAINTAINS BALL IN ENGAGED POSITION",
        "SEE DWG-001 FOR TANG DETAIL, DWG-002 FOR RECEIVER",
        "SEE DWG-003 FOR BUTTON/DETENT ASSEMBLY",
        "ALL INTERFACE DIMENSIONS ARE CTF — 100% INSPECTION",
    ]
    dwg.draw_notes(notes, x=5.5*inch, y=1.5*inch)
    
    dwg.save()


# ============================================================
# MAIN: Generate all drawings
# ============================================================
if __name__ == "__main__":
    print("=" * 60)
    print("TAYLKOMB Manufacturing Drawing Generator")
    print("GD&T per ASME Y14.5-2018")
    print("=" * 60)
    
    draw_tang()          # DWG-001
    draw_receiver()      # DWG-002
    draw_button()        # DWG-003
    draw_comb("TC-001", "TC-001", 4)   # DWG-004
    draw_comb("TC-002", "TC-002", 5)   # DWG-005
    draw_comb("TC-003", "TC-003", 6)   # DWG-006
    draw_handle("TH-001", "TH-001", 7) # DWG-007
    draw_handle("TH-002", "TH-002", 8) # DWG-008
    draw_handle("TH-003", "TH-003", 9) # DWG-009
    draw_assembly()      # DWG-010
    draw_interface_detail()  # DWG-011
    
    print("")
    print("=" * 60)
    print(f"Generated 11 manufacturing drawings in {OUT_DIR}")
    print("=" * 60)
