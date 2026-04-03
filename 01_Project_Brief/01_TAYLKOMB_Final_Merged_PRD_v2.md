# TAYLKOMB MODULAR COMB SYSTEM — FINAL MERGED PRD v2

**Document No:** TK-PRD-003  
**Revision:** 2.0  
**Date:** April 2, 2026  
**Classification:** Confidential — Patent-Pending Product  
**Prepared for:** TAYLKOMB LLC / Michael David Warren Jr.  
**Status:** SUPERSEDES ALL PRIOR PRDs (TK-PRD-001, TK-PRD-002, and Corrected Master PRD v1)

---

## CHANGE NOTICE

> This document merges and supersedes both prior corrected packages.  
> It adds **durability engineering**, **ergonomic comfort requirements**, and **corrected force targets** that were missing from both predecessors.

---

## 1. Product Vision

TAYLKOMB is a modular 5-in-1 professional styling platform built around one core comb. The Main Comb is the central hub — it carries a single precision male docking tang. Five interchangeable attachments — the Narrow Comb, Wide Comb, Double Handle, Flat Handle, and Round Handle — each slide onto that tang through a shared female receiver interface.

Each attachment locks onto the Main Comb with a positive mechanical detent, so the connection is quick, repeatable, and secure in real salon use. The result is one adaptable tool system that can shift from detangling to precision cutting, sectioning, wig work, and tail-comb parting without changing your grip or reaching for a different full-size tool.

**Investor summary:** One core comb, five interchangeable attachments, one universal docking standard. The base comb carries the docking spine, and every attachment uses the same locking receiver, so the system is fast to swap, easy to learn, and scalable as a product platform.

---

## 2. System Architecture

### 2.1 Correct Topology

```
                    ┌── TC-002 Narrow Comb  (RECEIVER)
                    ├── TC-003 Wide Comb    (RECEIVER)
TC-001 Main Comb ──TANG──┼── TH-001 Double Handle (RECEIVER)
   (sole male)      ├── TH-002 Flat Handle  (RECEIVER)
                    └── TH-003 Round Handle (RECEIVER)
```

| Part ID | Part Name | Connector | Lock Hardware | Material |
|---------|-----------|-----------|---------------|----------|
| TC-001 | Main Comb | **MALE** — passive tang + notch | NONE | Carbon composite |
| TC-002 | Narrow Comb | **FEMALE** — receiver + lock | Ball + Spring + Button | Carbon composite |
| TC-003 | Wide Comb | **FEMALE** — receiver + lock | Ball + Spring + Button | Carbon composite |
| TH-001 | Double Handle | **FEMALE** — receiver + lock | Ball + Spring + Button | 316L stainless |
| TH-002 | Flat Handle | **FEMALE** — receiver + lock | Ball + Spring + Button | 316L stainless |
| TH-003 | Round Handle | **FEMALE** — receiver + lock | Ball + Spring + Button | 316L stainless |

### 2.2 Docking Behavior

- TC-002 and TC-003 dock **inverted** onto TC-001 → double-ended comb (teeth on both ends)
- TH-001, TH-002, TH-003 dock in same direction → Main Comb + specialized handle below

### 2.3 Configuration Matrix (5 configurations from 6 parts)

| Config | Assembly | Primary Use |
|--------|----------|-------------|
| 1 | TC-001 + TC-002 | Double-ended: fine + narrow cutting teeth |
| 2 | TC-001 + TC-003 | Double-ended: fine + wide detangling teeth |
| 3 | TC-001 + TH-001 | Main comb + fork for sectioning/weaving/braiding |
| 4 | TC-001 + TH-002 | Main comb + flat handle for wig work/edge control |
| 5 | TC-001 + TH-003 | Main comb + pointed tail for precision parting/foils |

---

## 3. Locking Mechanism

### 3.1 Primary Lock: Spring-Loaded Ball Detent (Receiver Side)

**Sequence:** Slide on → ball deflects → notch aligns → click → locked.  
**Release:** Press button → ball retracts → slide off.

