# TAYLKOMB — Detailed Next Steps Roadmap
### From Corrected Handoff Package v4 → Manufacturing-Ready Release

**Prepared for:** Michael David · TAYLKOMB LLC  
**Date:** April 2026  
**Status:** ACTIVE — Execute Phase 1 immediately  

---

## Your Current Position

You have a **strong concept-to-prototype package**. The corrected architecture is clear, consistent, and properly documented. The fit-coupon STEP files exist and are ready to print. But between where you are now and a manufacturer being able to cut tooling, there are five phases of work — and the single most important thing is to **not skip Phase 1**.

---

## PHASE 1: FIT-COUPON VALIDATION (Do This Week)

**Why this is first:** Every dimension in the tolerance spec, every hardware choice in the BOM, and every decision in the material freeze depends on physical test results. If you skip this and go straight to a CAD designer, they'll build parts around unvalidated geometry and you'll pay for two rounds of design instead of one.

### Step 1.1 — Print the Coupons (Days 1–3)

Take these four STEP files from your `D_Fit_Coupons/` folder and send them to a 3D print service:

| File | What It Is | Print In | Qty |
|------|-----------|----------|-----|
| `TK-FIT_Male_Tang_Coupon.step` | The tang connector | PA12 SLS (best) or PLA+ FDM | 5 |
| `TK-FIT_Female_Receiver_Nominal.step` | Receiver at exact nominal slot size | PA12 SLS | 5 |
| `TK-FIT_Female_Receiver_Relief.step` | Receiver with +0.10mm extra clearance | PA12 SLS | 3 |
| `TK-FIT_Lock_Test_Block.step` | Receiver with ball/spring/button bores | PA12 SLS (important — bore accuracy matters) | 3 |

**Where to print:**
- **Fastest:** Xometry, Shapeways, or Craftcloud — upload STEP files, select PA12 SLS (or "Nylon 12"), standard accuracy. Turnaround: 3–5 business days. Cost estimate: $80–$150 total.
- **Budget option:** If you have access to an FDM printer, print the tang and nominal receiver in PLA+ at 0.12mm layer height for a quick dry fit check. But the lock test block really needs SLS for bore accuracy.

**When prints arrive:**
- Measure tang width and thickness with calipers before doing anything else
- Record actual dimensions — your tolerance spec assumes ±0.03mm but 3D prints may be off by ±0.10mm. That's fine for fit validation, just record the actual values

### Step 1.2 — Order the Hardware (Days 1–3, Parallel with Printing)

Order all of this from McMaster-Carr (or equivalent). Total spend: approximately $120–$200.

**Balls:**
- McMaster #9291K11 — 3/32" (2.38mm) chrome steel balls, Grade 25, pack of 100: ~$8
- McMaster #9291K13 — 1/8" (3.18mm) chrome steel balls, Grade 25, pack of 100: ~$8
- McMaster #9291K71 — 3/32" 316 stainless balls, pack of 100: ~$12
- McMaster #9291K73 — 1/8" 316 stainless balls, pack of 100: ~$12

**Springs:**
- Order a compression spring assortment from Lee Spring or Century Spring
- Target OD: 2.5–4.0mm (to fit the spring pocket bore)
- Target rates: 0.3, 0.5, 0.8, 1.0, 1.5 N/mm
- You need springs in multiple rates to find the one that gives the right "click feel"

**Magnets:**
- K&J Magnetics D2x1-N52 (3mm × 1.5mm N52 discs), qty 20: ~$10
- K&J Magnetics D3x2-N52 (4mm × 2mm N52 discs), qty 20: ~$12

**Test Equipment:**
- Push-pull force gauge, 0–20N range, 0.1N resolution, peak-hold: $30–80 on Amazon (search "digital force gauge 20N")
- Dial indicator, 0.01mm resolution, with magnetic base: $25–50 on Amazon (Mitutoyo or iGaging)
- Digital calipers, 0.01mm resolution: $15–30 (you may already have these)

### Step 1.3 — Run the Test Protocol (Days 5–10)

When prints + hardware arrive, execute the 8 tests from TK-FIT-001 in order. Here's the short version:

**T-01: Push tang into receiver (no ball). Target: 3–8N.** If it's too tight, use the relief receiver. If it's too loose, note the clearance for future tightening.

**T-02: Push tang into lock test block (with ball + spring). Target: 5–12N.** Try 3 different spring rates. You're looking for a satisfying "click." Record which spring rate feels best.

**T-03: Pull tang OUT without pressing button. Target: 15–40N.** This is the most critical test. Below 12N = the comb will release during use. Above 50N = the button better work perfectly.

**T-04: Press button to release. Target: 3–8N dry, ≤12N wet.** Try it with wet, conditioner-coated fingers. If you can't release it one-handed with wet fingers, the button needs more texture or the spring needs to be softer.

