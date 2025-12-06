import re
import argparse


def parse_log(input_file):
    """Extract ERROR lines and return them as a list."""

    errors = []

    with open(input_file, "r", encoding="utf8", errors="ignore") as f:
        for line in f:
            if "ERROR" in line:
                errors.append(line.strip())

    return errors


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument("--input", required=True, help="Log file path")
    parser.add_argument("--output", required=True, help="Report output path")
    args = parser.parse_args()

    from report_generator import generate_report

    errors = parse_log(args.input)
    generate_report(errors, args.output)