**Lock hardware lives in EACH of the 5 attachments. TC-001 is entirely passive.**

### 3.2 Corrected Force Targets

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| Insertion force (past ball) | **4–8 N** | One-handed swap mid-session; firm enough to feel deliberate, light enough for speed |
| Pull-out resistance (locked) | **≥20 N** | Secure during aggressive combing, twisting, pulling through resistant hair |
| Button release force | **5–8 N** | Intentional press required, but not fatiguing for repeated swaps |
| Detent engagement (click) | **≥2.0 N** | Clear tactile + audible confirmation |
| Lateral play (locked) | **<0.15 mm** | No perceptible wobble |
| Rotational play (locked) | **<0.5°** | Keyed rectangle prevents rotation |
| Cycle life | **≥10,000** | Pro stylist swapping 20+/day → 10K cycles = ~18 months |

### 3.3 Secondary: Optional Magnet Assist

Design magnet pockets now. Validate detent-only first. Add magnets in Rev B for alignment + premium feel. Do NOT use magnets as primary retention.

### 3.4 Lock Component Stack (per attachment)

| Component | Spec | Qty/System |
|-----------|------|------------|
| Detent ball | 3.00 mm, AISI 52100, Grade 25 | 5 |
| Compression spring | 2.80 OD × 0.40 wire × 6.00 FL, 302 SS, closed/ground, ~0.75 N/mm | 5 |
| Release button | 3.80 mm shaft, 4.50 mm flange, 0.50 mm flange-t, domed cap | 5 |
| N52 magnet (optional) | 4.00 × 2.00 mm disc, NiCuNi coating | 10 (2 per joint) |

---

## 4. DURABILITY ENGINEERING (NEW)

### 4.1 Tooth Breakage Risk — TC-001 Main Comb

**Problem:** The fine-tooth array has ~0.59 mm tooth width at 15.86 mm height = **27:1 aspect ratio**. Under lateral bending (pulling through resistant hair), teeth will fracture at the root in injection-molded carbon nylon if the root has a sharp internal corner.

**Required fixes:**

| Fix | Specification | Priority |
|-----|--------------|----------|
| Tooth root fillet | ≥0.5 mm radius at every tooth-to-spine junction | CRITICAL |
| Tooth taper | Wider at root (0.8 mm), narrower at tip (0.5 mm) | CRITICAL |
| Material selection | PA12-CF or PA66-GF30 (glass-filled nylon for flex resistance) | HIGH |
| Draft angle | ≥1.5° on tooth sidewalls for demolding | HIGH |
| Tooth height limit | Max 25:1 aspect ratio after taper (reduce height or widen root) | RECOMMENDED |

### 4.2 Crown Peak Sharpness

**Problem:** The zigzag crown peaks are ~3.2 mm tip width with sharp internal valleys. These are snag points that catch hair and chip if the comb is dropped.

**Required fixes:**

| Fix | Specification |
|-----|--------------|
| Crown peak radius | ≥1.5 mm fillet on all crown tips |
| Crown spine thickness | ≥4.0 mm at peaks (currently appears thinner) |
| Valley fillet | ≥1.0 mm at internal crown valleys |
| Mold venting | Required at crown valley deepest points |

### 4.3 Fork Junction — TH-001 Double Handle

**Problem:** The two-pronged fork creates a stress riser at the junction where the prongs split from the main body. Under lateral force (especially during weaving/braiding), the junction can crack.

**Required fix:** ≥3.0 mm fillet radius at the fork junction on all faces. Thicken junction zone to ≥4.0 mm cross-section if geometry allows.

### 4.4 Connection Zone Durability

**Problem:** The tang-to-receiver joint must resist bending moment from a 200+ mm comb head. A 5 mm post at 45 mm engagement sees significant leverage.

**Required validation:**

