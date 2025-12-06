def generate_report(errors, output_file):
    """Write extracted errors into a readable report."""

    with open(output_file, "w") as f:
        f.write("=== Log Error Report ===\n\n")
        for err in errors:
            f.write(err + "\n")

    print(f"[SUCCESS] Log report saved → {output_file}")
