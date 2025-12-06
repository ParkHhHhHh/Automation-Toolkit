import pandas as pd
import argparse


def generate_csv_report(input_file, output_file):
    """Generate summary statistics from a CSV dataset."""

    df = pd.read_csv(input_file)
    summary = df.describe()

    with open(output_file, "w") as f:
        f.write("=== CSV Summary Report ===\n\n")
        f.write(str(summary))

    print(f"[SUCCESS] CSV report saved → {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CSV Report Generator")
    parser.add_argument("--input", required=True, help="CSV file path")
    parser.add_argument("--output", required=True, help="Report output path")
    args = parser.parse_args()

    generate_csv_report(args.input, args.output)
