# HB100 Doppler Data Analysis - Improved Collection Recommendations

**Current Status:** Dataset analyzed with 12 flow rates (0.01 to 4.6 GPM)  
**Usability:** 2/5 indicators passed - **MARGINALLY USABLE**  
**Recommendation:** Re-collect data with improvements listed below

---

## Analysis Summary

After analyzing the complete dataset through multiple approaches, here's what we found:

### ❌ What's NOT Working

1. **No Amplitude Correlation** (r = -0.34, p = 0.28)
   - Mean amplitude doesn't correlate with flow rate
   - Standard deviation doesn't correlate with flow rate
   - Signal range doesn't correlate with flow rate
   - **Problem:** The sensor output amplitude is essentially random with respect to flow

2. **Weak Doppler Shift** (r = 0.41, p = 0.19)
   - Peak frequencies vary (6 Hz to 36 Hz) but not systematically with flow
   - No clear linear or monotonic relationship
   - **Problem:** The Doppler effect is not being captured consistently

3. **Poor Spectral Features** (r = 0.15)
   - Spectral centroids don't correlate with flow rate
   - All flow rates show similar frequency content distribution
   - **Problem:** Spectral shape doesn't encode flow information

### ✓ What IS Working

1. **Signal Separability** (48.5% overlap)
   - Signal ranges do vary between different flow rates
   - About half of the flow rate pairs have non-overlapping ranges
   - This shows the sensor IS detecting something

2. **Signal-to-Noise Ratio** (F-ratio = 13.1)
   - Between-group variance is 13x larger than within-group variance
   - Signal is definitely present and detectable above noise
   - **Good news:** The hardware is working, just not optimally

---

## Root Cause Analysis

### Why Is The HB100 Not Working Well?

The HB100 Doppler radar detects movement via the Doppler effect. For water flow in a pipe:

**Expected Behavior:**
- Water molecules moving = Doppler frequency shift
- Higher flow = Higher Doppler frequency
- Turbulence = More variance/noise in signal

**What We're Seeing:**
- Frequencies vary but don't correlate with flow rate
- Some flow rates (0.54 GPM) have very different signals
- No systematic pattern

**Likely Problems:**

1. **Clean Water Issue**
   - Water is transparent to microwaves
   - HB100 can't "see" pure water very well
   - No particles = minimal reflection = weak signal
   
2. **Laminar Flow**
   - In small tubes at low flow, water flows smoothly (laminar)
   - No turbulent eddies or movement variations
   - Doppler sensor has nothing dynamic to detect
   
3. **Sensor Positioning**
   - Beam might not be hitting the water column optimally
   - Could be detecting pipe vibrations instead of flow
   - Reflection geometry might be poor

4. **Signal Swamping**
   - One dominant reflection (pipe wall, static water) drowns out flow signal
   - DC component is very large, flow component is tiny
   - Need better signal conditioning

---

## Recommendations for Improved Data Collection

### 🔥 CRITICAL CHANGES (Do These First)

#### 1. **Use Dirty/Seeded Water**

**Why:** The HB100 needs particles to reflect the microwave signal back.

**Options:**
- Add **milk** (1-2 tablespoons per gallon) - scatters microwaves well
- Add **cornstarch** (1 tablespoon per gallon) - safe, disperses well
- Use **dirty water** with sediment, particles, or turbidity
- Add **tiny polystyrene beads** (0.5-2mm) - good scatterers
- Use **soapy water** - creates micro-bubbles that scatter

