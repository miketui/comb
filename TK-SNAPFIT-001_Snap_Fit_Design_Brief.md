# TK-SNAPFIT-001 — Snap-Fit Receiver Design Brief
**Document:** TK-SNAPFIT-001 Rev A  
**Date:** April 2026  
**Owner:** Michael David Warren Jr. / TAYLKOMB LLC  
**Status:** PROPOSED — Pending Prototype Validation  
**Patent Status:** Patent Pending — keep confidential

---

## 1. Objective

Redesign the **TK-RECV-001 Receiver** to replace the 3-piece ball + spring + button lock assembly with a **single-piece molded snap-fit lock**. The new design must:

- Match all existing force targets (insertion, retention, release)
- Require **zero loose hardware** per receiver unit
- Be **injection-moldable** in POM (Delrin/acetal)
- Produce the same audible/tactile click on engagement

---

## 2. What Changes vs. What Stays the Same

### Changes
| Component | Current | Proposed |
|-----------|---------|---------|
| TK-RECV-001 Receiver | Has ball pocket bore + spring pocket + button bore | Redesigned with molded snap arm + integrated tab |
| TK-BTN-001 Button | Separate injection-molded part | **Eliminated** — integrated as tab on receiver |
| Material (receiver) | PA66-GF30 or carbon composite | **POM (Delrin 500 or equiv)** |

### Stays the Same — Do Not Change
| Component | Why Unchanged |
|-----------|--------------|
| TC-001 Main Comb | Passive part — no lock hardware, no change needed |
| TC-002 Narrow Comb | Tang notch geometry likely compatible — confirm with fit coupon |
| TC-003 Wide Comb | Same as above |
| TH-001 Double Handle | Same as above |
| TH-002 Flat Handle | Same as above |
| TH-003 Round Handle | Same as above |
| TK-TANG-001 Tang | Notch profile (R1.5mm, 0.8mm deep) likely compatible — minor adjustment possible after coupon testing |

---

## 3. Snap Arm Geometry Targets

These are starting-point dimensions for the designer. Expect 1–2 prototype iterations to tune forces.

| Parameter | Target | Notes |
|-----------|--------|-------|
| Arm length | 14–18mm | Longer = lighter insertion force |
| Arm thickness at root | 1.8–2.2mm | Controls spring stiffness |
| Arm width | 3.0–4.0mm | Controls retention force |
| Tip engagement depth | 0.8mm | Matches existing tang notch depth |
| Tip lead-in chamfer | 30–40° | Controls insertion feel — shallower = smoother |
| Root radius | ≥0.8mm | Critical — prevents fatigue cracking |
| Side clearance (arm to bore wall) | 0.5mm min | Prevents arm binding in bore |
| Tab travel (release press) | 1.5–2.0mm | Same feel as button on current design |

### Arm cross-section
```
  Root (thick end)                    Tip (engagement end)
  at bore back wall                   at notch location
  
  ┌──────────────────────────────────────────────┐
  │  2.0mm thick × 3.5mm wide                   │◄── snap notch hook
  │  fixed to bore wall                          │    (ramp + tooth)
  └──────────────────────────────────────────────┘
  ↑ root radius 0.8mm min
```

---

## 4. Material Specification

### Receiver — POM (Required)

**Grade:** DuPont Delrin 500 (or equivalent homopolymer acetal)

| Property | Value |
|----------|-------|
| Flexural modulus | ~2,700 MPa |
| Elongation at break | ≥40% |
| Heat deflection temp (HDT) | 100°C @ 1.82 MPa |
| Cycle life (snap feature) | 100,000+ cycles (far exceeds 10,000 target) |
| Chemical resistance | Excellent vs. salon chemicals |
| Friction coefficient | Low — self-lubricating, ideal for tang/bore interface |
| Injection moldable | Yes — standard tooling |

**Why not glass-filled nylon (PA66-GF30)?**
Glass fill adds rigidity but reduces elongation and fatigue resistance. A snap arm in GF30 will crack within a few thousand cycles. POM is the industry standard material for snap-fit features in precision consumer products.

**Two-material option:** If matching the existing comb body color/material is important, the receiver body can be two-shot molded — POM for the snap arm section, PA66-GF30 for the outer body. Discuss with your injection mold vendor.

---

## 5. Force Targets (Unchanged from Original Spec)

| Test | Target | Notes |
|------|--------|-------|
| T-01: Insertion force | 4–8 N | One-handed swap |
| T-02: Pull-out resistance | ≥20 N | Stylist pulling through hair |
| T-03: Release (tab press) | 5–8 N | Intentional thumb press |
| T-04: Radial play | <0.15mm | |
| T-05: Angular play | <0.5° | |
| Cycle life | ≥10,000 insertions | POM snap features easily achieve this |

**Tuning the snap arm forces:**
- Insertion too high → increase lead-in chamfer angle (more ramp, less abrupt)
- Insertion too low → decrease chamfer angle (steeper ramp)
- Pull-out too low → increase notch depth (0.8 → 1.0mm) OR increase arm width
- Pull-out too high → reduce notch depth OR increase chamfer at exit angle

---

## 6. Files to Update in GitHub Repo

**Repository:** https://github.com/miketui/comb

