# TK-HW-001 Rev A — TAYLKOMB Lock Hardware Bill of Materials

**Document Owner:** Michael David · TAYLKOMB LLC  
**Date:** April 2026  
**Status:** DRAFT — Pending prototype validation  
**Classification:** Confidential Engineering Documentation  

---

## 1. Scope

This document specifies all purchased and custom hardware required for the TAYLKOMB ball-detent lock system. Per corrected architecture (TK-ARCH-001 Rev B):

- Lock hardware lives in the **5 female attachments ONLY**
- TC-001 Main Comb tang is passive (detent notch + optional magnet pockets)
- Each of the 5 attachments contains one complete lock hardware set
- One complete TAYLKOMB system requires **5 sets** of lock hardware

---

## 2. Hardware Summary Table

| Item | Qty/System | Location | Custom/COTS | Priority |
|------|-----------|----------|-------------|----------|
| Detent ball | 5 | Each attachment receiver | COTS | CRITICAL |
| Detent spring | 5 | Each attachment receiver | COTS | CRITICAL |
| Release button | 5 | Each attachment receiver | Custom | HIGH |
| Alignment magnet (optional) | Up to 10 | Attachment shoulder + tang shoulder | COTS | MEDIUM |

---

## 3. Detailed Specifications

### 3.1 Detent Ball

**Priority: CRITICAL — blocks detent notch dimensioning on tang**

