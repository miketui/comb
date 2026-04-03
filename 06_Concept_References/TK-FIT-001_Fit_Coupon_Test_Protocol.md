# TK-FIT-001 Rev A — TAYLKOMB Fit-Coupon Test Protocol

**Document Owner:** Michael David · TAYLKOMB LLC  
**Date:** April 2026  
**Status:** ACTIVE — Execute BEFORE full styled-part refinement  
**Classification:** Confidential Engineering Documentation  

---

## 1. Purpose

This protocol defines the test sequence for validating the TAYLKOMB passive-tang / active-receiver interface using simplified fit coupons. The goal is to confirm interface geometry, select hardware (ball diameter, spring rate), and validate retention/release force targets BEFORE investing in full styled-part CAD refinement.

**CRITICAL: Do not proceed to full-part prototyping without completing this coupon validation. Iterate coupons until the interface works. Then propagate validated dimensions to styled parts.**

---

## 2. Fit Coupon Inventory

The following STEP files exist in `D_Fit_Coupons/` and are ready for 3D printing:

| File | Description | Print Material | Min Qty |
|------|------------|---------------|---------|
| `TK-FIT_Male_Tang_Coupon.step` | Passive male tang with detent notch — represents TC-001 connector geometry | PA66-GF30 (preferred) or PA12 SLS | 5 |
| `TK-FIT_Female_Receiver_Nominal.step` | Shared female receiver at nominal slot dimensions (5.18 × 2.64 mm) | PA12 SLS or FDM PLA+ | 5 |
| `TK-FIT_Female_Receiver_Relief.step` | Female receiver with +0.10 mm relief on slot width/depth (5.28 × 2.74 mm) | Same as nominal | 3 |
| `TK-FIT_Lock_Test_Block.step` | Full receiver core with ball/spring/button cavity for complete lock cycle testing | PA12 SLS (preferred for bore accuracy) | 3 |

### 2.1 Print Specifications

| Parameter | Requirement |
|-----------|------------|
| Process | SLS PA12 preferred for dimensional accuracy; FDM PLA+ acceptable for quick-check only |
| Layer height | ≤0.10 mm (SLS) or ≤0.12 mm (FDM) |
| Orientation | Print tang coupon with insertion axis vertical (best accuracy on width/thickness) |
| Post-processing | Light bead blast or vapor smooth for SLS; no post-processing for FDM |
| Dimensional verification | Measure tang width and thickness with calipers BEFORE testing; record actual dimensions |

---

## 3. Required Test Equipment

| Equipment | Specification | Estimated Cost | Supplier |
|-----------|--------------|---------------|----------|
| Push-pull force gauge | 0–20 N range, 0.1 N resolution, peak-hold function | $30–80 | Amazon, Imada, Shimpo |
| Dial indicator | 0.01 mm resolution, magnetic base | $25–50 | Amazon, Mitutoyo |
| Digital calipers | 0.01 mm resolution, 150 mm range | $15–30 | Mitutoyo, iGaging |
| Small vise or fixture | Benchtop vise with soft jaws | $20–40 | Any |
| Spray bottle + conditioner | Salon conditioner mixed with water (simulate wet-use conditions) | $5 | Salon supply |

---

## 4. Test Sequence

Execute tests in this order. Do not skip ahead. Each test builds on the results of the previous test.

### TEST T-01: Dry Insertion Force (No Detent)

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate basic tang/receiver clearance and insertion feel without lock hardware |
| **Coupons** | Tang coupon + Nominal receiver coupon + Relief receiver coupon |
| **Equipment** | Push-pull force gauge |
| **Setup** | Mount receiver coupon in vise (soft jaws). Insert tang coupon by hand while measuring peak force. |
| **Metric** | Peak insertion force (N) |
| **Target** | 3–8 N (comfortable one-hand push) |
| **Pass criteria** | ≤10 N for any single trial across 5 coupon pairs |
| **Fail action** | If nominal >10 N: use relief coupon for subsequent tests, then tighten tolerance incrementally. If relief >10 N: slot dimensions too tight — widen by 0.05 mm and reprint. |
| **Trials** | 5 insertions per coupon pair (nominal and relief) |

