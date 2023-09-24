# MetaLens Detective (Image Metadata Extraction Tool)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)

**Author**: Tushar Santosh Patil

**Email**: tushar.patil.5202@gmail.com

&ensp;&ensp;&ensp;&ensp;The MetaLens Detective (Image Metadata Extraction Tool) is a user-friendly Python script designed to extract metadata from various image formats, including .jpg, .jpeg, .png, .gif, .bmp, and more. This tool automates the extraction of Exif data, GPS coordinates, and generates an HTML report, making it useful for analyzing image properties.

## Features

- **Metadata Extraction**: Automatically extracts image metadata, including Exif data, camera information, and more.
- **GPS Coordinates**: Retrieves GPS coordinates if available in the image metadata.
- **Reverse Geocoding**: Performs reverse geocoding to translate GPS coordinates into human-readable location information.
- **HTML Report Generation**: Generates an HTML report summarizing the extracted metadata and location details.
- **Wide Image Format Support**: Supports a variety of image formats, making it versatile for different types of images.

## Dependencies

- [exifread](https://pypi.org/project/ExifRead): A Python library for reading Exif metadata from image files.
- [argparse](https://docs.python.org/3/library/argparse.html): A Python library for parsing command-line arguments.
- [geopy](https://pypi.org/project/geopy): A Python library for geocoding and reverse geocoding.
- [Pillow](https://pillow.readthedocs.io/en/stable/): A Python Imaging Library (PIL) fork for opening, manipulating, and saving various image file formats.


## Prerequisites

Before using the Image Metadata Extraction Tool, ensure that your system meets the following prerequisites:

- **Python**: The tool requires Python to be installed on your system. You can download and install Python from the [official Python website](https://www.python.org/downloads/).

- **Python Libraries**: Install the necessary Python libraries using `pip`. Open your terminal and run the following command to install the required libraries:

  ```shell
  pip install exifread argparse geopy Pillow

This command will install the following libraries:

- `exifread`: For processing Exif metadata.
- `argparse`: For parsing command-line arguments.
- `geopy`: For geocoding and reverse geocoding.
- `Pillow`: For working with various image formats.

Once you have Python and the required libraries installed, you can proceed to use the Image Metadata Extraction Tool.

## Installation

Follow these steps to install and use the Image Metadata Extraction Tool:

1. **Download the Script**: Download the script by either directly downloading it from the repository or by cloning the entire repository to your local machine.

2. **Run the Script**: Open your terminal and navigate to the directory where you downloaded the script or where you cloned the repository.

3. **Execute the Script**: Run the script by entering the following command, replacing `path_to_image.jpg` with the actual file path of the image you want to analyze:

   ```shell
   python image_metadata_tool.py path_to_image.jpg

## Usage

- **Execute the Script**: Run the script with the path to the image file as an argument to extract metadata.

- **Review Output**: The script will display extracted metadata, GPS coordinates (if available), and generate an HTML report.


## License

MetaLens Detective is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the script in accordance with the terms of this license.

## Disclaimer

Please note that the MetaLens Detective script is provided as-is, without any warranty or guarantee. Use it at your own risk. Always review the code and understand the actions it performs before running it on your system.

## Documentation

For detailed information on how to use and customize the script, refer to the [Wiki](https://github.com/your-repo/wiki).