| Test | Method | Pass |
|------|--------|------|
| Lateral deflection | 5 N lateral load at comb tip, measure tang deflection | ≤1.0 mm at joint |
| Bending fatigue | 2 N cyclic lateral load, 10,000 cycles | No visible wear or loosening |
| Drop test | 1 m drop onto concrete, 6 orientations | No separation, lock still functional |

### 4.5 Material Durability Targets

| Component | Environment | Requirement |
|-----------|-------------|-------------|
| Carbon combs (TC-001/002/003) | Heat adjacency | Withstand 200°C radiant heat for 30 min without warping |
| Carbon combs | Chemical | Resistant to alcohol, acetone, styling product chemicals |
| Steel handles (TH-001/002/003) | Glue contact | Surface treatment prevents hair glue adhesion |
| Steel handles | Corrosion | No visible corrosion after 500 hr salt spray (ASTM B117) |
| All parts | UV | No discoloration after 200 hr UV exposure |

---

## 5. ERGONOMIC COMFORT REQUIREMENTS (NEW)

### 5.1 Handle Diameter Minimums

**Problem:** TH-003 Round Handle at 3.11 mm diameter is thinner than a standard pencil (7 mm). TH-002 Flat Handle at 2.54 mm thickness can dig into the palm. Extended professional use (6–10 hr sessions) will cause hand fatigue, reduced control, and potential repetitive strain.

**Required minimums:**

| Part | Current | Required Minimum | Rationale |
|------|---------|-------------------|-----------|
| TH-003 Round Handle | 3.11 mm dia | **≥4.5 mm dia** at narrowest point | Comfort threshold for extended grip; tapered tip can be thinner |
| TH-002 Flat Handle | 2.54 mm thick | **≥3.5 mm thick** in grip zone | Prevents palm digging; can taper thinner at working tip |
| TH-001 Double Handle | 8.00 mm × 27.2 mm | **OK as-is** | Fork shape distributes load well |

### 5.2 Grip Zones

**Problem:** No handles specify grip texture. Professional stylists work with wet, oily, product-coated hands. Smooth metal or plastic is slippery.

**Required treatment per handle:**

| Handle | Grip Zone | Treatment |
|--------|-----------|-----------|
| TH-001 Double Handle | 30–60 mm from receiver end | Fine diamond knurling OR laser-etched micro-texture |
| TH-002 Flat Handle | Full body length | Matte bead-blast finish + optional silicone overmold grip band |
| TH-003 Round Handle | 40–80 mm from receiver end | Fine circumferential knurling OR spiral groove |
| TC-001 Main Comb spine | Crown zone | Subtle spine texture (molded-in logo area doubles as grip) |

### 5.3 Ergonomic Transition Zones

Every attachment must have a **smooth, radiused transition** from the receiver block (8 × 16 mm) to the body cross-section. No sharp edges or abrupt steps at the junction — the hand naturally slides across this zone during use.

| Part | Receiver Block | Body Cross-Section | Transition |
|------|---------------|-------------------|------------|
| TC-002 | 8 × 16 mm | 8 × ~4 mm spine | ≥10 mm taper with ≥2 mm fillets |
| TC-003 | 8 × 16 mm | 8 × ~4 mm spine | ≥10 mm taper with ≥2 mm fillets |
| TH-001 | 8 × 16 mm | 8 × 27.2 mm fork | ≥15 mm flared transition |
| TH-002 | 8 × 16 mm | 7.64 × 3.5 mm flat | ≥12 mm taper, rounded edges |
| TH-003 | 8 × 16 mm | 4.5 mm dia round | ≥15 mm conical taper |

### 5.4 Weight and Balance

The assembled tool should feel balanced in the hand — not tip-heavy or handle-heavy. Target center of gravity within 40% of total length from the grip center.

| Assembly | Estimated CG Target |
|----------|-------------------|
| TC-001 + TH-001 | Within 100 mm of receiver junction |
| TC-001 + TH-002 | Within 90 mm of receiver junction |
| TC-001 + TH-003 | Within 95 mm of receiver junction |
| TC-001 + TC-002 (double-ended) | Centered at junction (symmetric) |
| TC-001 + TC-003 (double-ended) | Centered at junction (symmetric) |

