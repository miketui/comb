# TK-MAT-001 Rev A — TAYLKOMB Material & Finish Specification

**Document Owner:** Michael David · TAYLKOMB LLC  
**Date:** April 2026  
**Status:** DRAFT — Pending chemical/heat validation testing  
**Classification:** Confidential Engineering Documentation  

---

## 1. Scope

This document specifies materials, surface finishes, and coatings for all TAYLKOMB system components. It provides recommendations per product tier and identifies required validation tests before material freeze.

---

## 2. Material Decision Matrix

### 2.1 Comb Bodies (TC-001 Main Comb, TC-002 Narrow Comb, TC-003 Wide Comb)

| Parameter | PA66-GF30 (RECOMMENDED) | PA12-CF (PREMIUM OPTION) |
|-----------|------------------------|-------------------------|
| **Full name** | Polyamide 6/6, 30% glass fiber reinforced | Polyamide 12, carbon fiber reinforced |
| **Tensile strength** | 185–210 MPa | 150–180 MPa |
| **Flexural modulus** | 9,500–11,000 MPa | 12,000–18,000 MPa |
| **Moisture absorption** | 2.5% at equilibrium (dimensional concern) | 0.3% (minimal dimensional change) |
| **Chemical resistance** | Excellent to salon chemicals | Excellent to salon chemicals |
| **Heat deflection** | 250°C (1.82 MPa) | 175°C (1.82 MPa) |
| **Moldability** | Excellent — well-established processing | Good — higher mold wear from CF |
| **Tooth snap resistance** | Good — GF adds toughness | Moderate — CF is stiffer but more brittle at thin sections |
| **Cost (relative)** | 1.0× baseline | 1.8–2.5× baseline |
| **Supplier examples** | DuPont Zytel 70G30HSL, BASF Ultramid A3HG6 | EMS Grilamid LCF-30, Solvay Rilsan |
| **Tier recommendation** | Tier 1 (Essentials) + Tier 2 (Studio) | Tier 3 (Pro Line) only |

**FREEZE RECOMMENDATION:** PA66-GF30 for all tiers initially. Reserve PA12-CF for Tier 3 launch only after validating that the moisture absorption of PA66-GF30 does not cause dimensional issues on the tang width (CTF dimension per TK-TOL-001).

**MOISTURE CONCERN:** PA66-GF30 absorbs moisture and can swell 0.2–0.5% in the tang width direction. At 5.08 mm nominal, a 0.5% swell = 0.025 mm — within the ±0.03 mm tolerance but reduces the clearance margin. Conduct moisture conditioning test (Section 5) to validate.

### 2.2 Handle Bodies (TH-001 Double Handle, TH-002 Flat Handle, TH-003 Round Handle)

| Parameter | 316L Stainless Steel (RECOMMENDED) | 304 Stainless Steel (ACCEPTABLE) |
|-----------|-----------------------------------|----------------------------------|
| **Grade** | AISI 316L (UNS S31603) | AISI 304 (UNS S30400) |
| **Corrosion resistance** | Excellent — resists chloride pitting (bleach, color) | Good — adequate for water, mild chemicals |
| **Salon chemical resistance** | Resists bleach (NaOCl), peroxide (H₂O₂), ammonia | May pit with prolonged bleach/chloride contact |
| **Density** | 7.99 g/cm³ | 7.93 g/cm³ |
| **Machinability** | Moderate — work-hardens, requires sharp tooling | Good — slightly easier than 316L |
| **MIM compatibility** | Excellent — standard MIM alloy | Excellent — standard MIM alloy |
| **Cost (relative)** | 1.3× baseline | 1.0× baseline |
| **Supplier examples** | Any qualified 316L bar stock or MIM feedstock | Any qualified 304 bar stock or MIM feedstock |
| **Tier recommendation** | All tiers | Tier 1 only (if cost reduction is mandatory) |

