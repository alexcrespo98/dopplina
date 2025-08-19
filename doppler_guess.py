import serial
import time
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal import get_window
import joblib
import pandas as pd
import os

# --- Configuration ---
SERIAL_PORT = "COM8"
BAUD_RATE = 115200
DURATION_SEC = 10
SAMPLE_RATE_HZ = 100
MODEL_PATH = "doppler_classifier.pkl"
RESULTS_CSV = "doppler_guess_results.csv"

def collect_data():
    print(f"Collecting data for {DURATION_SEC} seconds...")
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
    except serial.SerialException as e:
        print(f"bro... Could not open serial port: {e}")
        return np.array([])

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
    if values.size == 0:
        print("bro... No data collected to extract features from.")
        return None, None, None

    values = values - np.mean(values)
    windowed = values * get_window("hamming", len(values))

    N = len(windowed)
    T = 1.0 / SAMPLE_RATE_HZ
    fft_result = np.abs(fft(windowed))[:N//2]
    fft_freq = fftfreq(N, T)[:N//2]

    peak_idx = np.argmax(fft_result)
    peak_freq = fft_freq[peak_idx]
    avg_amp = np.mean(fft_result)
    std_amp = np.std(fft_result)

    return peak_freq, avg_amp, std_amp

def label_guess(guess):
    # Try to convert to float if possible
    try:
        g = float(guess)
    except (ValueError, TypeError):
        return f"Unknown ({guess})"

    if g == 0:
        return "FLOW OFF"
    elif 0 < g < 1:
        percent = int(round(g * 100))
        return f"FLOW {percent}%"
    elif g >= 1:
        return f"{g} GPM"
    else:
        return f"Unknown ({guess})"

def main():
    # Ask if results should be saved
    save_results = input("Do you want me to save the results? (y/n): ").strip().lower() == "y"
    trial_number = 1
    results = []

    # Load model
    if not os.path.exists(MODEL_PATH):
        print(f"bro... I'm expecting the model file at {MODEL_PATH}, but I don't see it.")
        return

    try:
        clf = joblib.load(MODEL_PATH)
    except Exception as e:
        print(f"bro... Failed to load model: {e}")
        return

    while True:
        raw_values = collect_data()
        if raw_values.size == 0:
            print("bro... No data to process. Exiting.")
            return

        peak_freq, avg_amp, std_amp = extract_features(raw_values)
        if peak_freq is None:
            print("bro... Could not extract features. Exiting.")
            return

        print(f"Extracted features: peak_freq={peak_freq:.3f}, avg_amp={avg_amp:.3f}, std_amp={std_amp:.3f}")

        features_df = pd.DataFrame([{
            'peak_freq': peak_freq,
            'avg_amp': avg_amp,
            'std_amp': std_amp
        }])

        try:
            prediction = clf.predict(features_df)[0]
            label = label_guess(prediction)
            print(f"Prediction: {label}")
            if save_results:
                results.append({'trial_number': trial_number, 'guess': label})
                trial_number += 1
        except Exception as e:
            print(f"bro... Prediction failed: {e}")

        if save_results:
            cont = input("Run another trial? (y/n): ").strip().lower()
            if cont != "y":
                # Save results
                pd.DataFrame(results).to_csv(RESULTS_CSV, index=False)
                print(f"Results saved to {RESULTS_CSV}")
                break
        else:
            break

if __name__ == "__main__":
    main()