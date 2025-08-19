import serial
import time
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import get_window
import joblib
import pandas as pd

# --- Configuration ---
SERIAL_PORT = "COM8"
BAUD_RATE = 115200
DURATION_SEC = 10
SAMPLE_RATE_HZ = 100  # expected sampling rate
MODEL_PATH = "doppler_classifier.pkl"

def collect_data():
    print(f"Collecting data for {DURATION_SEC} seconds...")
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    time.sleep(2)  # allow connection to settle

    data = []
    start_time = time.time()

    while (time.time() - start_time) < DURATION_SEC:
        line = ser.readline().decode('utf-8').strip()
        if line:
            try:
                value = int(line)
                data.append(value)
            except ValueError:
                continue

    ser.close()
    print(f"Collected {len(data)} samples.")
    return np.array(data)

def extract_features(values):
    # Mean subtraction
    values = values - np.mean(values)

    # Apply Hamming window
    windowed = values * get_window("hamming", len(values))

    # FFT
    N = len(windowed)
    T = 1.0 / SAMPLE_RATE_HZ
    fft_result = np.abs(fft(windowed))[:N//2]
    fft_freq = fftfreq(N, T)[:N//2]

    # Features
    peak_idx = np.argmax(fft_result)
    peak_freq = fft_freq[peak_idx]
    avg_amp = np.mean(fft_result)
    std_amp = np.std(fft_result)

    return peak_freq, avg_amp, std_amp

def main():
    # Load the model
    clf = joblib.load(MODEL_PATH)

    # Collect data
    raw_values = collect_data()

    # Extract features
    peak_freq, avg_amp, std_amp = extract_features(raw_values)
    print(f"Extracted features: peak_freq={peak_freq:.3f}, avg_amp={avg_amp:.3f}, std_amp={std_amp:.3f}")

    # Package as DataFrame with correct column names
    features_df = pd.DataFrame([{
        'peak_freq': peak_freq,
        'avg_amp': avg_amp,
        'std_amp': std_amp
    }])

    # Predict
    prediction = clf.predict(features_df)[0]
    state = "FLOW ON" if prediction == 1 else "FLOW OFF"
    print(f"Prediction: {state}")

if __name__ == "__main__":
    main()
