# TK-TOL-001 Rev A — TAYLKOMB Interface Tolerance Specification

**Document Owner:** Michael David · TAYLKOMB LLC  
**Date:** April 2026  
**Status:** DRAFT — Pending fit-coupon validation  
**Classification:** Confidential Engineering Documentation  
**Supersedes:** All prior undimensioned or concept-grade interface specifications  

---

## 1. Scope

This document defines all critical-to-function (CTF) dimensions and tolerances for the TAYLKOMB modular interface system. It governs:

- The passive male tang on TC-001 Main Comb
- The shared female receiver core across all 5 attachments (TC-002, TC-003, TH-001, TH-002, TH-003)
- The ball-detent lock sub-assembly housed in each attachment
- The optional magnetic alignment pockets

All dimensions reference the corrected 1-male / 5-female architecture per TK-ARCH-001 Rev B.

---

## 2. Datum Reference Framework

| Datum | Definition | Location |
|-------|-----------|----------|
| **A** | Tang centerline axis (longitudinal insertion axis) | TC-001 Main Comb tang |
| **B** | Tang shoulder seating face (perpendicular to Datum A) | TC-001 Main Comb shoulder |
| **C** | Receiver slot centerline (mating reference to Datum A) | All 5 attachment receiver cores |

**General tolerance (non-CTF features):** ±0.15 mm linear, ±0.5° angular per ASME Y14.5-2018  
**Surface finish (general):** Ra 1.6 μm unless otherwise specified  

---

## 3. Passive Male Tang Dimensions (TC-001 Main Comb)

| Feature | Nominal | Tolerance | CTF | Datum Ref | Notes |
|---------|---------|-----------|-----|-----------|-------|
| Tang width | 5.08 mm | ±0.03 mm | **YES** | A | Controls lateral fit in receiver slot |
| Tang thickness | 2.54 mm | ±0.03 mm | **YES** | A | Controls vertical play in receiver |
| Tang overall length | 50.80 mm | ±0.10 mm | No | A | Controls insertion depth limit |
| Shoulder face width | 8.00 mm | ±0.05 mm | **YES** | B | Seating plane contact area |
| Shoulder face height | 16.00 mm | ±0.05 mm | **YES** | B | Seating plane contact area |
| Detent notch center from tip | 35.00 mm | ±0.05 mm | **YES** | A | Controls lock engagement position |
| Detent notch width | TBD (≈2.5 mm) | ±0.03 mm | **YES** | — | Must match ball diameter + spring preload geometry |
| Detent notch depth | TBD (≈0.5 mm) | ±0.02 mm | **YES** | — | Controls retention force directly |
| Detent notch radius (bottom) | TBD | ±0.05 mm | **YES** | — | Must match ball radius for positive seat |
| Lead-in chamfer | 0.5 × 45° | ±0.1 mm | No | — | Guides insertion; not retention-critical |
| Tang root fillet radius | R1.0 mm min | +0.5 / −0.0 | No | — | Stress relief; must not undercut shoulder |
| Tip chamfer | 0.3 × 45° | ±0.1 mm | No | — | Prevents edge damage during insertion |

### Tang Surface Finish Requirements

| Surface | Ra Requirement | Reason |
|---------|---------------|--------|
| Tang sides (slot contact faces) | Ra 0.8 μm max | Low friction insertion/removal |
| Detent notch | Ra 0.4 μm max | Ball must seat and release cleanly |
| Shoulder seating face | Ra 1.6 μm | Adequate for stop surface |
| Tang root fillet | Ra 1.6 μm | Standard |

---

## 4. Shared Female Receiver Dimensions (All 5 Attachments)

