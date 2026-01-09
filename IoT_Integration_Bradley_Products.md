# IoT Integration in Bradley Products:  Competitor Analysis & Turbine Technology Assessment
**Summary of Research (Tarek) and Path Forward**

## Summary

This document summarizes research conducted on IoT integration for Bradley products, specifically focusing on turbine technology for two critical functionalities: (1) **precise water metering** for accurate volume dispensing, and (2) **hydropower generation** to power IoT sensor systems. The analysis centers on competitive teardowns of smart faucet products and evaluation of GEMS Sensors turbine insert technology, which has emerged as the industry standard for precision flow measurement in smart plumbing fixtures.  These turbine technologies also have broader applications in non-IoT systems that require flow sensing and solenoid control, expanding their potential use across Bradley's product portfolio.

---

## 1. Background & Objectives

Following Bradley's acquisition, the team evaluated competitor smart faucet technologies to identify optimal solutions for IoT-enabled fixtures. The dual objectives are:

1. **Water Metering**: Achieve accurate flow measurement for precise volume dispensing across various applications (kitchen sinks, bathrooms, commercial restrooms)
2. **Hydropower Generation**: Generate sufficient power from water flow to operate: 
   - On/off sensors
   - Solenoids
   - Microcontroller with WiFi connectivity
   - Data transmission systems
   - Potentially the flow metering turbine itself (if not combined)

These turbine technologies are not limited to IoT applications; they can also be integrated into traditional systems requiring flow sensing and solenoid actuation, providing flexibility for both smart and conventional product lines.

---

## 2.  Competitor Analysis:  Smart Faucet Teardown

**Products Evaluated**

Tarek's research focused on two leading smart home faucets: 
- **U by Moen** (voice-controlled smart faucet)
- **Delta Essa VoiceIQ** (Alexa/Google Assistant integrated)

**Key Findings**

*Common Architecture:*
Both premium smart faucets utilized identical core sensing technology: 
- **GEMS-SETRA Model 238600** turbine insert (FT-100 series)
- **Allegro A2110** Hall-effect tachometer on nearby PCB for flow rate measurement

The manufacturers did not purchase the FT-110 complete assembly with housing.  Instead, they integrated the bare FT-100 insert into their own custom-designed housings.  Specifications listed below. 

*Laboratory Testing Results:*
- Tested GEMS insert against 4 Amazon competitor products
- Superior accuracy and repeatability across all competitive alternatives
- Measurable turbine motion detected at **0.1 GPM** (2x lower than advertised 0.2 GPM minimum)

*EFX Integration Testing:*
- Preliminary testing showed **negligible pressure drop** up to 5 GPM
- Compatible with existing product line requirements

---

## 3. Application-Specific Flow Requirements

To properly size turbine technology, operating parameters for target applications were analyzed:

**Kitchen Sink Faucets**
- **Federal Maximum**:  2.2 GPM @ 60 PSI
- **Typical Modern Flow**: 1.5 to 1.8 GPM
- **Pressure Range**: 40 to 80 PSI (typical municipal supply)
- **Special Requirements**: Some states (CA, TX, NY, CO) restrict to 1.8 GPM base with 2.2 GPM temporary boost

**Bathroom/Lavatory Faucets**
- **Federal Maximum**: 2.2 GPM @ 60 PSI
- **WaterSense Certified**: 1.5 GPM or less
- **High-Efficiency Models**: 0.8 to 1.0 GPM
- **Pressure Range**: 40 to 80 PSI

**Commercial Restroom Faucets**
- **Federal Maximum**:  2.2 GPM @ 60 PSI
- **Typical Commercial**: 0.5 to 1.5 GPM (conservation-focused)
- **Sensor/Metered Fixtures**: Often 0.5 to 1.0 GPM
- **Pressure Range**:  40 to 80 PSI

**Conclusion**:  All target applications fall within the 0.5 to 2.2 GPM operational range, well-suited to GEMS FT-series capability.

---

## 4. GEMS Sensors Product Line Analysis

### FT-100 Series:  Turbine Insert (OEM Component)