| File | Action | What to Do |
|------|--------|-----------|
| `03_Reference_Geometry/B_Geometry/STEP_Parametric/TK-RECV-001.step` | **REPLACE** | Export new snap-fit receiver STEP from native CAD |
| `03_Reference_Geometry/B_Geometry/STL/TK-RECV-001.stl` | **REPLACE** | Export new STL from native CAD |
| `03_Reference_Geometry/B_Geometry/STEP_Parametric/TK-BTN-001.step` | **ARCHIVE** | Move to `_archived/` folder — no longer a standalone part |
| `03_Reference_Geometry/B_Geometry/STL/TK-BTN-001.stl` | **ARCHIVE** | Same |
| `02_CAD_Source/A_CAD_Source/openscad/TK_receiver_core.scad` | **REPLACE** | Rewrite with snap arm + integrated tab geometry |
| `02_CAD_Source/A_CAD_Source/openscad/TK_button_detent.scad` | **ARCHIVE** | No longer needed |
| `02_CAD_Source/A_CAD_Source/parameters.json` | **UPDATE** | Add snap arm parameters (see Section 3) |
| `04_Drawings/C_Drawings/PDF/DWG-002-Receiver.pdf` | **REPLACE** | New drawing with snap arm geometry fully dimensioned |
| `04_Drawings/C_Drawings/PDF/DWG-003-Button-Detent.pdf` | **ARCHIVE** | No longer a standalone part |
| `05_Specs_and_Testing/D_Specifications/TK-HW-001-Hardware-BOM.pdf` | **UPDATE** | Remove: 4mm ball, 3.5mm spring, button (saves 3 BOM line items per attachment) |
| `05_Specs_and_Testing/E_Fit_Coupons/STL/TK-FIT-001-All-Coupons.stl` | **ADD** | New snap-fit coupon: just the arm + notch interface, 3 arm-thickness variants |

**Files NOT changed:** Everything else — all comb and handle parts, tang, assembly drawing, BOM for handles, tolerance stack-up doc.

---

## 7. Prototype / Fit Coupon Strategy

Before redesigning all 5 receivers, print a **minimal snap-fit coupon**:
- Just the snap arm geometry inside a short receiver tube stub (50mm long, not the full receiver)
- Print 3 variants: arm thickness 1.8mm / 2.0mm / 2.2mm
- Print in POM-compatible resin (SLA: Formlabs Rigid 4000 or similar) or FDM POM filament
- Test insertion, pull-out, and release force with push-pull gauge
- Choose the arm thickness that hits 4–8 N insertion and ≥20 N pull-out
- Then commit that geometry to the full receiver design

This saves you from re-iterating on the complete part. Coupon prints are fast (hours) vs. full parts (days).

---

## 8. What to Hand Your CAD Designer

Send them these files from your repo as reference:
1. `03_Reference_Geometry/B_Geometry/STEP_Parametric/TK-RECV-001.step` — dimensional reference for the existing receiver
2. `03_Reference_Geometry/B_Geometry/STEP_Parametric/TK-TANG-001.step` — shows the notch they need to engage
3. `04_Drawings/C_Drawings/PDF/DWG-002-Receiver.pdf` — current drawing with all critical dimensions
4. `04_Drawings/C_Drawings/PDF/DWG-001-Tang.pdf` — notch geometry
5. `02_CAD_Source/A_CAD_Source/parameters.json` — all key dimensions
6. `05_Specs_and_Testing/D_Specifications/TK-TOL-001-Tolerance-Stack-Up.pdf` — interface tolerances

### Deliverables expected back from designer:
1. Native CAD file — `TK-RECV-001-SnapFit.sldprt` (or `.f3d` / `.FCStd`)
2. STEP export — `TK-RECV-001-SnapFit.step`
3. STL export — `TK-RECV-001-SnapFit.stl`
4. Fit coupon STL — 3 arm-thickness variants for rapid iteration
5. Updated drawing — `DWG-002-Receiver-SnapFit.pdf` with:
   - Arm fully dimensioned (length, thickness, width, root radius, chamfer angle)
   - Material callout: POM (Delrin 500 or equiv)
   - Tab clearance and travel dimensioned
   - All existing critical dimensions preserved

---

## 9. Comparison Summary

| | Ball + Spring + Button | Snap-Fit (Proposed) |
|--|--|--|
| Parts per receiver | 3 loose + receiver body | 1 (receiver body only) |
| Factory assembly steps | 3 (press ball, insert spring, insert button) | 0 |
| Supplier relationships | Ball: BC Precision / McMaster; Spring: Lee Spring; Button: mold vendor | None — everything in receiver mold |
| Force behavior | Easy to tune (change spring rate) | Tuneable via geometry (arm length/thickness) |
| Cycle life | ~10,000+ (spring fatigue driven) | 100,000+ (POM fatigue resistance) |
| Repairability | Hardware replaceable | Cannot repair arm — replace receiver unit |
| Cost at volume | Higher (3 components + assembly labor) | Lower (single part, zero assembly) |
| Development work | Minimal (hardware already designed) | One design iteration + coupon validation |

---

*TAYLKOMB LLC — Patent Pending — Confidential Engineering Documentation*  
*TK-SNAPFIT-001 Rev A*