### 5.5 Button Placement and Accessibility

The release button must be:
- Accessible with the thumb or index finger without repositioning the tool
- Recessed or flush (≤0.5 mm proud) to prevent accidental activation during combing
- On the same side across all 5 attachments (consistent muscle memory)
- Positioned so the natural grip does NOT rest on it

**Recommended position:** +X face of receiver block, centered at Z = 35 mm from Datum C (the opening). This places the button approximately 20 mm from the receiver end — reachable with thumb but outside the primary grip zone.

---

## 6. Interface Specification (Merged — TK-IF-003)

### 6.1 Male Tang (TC-001 Only)

| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Width (Y) | 5.08 mm | ±0.02 mm |
| Thickness (X) | 2.54 mm | ±0.02 mm |
| Length | 50.80 mm | ±0.10 mm |
| Corner radius | 0.25 mm | ±0.05 mm |
| Tip chamfer | 0.50 mm × 45° | — |
| Shoulder face | 8.00 × 16.00 mm | ±0.05 mm |
| Shoulder flatness | — | ≤0.10 mm |
| Detent notch center | 35.00 mm from tip | ±0.10 mm |
| Notch depth | 0.80 mm | ±0.05 mm |
| Notch width | 3.00 mm | ±0.10 mm |
| Notch profile | Half-round R1.50 mm | — |
| Tang root fillet | ≥2.00 mm | minimum |
| Magnet pockets | 2× ∅4.10 × 2.20 mm at ±4.50 mm Y | ±0.05 mm |

### 6.2 Female Receiver (All 5 Attachments — Identical Core)

| Parameter | Value | Tolerance |
|-----------|-------|-----------|
| Slot width (Y) | 5.18 mm | +0.05/−0.00 mm |
| Slot thickness (X) | 2.64 mm | +0.05/−0.00 mm |
| Slot depth | 46.00 mm | ±0.20 mm |
| Slot corner radius | 0.30 mm | ±0.05 mm |
| Opening chamfer | 1.00 mm × 45° | — |
| Receiver block outer | 8.00 × 16.00 mm | ±0.05 mm |
| Receiver block length | 55.00 mm | ±0.20 mm |
| Ball window dia | 2.50 mm | ±0.02 mm |
| Ball window center | 35.00 mm from Datum C | ±0.10 mm |
| Spring pocket | ∅3.20 × 8.00 mm | ±0.05/±0.20 mm |
| Button bore | ∅4.00 mm | ±0.05 mm |
| Magnet pockets | 2× ∅4.10 × 2.20 mm in Datum C face | ±0.05 mm |

### 6.3 Prototype Relief Receiver (Fit Coupons Only)

For first-print validation, produce an additional coupon set with relaxed slot dimensions:

| Parameter | Nominal | Prototype Relief |
|-----------|---------|-----------------|
| Slot width | 5.18 mm | 5.23–5.28 mm |
| Slot thickness | 2.64 mm | 2.69–2.74 mm |

This prevents wasted iterations on first SLA/FDM prints where dimensional accuracy is ±0.10–0.15 mm.

---

## 7. Tolerance Study (Merged)

### Chain 1: Width Fit (Y-axis)

| Condition | Tang | Slot | Clearance |
|-----------|------|------|-----------|
| Tightest | 5.10 mm | 5.18 mm | 0.08 mm |
| Nominal | 5.08 mm | 5.18 mm | 0.10 mm |
| Loosest | 5.06 mm | 5.23 mm | 0.17 mm |

**Verdict:** Acceptable. Min clearance prevents binding; max is damped by ball + shoulder.

### Chain 2: Thickness Fit (X-axis)

| Condition | Tang | Slot | Clearance |
|-----------|------|------|-----------|
| Tightest | 2.56 mm | 2.64 mm | 0.08 mm |
| Nominal | 2.54 mm | 2.64 mm | 0.10 mm |
| Loosest | 2.52 mm | 2.69 mm | 0.17 mm |

