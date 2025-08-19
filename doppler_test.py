import serial
import time
import csv
import os

# ----- Configuration -----
SERIAL_PORT = "COM8"
BAUD_RATE = 115200

# Directories for storing CSV files
DATA_DIR = "data_collection"
FLOW_ON_DIR = os.path.join(DATA_DIR, "1")
FLOW_OFF_DIR = os.path.join(DATA_DIR, "0")

# Ensure directories exist
os.makedirs(FLOW_ON_DIR, exist_ok=True)
os.makedirs(FLOW_OFF_DIR, exist_ok=True)

def record_data(ser, duration_sec):
    """
    Records data from the serial port for duration_sec seconds.
    Each data point is timestamped (in ms) relative to start.
    Returns a list of tuples: (timestamp_ms, value)
    """
    data = []
    start_time = time.time()
    while (time.time() - start_time) < duration_sec:
        try:
            # Read a line from serial, decode it and strip whitespace
            line = ser.readline().decode('utf-8').strip()
            if line:
                try:
                    value = int(line)
                except ValueError:
                    # If the value can't be converted to int, skip it
                    continue
                timestamp_ms = int((time.time() - start_time) * 1000)
                data.append((timestamp_ms, value))
        except serial.SerialException as e:
            print("Serial exception:", e)
            break
    return data

def write_csv(filename, data):
    """
    Writes the provided data (list of (timestamp_ms, value)) to a CSV file.
    """
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["timestamp_ms", "value"])
        writer.writerows(data)
    print(f"Data saved to {filename}")

def main():
    # Ask for number of tests and duration per test
    num_tests = int(input("How many test cycles would you like to run? "))
    test_duration = float(input("How many seconds per test? "))

    # Attempt to open the serial port
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        # Give some time to establish the connection
        time.sleep(2)
    except serial.SerialException as e:
        print("Could not open serial port:", e)
        return

    # Loop for each test cycle
    for test_num in range(1, num_tests + 1):
        # FLOW ON test
        input_msg = f"Ready for FLOW ON test {test_num}/{num_tests}? (type 'yes' to start) "
        if input(input_msg).strip().lower() != "yes":
            print("Test aborted by user.")
            break

        print(f"Collecting FLOW ON data for {test_duration} seconds...")
        data_flow_on = record_data(ser, test_duration)
        filename_on = os.path.join(FLOW_ON_DIR, f"flow_on_test{test_num}.csv")
        write_csv(filename_on, data_flow_on)

        # FLOW OFF test
        input_msg = f"Ready for FLOW OFF test {test_num}/{num_tests}? (type 'yes' to start) "
        if input(input_msg).strip().lower() != "yes":
            print("Test aborted by user.")
            break

        print(f"Collecting FLOW OFF data for {test_duration} seconds...")
        data_flow_off = record_data(ser, test_duration)
        filename_off = os.path.join(FLOW_OFF_DIR, f"flow_off_test{test_num}.csv")
        write_csv(filename_off, data_flow_off)

    ser.close()
    print("Data collection complete.")

if __name__ == "__main__":
    main()
