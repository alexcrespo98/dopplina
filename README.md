# Dopplina (stop dopp and flow)

**Dopplina** is a project for collecting, processing, and analyzing data from an HB100 Doppler radar sensor. The HB100's analog output is conditioned by an LM358 op amp and two potentiometers, allowing you to tune baseline and gain for optimal sensor resolution. The system features a microcontroller with an OLED display for live waveform visualization, helping you adjust the pots for best results. The processed signal is posted to the TX pin, ready for serial data logging (e.g., with DataBuddy).

## Hardware Overview

- **Sensor:** HB100 Doppler radar module
- **Amplification:** Op-amp (LM358)
- **Potentiometers:**
  - **Left:** Baseline adjustment
  - **Right:** Signal amplification
- **Microcontroller:** Reads analog signal, displays the waveform on OLED, posts values to TX (serial)
- **OLED Display:** Provides real-time visualization so you can maximize signal resolution by tuning both pots

## Usage

### 1. Adjusting & Tuning

- Power up the system; the microcontroller runs `doppler_test.ino`, reading analog values from the HB100/LM358 circuit.
- The OLED display shows the live waveform. Tune the left pot for baseline (offset), and the right pot for amplification (gain), aiming for the clearest signal range without clipping.

### 2. Data Logging

- The microcontroller sends processed analog values out the TX pin (serial, 115200 baud).
- Use DataBuddy or the included Python scripts (e.g., `doppler_collection.py`, `doppler_test.py`) to record serial data into CSV files, organized by flow rate.

### 3. Preprocessing

- Run `data_preprocess.py` to normalize, window, and extract frequency features (FFT) from collected CSV data.

### 4. Model Training

- Use `doppler_train.py` to train a classifier (RandomForest) based on extracted features.
- The trained model is saved as `doppler_classifier.pkl`.

### 5. Flow Rate Guessing

- Use `doppler_guess.py` to collect new data, preprocess it, and infer flow rate using the trained model.

### 6. Pipeline Automation

- Use `doppler_king.py` for a step-by-step interactive pipeline through all stages.

### 7. Data Analysis

- Use Jupyter notebooks in `notebooks/` directory for comprehensive analysis:
  - `doppler_analysis.ipynb`: Analyze Doppler data with signal processing and ML techniques
  - See `notebooks/README.md` for setup instructions

## Scripts Overview

| Script/Notebook              | Purpose                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| doppler_test.ino             | Microcontroller code: displays signal for tuning, outputs to serial     |
| doppler_collection.py        | Collects labeled speed samples, saves as CSV                            |
| doppler_test.py              | Interactive test cycles for flow on/off, saves CSV                      |
| data_preprocess.py           | Processes CSV data, extracts features, saves FFT results                |
| doppler_train.py             | Trains ML model from features                                           |
| doppler_guess.py             | Uses model to predict flow on new data                                  |
| doppler_king.py              | Interactive pipeline for all steps                                      |
| notebooks/doppler_analysis.ipynb | Comprehensive Doppler data analysis with signal processing and ML   |

## How It Works

1. **Signal Acquisition:**  
   HB100 radar detects movement (e.g., water flow). The analog signal is amplified by the LM358; baseline and gain are tuned live using the pots, visualized on the OLED.

2. **Data Logging:**  
   The microcontroller posts the tuned analog value to the TX pin, which can be read by DataBuddy or the Python scripts.

3. **Data Processing:**  
   Scripts read the serial port, timestamp the data, and save it in folders organized by flow rate for each sample.

4. **Feature Extraction:**  
   Preprocessing applies a Hamming window and FFT, extracting frequency/amplitude features.

5. **Training & Inference:**  
   A classifier is trained to recognize flow states; later, new data is classified in real time.

## Requirements

- Microcontroller (tested on ESP32, others may work)
- HB100 Doppler radar module
- LM358 (or similar) op amp for signal conditioning
- Potentiometers for baseline/gain
- OLED display (for signal visualization with `doppler_test.ino`)
- Python 3.x
- Packages: `numpy`, `pandas`, `scipy`, `scikit-learn`, `joblib`, `matplotlib`, `pyserial`

## Wiring Diagram

(Schematic not provided—describe:  
- HB100 OUT → op amp IN  
- Op amp OUT → microcontroller analog IN  
- Pots adjust op amp baseline/gain  
- OLED connected via I2C/SPI to microcontroller  
- Microcontroller TX → USB → PC (for DataBuddy or Python scripts))

## File Tree

- `doppler_test.ino` (Arduino/ESP32 code)
- `doppler_collection.py`
- `doppler_test.py`
- `data_preprocess.py`
- `doppler_train.py`
- `doppler_guess.py`
- `doppler_king.py`
- `notebooks/` (Jupyter notebooks for analysis)
  - `doppler_analysis.ipynb` (comprehensive analysis)
  - `README.md` (notebook documentation)
- `data_collection/` (CSV files)
- `preprocessed_data/` (FFT/features)
- `doppler_classifier.pkl` (trained model)
- `requirements.txt` (Python dependencies)

## Notes

- Tune baseline/gain pots with help of OLED display for best results.
- If you change pin numbers, serial port, or hardware, update the config in the scripts.
- For full details and updates, see [dopplina repo](https://github.com/alexcrespo98/dopplina).

