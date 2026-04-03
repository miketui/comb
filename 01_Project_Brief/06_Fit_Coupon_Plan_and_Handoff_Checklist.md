# TAYLKOMB FIT COUPON PLAN (Merged) + DESIGNER HANDOFF CHECKLIST

**Date:** April 2, 2026

---

## Fit Coupon Set (6 coupons)

### Coupon A — Male Tang

Represents TC-001 connection zone. Tang 5.08 × 2.54 mm, length 50.80 mm, shoulder 8 × 16 × 5 mm, detent notch at 35 mm (0.80 mm deep, 3.00 mm wide), magnet pockets at ±4.50 mm. Handling plate 20 × 20 × 5 mm on back.

### Coupon B — Nominal Receiver

Slot 5.18 × 2.64 mm, depth 46 mm, block 8 × 16 × 55 mm. Ball window ∅2.50 at Z=35. Spring pocket ∅3.20 × 8.00. Button bore ∅4.00. Magnet pockets in Datum C face. Handling plate on back.

### Coupon C — Tight Receiver

Slot 5.14 × 2.60 mm. Tests minimum clearance condition (0.06 mm diametral). Everything else same as B.

### Coupon D — Loose Receiver

Slot 5.26 × 2.72 mm. Tests maximum clearance condition (0.18 mm diametral). Everything else same as B.

### Coupon E — Prototype Relief Receiver (from Package B)

Slot 5.23–5.28 × 2.69–2.74 mm. Compensates for first-print dimensional error on SLA/FDM. **Use this coupon FIRST** for initial validation — it's most likely to fit on first print.

### Coupon F — Ball/Spring/Button Receiver Block (from Package B)

Full receiver with assembled lock hardware. Validate: ball snaps into notch, button releases, spring returns ball. This is the first functional test of the lock mechanism.

## Print Recommendations

| Method | Material | Accuracy | Use |
|--------|----------|----------|-----|
| SLA resin (preferred) | Standard grey | ±0.05 mm | Best for fit validation |
| FDM (budget) | PETG or PLA+ at 0.10 mm | ±0.15 mm | Use Coupon E (relief) first |
| CNC aluminum | 6061-T6 | ±0.02 mm | Production-intent validation |

## Validation Sequence

1. Print Coupon A + Coupon E (relief) → test basic insertion
2. If relief fits: print Coupon B (nominal) → test target fit
3. Print Coupon F → assemble lock hardware → test click, hold, release
4. Measure insertion force (target 4–8 N), pull-out (target ≥20 N), release (target 5–8 N)
5. Print Coupon C (tight) and D (loose) → test boundary conditions
6. Record all results → proceed to full-part revision only after acceptance

---

## DESIGNER HANDOFF CHECKLIST

### Before sending to CAD designer:

**Architecture verification:**
- [ ] TC-001 is the ONLY male part (passive tang, no lock hardware)
- [ ] All 5 attachments have identical female receivers
- [ ] Lock hardware in attachments only
- [ ] Interface spec TK-IF-003 governs (receiver outer = 8 × 16 mm, NOT 20 mm)

**Ergonomic verification:**
- [ ] TH-003 diameter ≥4.5 mm specified
- [ ] TH-002 thickness ≥3.5 mm specified
- [ ] TH-001 fork junction fillet ≥3.0 mm specified
- [ ] Grip texture zones specified for all 3 handles
- [ ] Transition zones radiused for all 5 attachments
- [ ] Tooth root fillets ≥0.5 mm for all combs
- [ ] Crown peak fillets ≥1.5 mm specified
- [ ] Tooth taper (wider root, narrower tip) specified

**Document package:**
- [ ] Final Merged PRD v2 (TK-PRD-003)
- [ ] Architecture Overview v2
- [ ] Ergonomic & Durability Spec v1 (TK-ERGO-001)
- [ ] Family Revision Matrix CSV
- [ ] Fit Coupon Plan (this document)
- [ ] All CAD scripts (OpenSCAD + build123d)

**Reference files (include as-is):**
- [ ] All 6 original STEP files (outer body reference only)
- [ ] All 6 original PDFs (dimension reference only)
- [ ] TK-TANG and TK-RECV STEP files (update with magnet pockets)

**What designer must return:**
- [ ] Native CAD for all 6 updated parts
- [ ] STEP exports for all 6 parts
- [ ] STL exports for fit coupons + prototype parts
- [ ] Exploded lock assembly view
- [ ] Section view through lock centerline
- [ ] Tolerance/clearance verification sheet
- [ ] Prototype BOM with material and surface treatment assumptions
- [ ] Note describing any geometry rebuilt from scratch
- [ ] Confirmation of ergonomic minimums (handle diameters, fillets, grip zones)

**Approval sequence:**
1. Fit coupon geometry (Coupons A through F)
2. Lock section view + tolerance plan
3. Full comb/handle revisions with ergonomic fixes
4. Prototype exports + BOM
