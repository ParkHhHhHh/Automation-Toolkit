import pandas as pd
from db_handler import connect_to_db, create_table_from_df
from data_validation import validate_data
import argparse
import os


def convert_excel_to_db(input_file, output_file, db_type='sqlite'):
    """
    Convert an Excel file into a SQLite database with validation.

    Args:
        input_file (str): Path to input Excel file.
        output_file (str): Destination database file path.
        db_type (str): Type of database (default: sqlite).
    """

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' does not exist.")

    df = pd.read_excel(input_file)

    if not validate_data(df):
        raise ValueError("Data validation failed. Please check your Excel file.")

    conn = connect_to_db(output_file, db_type)
    create_table_from_df(df, conn)

    print(f"[SUCCESS] Converted '{input_file}' → '{output_file}'")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Excel → SQLite Converter")
    parser.add_argument("--input", required=True, help="Excel file path")
    parser.add_argument("--output", required=True, help="Output database path")
    parser.add_argument("--db-type", default="sqlite", choices=["sqlite"])

    args = parser.parse_args()

    try:
        convert_excel_to_db(args.input, args.output, args.db_type)
    except Exception as e:
        print(f"[ERROR] {e}")
