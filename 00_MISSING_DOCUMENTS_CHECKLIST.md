# TAYLKOMB — Missing Documents Checklist
**Product:** TAYLKOMB Modular Comb System  
**Owner:** Michael David Warren Jr. / TAYLKOMB LLC  
**Last Updated:** April 2026  
**Status:** Pre-Manufacturing — Gap Closure Tracker

Use this as your running checklist. Check off each item as it is completed and signed off.

---

## SECTION A — CAD & Geometry

| # | Document | Status | Who Does It | Notes |
|---|----------|--------|------------|-------|
| A1 | Native CAD part file — TC-001 Main Comb (.sldprt or .f3d) | ☐ Not started | CAD designer | Use STEP_Parametric + drawings as reference |
| A2 | Native CAD part file — TC-002 Narrow Comb | ☐ Not started | CAD designer | |
| A3 | Native CAD part file — TC-003 Wide Comb | ☐ Not started | CAD designer | |
| A4 | Native CAD part file — TH-001 Double Handle | ☐ Not started | CAD designer | |
| A5 | Native CAD part file — TH-002 Flat Handle | ☐ Not started | CAD designer | |
| A6 | Native CAD part file — TH-003 Round Handle | ☐ Not started | CAD designer | |
| A7 | Native CAD part file — TK-TANG-001 Tang | ☐ Not started | CAD designer | |
| A8 | Native CAD part file — TK-RECV-001 Receiver | ☐ Not started | CAD designer | Highest priority — interface part |
| A9 | Native CAD part file — TK-BTN-001 Button | ☐ Not started | CAD designer | |
| A10 | Assembly file with mates/constraints (all 9 parts) | ☐ Not started | CAD designer | After A1–A9 complete |
| A11 | Fresh STEP exports from native CAD (all parts) | ☐ Not started | CAD designer | After A10 |
| A12 | Fresh STL exports from native CAD (all parts) | ☐ Not started | CAD designer | After A10 |
| A13 | Exploded assembly view | ☐ Not started | CAD designer | For assembly instructions |

**What you have now:** OpenSCAD scripts, FreeCAD Python scripts (Tang + Receiver only), and STEP files (not fully editable). A CAD designer can use those as dimensional reference to rebuild.

---

## SECTION B — Engineering Drawings

| # | Document | Status | Who Does It | Notes |
|---|----------|--------|------------|-------|
| B1 | Updated drawings with CTF flags (◆ on critical dims) | ☐ Not started | CAD designer or agent | 7 critical dimensions need flagging |
| B2 | Drawings regenerated from native CAD (true projected views) | ☐ Not started | CAD designer | After Section A complete |
| B3 | Wall thickness callouts added to all 9 part drawings | ☐ Not started | CAD designer | Min walls: 1.5mm comb, 2.0mm handle |
| B4 | Inspection point callouts (bubbles ①②③) on CTF dims | ☐ Not started | CAD designer | Cross-refs to TK-INSP-001 |
| B5 | Inspection plan document (TK-INSP-001) | ☐ Not started | Agent can generate | Sequence + instrument for each CTF dim |

**What you have now:** 11 PDF drawings (DWG-001 through DWG-011) with GD&T, surface finish callouts, and tolerance blocks. These are good dimensional references but are programmatically drawn, not true CAD projections.

---

## SECTION C — Hardware & BOM

| # | Document | Status | Who Does It | Notes |
|---|----------|--------|------------|-------|
| C1 | Purchasable supplier part numbers for all hardware (TK-HW-002) | ☐ Not started | Agent can generate | McMaster, Lee Spring, K&J Magnetics |
| C2 | Hardware sample order placed | ☐ Not started | You | Ball, spring, magnet assortment kits |
| C3 | Assembly sequence document with illustrations (TK-ASM-SEQ-001) | ☐ Not started | Agent can generate | Step-by-step install order |
| C4 | Press-fit specification (ball-to-bore, magnet-to-pocket) | ☐ Not started | Agent can generate | Interference fit values, press forces |
| C5 | Final hardware sign-off (force + supplier confirmed) | ☐ Not started | You (after testing) | Sign off after coupon tests |

**What you have now:** Hardware BOM with specs (TK-HW-001). Suppliers referenced but no purchasable part numbers yet.

---

## SECTION D — Materials & Finish

| # | Document | Status | Who Does It | Notes |
|---|----------|--------|------------|-------|
| D1 | Material freeze sign-off sheet (TK-MAT-FREEZE-001) | ☐ Not started | Agent can generate form, you sign | Formal PDF with signature lines |
| D2 | Color specification — Comb body (RAL or Pantone number) | ☐ Not started | You / brand team | Required before tooling |
| D3 | Color specification — Button color | ☐ Not started | You / brand team | Match or contrast comb? |
| D4 | Handle finish decision — brushed / PVD / electropolish | ☐ Not started | You / brand team | |
| D5 | Chemical resistance test protocol (TK-CHEM-001) | ☐ Not started | Agent can generate | ASTM D543 — salon chemicals |
| D6 | Heat resistance test protocol (TK-HEAT-001) | ☐ Not started | Agent can generate | ASTM D648 HDT test |
| D7 | UV resistance specification (TK-UV-001) | ☐ Not started | Agent can generate | ASTM G154 — 500hr UV test |
| D8 | Chemical resistance test results | ☐ Not started | Lab / you | Requires physical samples |
| D9 | Heat resistance test results | ☐ Not started | Lab / you | Requires physical samples |
| D10 | UV resistance test results | ☐ Not started | Lab / you | Requires physical samples |