**DATA RECORDING:**

| Trial | Coupon Type | Tang Width (actual) | Receiver Width (actual) | Clearance (calc) | Insertion Force (N) | Pass/Fail | Notes |
|-------|------------|--------------------|-----------------------|-----------------|--------------------|-----------| ------|
| 1 | Nominal | | | | | | |
| 2 | Nominal | | | | | | |
| ... | | | | | | | |

---

### TEST T-02: Dry Insertion Force with Detent

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate detent click feel and over-center insertion force |
| **Coupons** | Tang coupon + Lock test block (with ball and spring installed) |
| **Equipment** | Push-pull force gauge + hardware assortment |
| **Setup** | Install ball + spring in lock test block. Insert tang and measure peak force as ball rides over tang surface and clicks into detent notch. |
| **Metric** | Peak over-center insertion force (N) |
| **Target** | 5–12 N (firm click without requiring two hands) |
| **Pass criteria** | ≤15 N for any single trial |
| **Fail action** | If >15 N: try softer spring rate. If softest spring still >15 N: detent notch ramp angle is too steep — redesign notch entry geometry. |
| **Trials** | 10 insertions per spring rate tested (test 3–5 spring rates) |

**DATA RECORDING:**

| Trial | Ball Ø (mm) | Ball Material | Spring Rate (N/mm) | Spring ID | Insertion Force (N) | Click Feel (1-5) | Pass/Fail | Notes |
|-------|------------|--------------|--------------------|-----------|--------------------|------------------|-----------| ------|
| 1 | | | | | | | | |
| ... | | | | | | | | |

*Click Feel Scale: 1=no click, 2=weak, 3=satisfying, 4=firm, 5=too hard*

---

### TEST T-03: Retention Force (Pull-Out Without Button)

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate that the detent holds securely during vigorous use |
| **Coupons** | Tang coupon + Lock test block (ball/spring installed, detent engaged) |
| **Equipment** | Push-pull force gauge |
| **Setup** | With tang fully engaged and detent locked, pull tang axially WITHOUT pressing release button. Measure force at which tang releases or ball disengages. |
| **Metric** | Pull-out retention force (N) |
| **Target** | 15–40 N (secure during vigorous combing) |
| **Pass criteria** | ≥12 N minimum. If >50 N: system may be too tight — verify button can still release. |
| **Fail action** | If <12 N: increase spring rate or deepen detent notch. If >50 N: decrease spring rate or reduce ball protrusion. |
| **Trials** | 10 pulls per spring rate tested |

> **THIS IS THE MOST CRITICAL TEST.** If retention force is below 12 N, the system will release during professional hairstyling use. This is a hard block.

**DATA RECORDING:**

| Trial | Ball Ø | Spring Rate | Retention Force (N) | Release Mode (gradual/sudden) | Pass/Fail | Notes |
|-------|--------|------------|--------------------|-----------------------------|-----------|-------|
| 1 | | | | | | |
| ... | | | | | | |

---

### TEST T-04: Button Release Force

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate button actuation is easy enough for one-thumb operation with wet fingers |
| **Coupons** | Tang coupon + Lock test block (full hardware installed) |
| **Equipment** | Push-pull force gauge applied to button |
| **Setup** | With tang engaged, press button with gauge until detent ball fully retracts and tang can be pulled free. Test with dry fingers AND wet fingers (water + conditioner). |
| **Metric** | Button press force (N) |
| **Target** | 3–8 N dry, ≤12 N wet |
| **Pass criteria** | ≤12 N with wet fingers. Must be achievable with single thumb. |
| **Fail action** | If >12 N wet: reduce spring rate, increase button mechanical advantage (longer lever arm), or redesign button texture. |
| **Trials** | 10 presses dry + 5 presses wet |