**FREEZE RECOMMENDATION:** 316L for all tiers. The salon chemical environment (bleach, peroxide, ammonia, color developers) justifies the modest cost premium over 304. Pitting on a professional tool is a brand-damaging failure mode.

### 2.3 Lock Button

| Parameter | POM / Delrin (RECOMMENDED) | PA66-GF15 (ALTERNATE) |
|-----------|---------------------------|----------------------|
| **Full name** | Polyoxymethylene (acetal copolymer) | Polyamide 6/6, 15% glass fiber |
| **Friction coefficient** | 0.15–0.25 (self-lubricating) | 0.35–0.45 (higher friction) |
| **Dimensional stability** | Excellent — low moisture absorption | Moderate — PA66 moisture sensitivity |
| **Fatigue resistance** | Excellent — ideal for repeated click cycling | Good |
| **Chemical resistance** | Good — resistant to most salon chemicals | Excellent |
| **Processing** | Injection molding, CNC machining | Injection molding |
| **Tier recommendation** | All tiers | Only if POM sourcing is an issue |

**FREEZE RECOMMENDATION:** POM (Delrin 500 or equivalent) for all tiers. The self-lubricating property is critical for smooth button feel over thousands of actuation cycles.

---

## 3. Surface Finish & Coating Specifications

### 3.1 Comb Bodies (PA66-GF30)

| Surface | Treatment | Specification | Purpose |
|---------|-----------|--------------|---------|
| External body | Mold texture | VDI 27 (fine matte) or SPI B-2 | Hides flow lines, professional feel |
| Tang sliding surfaces | Mold polish | SPI A-2 or better (Ra ≤ 0.8 μm) | Low friction insertion/removal |
| Detent notch | Mold polish | SPI A-1 (Ra ≤ 0.4 μm) | Clean ball seating/release |
| Color | Molded-in | RAL 9005 (Jet Black) | Match ACISS Obsidian palette |
| Color match tolerance | — | ΔE ≤ 2.0 (CIE Lab) | Consistent across production runs |

### 3.2 Handle Bodies (316L Stainless Steel)

| Surface | Treatment | Specification | Purpose |
|---------|-----------|--------------|---------|
| External body (Tier 1/2) | Bead blast + passivation | Ra 0.8–1.6 μm, ASTM A967 | Uniform satin finish, corrosion activation |
| External body (Tier 3 Pro) | PVD gold coating | TiN or ZrN, 1–3 μm thickness | ACISS Gold accent for premium tier |
| Receiver slot internal | Machine finish + passivation | Ra ≤ 0.8 μm | Low friction tang sliding |
| Ball bore | Reamed + passivation | Ra ≤ 0.4 μm | Consistent ball seating |
| Button bore | Reamed + passivation | Ra ≤ 0.8 μm | Smooth button sliding |

### 3.3 Lock Button (POM)

| Surface | Treatment | Specification | Purpose |
|---------|-----------|--------------|---------|
| Cap (user-facing) | Knurl or crosshatch texture | 0.5 mm pitch diamond knurl | Wet-finger grip |
| Bore-contact surfaces | As-molded | No coating — POM is self-lubricating | Smooth cycling |
| Color (production) | Molded-in | Black (Delrin 500 BK) | Match system aesthetic |
| Color (prototype) | Natural | Natural white POM | Distinguish prototype from production |

---

## 4. Manufacturing Process Recommendations

| Component | Recommended Process | Alternative | Notes |
|-----------|-------------------|------------|-------|
| Comb bodies (PA66-GF30) | Injection molding | — | Single-cavity for proto; multi-cavity for production |
| Handle bodies (316L) | CNC machining (proto) → MIM (production) | Investment casting | MIM preferred for production volume; CNC for <500 units |
| Lock button (POM) | Injection molding | CNC turning | Simple geometry; moldable at moderate volume |
| Detent ball | Purchase COTS | — | See TK-HW-001 |
| Detent spring | Purchase COTS | Custom wind | See TK-HW-001 |
| Magnets (optional) | Purchase COTS | — | See TK-HW-001 |

