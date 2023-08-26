# File Format Conversion CLI Tool

This is a command-line tool for converting between CSV and JSON file formats using Python and pandas.

## Installation

1. Clone or download this repository.

2. Install the required dependencies (pandas) using the following command:

```bash
pip install -r requirements.txt
```

## Usage

Run the CLI tool using the following command:

```bash
python file-conversions.py input_file --output output_file
```

Replace `input_file` with the path to the input file and `output_file` with the desired path for the output file. The tool will automatically infer the formats based on the file extensions and perform the conversion.

### Examples

1. Convert CSV to JSON:

```bash
python file-conversions.py data.csv --output data.json
```

2. Convert JSON to CSV:

```bash
python file-conversions.py data.json --output data.csv
```

## Supported Formats

Currently, the tool supports conversion between CSV and JSON formats. You can easily extend it to support additional formats by adding new methods to the `Converter` class in the `file-conversions.py` script.

## Contributing

Feel free to contribute to this project by adding new features, improving existing code, or suggesting enhancements. Fork this repository, make your changes, and submit a pull request.

Thanks for reading 
