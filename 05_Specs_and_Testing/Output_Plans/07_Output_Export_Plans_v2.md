# TAYLKOMB OUTPUT & EXPORT PLANS (Merged)

**Date:** April 2, 2026

---

## STEP Export Plan

| # | File | Priority |
|---|------|----------|
| 1 | TC-001_Main_Comb_v2.step | HIGH — add tooth fillets, crown radii, verified tang |
| 2 | TC-002_Narrow_Comb_v2.step | HIGH — remove tang, add receiver + lock |
| 3 | TC-003_Wide_Comb_v2.step | HIGH — remove tang, add receiver + lock |
| 4 | TH-001_Double_Handle_v2.step | MEDIUM — add lock, fork junction fillet, grip knurling |
| 5 | TH-002_Flat_Handle_v2.step | MEDIUM — add lock, increase to ≥3.5mm, bead-blast |
| 6 | TH-003_Round_Handle_v2.step | MEDIUM — add lock, increase to ≥4.5mm, knurling |
| 7 | TK-TANG_Universal_Tang_v2.step | MEDIUM — add magnet pockets |
| 8 | TK-RECV_Universal_Receiver_v2.step | MEDIUM — add all lock bores + magnets |
| 9 | TK-BTN_Release_Button_v2.step | MEDIUM — rebuild native |

## STL Export Plan

| # | File | Priority |
|---|------|----------|
| 1 | FIT_Coupon_A_Tang.stl | IMMEDIATE |
| 2 | FIT_Coupon_B_Receiver_Nominal.stl | IMMEDIATE |
| 3 | FIT_Coupon_E_Receiver_Relief.stl | IMMEDIATE — print first |
| 4 | FIT_Coupon_F_Lock_Block.stl | IMMEDIATE |
| 5 | FIT_Coupon_C_Tight.stl | AFTER nominal validation |
| 6 | FIT_Coupon_D_Loose.stl | AFTER nominal validation |
| 7–12 | Full parts (all 6) | AFTER fit coupon acceptance |

## Section View Plan

| # | View | Shows |
|---|------|-------|
| 1 | Lock cross-section (Y=0) | Ball, spring, button, notch engagement |
| 2 | Tang-receiver fit (Y=0, zoomed) | Clearance, walls, chamfer |
| 3 | Shoulder seating (X=0) | Shoulder contact, magnet alignment |
| 4 | Comb extension docking (Y=0) | Inverted double-ended assembly |
| 5 | Tooth root detail | Fillet radius at spine junction |

## Render Plan

| # | View | Purpose |
|---|------|---------|
| 1 | System exploded (all 6 parts) | Investor hero shot |
| 2 | Lock exploded (receiver cutaway) | Engineering communication |
| 3 | All 5 configurations | Product catalog |
| 4 | Double-ended comb close-up | Unique value proposition |
| 5 | Grip texture details | Ergonomic story |
| 6 | Material tiers (black / ACISS / steel) | Product line strategy |

## Approval Sequence

```
1. FIT COUPONS (print E first, then A+B, then F)
   → validate insertion, click, hold, release forces
   ↓ APPROVE

2. LOCK SECTION + TOLERANCE
   → verify ball engagement, spring force, button travel
   ↓ APPROVE

3. FULL PART REVISIONS (with ergonomic fixes)
   → rebuild all 6 parts, verify comfort dimensions
   ↓ APPROVE

4. PROTOTYPE EXPORTS
   → generate all STEP/STL, BOM, surface treatment specs
   ↓ APPROVE → PROTOTYPE BUILD
```
