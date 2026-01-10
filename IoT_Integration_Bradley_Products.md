# IoT Integration in Bradley Products:  Competitor Analysis & Turbine Technology Assessment
**Summary of Research (Tarek) and Path Forward**

## Summary

This document summarizes IoT integration research for Bradley products, focusing on turbine technology for (1) **precise water metering** for volume dispensing, and (2) **hydropower generation** to power IoT sensors. Competitive teardown analysis identified GEMS Sensors turbine technology as the industry standard for flow measurement in smart faucets. These technologies apply to both IoT-enabled and traditional solenoid-controlled fixtures across Bradley's product portfolio.

---

## Work Completed: Competitor Analysis & Flow Metering

**Smart Faucet Teardown** - Tarek analyzed U by Moen and Delta Essa VoiceIQ smart faucets, revealing:
- Both use identical **GEMS-SETRA Model 238600** turbine insert ([FT-100 series](https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft-100-series.pdf?sfvrsn=7562eccc_4))
- **Allegro A2110** Hall-effect sensor for flow rate measurement
- Manufacturers integrate bare turbine insert into custom housings (not complete FT-110 assembly)

**Laboratory Testing Results:**
- GEMS insert outperformed 4 Amazon competitor products in accuracy and repeatability
- Turbine operates at **0.1 GPM** (2x better than 0.2 GPM spec)
- **Negligible pressure drop** up to 5 GPM - compatible with Bradley product requirements

**Application Requirements:** All target applications (kitchen, bathroom, commercial) fall within 0.5 to 2.2 GPM operational range, well-suited to GEMS FT-series capability.

---

## GEMS Sensors Product Line: Key Options

### Comparative Analysis

| **Feature** | **[FT-110](https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft110-series.pdf?Status=Master&sfvrsn=178e9bc2_10)** | **[FT-210](https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft210-series.pdf?Status=Master&sfvrsn=84ffb17_6)** | **[FT-330](https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft330-series.pdf?Status=Master&sfvrsn=c3c253a8_6)** |
|------------|------------------|------------------|-------------------|
| **Flow Range** | 0.13 to 9.2 GPM (6 options) | 0.026 to 0.65 GPM | 0.2 to 4 GPM (2 models) |
| **Accuracy** | ±3% | ±3% | ±2% (best in class) |
| **Pressure Rating** | 200 to 350 PSI | 350 PSI | 200 PSI |
| **Pressure Drop** | ~7 PSI @ 6 GPM | ~2 PSI @ 0.66 GPM (lowest) | ~3 PSI @ 2 GPM |
| **Port Size** | 3/8" NPT | 1/4" NPT | 3/8" NPT |
| **Best Application** | Kitchen/General | Bathroom/Low-flow | Kitchen/Mid-range |
| **Estimated Price** | ~$250 | ~$318 | ~$180 |
| **Key Advantage** | Widest flow range | Lowest pressure drop | Best accuracy, NSF certified |

**Critical Sourcing Issue:** Only the FT-100 bare insert is publicly available from GEMS. However, the existence of 6 different FT-110 configurations and 2 FT-330 models strongly indicates additional turbine insert variants exist beyond the publicly cataloged FT-100. **Re-contact GEMS technical sales to inquire about the full range of available turbine inserts**, as these unlisted variants may better suit specific Bradley applications.

---

## Work in Progress: Hydropower Generation Analysis

**Products Acquired for Testing** (currently on desk ready for laboratory testing):

**IoT-Enabled System:**
- **Sloan EFP40A**: All-in-one control box with BLE connectivity, lithium-ion battery + turbine backup. *Limitation:* Uses time-based volume calculation (inaccurate with variable flow) - unsuitable for precise kitchen dispensing.

**Hydropower Turbines:**
- **Zurn P6900-HYD**: Modular hydropower generator, 10-year lifespan, self-sustaining (no battery replacement)
- **TOTO 1000190XX**: EcoPower generator with 10-second post-flow operation, 19-year battery backup
- **TOTO NTQ302ZA1**: Dual-coil system for potentially higher power output

**Test Setup Prepared:**
- Custom tubing with controlled water flow (0.5 to 4.0 GPM range, 40 to 80 PSI)
- ESP32 microcontroller with load resistor circuit for voltage/power measurement
- Special configuration for dual-coil TOTO testing

---

## Next Steps (Near Term)

1. **Execute Hydropower Turbine Testing**: Complete laboratory measurements of all four turbine systems across full flow rate and pressure range. Generate comparative power output and pressure drop data.

2. **Conduct Teardown Analysis**: Disassemble tested units to identify internal components, bearing materials, turbine blade design. Assess manufacturability and check for GEMS inserts.

3. **Re-engage GEMS Technical Sales** (HIGH PRIORITY): 
   - **Request catalog of all available turbine inserts beyond the FT-100** - evidence suggests multiple unlisted variants exist
   - Clarify whether the 6 FT-110 part number variations use different turbine inserts or just housing flow restrictors
   - Inquire about accessing bare inserts for FT-210 and FT-330 series for custom integration
   - Discuss OEM pricing and minimum order quantities for development phase

4. **Define System Architecture**: Based on power generation results, determine if single dual-purpose turbine or separate metering and generation turbines are required. Establish power budget for WiFi microcontroller, solenoid, and sensors.

5. **Develop Integration Roadmap**: Map flow metering and power generation solutions to specific Bradley product lines (kitchen, bathroom, commercial) for both IoT and traditional fixtures.

---

## Conclusion

Competitive analysis confirms **GEMS turbine technology as the industry standard** - the FT-100 insert is used by both Moen and Delta in their premium smart faucets, with laboratory testing confirming operation down to 0.1 GPM and negligible pressure drop. **The immediate priority is re-contacting GEMS technical sales to identify what additional turbine insert variants are available beyond the publicly listed FT-100**, as the product line evidence strongly suggests a broader portfolio exists. With hydropower turbines ready for testing and GEMS as the proven flow metering solution, Bradley can finalize system architecture decisions and move forward with integration across residential and commercial product lines.