**T-05: Check wobble. Target: <0.10mm total play.** With tang engaged, try to wiggle it. If it feels sloppy, the clearance is too large.

**After T-01 through T-05: STOP and decide.** Select your final ball size, spring rate, and whether to use nominal or relief receiver dimensions. Only then proceed to:

**T-06: Cycle test (1,000+ insert/release cycles).** Measure retention force degradation.

**T-07: Wet grip test.** Repeat insertion and button release under salon-wet conditions.

**T-08: Round Handle stiffness.** (You'll need the Round Handle prototype for this — can defer to Phase 2 if Round Handle print isn't ready.)

### Step 1.4 — Document Results and Decide

Fill out the Results Summary Template in TK-FIT-001. You now have:
- Final ball diameter (2.38mm or 3.18mm)
- Final ball material (52100 or 316SS)
- Final spring rate
- Final receiver clearance (nominal or adjusted)
- Go/no-go on magnet inclusion

**These results unlock Phase 2.** Without them, your CAD designer is guessing.

---

## PHASE 2: FIND AND BRIEF A CAD DESIGNER (Weeks 2–4)

### What You Need in a Designer

You need someone who works in a parametric CAD environment (SolidWorks, Fusion 360, or Siemens NX) and can produce:
- Native editable part files
- Assembly files with mates/constraints
- Formal manufacturing drawings with GD&T
- STEP/STL exports

**Where to find one:**
- **Upwork/Fiverr:** Search "mechanical product designer" or "injection mold CAD designer." Look for portfolio with consumer product experience (combs, clips, tools). Budget: $2,000–$5,000 for the full package.
- **Komaspec, Protolabs, Xometry:** These manufacturing platforms often have design-for-manufacturing (DFM) services. They'll review your geometry for moldability. Some offer CAD redesign.
- **Local maker spaces / universities:** Mechanical engineering students or recent grads can do excellent CAD work at lower cost. Check local makerspaces for referrals.

### What to Send the Designer

Send them this exact package:
1. **The designer letter** (Document 3 from your original uploads — the "Hi [Designer Name]" letter with corrected architecture, part-by-part instructions, and deliverables list)
2. **Your fit-coupon test results** (the completed Results Summary from TK-FIT-001)
3. **TK-TOL-001** (tolerance spec — gives them all the dimensions)
4. **TK-HW-001** (hardware BOM — gives them ball/spring/button specs)
5. **TK-MAT-001** (material spec — gives them material decisions)
6. **The current STEP files** from `B_CAD_Models/step/` — as dimensional references ONLY
7. **The current STL files** — as shape references
8. **The render PNGs** — as visual references for how the parts should look
9. **The CadQuery Python scripts** — documents the design intent parametrically (tang_production.py, receiver_production.py, button_production.py)

**Tell the designer explicitly:**
> "The current STEP files are mesh-derived or API-generated. Do NOT use them as production geometry. Rebuild everything from scratch in native parametric CAD. Use the STEP files only as dimensional references. The critical interface dimensions are defined in TK-TOL-001."

### What the Designer Delivers

Per the designer letter, you need back:
1. Native CAD files for all 9 parts (6 styled parts + tang + receiver + button)
2. System assembly file with all 6 docking configurations
3. Fit coupon files (updated with test-validated dimensions)
4. STEP exports for every part
5. Watertight STL exports for every part
6. Exploded assembly view
7. Section view through the lock

---

## PHASE 3: PRODUCTION DRAWING PACKAGE (Weeks 4–6)

The same CAD designer (or a dedicated draftsperson) produces formal manufacturing drawings. These are the documents that go to the injection molder, the CNC shop, and the assembly house.

**Every drawing must include:**
- Title block with part number, revision, material, finish, drawn/checked/date
- Datum reference frame (A, B, C per TK-TOL-001)
- All CTF dimensions flagged with inspection triangles
- GD&T callouts per ASME Y14.5-2018
- Surface finish (Ra values) on functional surfaces
- Section views through the lock at engaged and released positions
- BOM for hardware components

**You need these specific drawings:**
1. Passive male tang detail
2. Shared female receiver core detail
3. Button/detent sub-assembly detail
4. TC-001 Main Comb full drawing
5. TC-002 Narrow Comb full drawing
6. TC-003 Wide Comb full drawing
7. TH-001 Double Handle full drawing
8. TH-002 Flat Handle full drawing
9. TH-003 Round Handle full drawing
10. System assembly with exploded view + BOM
11. Interface section detail (tang-in-receiver, lock engaged)
12. Fit/clearance stack-up analysis document

---

## PHASE 4: MATERIAL & FINISH VALIDATION (Weeks 4–8, Parallel with Phase 3)