| Parameter | Specification | Notes |
|-----------|--------------|-------|
| **Type** | Precision ball | Grade 25 or better |
| **Diameter — Option A** | 2.381 mm (3/32") | Standard COTS size; smaller = finer click feel |
| **Diameter — Option B** | 3.175 mm (1/8") | Standard COTS size; larger = stronger retention per unit spring force |
| **Material — Primary** | AISI 52100 chrome steel | Hardness 60-66 HRC; excellent wear resistance |
| **Material — Alternate** | AISI 316 stainless steel | Hardness 25-30 HRC; corrosion resistant but wears faster |
| **Surface finish** | Grade 25 (Ra ≤ 0.625 μm) | Ensures consistent detent feel |
| **Quantity per system** | 5 | One per attachment |
| **Suggested supplier** | McMaster-Carr #9291K11 (3/32" 52100) or #9291K13 (1/8" 52100) | Also Misumi, MSC Industrial |

**DECISION REQUIRED:**
- Select 2.38 mm or 3.18 mm diameter — this sets the detent notch geometry on the tang and the bore geometry in the receiver
- Select 52100 or 316SS — 52100 recommended unless salon chemical corrosion is validated as a risk in testing
- **Order both sizes in both materials for prototype testing**

### 3.2 Detent Spring

**Priority: CRITICAL — blocks lock force tuning**

| Parameter | Specification | Notes |
|-----------|--------------|-------|
| **Type** | Compression spring | Helical, round wire |
| **Wire material — Primary** | Music wire (ASTM A228) | Highest spring rate per size; not corrosion resistant |
| **Wire material — Alternate** | 302 stainless steel | Corrosion resistant; ~10% lower spring rate |
| **Free length** | TBD — depends on receiver cavity depth | Must be determined from CAD after receiver core dimensioning |
| **OD** | TBD — must fit spring pocket bore | Pocket bore = spring OD + 0.3 mm clearance minimum |
| **Wire diameter** | TBD — drives spring rate | Target range: 0.3–0.6 mm |
| **Spring rate target** | 0.5–1.5 N/mm | Lower = softer click; higher = firmer click |
| **Preload at assembly** | TBD | Must overcome ball weight + friction; typically 0.3–1.0 N |
| **Max compressed height** | Must not coil-bind at full button press | Free length minus max travel must exceed solid height |
| **Ends** | Closed and ground (preferred) | Closed not ground acceptable for prototype |
| **Quantity per system** | 5 | One per attachment |
| **Suggested supplier** | Lee Spring (stock compression springs) or Century Spring | Order assortment kit with 3–5 rates in target range |

**PROTOTYPE PROCUREMENT PLAN:**
Order a compression spring assortment kit containing springs in the following approximate ranges:
- OD: 2.5–4.0 mm (sized to spring pocket bore, TBD)
- Rate: 0.3, 0.5, 0.8, 1.0, 1.5 N/mm
- Free length: 5–10 mm (estimate based on receiver depth)

Test each rate in the lock test block coupon. Select the spring that gives:
- Insertion force (T-02): 5–12 N
- Retention force (T-03): 15–40 N
- Button release force (T-04): 3–8 N

### 3.3 Release Button

**Priority: HIGH — custom geometry, requires prototype iteration**

| Parameter | Specification | Notes |
|-----------|--------------|-------|
| **Type** | Custom molded/machined piston | Cylindrical or rectangular profile |
| **Material — Primary** | POM (Delrin 500) | Self-lubricating, low friction in bore |
| **Material — Alternate** | PA66-GF15 | Matches comb body family; higher friction |
| **Geometry** | Cylindrical piston with textured cap | Cap protrudes from attachment body |
| **Cap texture** | Knurled or crosshatched | Wet-finger grip for salon use |
| **Travel** | TBD — minimum 1.5× ball protrusion depth | Must fully retract ball from detent notch |
| **Retention feature** | Internal shoulder or snap ring groove | Prevents button ejection during use |
| **Fit in bore** | H7/g6 sliding fit | Smooth but no rattle |
| **Quantity per system** | 5 | One per attachment |
| **Prototype method** | SLS PA12 or SLA (POM-like resin) | Print 3 lengths for travel testing |

**DESIGN NOTES:**
- Button actuates perpendicular to tang insertion axis
- Button cap must be accessible with thumb during one-handed operation
- Button must not protrude enough to be accidentally pressed during combing
- Button bore must be sealed against hair/product ingress (simple labyrinth or o-ring if needed)

### 3.4 Alignment Magnet (Optional)

**Priority: MEDIUM — does not block primary lock function**

| Parameter | Specification | Notes |
|-----------|--------------|-------|
| **Type** | Neodymium disc, axially magnetized | N52 grade per prior engineering review |
| **Grade** | N52 | Maximum pull force for size |
| **Diameter — Option A** | 3.0 mm | Smaller, easier to pocket |
| **Diameter — Option B** | 4.0 mm | Stronger pull, needs more pocket depth |
| **Height** | 1.5 mm or 2.0 mm | 2.0 mm gives ~30% more pull than 1.5 mm |
| **Coating** | NiCuNi (nickel) standard | Epoxy coating if chemical exposure risk |
| **Polarity** | Axially magnetized, north/south marked | Must assemble with correct orientation |
| **Operating temp** | 80°C max (N52 Curie point considerations) | Verify with hot tool proximity testing |
| **Quantity per system** | Up to 10 (2 per attachment shoulder + 2 on tang shoulder) | Or 5 pairs depending on final pocket strategy |
| **Suggested supplier** | K&J Magnetics, Supermagnetman | Order D3x1.5 and D4x2 for testing |

**CRITICAL DECISION REQUIRED:**
Are magnets **prototype-only** (for alignment feel testing) or **production-intent**?

- If **prototype-only:** magnet pockets should be present in fit coupons but noted as "optional feature — omit if not specified on PO" in production drawings
- If **production-intent:** magnet pockets must be dimensioned and toleranced in production drawings, and magnet procurement must be included in production BOM

The detent system MUST work without magnets. Magnets are secondary alignment/preload assist only.

---

## 4. Prototype Hardware Procurement Checklist

| Item | Supplier | Part Number / Description | Qty | Est. Cost |
|------|----------|--------------------------|-----|-----------|
| ☐ Ball assortment — 3/32" 52100 | McMaster-Carr | 9291K11 (pack of 100) | 1 pk | ~$8 |
| ☐ Ball assortment — 1/8" 52100 | McMaster-Carr | 9291K13 (pack of 100) | 1 pk | ~$8 |
| ☐ Ball assortment — 3/32" 316SS | McMaster-Carr | 9291K71 (pack of 100) | 1 pk | ~$12 |
| ☐ Ball assortment — 1/8" 316SS | McMaster-Carr | 9291K73 (pack of 100) | 1 pk | ~$12 |
| ☐ Compression spring assortment | Lee Spring / Century Spring | 3–5 rates, OD 2.5–4mm | 1 kit | ~$25–50 |
| ☐ N52 disc magnets — 3mm×1.5mm | K&J Magnetics | D2x1-N52 or similar | 20 pcs | ~$10 |
| ☐ N52 disc magnets — 4mm×2mm | K&J Magnetics | D3x2-N52 or similar | 20 pcs | ~$12 |
| ☐ Push-pull force gauge | Amazon / Imada | 0–20N range, 0.1N resolution | 1 | ~$30–80 |
| ☐ Dial indicator | Amazon / Mitutoyo | 0.01mm resolution, magnetic base | 1 | ~$25–50 |

**Estimated total prototype hardware procurement: $145–250**

---

## 5. Assembly Sequence (Per Attachment)

1. Press or place detent ball into ball bore (interference or slight clearance fit per bore tolerance)
2. Insert compression spring behind ball in spring pocket
3. Insert release button into button bore, compressing spring
4. Verify button retention feature engages (button cannot be pulled out)
5. Verify ball protrudes into receiver slot when button is released
6. Verify ball retracts when button is pressed
7. If magnets are used: press-fit or adhesive-bond magnets into pockets, verify polarity orientation

**Note:** Assembly sequence must be achievable without specialized tooling for Tier 1 / Tier 2 products. Tier 3 (Pro Line) may allow tighter assembly tolerances.

---

## 6. Revision History

| Rev | Date | Description |
|-----|------|-------------|
| A | April 2026 | Initial release — TBD values pending fit-coupon validation and hardware selection |

---

*This document is the property of TAYLKOMB LLC. Patent pending. Do not distribute without authorization.*
