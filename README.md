# QuietDirTozipFile.py

A simple Python script to create a zip archive from a specified directory.

## Description

`QuietDirTozipFile.py` is a Python 3.11 script that compresses the contents of a specified directory into a `.zip` archive. It takes two arguments:
1. `source_folder`: The path to the folder you want to compress.
2. `zip_file`: The desired output zip file path (with a `.zip` suffix).

This script will silently archive the contents of the folder without any prompts or additional outputs, except for a completion message.

## Requirements

- Python 3.10 or higher
- Standard Python libraries: `shutil`, `os`, `argparse`

## Installation

No installation required. Simply download or clone the repository and run the script using Python 3.11.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `QuietDirTozipFile.py` is located.
3. Run the script using the following command:

   ```bash
   python QuietDirTozipFile.py <source_folder> <zip_file>
   ```

   - `<source_folder>`: The directory path you want to compress.
   - `<zip_file>`: The path where you want the output `.zip` file to be saved (including the `.zip` extension).

### Example

To compress the folder `my_folder` into `my_archive.zip`, run:

```bash
python QuietDirTozipFile.py my_folder my_archive.zip
```

Once the process is complete, you will see the following message:

```
Finish my_folder > my_archive.zip
```
