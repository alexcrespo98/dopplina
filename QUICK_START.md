# Quick Start Guide - Doppler Flow Analysis

## Current Status: Data Analysis Complete ✓

Your HB100 Doppler sensor data has been analyzed. **Usability: 2/5 (Marginally Usable)**

---

## 📊 What We Found

✓ **Good news:** Hardware works! (Signal-to-noise ratio is 13:1)  
❌ **Bad news:** Signal quality too poor for reliable flow detection

**The problem:** Clean water doesn't reflect microwaves well enough.

---

## 🚀 Next Steps (In Order)

### 1. Quick Test (5 minutes)
Try this RIGHT NOW to see immediate improvement:

```bash
# Add 2 tablespoons milk to 1 gallon of water
# Tilt HB100 sensor to 45° angle
# Increase LM358 gain pot to maximum
# Measure at 3-4 GPM (higher flow)
# Compare signal to previous data
```

**Expected:** Stronger signal, clearer frequency patterns

### 2. Full Improvement (30 minutes)
If quick test works, implement full protocol:

- ✓ Seeded water (milk/cornstarch) in system
- ✓ Sensor at 45° angle, 3 inches from pipe
- ✓ Flow turbulator (mesh screen) installed
- ✓ High-pass filter (0.1µF + 10kΩ) added
- ✓ Collect 5 repetitions per flow rate

### 3. Re-analyze Data
Run the Jupyter notebook on new data:

```bash
pip install -r requirements.txt
jupyter notebook notebooks/doppler_analysis.ipynb
```

The notebook will automatically:
- Extract 19+ features
- Compare ML models
- Show which features work best

---

## 📁 Files You Need

| File | Purpose |
|------|---------|
| `IMPROVED_DATA_COLLECTION_RECOMMENDATIONS.md` | **READ THIS FIRST** - Complete improvement guide |
| `notebooks/doppler_analysis.ipynb` | Analysis notebook (use after re-collecting data) |
| `analysis_results/comprehensive_analysis.png` | Current data visualization (2/5 usability) |
| `requirements.txt` | Python dependencies |

---

## 🎯 Expected Results After Improvements

| Metric | Current | After Seeded Water |
|--------|---------|-------------------|
| Doppler correlation | r=0.41 (weak) | r>0.7 (strong) |
| Signal strength | Baseline | 5-10x stronger |
| ML accuracy | ~40% | 70-85% |
| Frequency range | 6-36 Hz (scattered) | Clear monotonic trend |

---

## ❓ Quick FAQ

**Q: Why isn't my current data usable?**  
A: Clean water is transparent to microwaves. HB100 needs particles to reflect signal back.

**Q: Will milk ruin my system?**  
A: No. Use 1-2 tbsp per gallon (very dilute). Flush with clean water after testing.

**Q: What if seeded water doesn't help?**  
A: Try alternatives: ultrasonic Doppler, pressure sensors, or hybrid approach. See recommendations doc.

**Q: Can I use the notebook now?**  
A: You can run it on current data to see analysis structure, but results won't be useful until you have better data.

---

## 📞 Summary

**Current data:** 2/5 usability indicators - marginally usable  
**Root cause:** Clean water + suboptimal setup  
**Solution:** Seeded water + better positioning = 5-10x improvement  
**Next action:** Run quick test with milk + 45° angle  

**Most important file:** `IMPROVED_DATA_COLLECTION_RECOMMENDATIONS.md`

---

*Analysis performed: 2025-12-12*  
*HB100 Doppler sensor on 3/4" pipe, 12 flow rates (0.01-4.6 GPM)*
