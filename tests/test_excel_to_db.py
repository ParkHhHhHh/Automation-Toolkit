import unittest
import os
from excel_to_db.converter import convert_excel_to_db


class TestExcelToDB(unittest.TestCase):

    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            convert_excel_to_db("missing.xlsx", "output.db")

    def test_valid_conversion(self):
        # Requires sample.xlsx to exist
        if not os.path.exists("sample.xlsx"):
            return

        convert_excel_to_db("sample.xlsx", "test.db")
        self.assertTrue(os.path.exists("test.db"))
        os.remove("test.db")


if __name__ == "__main__":
    unittest.main()