| Feature | Nominal | Tolerance | CTF | Datum Ref | Notes |
|---------|---------|-----------|-----|-----------|-------|
| Receiver slot width | 5.18 mm | ±0.03 mm | **YES** | C | Clearance to tang = 0.10 mm nom bilateral |
| Receiver slot depth (thickness dir) | 2.64 mm | ±0.03 mm | **YES** | C | Clearance to tang = 0.10 mm nom bilateral |
| Receiver slot length | 48.00 mm | ±0.15 mm | No | C | Must accept full tang minus shoulder stop |
| Shoulder seating plane flatness | — | 0.05 mm | **YES** | B,C | Ensures flush mate at shoulder |
| Ball bore diameter | TBD | ±0.01 mm | **YES** | — | Press-fit or slip-fit; drives retention |
| Ball bore depth | TBD | ±0.02 mm | **YES** | — | Controls ball protrusion into slot |
| Ball bore centerline to slot floor | TBD | ±0.03 mm | **YES** | — | Must align with tang detent notch center |
| Spring pocket diameter | TBD | ±0.03 mm | No | — | Must accept spring OD with clearance |
| Spring pocket depth | TBD | ±0.05 mm | No | — | Controls spring preload at assembly |
| Button bore diameter | TBD | ±0.02 mm | No | — | Sliding fit for button actuation |
| Button bore depth | TBD | ±0.10 mm | No | — | Accommodates button + travel |
| Insertion stop face position | 48.00 mm from entry | ±0.10 mm | No | C | Limits tang insertion depth |
| Magnet pocket diameter (if used) | TBD | ±0.05 mm | No | — | Press-fit or adhesive retention |
| Magnet pocket depth (if used) | TBD | ±0.05 mm | No | — | Flush or sub-flush to mating surface |
| Receiver entry chamfer | 0.5 × 30° | ±0.1 mm | No | — | Guides tang entry |
| Minimum wall thickness (any direction) | 1.50 mm | +∞ / −0.0 | No | — | Structural minimum |

### Receiver Surface Finish Requirements

| Surface | Ra Requirement | Reason |
|---------|---------------|--------|
| Slot internal faces | Ra 0.8 μm max | Low friction sliding |
| Ball bore | Ra 0.4 μm max | Consistent ball seating/release |
| Button bore | Ra 0.8 μm max | Smooth button sliding |
| Shoulder mating face | Ra 1.6 μm | Stop surface |

---

## 5. Tolerance Stack-Up Analysis (Preliminary)

### 5.1 Lateral Fit (Width Direction)

| Parameter | Min | Nominal | Max |
|-----------|-----|---------|-----|
| Receiver slot width | 5.15 | 5.18 | 5.21 |
| Tang width | 5.05 | 5.08 | 5.11 |
| **Clearance** | **0.04** | **0.10** | **0.16** |

**Assessment:** Maximum clearance of 0.16 mm is marginal. If wobble is perceptible in fit-coupon testing (T-05), tighten receiver tolerance to ±0.02 mm (giving max clearance 0.13 mm) or add receiver shim lands.

### 5.2 Vertical Fit (Thickness Direction)

| Parameter | Min | Nominal | Max |
|-----------|-----|---------|-----|
| Receiver slot depth | 2.61 | 2.64 | 2.67 |
| Tang thickness | 2.51 | 2.54 | 2.57 |
| **Clearance** | **0.04** | **0.10** | **0.16** |

**Assessment:** Same profile as width direction. Combined worst-case (both at max clearance) could produce noticeable wobble. Fit-coupon test T-05 will validate.

### 5.3 Detent Engagement (CRITICAL — Cannot calculate until hardware is selected)

| Parameter | Requirement |
|-----------|------------|
| Ball protrusion above slot floor | Must be > detent notch depth to generate retention force |
| Ball retraction below slot floor | Must be achievable via button press to allow tang removal |
| Spring preload at assembly | Must overcome ball weight + friction to maintain engagement |
| Spring force at full button press | Must not exceed 12N button force target |

**ACTION:** Complete this analysis after ball diameter, spring rate, and bore dimensions are finalized from fit-coupon testing.

---

## 6. Drawing Requirements for Designer

All production drawings must include:

1. **Title block** with: part number, revision, material, finish, drawn by, checked by, date, scale
2. **Datum reference frame** (A, B, C as defined above)
3. **All CTF dimensions** flagged with inspection point callout (triangle symbol)
4. **GD&T callouts** per ASME Y14.5-2018 for:
   - Position tolerance on ball bore relative to slot centerline
   - Flatness on shoulder seating faces
   - Straightness on tang over full length
   - Perpendicularity of shoulder face to tang axis
5. **Surface finish callouts** (Ra values) on all functional surfaces
6. **Section views** through the lock mechanism showing ball/spring/button in engaged and released positions
7. **Material and finish specification** in title block and/or notes
8. **General tolerance note** referencing this document (TK-TOL-001)

---

## 7. Revision History

| Rev | Date | Description |
|-----|------|-------------|
| A | April 2026 | Initial release — TBD values pending fit-coupon validation |

---

*This document is the property of TAYLKOMB LLC. Patent pending. Do not distribute without authorization.*
