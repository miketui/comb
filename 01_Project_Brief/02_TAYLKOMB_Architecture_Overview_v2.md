# TAYLKOMB CORRECTED ARCHITECTURE OVERVIEW v2

**Document No:** TK-ARCH-002  
**Date:** April 2, 2026

---

## System Diagram

```
                         ┌─────────────────────────────┐
                         │   TC-001 MAIN COMB            │
                         │   • Carbon composite          │
                         │   • Fine-tooth array           │
                         │   • Zigzag crown (fillet peaks)│
                         │   • SOLE MALE TANG (passive)   │
                         │   • Detent notch               │
                         │   • Shoulder stop + mag pockets │
                         │   • NO moving lock parts       │
                         │   • Root fillets ≥0.5mm        │
                         │   • Tooth taper: 0.8mm→0.5mm   │
                         └────────────┬──────────────────┘
                                      │
                              UNIVERSAL TANG
                          5.08 × 2.54 mm keyed rect
                                      │
         ┌──────────────┬─────────────┼──────────────┬──────────────┐
         │              │             │              │              │
    ┌────┴────┐   ┌─────┴────┐  ┌────┴─────┐  ┌────┴────┐  ┌─────┴─────┐
    │ TC-002  │   │ TC-003   │  │ TH-001   │  │ TH-002  │  │ TH-003    │
    │ Narrow  │   │ Wide     │  │ Double   │  │ Flat    │  │ Round     │
    │ Comb    │   │ Comb     │  │ Handle   │  │ Handle  │  │ Handle    │
    │         │   │          │  │          │  │         │  │           │
    │ Carbon  │   │ Carbon   │  │ 316L SS  │  │ 316L SS │  │ 316L SS   │
    │ INVERTED│   │ INVERTED │  │ Fork     │  │ Flat    │  │ Pintail   │
    │ dock    │   │ dock     │  │          │  │ ≥3.5mm  │  │ ≥4.5mm    │
    │         │   │ zigzag   │  │ ≥3mm     │  │ grip    │  │ dia grip  │
    │         │   │ bottom   │  │ junction │  │ bead-   │  │ knurled   │
    │         │   │          │  │ fillet   │  │ blast   │  │           │
    └────┬────┘   └────┬─────┘  └────┬─────┘  └────┬────┘  └─────┬─────┘
         │              │             │              │              │
         └──────────────┴─────────────┴──────────────┴──────────────┘
                                      │
                        SHARED FEMALE RECEIVER
                     5.18 × 2.64 mm slot + lock
                                      │
                        ┌─────────────┴─────────────┐
                        │  COMMON LOCK CARTRIDGE      │
                        │  • Ball 3.0mm Gr25          │
                        │  • Spring 2.8OD×0.4w×6.0FL  │
                        │  • Button 3.8mm + 4.5 flange│
                        │  • Ball window 2.5mm         │
                        │  • Optional N52 mag pockets  │
                        └─────────────────────────────┘
```

## Key Design Rules

1. **One hub, one standard, infinite scalability** — TC-001 never changes; future attachments just implement the receiver
2. **Lock in the accessory, not the hub** — simplest possible base part, all complexity in swappable pieces
3. **Durability first** — tooth fillets, crown radii, junction strengthening, grip texture before aesthetics
4. **Comfort drives dimensions** — handle diameters set by ergonomics, not aesthetics
5. **Prototype relief** — always make one loose coupon for first-print validation

## Material Architecture

| Component | Material | Key Property |
|-----------|----------|-------------|
| TC-001, TC-002, TC-003 | PA12-CF or PA66-GF30 | Heat-resistant (200°C), stiff, chemical-resistant |
| TH-001, TH-002, TH-003 | 316L stainless steel | Glue-resistant (with PTFE/electropolish), corrosion-resistant |
| Detent balls | AISI 52100 chrome steel | 60-66 HRC hardness, Grade 25 precision |
| Springs | 302 stainless wire | Corrosion-resistant, consistent force |
| Buttons | 303 stainless | Smooth actuation, machinable |
| Magnets (optional) | N52 neodymium, NiCuNi coating | ~1.2N pull force per pair |

## Scalability Path

Every future attachment (heated comb, edge tool, pin curl pick, foil lifter) only needs:
- Same 5.18 × 2.64 mm receiver slot
- Same ball/spring/button lock stack
- Same 8 × 16 mm shoulder interface
- Unique outer body only
