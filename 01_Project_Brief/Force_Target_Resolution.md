# TAYLKOMB Force Target Resolution

## Why prior packages disagreed on force targets

| Parameter | Package A (Claude) | Package B (DOCX) | Final Merged |
|-----------|-------------------|------------------|-------------|
| Insertion force | 3–6 N | 8–12 N | **4–8 N** |
| Pull-out resistance | ≥15 N | ≥20 N | **≥20 N** |
| Button release | 5–10 N | 3–5 N | **5–8 N** |
| Lateral play | Not specified | <0.15 mm | **<0.15 mm** |
| Rotational play | Not specified | <0.5° | **<0.5°** |
| Cycle life | ≥10,000 | ≥1,000 | **≥10,000** |

## Rationale for merged values

**Insertion 4–8 N:** Package A's 3–6 N is too light — a stylist might accidentally dock an attachment while setting it down. Package B's 8–12 N is too firm for one-handed speed swaps. 4–8 N gives deliberate but fast operation.

**Pull-out ≥20 N:** Package B's ≥20 N is the correct target. A stylist pulling through resistant curly/coily hair generates significant axial force on the tool. 15 N risks accidental separation. 20 N provides real-world security.

**Release 5–8 N:** Package B's 3–5 N is too light — accidental button presses during aggressive combing would release the attachment. 5–8 N requires an intentional thumb press.

**Cycle life ≥10,000:** Package B's 1,000 target would be reached in ~2 months of professional use. A professional tool needs 12–18 months minimum before degradation. 10,000 cycles gives ~18 months at 20 swaps/day.

## Spring design implication

To achieve 4–8 N insertion and ≥20 N pull-out, the spring/ball/notch system needs:
- Spring preload (ball against tang face): ~2 N
- Spring force at full ball depression: ~4 N  
- Notch depth: 0.80 mm
- Ball engagement angle and notch profile determine the pull-out force multiplication

The half-round R1.50 notch profile with 0.80 mm depth and 3.00 mm ball provides approximately 3–4× force multiplication from spring force to pull-out resistance. At ~5 N spring force at engagement depth, pull-out resistance should be 15–20 N. **Validate on Coupon F.**
