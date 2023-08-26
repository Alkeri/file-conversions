import argparse
import pandas as pd
from typing import Dict, Union


class Converter:
    def __init__(self) -> None:
        """
        Converter class for handling format conversions.
        """
        self.read_formats = {
            "csv": self.read_csv,
            "json": self.read_json,
            "tsv": self.read_tsv,
            # Add more format reading functions here
        }

        self.write_formats = {
            "csv": self.write_csv,
            "json": self.write_json
            # Add more format writing functions here
        }

    def read_csv(self, input_path: str) -> pd.DataFrame:
        """
        Read data from a CSV file using pandas.

        Args:
            input_path (str): Path to the input CSV file.

        Returns:
            pd.DataFrame: Loaded data as a pandas DataFrame.
        """
        return pd.read_csv(input_path)

    def read_json(self, input_path: str) -> pd.DataFrame:
        """
        Read data from a JSON file using pandas.

        Args:
            input_path (str): Path to the input JSON file.

        Returns:
            pd.DataFrame: Loaded data as a pandas DataFrame.
        """
        return pd.read_json(input_path)

    def read_tsv(self, input_path: str) -> pd.DataFrame:
        """
        Read data from a TSV file using pandas.

        Args:
            input_path (str): Path to the input TSV file.

        Returns:
            pd.DataFrame: Loaded data as a pandas DataFrame.
        """
        return pd.read_csv(input_path, sep='t')

    def write_csv(self, data: pd.DataFrame, output_path: str) -> None:
        """
        Write data to a CSV file using pandas.

        Args:
            data (pd.DataFrame): Data to be written as a pandas DataFrame.
            output_path (str): Path to the output CSV file.
        """
        data.to_csv(output_path, index=False)

    def write_json(self, data: pd.DataFrame, output_path: str) -> None:
        """
        Write data to a JSON file using pandas.

        Args:
            data (pd.DataFrame): Data to be written as a pandas DataFrame.
            output_path (str): Path to the output JSON file.
        """
        data.to_json(output_path, orient="records", indent=4)

    def convert(self, input_path: str, output_path: str) -> None:
        """
        Convert data from one format to another.

        Args:
            input_path (str): Path to the input file.
            output_path (str): Path to the output file.
        """
        input_extension = input_path.split(".")[-1]
        output_extension = output_path.split(".")[-1]

        if input_extension == output_extension:
            print("Input and output formats are the same.")
            return

        if input_extension not in self.read_formats:
            print(f"Unsupported input format: {input_extension}")
            return

        if output_extension not in self.write_formats:
            print(f"Unsupported output format: {output_extension}")
            return

        data = self.read_formats[input_extension](input_path)
        self.write_formats[output_extension](data, output_path)
        print(f"Conversion from {input_extension} to {output_extension} successful.")


def main() -> None:
    """
    Main function for the format conversion CLI tool.
    """
    parser = argparse.ArgumentParser(
        description="Convert between CSV and JSON formats."
    )
    parser.add_argument("input", help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    args = parser.parse_args()

    converter = Converter()
    converter.convert(args.input, args.output)


if __name__ == "__main__":
    main()
