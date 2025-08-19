import os
import numpy as np
import pandas as pd
from scipy.fft import fft, fftfreq
from scipy.signal import get_window
import matplotlib.pyplot as plt

# Paths
base_dir = os.path.dirname(__file__)
data_dir = os.path.join(base_dir, "data_collection")
out_dir = os.path.join(base_dir, "preprocessed_data")
os.makedirs(os.path.join(out_dir, "0_pp"), exist_ok=True)
os.makedirs(os.path.join(out_dir, "1_pp"), exist_ok=True)

def preprocess_file(filepath, label, output_dir):
    try:
        df = pd.read_csv(filepath)

        # Force numeric conversion (coerce invalid entries to NaN)
        df['timestamp_ms'] = pd.to_numeric(df['timestamp_ms'], errors='coerce')
        df['value'] = pd.to_numeric(df['value'], errors='coerce')

        # Drop rows with NaN
        df = df.dropna()

        timestamps = df['timestamp_ms'].values
        values = df['value'].values

        # Normalize to zero mean
        values = values - np.mean(values)

        # Apply Hamming window
        windowed = values * get_window("hamming", len(values))

        # Perform FFT
        N = len(windowed)
        T = 1.0 / 100.0  # Sampling interval (100 Hz)
        fft_result = np.abs(fft(windowed))
        fft_freq = fftfreq(N, T)[:N // 2]
        fft_amp = fft_result[:N // 2]

        # Save FFT magnitude
        filename = os.path.basename(filepath).replace(".csv", "_fft.csv")
        out_path = os.path.join(output_dir, filename)
        pd.DataFrame({
            "frequency": fft_freq,
            "magnitude": fft_amp
        }).to_csv(out_path, index=False)

        # Extract features (simple for now)
        peak_freq = fft_freq[np.argmax(fft_amp)]
        avg_amp = np.mean(fft_amp)
        std_amp = np.std(fft_amp)

        return {
            "file": os.path.basename(filepath),
            "label": label,
            "peak_freq": peak_freq,
            "avg_amp": avg_amp,
            "std_amp": std_amp
        }

    except Exception as e:
        print(f"Failed to process {os.path.basename(filepath)}: {e}")
        return None

def main():
    all_features = []

    for label_str in ["0", "1"]:
        label = int(label_str)
        folder = os.path.join(data_dir, label_str)
        output_subdir = os.path.join(out_dir, f"{label_str}_pp")

        for file in os.listdir(folder):
            if file.endswith(".csv"):
                path = os.path.join(folder, file)
                features = preprocess_file(path, label, output_subdir)
                if features:
                    all_features.append(features)

    # Save feature summary for ML
    if all_features:
        features_df = pd.DataFrame(all_features)
        features_df.to_csv(os.path.join(out_dir, "doppler_features.csv"), index=False)
        print("✅ Preprocessing complete. Features saved to 'preprocessed_data/doppler_features.csv'.")
    else:
        print("⚠️ No valid data processed.")

if __name__ == "__main__":
    main()