**DATA RECORDING:**

| Trial | Condition | Button Force (N) | Tang Released? | Ease of Use (1-5) | Pass/Fail | Notes |
|-------|----------|------------------|--------------|--------------------|-----------|-------|
| 1 | Dry | | | | | |
| 2 | Wet | | | | | |
| ... | | | | | | |

---

### TEST T-05: Lateral Play / Wobble

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate that tang-in-receiver fit is snug enough to feel solid during use |
| **Coupons** | Tang coupon + Nominal receiver coupon (detent engaged) |
| **Equipment** | Dial indicator (0.01 mm) + fixture |
| **Setup** | With tang fully engaged, apply 2 N lateral force at tang tip (perpendicular to insertion axis). Measure deflection. Test both width and thickness axes. |
| **Metric** | Total lateral play (mm) — total indicator reading |
| **Target** | <0.10 mm TIR |
| **Pass criteria** | ≤0.15 mm. If >0.15 mm: tighten slot clearance or add receiver shim lands. |
| **Fail action** | If >0.15 mm: print receiver with −0.05 mm clearance adjustment and retest. |
| **Trials** | 5 measurements per axis (width and thickness) |

Also conduct subjective assessment: hand the assembled coupon pair to a hairstylist and ask: "Does this feel solid or wobbly?" Record response.

---

### DECISION GATE — Review T-01 through T-05 results before proceeding

After completing T-01 through T-05:
1. Select the final ball diameter that gives the best click feel
2. Select the final spring rate that balances insertion, retention, and button force
3. Determine if nominal or relief receiver clearance is the correct production target
4. If any test failed: adjust geometry/hardware and reprint coupons. DO NOT proceed to T-06.
5. If all tests pass: proceed to T-06 (cycle life) and T-07 (wet grip).

---

### TEST T-06: Cycle Life (Lock/Unlock Durability)

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate that the lock mechanism maintains retention force over repeated use |
| **Coupons** | Tang coupon + Lock test block (final hardware selection from Decision Gate) |
| **Equipment** | Push-pull force gauge + manual or automated cycling fixture |
| **Setup** | Insert tang → confirm click → press button → remove tang. Repeat. Measure retention force at checkpoints. |
| **Metric** | Retention force at cycle 0, 100, 500, 1,000, 2,500, 5,000 |
| **Target** | ≥5,000 cycles with <20% retention force degradation from cycle 0 |
| **Pass criteria** | 1,000 cycles minimum with no mechanical failure. 5,000 cycles target. |
| **Fail action** | If >20% degradation before 1,000 cycles: ball or spring material/hardness must change. Consider 52100 ball if using 316SS. |
| **Trials** | 3 coupon sets tested to 5,000 cycles each |

**DATA RECORDING:**

| Coupon Set | Cycle 0 (N) | Cycle 100 | Cycle 500 | Cycle 1,000 | Cycle 2,500 | Cycle 5,000 | % Degradation | Pass/Fail |
|-----------|------------|-----------|-----------|-------------|-------------|-------------|--------------|-----------|
| A | | | | | | | | |
| B | | | | | | | | |
| C | | | | | | | | |

---

### TEST T-07: Wet Grip Insertion/Release

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate operation under salon conditions (water, conditioner, product) |
| **Coupons** | Tang coupon + Lock test block |
| **Equipment** | Push-pull force gauge + spray bottle with salon conditioner/water mix |
| **Setup** | Thoroughly wet tang and receiver surfaces. Repeat T-01 (insertion) and T-04 (button release). |
| **Metric** | Wet insertion force (N) and wet button release force (N) |
| **Target** | Insertion: ≤12 N wet. Button release: ≤15 N wet. |
| **Pass criteria** | Must remain operable with wet, product-coated fingers. |
| **Fail action** | If wet insertion >12 N: add lube groove to receiver entry or increase entry chamfer. If wet button >15 N: increase button knurl depth. |
| **Trials** | 5 wet insertions + 5 wet button releases |