**Don't use:**
- Salt water (conducts, doesn't scatter as well)
- Metal particles (dangerous, conductive)

**Safety & Cleanup Notes:**
- Use food-safe additives only (milk, cornstarch) for potable water systems
- Flush system thoroughly after testing to prevent biological growth
- Polystyrene beads may clog fine filters - use with caution
- Dispose of test water appropriately (milk/cornstarch solutions can be poured down drain)

#### 2. **Increase Turbulence**

**Why:** Turbulent flow creates moving eddies that produce stronger Doppler signatures.

**How:**
- Install a **flow restrictor** or **orifice** in the pipe
- Add a **mesh screen** or **perforated plate** downstream of sensor
- Use **rough pipe interior** (textured, not smooth)
- Position sensor **after a bend** or **T-junction**
- Increase flow rates to exceed laminar threshold (Reynolds > 2300 for 3/4" pipe at ~2 GPM)

#### 3. **Optimize Sensor Position**

**Why:** Beam geometry affects signal quality dramatically.

**Best Practices:**
- Mount at **45-60° angle** to pipe axis (not perpendicular)
- Point sensor **along flow direction** (detects axial velocity)
- Keep sensor **2-4 inches** from pipe (optimal for HB100)
- Use **radar-transparent** pipe section (PVC ok, not metal)
- Ensure **no air gaps** between sensor and pipe

#### 4. **Improve Signal Conditioning**

**Why:** Current signal might have too much DC, not enough gain, or wrong filtering.

**Circuit Improvements:**
- Increase **AC gain** (try 100x instead of 10x)
- Add **high-pass filter** (cut DC below 0.5 Hz)
- Add **bandpass filter** (0.5-50 Hz optimal for flow)
- Reduce **baseline/offset** adjustment (let software handle DC)
- Add **adjustable gain** pot (tune per flow rate)

---

### 📊 DATA COLLECTION PROTOCOL

#### Test Setup
1. Use seeded water (milk or cornstarch)
2. Position sensor at 45° angle, 3 inches from pipe
3. Add flow turbulator downstream of sensor
4. Adjust circuit for maximum sensitivity without saturation
5. Let flow stabilize for 30 seconds before recording

#### Per Flow Rate
1. Set flow rate and wait for stabilization (30-60 sec)
2. Record **5 repetitions** of 5000 samples each
3. Between repetitions, stop flow, then restart
4. Verify no clipping or saturation (values should vary, not stuck at limits)
5. Save each repetition separately with metadata

#### Flow Rate Selection
- Test at least **10 flow rates** evenly spaced
- Include **zero flow** (baseline)
- Test **both directions** if possible (forward/reverse)
- Go high enough to ensure turbulence (>2 GPM for 3/4" pipe)

---

### 🔬 ALTERNATIVE SENSOR APPROACHES

If HB100 still doesn't work well after improvements:

#### Option 1: Different Doppler Sensor
- **Ultrasonic Doppler** - better for water (Speed Sensor DG10)
- **Laser Doppler velocimetry** - very accurate but expensive
- **Radar with lower frequency** (2.4 GHz better than 10.5 GHz for water)

#### Option 2: Different Sensing Principle
- **Differential pressure** sensor across orifice (very reliable)
- **Turbine flow meter** - mechanical but accurate
- **Thermal mass flow sensor** - no moving parts
- **Magnetic flow meter** - good for conductive fluids

#### Option 3: Hybrid Approach
- Use **HB100 for presence detection** (flow/no flow)
- Use **pressure sensor for rate estimation**
- Combine both signals with ML model

---

### 🎯 SPECIFIC EXPERIMENTS TO TRY

#### Experiment 1: Particle Density Test
- Test with 0%, 0.5%, 1%, 2% milk concentration
- See which gives strongest Doppler signal
- Measure SNR at each concentration

#### Experiment 2: Angle Sweep
- Test sensor at 0°, 30°, 45°, 60°, 90° to pipe
- Record signal strength and frequency content
- Find optimal angle

#### Experiment 3: Turbulator Test
- Compare signal with/without mesh screen in pipe
- Measure frequency spread (should increase with turbulence)
- Check if correlation improves

#### Experiment 4: Frequency Band Analysis
- Split signal into frequency bands (0-10 Hz, 10-20 Hz, 20-30 Hz, etc.)
- Check which band has best correlation with flow
- Design narrowband filter for that range

---

## Expected Improvements

### With Seeded Water
- **Signal strength:** 5-10x improvement
- **Doppler correlation:** Should see r > 0.7
- **Frequency range:** Clearer separation between flow rates

### With Turbulence Enhancement
- **Signal variance:** 3-5x increase
- **Feature richness:** More dynamic range in spectrum
- **ML accuracy:** Estimated 70-85% (up from ~40%)

### With Optimal Positioning
- **SNR:** 10-20 dB improvement
- **Consistency:** Less variation between measurements
- **Stability:** More repeatable readings

---

## Testing Checklist

Before collecting new data, verify:

- [ ] Water has visible particles/turbidity
- [ ] Sensor angle is 45° to pipe, pointing with flow
- [ ] Circuit gain is adjusted for max range without clipping
- [ ] Flow turbulator installed (mesh/orifice)
- [ ] Zero flow measurement recorded first
- [ ] Flow meter or reference measurement available
- [ ] Multiple repetitions planned (5+ per flow rate)
- [ ] Sampling rate is adequate (100+ Hz)
- [ ] Recording length is sufficient (30+ seconds per measurement)
- [ ] Data validation script ready (check for NaN, clipping, etc.)

---

## Quick Wins to Try Right Now

If you want to test improvements immediately without major changes:

1. **Add milk to water** - 2 tablespoons per gallon, run test at one flow rate
2. **Tilt the sensor** - Try 45° angle instead of perpendicular
3. **Increase LM358 gain** - Turn gain pot to maximum
4. **Add high-pass filter** - 0.1µF capacitor in series with 10kΩ resistor (fc = 159 Hz cutoff)
5. **Measure at higher flow** - Try 3-4 GPM instead of lower values

---

## Success Criteria for New Data

You'll know the improved setup is working when:

✓ **Doppler shift correlation > 0.7** (frequency increases with flow)  
✓ **Signal amplitude varies by >20%** between flow rates  
✓ **Within-measurement std dev < between-measurement differences**  
✓ **Frequency spectra are clearly different** for different flows  
✓ **ML model achieves >75% accuracy** on holdout test set  

---

## Conclusion

The current data shows the HB100 hardware is functional but the signal quality is too poor for reliable flow rate detection. The sensor can distinguish between some flow rates (2/5 indicators passed) but not systematically.

**Key insight:** The variance BETWEEN flow rates (13x) is larger than variance WITHIN each flow rate, which means a signal exists. It's just buried under poor collection conditions.

**Most impactful change:** Add particles to the water. This single change will likely improve results more than anything else.

**Next steps:**
1. Run "Quick Wins" tests to validate improvements
2. If successful, implement full protocol with seeded water
3. Re-run the analysis notebook on new data
4. Iterate on sensor positioning and signal conditioning

---

*Analysis performed on doppler_data_20251031_122655.csv*  
*See comprehensive_analysis.png for visualizations*  
*Usability score: 2/5 - Marginally usable with current setup*