---

## 5. Required Validation Tests Before Material Freeze

All tests must be completed and results documented before material freeze sign-off.

### 5.1 Chemical Resistance Tests

| Test | Material | Exposure | Conditions | Pass Criteria |
|------|----------|----------|-----------|---------------|
| CR-01 | PA66-GF30 coupon | Bleach (6% NaOCl) | Immersion 30 min @ 40°C | No crazing, discoloration, or >5% property loss |
| CR-02 | PA66-GF30 coupon | Hair color developer (6% H₂O₂) | Immersion 30 min @ 40°C | Same as CR-01 |
| CR-03 | PA66-GF30 coupon | Ammonia-based color (10% NH₃) | Immersion 30 min @ 40°C | Same as CR-01 |
| CR-04 | PA66-GF30 coupon | Salon conditioner (silicone-based) | Immersion 60 min @ 25°C | No surface degradation or swelling |
| CR-05 | 316L coupon | Same as CR-01 through CR-04 | Same conditions | No pitting, discoloration, or corrosion |
| CR-06 | POM button coupon | Same as CR-01 through CR-04 | Same conditions | No swelling >0.5%, no dimensional change |

### 5.2 Heat Resistance Tests

| Test | Material | Exposure | Conditions | Pass Criteria |
|------|----------|----------|-----------|---------------|
| HR-01 | PA66-GF30 coupon | Flat iron contact | 230°C for 10 sec, repeated 5× | No visible deformation, warping, or surface damage |
| HR-02 | PA66-GF30 coupon | Curling iron contact | 200°C for 10 sec, repeated 5× | Same as HR-01 |
| HR-03 | PA66-GF30 coupon | Blow dryer proximity | 150°C airstream for 60 sec | No deformation |
| HR-04 | N52 magnet (if used) | Oven exposure | 80°C for 2 hours | No measurable loss of pull force (>5%) |

### 5.3 Moisture Conditioning Test (PA66-GF30 Specific)

| Test | Specimen | Conditions | Measurement | Pass Criteria |
|------|----------|-----------|-------------|---------------|
| MC-01 | Tang-width coupon (5.08 mm nominal) | 50% RH, 23°C, 7 days | Tang width change | ΔW < 0.025 mm (stays within ±0.03 mm tolerance) |
| MC-02 | Tang-width coupon (5.08 mm nominal) | 95% RH, 23°C, 7 days | Tang width change | ΔW < 0.04 mm (stays within receiver clearance) |
| MC-03 | Full tang coupon | Water immersion, 23°C, 24 hours | Tang width + length change | Dimensional change documented for stack-up update |

---

## 6. Material Freeze Sign-Off

| Component | Material Decision | Signed By | Date |
|-----------|------------------|-----------|------|
| Comb bodies | ☐ PA66-GF30 / ☐ PA12-CF | _____________ | _______ |
| Handle bodies | ☐ 316L / ☐ 304 | _____________ | _______ |
| Lock button | ☐ POM / ☐ PA66-GF15 | _____________ | _______ |
| Magnets | ☐ Production-intent / ☐ Proto-only / ☐ Eliminated | _____________ | _______ |
| Comb body color | ☐ RAL 9005 / ☐ Other: _____ | _____________ | _______ |
| Handle finish (Tier 1/2) | ☐ Bead blast + passivation / ☐ Other: _____ | _____________ | _______ |
| Handle finish (Tier 3) | ☐ PVD gold / ☐ Other: _____ | _____________ | _______ |

---

## 7. Revision History

| Rev | Date | Description |
|-----|------|-------------|
| A | April 2026 | Initial release — pending validation test completion |

---

*This document is the property of TAYLKOMB LLC. Patent pending. Do not distribute without authorization.*