**Overview**
The FT-100 (<a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft-100-series.pdf?sfvrsn=7562eccc_4">catalog page</a>) is a bare turbine insert designed for OEM integration into custom housings.  This is the component identified in competitor teardowns. 

**Key Specifications:**
- **Flow Range**: 0.2 to 2.0 GPM (0.75 to 7.5 LPM)
- **Accuracy**: ±5% of reading
- **Repeatability**:  ±2% of reading
- **Max Pressure**: 150 PSI
- **Max Temperature**: 160°F (71°C)
- **Bore Diameter**: 0.335"
- **Materials**: Nylon, Polypropylene, or Stainless Steel
- **Certifications**: NSF 61 (drinking water), NSF 18 (food/beverage), WRAS, EU 1935
- **Output**: Hall-effect frequency output (13 to 348 Hz)

**Applications:** Smart faucets, beverage dispensers, agriculture fertilizer dosing, coffee makers, traditional solenoid-controlled fixtures.

**Advantages:**
- Industry-proven in competitive products
- NSF certified for drinking water
- Cost-effective OEM solution during development phase
- Compact; easily integrated into existing designs
- Readily available from multiple distributors

**Sourcing Observation**
Only the FT-100 insert is publicly available as a standalone component from GEMS. However, the product line reveals significant evidence of additional turbine insert variants:
- **FT-110**: **6 different part numbers, each with different flow rate specifications**
- **FT-210**: 1 flow rate option
- **FT-330**: 2 part numbers (226000 and 226100) with distinct flow ranges

The existence of six discrete flow rate options for the FT-110 alone **strongly suggests either multiple turbine insert designs with different rotor geometries, varying flow restriction mechanisms in the housing, or a combination of both**. Given that the FT-110 is described as simply housing the FT-100 insert, the range of options implies that GEMS manufactures a suite of turbine insert variants that are not publicly cataloged.

**Recommendation:  Contact GEMS technical sales to:**
- Clarify whether the six FT-110 flow rate options use different turbine inserts or housing restrictions
- Inquire about accessing the full range of turbine insert options for custom OEM integration

---

### FT-110 Series:  Economical Housed Flow Sensor

**Overview**
The FT-110 (<a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft110-series.pdf?Status=Master&sfvrsn=178e9bc2_10">catalog page</a>) features a turbine insert integrated into a complete housing assembly with threaded ports.  Widely available from distributors at approximately $250 per unit.

**Key Specifications:**
- **Flow Range**: The FT-110 series offers **6 different part numbers with distinct flow rate specifications**, including:
  - Range A: 0.13 to 2.6 GPM (0.5 to 10 LPM) - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft110-series.pdf?Status=Master&sfvrsn=178e9bc2_10">View graph</a>
  - Range B: 0.26 to 9.2 GPM (1 to 35 LPM) - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft110-series.pdf?Status=Master&sfvrsn=178e9bc2_10">View graph</a>
  - [Additional flow rate options between these ranges]
  
  *Note: The variety of flow configurations could indicate different turbine insert designs, different housing flow restrictors, or a combination approach.*

- **Accuracy**: ±3% of reading
- **Repeatability**: 0.5% of full scale
- **Pressure Rating**:
  - Nylon:  200 PSI (burst 1450 PSI)
  - Brass (FT-110M): 350 PSI (burst 2500 PSI)
- **Pressure Drop**: ~7 PSI @ 6 GPM - [View graph](https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft110-series.pdf?Status=Master&sfvrsn=178e9bc2_10)
- **Temperature Range**: -4°F to 212°F (-20°C to 100°C)
- **Ports**: 3/8" NPT or G3/8 male
- **Output**: NPN open collector, frequency output

**Applications:** Kitchen faucets, general flow measurement, solenoid-controlled systems. 

**Advantages:**
- Broader flow range options than bare insert
- Higher pressure tolerance (especially brass version)
- Plug-and-play installation with standard pipe threads

**Considerations:**
- Higher pressure drop than bare insert
- Larger footprint may not fit compact faucet designs

---

### FT-210 Series: Low-Flow Precision Sensor

**Overview**
The FT-210 (<a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft210-series.pdf?Status=Master&sfvrsn=84ffb17_6">catalog page</a>) is designed for ultra-low flow applications requiring high precision.  Estimated cost: **~$318 per unit**.

**Key Specifications:**
- **Flow Range**:  0.026 to 0.65 GPM (0.1 to 2.5 LPM) - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft210-series.pdf?Status=Master&sfvrsn=84ffb17_6">View graph</a>
- **Accuracy**: ±3% of reading
- **Repeatability**: 0.5% of full scale
- **Pressure Rating**:  350 PSI (burst 1400 PSI)
- **Pressure Drop**: ~2 PSI @ 2.5 LPM (~0.66 GPM) - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft210-series.pdf?Status=Master&sfvrsn=84ffb17_6">View graph</a>
- **Temperature Range**: -4°F to 212°F
- **Ports**: 1/4" NPT or G male (smaller than FT-110)
- **Materials**: Nylon 12, Grivory

**Applications:** High-efficiency bathroom faucets, precision dosing, low-flow commercial restroom fixtures.

**Advantages:**
- Lowest pressure drop in GEMS lineup
- Excellent for water conservation applications
- Compact with small port size

**Considerations:**
- Maximum flow (0.65 GPM) below federal kitchen faucet standards (2.2 GPM)
- Best suited for bathroom/commercial applications only

---

### FT-330 Series: Mid-Range Flow Applications

**Overview**
The FT-330 (<a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft330-series.pdf?Status=Master&sfvrsn=c3c253a8_6">catalog page</a>) series bridges the gap between low-flow and high-flow applications with NSF certification.  Estimated cost: **~$180 per unit**.

**Key Specifications:**
- **Flow Range**:
  - **Model 226000 (Range A)**: 0.2 to 2 GPM (0.8 to 7.6 LPM) - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft330-series.pdf?Status=Master&sfvrsn=c3c253a8_6">View graph</a>
  - **Model 226100 (Range B)**: 0.4 to 4 GPM (1.5 to 15 LPM) - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft330-series.pdf?Status=Master&sfvrsn=c3c253a8_6">View graph</a>
  
  *Note: The variety of flow configurations could indicate different turbine insert designs, different housing flow restrictors, or a combination approach.*

- **Accuracy**: ±2% of reading (best in class)
- **Repeatability**: ±0.5% of reading
- **Pressure Rating**:  200 PSI (burst 1000 PSI)
- **Pressure Drop**:
  - ~3 PSI @ 2 GPM
  - ~16 PSI @ 4 GPM (model 226000), lower for model 226100
  - <a href="https://www.gemssensors.com/docs/default-source/resource-files/catalog-pages/catalog-f_ft330-series.pdf?Status=Master&sfvrsn=c3c253a8_6">View graph</a>
- **Temperature Range**: -4°F to 176°F (-20°C to 80°C)
- **Ports**: 3/8" NPT male
- **Materials**: Glass Reinforced PPO (body), PA Composite (turbine), 316 SS (axle), Delrin (bearings)
- **Output**: NPN open collector, frequency output (34 to 343 Hz for 0.2 to 2 GPM, 29 to 343 Hz for 0.4 to 4 GPM)
- **Certifications**: NSF approved materials

**Applications:** Kitchen faucets, mid-range flow measurement, general commercial applications.

**Advantages:**
- Best accuracy in GEMS housed sensor lineup (±2%)
- Multiple flow range options
- NSF approved for drinking water contact
- Covers typical kitchen sink flow rates

**Considerations:**
- Higher pressure drop at upper flow ranges compared to FT-110
- Mid-range pricing between economy (FT-110) and precision (FT-210)

---

## 5. Comparative Analysis: FT-110 vs. FT-210 vs. FT-330

| **Feature** | **FT-110 Series** | **FT-210 Series** | **FT-330 Series** |
|------------|------------------|------------------|-------------------|
| **Flow Range** | 0.13 to 9.2 GPM (6 options) | 0.026 to 0.65 GPM | 0.2 to 4 GPM (2 models) |
| **Accuracy** | ±3% | ±3% | ±2% |
| **Pressure Rating** | 200 to 350 PSI | 350 PSI | 200 PSI |
| **Pressure Drop** | ~7 PSI @ 6 GPM | ~2 PSI @ 0.66 GPM | ~3 PSI @ 2 GPM, ~16 PSI @ 4 GPM |
| **Port Size** | 3/8" NPT | 1/4" NPT | 3/8" NPT |
| **Best Application** | Kitchen/General | Bathroom/Low-flow | Kitchen/Mid-range |
| **Key Advantage** | Widest flow range | Lowest pressure drop | Best accuracy |
| **Estimated Price** | ~$250 | ~$318 | ~$180 |

---

## 6. Hydropower Generation:  Competitive Turbine Analysis

To understand the state of hydropower generation for IoT-enabled plumbing fixtures, competitive products were purchased for laboratory analysis.  These fall into two categories: **IoT-enabled systems** (with app connectivity and smart features) and **non-IoT turbines** (standalone hydropower generators for sensor/solenoid power).

### Products Acquired for Testing

**IoT-Enabled Systems**

**Sloan EFP40A**
- **Type**: All-in-one control box for under-sink installation
- **Flow Rate**: 0.5 GPM (commercial low-flow)
- **Power Source**:  Lithium-ion battery pack with turbine for battery backup
- **Connectivity**:  Bluetooth Low Energy (BLE) via Sloan Connect smartphone app
- **Solenoid Control**: Integrated solenoid valve; can be toggled on/off via app or attached sensor
- **Volume Measurement Method**: **Time-based calculation** (user inputs flow rate; system measures solenoid open/closed time to calculate volume; no direct turbine volume measurement)
- **Key Features**:
  - Fully integrated system (sensor, solenoid, control module, battery in one unit)
  - Comes with compatible faucet
  - Splash-proof, vandal-resistant design
  - App allows remote adjustments, diagnostics, and usage monitoring
- **Limitations**: Flow measurement relies on solenoid timing and user-input flow rate, which is **less sensitive and inaccurate with uneven flow rates**.  This approach works for simple on/off devices (e.g., commercial restroom sensor faucets) but is unsuitable for kitchen sinks requiring precise volume dispensing.

**Non-IoT Hydropower Turbines**

**Zurn P6900-HYD**
- **Type**: Modular, standalone hydropower generator
- **Compatibility**:  Designed for Zurn AquaSense Z6900 series sensor faucets (part of ZG6913-W2 system)
- **Power Source**: Built-in rechargeable lithium-ion battery, continuously charged by water flow through internal turbine
- **Expected Lifespan**: 10 years with minimal maintenance
- **Power Output**: Powers sensor and solenoid for touchless faucet operation
- **Optimal Operating Conditions**: 1.0 to 1.5 GPM aerator, 40 to 80 PSI, ~70 activations/day
- **App Connectivity**: **No app connectivity**.  The P6900-HYD is purely an energy generation module that powers the sensor and solenoid valve system for touchless operation.
- **Key Features**: 
  - Drop-in retrofit for existing Zurn sensor faucets
  - Self-sustaining (no battery replacement needed)
  - Commercial-grade reliability

**TOTO 1000190XX (EcoPower Internal Component)**
- **Type**: Internal hydropower generator from TOTO EcoPower system
- **Advertised Functionality**: Operates continuously when water is flowing; continues to power system for **10 seconds after flow stops** (10s Dynamo version)
- **Power Source**: Water-driven turbine with coil/capacitor system for immediate energy storage
- **System Integration**: Part of a system that powers the sensor and solenoid valve for touchless faucet/flush valve operation
- **App Connectivity**: **No app connectivity**. The EcoPower module is purely a hydropower energy generation component.
- **Key Feature**: Minimal activation requirement (as few as 5 uses/day to maintain charge; optimized for ~10 uses/day)
- **Battery Backup**: Up to 19 years under normal usage
- **Maintenance**: Self-lubricating turbine, self-cleaning debris screen

**TOTO NTQ302ZA1**
- **Type**: Hydropower generator with **dual-coil system**
- **Electrical Configuration**: Requires connection to **two microcontroller ports** (vs. standard two-wire single-coil design of other turbines)
- **System Integration**: Part of a system that powers the sensor and solenoid valve for touchless operation
- **App Connectivity**: **No app connectivity**. 
- **Complexity**: More challenging for testing and integration; requires custom wiring and dual-channel measurement
- **Potential Advantages**: May offer higher power output or redundancy
- **Testing Considerations**: ESP32 test rig configured with special mode to handle dual-coil input

### Testing Methodology

All turbines have been prepared for comprehensive laboratory analysis:

**Test Setup:**
- Turbines connected to custom tubing system for controlled water flow
- **Load circuit**: Two 10kΩ resistors (rated for several watts) placed in series, draining to ground
  - This voltage divider configuration limits maximum voltage to safe levels for microcontroller input
  - The voltage remaining across the resistors corresponds to power generation capacity
  - Different resistor values can be tested to characterize turbine performance under varying loads
- ESP32 microcontroller with custom firmware for data acquisition: 
  - Records voltage output vs. flow rate
  - Measures pressure drop across turbine at various flow rates
  - Generates real-time graphs of power generation performance
  - Special mode for TOTO NTQ302ZA1 dual-coil measurement
- Before each test run, operator inputs flow rate and measures pressure drop
- Data captured and graphed for comparative analysis

**Test Parameters:**
- Flow rate range: 0.5 to 4.0 GPM (covering commercial restroom to kitchen sink applications)
- Pressure range: 40 to 80 PSI (typical municipal supply)
- Voltage output measurement under varying loads (testing different resistor values)
- Pressure drop quantification
- Power generation efficiency calculations

### Analysis Objectives

**System Architecture Study:**
- Understand differences between modular (Zurn) and all-in-one (Sloan) IoT system designs
- Identify components and integration strategies for under-sink IoT systems
- Evaluate power management approaches (battery + hydropower vs. hydropower-only)

**Volume Measurement Critique:**
The Sloan system's reliance on solenoid timing for volume calculation highlights a critical limitation.  This method: 
- Requires user to manually input flow rate
- Assumes constant flow rate (unrealistic in real-world use)
- Becomes **inaccurate with uneven flow rates** caused by: 
  - Fluctuating municipal water pressure
  - Partial valve opening
  - Aerator clogging
  - Simultaneous water use elsewhere in building
- **Adequate for simple on/off devices** (e.g., touchless restroom faucets where precise volume is not critical)
- **Unsuitable for kitchen sink applications** requiring accurate dispensing (e.g., "dispense exactly 8 ounces for recipe")

This reinforces the need for turbine-based flow metering (as identified in Section 2) for true volumetric accuracy.

**Teardown Analysis:**
Following performance testing, all units will be disassembled to: 
- Identify internal turbine components (check for GEMS or other commercial inserts)
- Analyze bearing materials, turbine blade design, and housing construction
- Assess manufacturability and cost-reduction opportunities
- Determine if proprietary designs offer technical innovations

**Power Generation Benchmarking:**
- Establish minimum power requirements for IoT system: 
  - WiFi microcontroller (ESP32 or similar): 100 to 300 mW active, <1 mW sleep
  - Solenoid valve actuation: 5 to 20W peak (varies by model)
  - Flow sensors (Hall-effect): <10 mW
  - Total continuous power budget estimation
- Determine if single turbine can serve dual purpose (metering + power generation) or if separate turbines are required
- Compare power output of commercial turbines

---

## 7. Conclusion and Next Steps

This analysis has established a comprehensive foundation for Bradley's IoT integration strategy.  Tarek's competitive teardown successfully identified the GEMS FT-100 turbine insert as the industry standard for precise flow metering in smart faucets, with laboratory testing confirming performance that exceeds manufacturer specifications.  The product exhibits measurable operation down to 0.1 GPM and negligible pressure drop across the target application range of 0.5 to 2.2 GPM.

The GEMS product line analysis reveals multiple housed sensor options (FT-110, FT-210, FT-330) with varying accuracy, pressure ratings, and flow ranges. The existence of six different FT-110 configurations and multiple FT-330 models suggests a broader portfolio of turbine insert variants exists beyond the publicly available FT-100, warranting direct engagement with GEMS technical sales.

For hydropower generation, competitive products from Sloan, Zurn, and TOTO have been procured and prepared for testing. The laboratory setup with load resistors and ESP32 data acquisition will enable comprehensive characterization of power output, pressure drop, and efficiency across realistic operating conditions. 

**Immediate Next Steps:**

1. **Execute Hydropower Turbine Testing**:  Complete laboratory measurements of all four turbine systems (Sloan EFP40A, Zurn P6900-HYD, TOTO 1000190XX, TOTO NTQ302ZA1) across the full flow rate and pressure range.  Generate comparative power output and pressure drop data.

2. **Conduct Teardown Analysis**: Disassemble all tested units to identify internal components, turbine design approaches, and potential use of GEMS or other commercial inserts. 

3. **Engage GEMS Technical Sales**: Request information on the full range of turbine insert variants, clarify differences between FT-110 part numbers, and discuss custom OEM integration options and pricing for development quantities.

4. **Define System Architecture**: Based on power generation test results, determine whether a single dual-purpose turbine or separate metering and generation turbines are required.  Establish power budget and battery backup requirements for target applications (kitchen, bathroom, commercial restroom).

5. **Develop Integration Roadmap**: With turbine performance data and GEMS product information in hand, map flow metering and power generation solutions to specific Bradley product lines, identifying opportunities for both IoT-enabled and traditional solenoid-controlled fixtures.

The combination of proven GEMS flow metering technology and competitive hydropower analysis positions Bradley to make informed design decisions for both precise volume dispensing and self-sustaining sensor/solenoid systems across residential and commercial applications.
