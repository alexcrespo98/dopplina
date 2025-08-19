import subprocess

def prompt_and_run(step_name, script_name):
    response = input(f"Are you ready for {step_name}? (yes/no) ").strip().lower()
    if response != 'yes':
        print("Aborted by user.")
        return False
    print(f"Running {script_name}...")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(f"Error running {script_name}:\n{result.stderr}")
        return False
    return True

def main():
    steps = [
        ("data collection (doppler_test.py)", "doppler_test.py"),
        ("preprocessing (data_preprocess.py)", "data_preprocess.py"),
        ("training (doppler_train.py)", "doppler_train.py"),
        ("guessing (doppler_guess.py)", "doppler_guess.py"),
    ]

    for step_name, script_name in steps:
        if not prompt_and_run(step_name, script_name):
            print("Pipeline stopped.")
            break
    else:
        print("All steps completed successfully.")

if __name__ == "__main__":
    main()