**What you have now:** Material decision matrix (PA66-GF30 vs PA12-CF, 316L vs 304). No final decisions signed off yet.

---

## SECTION E — Physical Testing

| # | Document | Status | Who Does It | Notes |
|---|----------|--------|------------|-------|
| E1 | Fit coupons 3D printed | ☐ Not started | You (send STL to print service) | STL at E_Fit_Coupons/TK-FIT-001-All-Coupons.stl |
| E2 | Hardware sourced for coupon testing | ☐ Not started | You | 4mm 316L ball, 3.5mm spring, button |
| E3 | Test equipment sourced | ☐ Not started | You | Push-pull gauge + dial indicator |
| E4 | Test T-01: Insertion force (target 4–8 N) | ☐ Not started | You | 10 cycles × 3 coupons |
| E5 | Test T-02: Pull-out resistance (target ≥20 N) | ☐ Not started | You | |
| E6 | Test T-03: Button release force (target 5–8 N) | ☐ Not started | You | |
| E7 | Test T-04: Wobble/play (target <0.15 mm radial, <0.5°) | ☐ Not started | You | |
| E8 | Test T-05: Cycle life (target ≥10,000 insertions) | ☐ Not started | You | Longest test — plan for it |
| E9 | Test T-06: Drop test (1m onto tile, 10 drops) | ☐ Not started | You | |
| E10 | Test T-07: Wet grip test | ☐ Not started | You | |
| E11 | Test T-08: Lock feel / audible click rating | ☐ Not started | You | |
| E12 | Test data recording sheets (blank forms) | ☐ Not started | Agent can generate | |
| E13 | Completed test data (all T-01 through T-08) | ☐ Not started | You | Gate to freeze interface dims |
| E14 | Full styled prototype assembled | ☐ Not started | You | After coupon results validated |
| E15 | Professional hairstylist trial (min 3 stylists, 2 weeks) | ☐ Not started | You | Structured feedback form |
| E16 | User feedback report | ☐ Not started | You | Fold findings into CAD/drawings |

**What you have now:** Fit coupon STL file and test protocol documents. Zero physical tests completed.

---

## SECTION F — Release Package

| # | Document | Status | Who Does It | Notes |
|---|----------|--------|------------|-------|
| F1 | Final signed drawings (all 9 parts + assembly) | ☐ Not started | CAD designer + you | After all testing complete |
| F2 | Revision-controlled STEP + STL exports | ☐ Not started | CAD designer | From native CAD, not scripts |
| F3 | Final signed BOM with supplier P/Ns | ☐ Not started | You | |
| F4 | Signed material freeze sheet | ☐ Not started | You | |
| F5 | Signed test results package | ☐ Not started | You | |
| F6 | Final manufacturing release bundle (zip) | ☐ Not started | You | Everything above in one folder |
| F7 | Tooling vendor selected + RFQ sent | ☐ Not started | You | Send release bundle to vendor |

---

## SECTION G — Agent Can Generate Now (Just Ask)

These documents don't require physical work or your signature — I can produce them immediately:

| # | Document | Est. Time |
|---|----------|-----------|
| G1 | Purchasable hardware supplier part numbers (TK-HW-002) | Immediate |
| G2 | Assembly sequence document with step-by-step instructions | Immediate |
| G3 | Press-fit specification document | Immediate |
| G4 | Material freeze sign-off sheet (blank, for your signature) | Immediate |
| G5 | Blank test data recording sheets (all 8 tests) | Immediate |
| G6 | Inspection plan document (TK-INSP-001) | Immediate |
| G7 | Chemical / Heat / UV resistance test protocols | Immediate |
| G8 | Updated drawings with CTF flags and wall thickness callouts | Immediate |
| G9 | 7 remaining FreeCAD rebuild scripts (all parts except Tang + Receiver) | Immediate |

---

## PRIORITY ORDER — What to Do First

```
WEEK 1 (Do this now, no CAD designer needed)
  ☐ E1  — Send fit coupon STL to print service (Protolabs / JLCPCB / Craftcloud)
  ☐ C2  — Order hardware samples (ball, spring, magnet assortment)
  ☐ E3  — Buy push-pull gauge + dial indicator
  ☐ G1  — Get supplier part numbers from agent

WEEK 2–3 (Decisions + hire)
  ☐ A1–A9  — Hire CAD designer for native rebuild
  ☐ D2–D4  — Decide colors + handle finish
  ☐ E4–E11 — Run all fit coupon tests when parts arrive
  ☐ D1     — Sign off on material freeze

WEEK 3–4 (After CAD rebuild)
  ☐ A10    — Assembly file complete
  ☐ B2–B4  — Final drawings from native CAD
  ☐ C5     — Final hardware sign-off after tests

WEEK 4–6 (Validation)
  ☐ E14    — Full prototype built
  ☐ E15    — Hairstylist user testing
  ☐ D8–D10 — Lab material testing

AFTER VALIDATION
  ☐ F1–F7  — Build and send final release package to tooling vendor
```

---

*TAYLKOMB LLC — Patent Pending — Confidential*  
*TK-CHECKLIST-001 Rev A*
