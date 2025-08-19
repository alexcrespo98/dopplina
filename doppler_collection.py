import serial
import time
import csv
import os

# ----- Configuration -----
SERIAL_PORT = "COM8"
BAUD_RATE = 115200
DATA_DIR = "data_collection"

def get_float_input(prompt, default):
    user = input(f"{prompt} [{default}]: ")
    return float(user) if user.strip() else float(default)

def get_int_input(prompt, default):
    user = input(f"{prompt} [{default}]: ")
    return int(user) if user.strip() else int(default)

def record_data(ser, duration_sec):
    data = []
    start_time = time.time()
    while (time.time() - start_time) < duration_sec:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    value = int(line)
                except ValueError:
                    continue
                timestamp_ms = int((time.time() - start_time) * 1000)
                data.append((timestamp_ms, value))
        except serial.SerialException as e:
            print("Serial exception:", e)
            break
    return data

def write_csv(filename, data):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp_ms", "value"])
        writer.writerows(data)
    print(f"Data saved to {filename}")

def main():
    print("=== Doppler Collection Protocol ===")
    num_splits = get_int_input("How many speed splits? (e.g. 4 for 0, .25, .5, .75, 1)", 4)
    num_samples = get_int_input("How many samples per speed?", 10)
    sample_duration = get_float_input("How many seconds per sample?", 10)

    # Calculate speed categories
    speeds = [round(i/num_splits, 3) for i in range(num_splits+1)]
    speed_labels = [str(s) for s in speeds]

    # Create directories for each speed
    for label in speed_labels:
        os.makedirs(os.path.join(DATA_DIR, label), exist_ok=True)

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
    except serial.SerialException as e:
        print("Could not open serial port:", e)
        return

    for label in speed_labels:
        print(f"\n=== Starting collection for {float(label)*100:.0f}% flow rate ===")
        speed_dir = os.path.join(DATA_DIR, label)
        for sample_num in range(1, num_samples + 1):
            input(f"Ready to take {sample_duration} seconds at {float(label)*100:.0f}% flow, sample {sample_num}/{num_samples}. Press Enter to start.")
            print(f"Recording for {sample_duration} seconds...")
            data = record_data(ser, sample_duration)
            filename = os.path.join(speed_dir, f"flow_{label}_sample{sample_num}.csv")
            write_csv(filename, data)
            print("Data collected! Please turn water off then on for next sample.")

    ser.close()
    print("All data collection complete.")

if __name__ == "__main__":
    main()