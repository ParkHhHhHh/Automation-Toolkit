import os

def analyze_log(file_path: str):
    error_count = 0
    warning_count = 0

    with open(file_path, "r") as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            if "WARNING" in line:
                warning_count += 1

    return error_count, warning_count

if __name__ == "__main__":
    path = "sample.log"
    if os.path.exists(path):
        errors, warnings = analyze_log(path)
        print(f"ERROR: {errors}, WARNING: {warnings}")
    else:
        print("No log file found.")