**Verdict:** Same fit class. Acceptable.

### Chain 3: Detent Engagement (Z-axis)

Worst-case Z misalignment: ±0.20 mm. Notch width 3.00 mm → 2.60 mm overlap at worst. Ball radial engagement ≥0.25 mm. **Robust.**

### Chain 4: Shoulder Seating

Receiver block (55 mm) − slot depth (46 mm) = 9 mm shoulder zone. Tang length (50.80) − slot depth (46) = 4.80 mm overshoot into shoulder zone. **Positive seating confirmed at all tolerance conditions.**

### Chain 5: Button-to-Ball Wall

Available wall: 2.68 mm minimum. Button bore radius: 2.00 mm. Ball window radius: 1.25 mm. Minimum web between bore and slot: ≥0.50 mm. **Tight but workable. Monitor in prototype.**

---

## 8. Family Revision Matrix (Merged)

| Part | Corrected Role | Required Changes | Ergonomic Flags | Priority |
|------|---------------|------------------|-----------------|----------|
| TC-001 Main Comb | Male hub (passive) | Remove any active lock hardware; add passive tang + notch + shoulder + magnet pockets; reinforce tang root ≥2 mm fillet | **Tooth root fillets ≥0.5 mm; tooth taper; crown peak radius ≥1.5 mm** | HIGH |
| TC-002 Narrow Comb | Female receiver | Remove tang → add receiver + lock stack; integrate shared core | Tooth root fillets; transition zone taper from receiver to spine | HIGH |
| TC-003 Wide Comb | Female receiver | Remove tang → add receiver + lock stack; integrate shared core | Tooth root fillets; inverted docking orientation per video | HIGH |
| TH-001 Double Handle | Female receiver | Integrate shared receiver core + lock | **Strengthen fork junction ≥3 mm fillet; add grip knurling 30–60 mm zone** | MEDIUM |
| TH-002 Flat Handle | Female receiver | Integrate shared receiver core + lock | **Increase grip zone to ≥3.5 mm thick; bead-blast finish; review glue-contact surface** | MEDIUM |
| TH-003 Round Handle | Female receiver | Integrate shared receiver core + lock | **Increase diameter to ≥4.5 mm; add circumferential knurling; anti-wobble check (long lever arm)** | MEDIUM |

---

## 9. Test Protocol (Merged)

### Stage 1: Dimensional Verification
All tang and receiver dimensions per Section 6. Go/no-go gauges.

### Stage 2: Fit Coupon Validation
- Coupon A: male tang
- Coupon B: nominal receiver (5.18 × 2.64 mm)
- Coupon C: tight receiver (5.14 × 2.60 mm)
- Coupon D: loose receiver (5.26 × 2.72 mm)
- Coupon E: prototype relief receiver (5.25 × 2.71 mm) ← from Package B
- Coupon F: receiver with ball/spring/button block ← from Package B

### Stage 3: Lock Functional Performance

| Test | Target | Method |
|------|--------|--------|
| Insertion force | 4–8 N | Push-pull gauge |
| Click engagement | Clear audible + tactile | Subjective + microphone dB check |
| Pull-out resistance | ≥20 N | Push-pull gauge, locked state |
| Button release force | 5–8 N | Push-pull gauge on button |
| Shoulder gap | ≤0.05 mm | Feeler gauge |
| Lateral play | <0.15 mm | Dial indicator |

### Stage 4: Interchangeability
All 5 attachments on TC-001. All must pass Stage 3 criteria.

### Stage 5: Cycle Life

| Milestone | Cycles | Pass Criteria |
|-----------|--------|---------------|
| Early screen | 100 | No visible wear; forces within spec |
| Intermediate | 500 | Forces within spec; no deformation |
| Standard | 1,000 | Pull-out ≥18 N (90% of target) |
| Professional grade | 5,000 | Pull-out ≥16 N (80% of target) |
| Target | 10,000 | Pull-out ≥15 N; no visible wear on tang notch or ball |