---

### TEST T-08: Round Handle Stiffness Validation

| Parameter | Specification |
|-----------|--------------|
| **Purpose** | Validate TH-003 Round Handle is stiff enough for precision parting while remaining slimmer than standard tail combs |
| **Coupons** | TH-003 Round Handle prototype (print or machine from production-intent material) |
| **Equipment** | 3-point bending fixture or hand test with force gauge |
| **Setup** | Fix tang end. Apply 5 N lateral force at tip. Measure deflection. |
| **Metric** | Tip deflection (mm) under 5 N lateral load |
| **Target** | ≤3 mm deflection (stiff enough for precision parting) |
| **Pass criteria** | ≤5 mm. If >5 mm: increase wall thickness or add internal ribs. |
| **Fail action** | If >5 mm: redesign Round Handle cross-section. Balance slimness with stiffness. |
| **Trials** | 3 specimens |

Also conduct subjective test: hand the Round Handle to 3 professional hairstylists. Ask: "Can you part hair precisely with this? Does it feel sturdy enough?" Record responses.

---

## 5. Results Summary Template

Complete this summary after all testing is done:

| Test | Result | Pass/Fail | Selected Hardware | Notes |
|------|--------|-----------|------------------|-------|
| T-01 Dry Insertion | ___N | ☐P / ☐F | Receiver type: ☐Nominal / ☐Relief | |
| T-02 Detent Insertion | ___N | ☐P / ☐F | Ball: ___mm / ___material | |
| T-03 Retention | ___N | ☐P / ☐F | Spring rate: ___N/mm | |
| T-04 Button Release (dry) | ___N | ☐P / ☐F | Button travel: ___mm | |
| T-04 Button Release (wet) | ___N | ☐P / ☐F | | |
| T-05 Lateral Play (width) | ___mm | ☐P / ☐F | | |
| T-05 Lateral Play (thickness) | ___mm | ☐P / ☐F | | |
| T-06 Cycle Life | ___cycles to ___% degradation | ☐P / ☐F | | |
| T-07 Wet Insertion | ___N | ☐P / ☐F | | |
| T-07 Wet Button | ___N | ☐P / ☐F | | |
| T-08 Round Handle | ___mm deflection | ☐P / ☐F | | |

### Final Hardware Selection

| Component | Selected Spec | Part Number | Supplier |
|-----------|--------------|-------------|----------|
| Ball | ☐ 2.38mm / ☐ 3.18mm — ☐ 52100 / ☐ 316SS | | |
| Spring | Rate: ___N/mm, OD: ___mm, FL: ___mm | | |
| Button | Travel: ___mm, Material: ☐ POM / ☐ PA66-GF15 | | |
| Magnet | ☐ Included / ☐ Excluded — ☐ 3mm / ☐ 4mm × ___mm | | |

---

## 6. Fold-Back to CAD

After testing is complete and hardware is selected, the following dimensions in TK-TOL-001 must be updated from TBD to final values:

1. Detent notch width → set to match selected ball diameter
2. Detent notch depth → set based on measured optimal retention force
3. Ball bore diameter → set from actual ball size + fit requirement
4. Ball bore depth → set to achieve target ball protrusion
5. Spring pocket diameter → set from selected spring OD + clearance
6. Spring pocket depth → set from spring free length + preload target
7. Button bore diameter → set from button OD + sliding clearance
8. Receiver slot dimensions → confirm nominal or adjusted based on T-01/T-05 results
9. Magnet pocket dimensions → finalize if magnets are production-intent

**These updated values must be reflected in the native CAD rebuild (Phase 2) and production drawings (Phase 3).**

---

## 7. Revision History

| Rev | Date | Description |
|-----|------|-------------|
| A | April 2026 | Initial release — ready for coupon printing and testing |

---

*This document is the property of TAYLKOMB LLC. Patent pending. Do not distribute without authorization.*