### Chemical Resistance Testing

You can do this yourself or send material coupons to a testing lab:

1. Get PA66-GF30 test bars (most injection mold material suppliers provide free samples)
2. Get 316L stainless test coupons (ask your CNC shop for scrap pieces)
3. Immerse in: bleach (6% NaOCl), hair color developer (6% H₂O₂), salon conditioner
4. Hold at 40°C for 30 minutes
5. Check for: crazing, discoloration, dimensional change, surface degradation

If you'd rather outsource, services like Intertek, SGS, or Element Materials Technology run standard chemical compatibility testing for ~$200–$500.

### Heat Testing

Touch a flat iron (230°C) to a PA66-GF30 coupon for 10 seconds. Repeat 5 times. If no deformation or damage, you're good.

### Material Freeze Sign-Off

Based on your test results, fill out the Material Freeze Sign-Off table in TK-MAT-001. This is a formal decision point — once you freeze materials, the drawings get updated with material callouts and you don't change them without a revision.

---

## PHASE 5: PRE-PRODUCTION VALIDATION (Weeks 8–12)

### Full Styled-Part Prototyping

With validated CAD and frozen materials:
1. Get injection-molded short-run samples for comb bodies (Protolabs, Xometry, or a local mold shop)
2. Get CNC-machined samples for stainless handles
3. Assemble complete TAYLKOMB system with all hardware

### Professional User Testing

**This is crucial for a hairstyling tool.** Send assembled prototypes to 3–5 professional hairstylists for a 2-week trial. Ask them:
- Does the Main Comb feel balanced with each attachment?
- Is the click engagement satisfying?
- Can you swap attachments one-handed while working on a client?
- Does the Round Handle feel precise enough for parting?
- Does the Flat Handle work for glue application?
- Any wobble, looseness, or unexpected releases?
- Any discomfort during extended use?

### Final Cycle Life Testing

Run 5,000 insert/release cycles on production-intent prototypes. Measure retention force at 0, 100, 500, 1000, 2500, 5000 cycles. If degradation exceeds 20%, reassess ball/spring/material.

### Release to Manufacturing

After all testing passes:
1. Update CAD with any final geometry adjustments from testing
2. Update drawings with final dimensions
3. Create final manufacturing package (CAD + drawings + BOM + assembly instructions + quality control plan)
4. Send to manufacturer for tooling quote

---

## Cost Estimates (Approximate)

| Phase | Activity | Estimated Cost | Timeline |
|-------|----------|---------------|----------|
| 1 | 3D print fit coupons | $80–150 | 3–5 days |
| 1 | Hardware assortment + test equipment | $120–200 | 2–3 days shipping |
| 1 | Your time for testing | $0 (your labor) | 3–5 days |
| 2 | CAD designer (full rebuild + assembly) | $2,000–5,000 | 2–4 weeks |
| 3 | Production drawings (GD&T) | $1,000–2,500 (often included in Phase 2) | 1–2 weeks |
| 4 | Material testing (outsourced) | $200–500 | 2–3 weeks |
| 5 | Short-run prototypes (molded + machined) | $3,000–8,000 | 4–6 weeks |
| 5 | User testing | $500–1,000 (compensate testers) | 2 weeks |
| **TOTAL** | **Concept-to-manufacturing-ready** | **$7,000–17,000** | **8–12 weeks** |

---

## What I Delivered Today

| File | Purpose |
|------|---------|
| **Interactive dashboard** (taylkomb_mfg_readiness.jsx) | 6-tab manufacturing readiness workstation |
| **TK-MFG-001** | Master gap analysis + phased execution plan |
| **TK-TOL-001** | Interface tolerance specification with 20 dimensioned features |
| **TK-HW-001** | Hardware BOM with McMaster part numbers |
| **TK-MAT-001** | Material + finish spec with validation tests |
| **TK-FIT-001** | 8-test fit-coupon protocol with data templates |
| **tang_production.py** | CadQuery script for passive male tang (run in CadQuery env) |
| **receiver_production.py** | CadQuery script for shared female receiver + lock test block |
| **button_production.py** | CadQuery script for release button |
| **Interface cross-section** | Technical drawing of lock mechanism (in-chat visual) |
| **This document** | Detailed next-steps roadmap with costs + timelines |

---

## The One Thing to Do Right Now

**Print the fit coupons and order the hardware.** Everything else follows from the test results. Don't hire a CAD designer until you have test data to give them. Don't freeze materials until you've validated chemical compatibility. Don't promise a manufacturer timeline until you've completed all five phases.

The engineering foundation is solid. The architecture is correct. The interface dimensions are reasonable. Now it needs physical validation.

---

*TAYLKOMB LLC · Patent Pending · Confidential*