### Stage 6: Durability & Comfort

| Test | Method | Pass |
|------|--------|------|
| Wet hands | Spray water, operate mechanism | Functional, no slip |
| Product residue | Apply styling gel/pomade, operate | Functional |
| Heat exposure | 30 min near 200°C flat iron | No warping, lock still works |
| Drop test | 1 m onto concrete, 6 orientations | No separation |
| Tooth flex | 5 N lateral at tooth tip (TC-001) | No fracture, ≤2 mm deflection |
| Fork stress | 10 N spread force on TH-001 prongs | No crack at junction |
| Grip fatigue | 30 min continuous styling simulation | No hand pain reported by 3 test stylists |

### Stage 7: Magnet Assessment (Rev B Only)
Self-alignment, retention after 100 cycles, no interference with flat irons/clippers.

---

## 10. Manufacturing Strategy

### One Passive Tang + One Universal Receiver = 2 Interface Geometries

**Before correction:** 6 unique interfaces. **After correction:** 2.

All 5 attachments share identical receiver core → one set of tooling inserts, one assembly fixture, one QC gauge, one BOM for lock components at bulk pricing.

### Assembly Sequence (per attachment)
1. Receiver cavity (molded/machined)
2. Drop-in spring
3. Drop-in ball
4. Button insertion (flange inward)
5. Function test: press button → ball retracts; release → ball returns
6. Optional: adhesive-set magnets with correct polarity

### Surface Treatments

| Treatment | Applied To | Purpose |
|-----------|-----------|---------|
| Teflon (PTFE) or electropolish | TH-001, TH-002, TH-003 body | Glue resistance |
| Grip knurling/texture | TH-001, TH-002, TH-003 grip zones | Anti-slip |
| Ceramic coating (optional) | TH-001, TH-002, TH-003 (alt) | Chemical resistance |

---

## 11. Deliverables Manifest

### This package includes:

**System Docs (A_System_Docs/):**
- 01 — This merged PRD (TK-PRD-003)
- 02 — Corrected architecture overview
- 03 — Ergonomic & durability specification (NEW)
- 04 — Superseded assumptions log

**CAD Control (B_CAD_Control/):**
- 05 — Family revision matrix CSV (with ergonomic flags)
- 06 — Fit coupon plan (with prototype relief variant)
- 07 — Designer handoff checklist

**CAD Scripts (C_CAD_Scripts/):**
- OpenSCAD: corrected lock mechanism (11+ display modes), comb extensions, fit coupons
- build123d: master tang, shared receiver, button/detent module, comb family, handle family, fit coupons
- Export runbook (bash script)

**Output Plans (D_Output_Plans/):**
- STEP/STL/section/render/exploded assembly plans

**Reference (E_Reference/):**
- Architecture SVG diagram
- Force target comparison table

---

## 12. Acceptance Criteria

- [ ] TC-001 is the ONLY male connector
- [ ] All 5 attachments are female receivers with identical lock cores
- [ ] Lock hardware in attachments only, NOT in TC-001
- [ ] Tooth root fillets ≥0.5 mm on all comb teeth
- [ ] Crown peaks filleted ≥1.5 mm radius
- [ ] TH-003 diameter ≥4.5 mm at narrowest grip point
- [ ] TH-002 thickness ≥3.5 mm in grip zone
- [ ] TH-001 fork junction fillet ≥3.0 mm
- [ ] Grip texture specified on all 3 handles
- [ ] Transition zones radiused on all attachments
- [ ] Insertion force 4–8 N, pull-out ≥20 N validated on fit coupons
- [ ] 10,000-cycle life target validated (or trajectory confirmed at 1,000)
- [ ] Fit coupons including prototype relief variant accepted
- [ ] All prior wrong-direction files marked SUPERSEDED

---

## Document Control

| Version | Date | Change |
|---------|------|--------|
| 2.0 | 2026-04-02 | Merged both prior packages; added durability engineering + ergonomic comfort requirements + corrected force targets |
