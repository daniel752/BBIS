# BBIS Hide and Extract

BBIS Hide and Extract is a Python PoC (Proof-of-Concept) project designed to hide and extract data within executables using the Binary-Based Instruction Substitution (BBIS) technique. This project includes two scripts: `bbis_hide.py` for hiding data within executables and `bbis_extract.py` for extracting hidden data from executables.

## Features

- Hiding data within executables using BBIS technique
- Extraction of hidden data from executables using BBIS technique
- Support for opcode mappings for data manipulation
- Conversion of data to binary representation for hiding
- Conversion of binary data back to the original file format for extraction
- Command-line interface for easy usage

## Prerequisites

- Python 3.x
- `magic` library for file type detection
- `argparse` library for command-line argument parsing

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/daniel752/BBIS.git

2. Navigate to project repository:
   
   ```shell
   cd BBIS

3. Install the required dependencies:
   
   ```shell
   pip install -r requirements.txt

## Usage
### Hiding Data within Executables
To hide data within an executable file, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   
   ```shell
   python bbis_hide.py -e /path/to/executable -d /path/to/data
   
Replace /path/to/executable with the actual path to the executable file you want to hide data in, and /path/to/data with the path to the data file you want to hide.
The script will modify the provided executable file to embed the data within it and save the modified executable as the output file.

### Extracting Hidden Data from Executables
To extract hidden data from an executable file, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   
   ```shell
   python bbis_extract.py -e /path/to/executable -o /path/to/output
   
Replace `/path/to/executable` with the actual path to the executable file you want to extract data from, and `/path/to/output` to your output location or name in case you want (it's optional).

The extracted file will be saved as `output-file.{file_type}` in the current directory if output is not specified, where `{file_type}` represents the detected file type of the extracted data.

## Contributing
Contributions to BBIS Hide and Extract are welcome! If you encounter any issues or have suggestions for improvements, please feel free to submit a pull request or create an issue on the repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
BBIS Hide and Extract is based on the BBIS technique and utilizes opcode mappings for data manipulation. Special thanks to the contributors of the `magic` and `argparse` libraries.

## Disclaimer
BBIS Hide and Extract is a Proof-of-Concept (PoC) system and should be used responsibly and in accordance with applicable laws. The authors of this project are not responsible for any misuse or illegal activities involving this software.
