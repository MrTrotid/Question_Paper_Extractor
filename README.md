# A-Level Question Paper Downloader

This program allows users to download A-Level question papers for various subjects. The user can select a subject, choose a year, and then download the question papers for that year. The downloaded papers are saved in their respective folders.

## Source

Papers are downloaded from [BestExamHelp](https://bestexamhelp.com/), which provides Cambridge International A-Level past papers. Please note that the availability and accessibility of papers depend on the website's content and policies.

Some subjects listed may not work with the current source website, but the source code is simple and can be modified to work with different websites or paper sources as needed.

## Features

- Select a subject from a list of A-Level subjects.
- Choose a year and season (June or November) for the selected subject.
- Filter papers by type (Paper 1, Paper 2, Paper 3, or Paper 4)
- Download individual question papers in PDF format
- Download all papers of a specific type in one click
- Modern dark-themed user interface with custom styling
- Save the downloaded papers in the format `Papers/{subject_name}-{subject_code}/{year}`.
- Currently supports papers from 2021-2024 (both Summer and Winter papers). 2025 Summer option is shown but papers are not yet available.

## Requirements

- Python 3.x (with tkinter, which is included by default)
- `requests` library
- `customtkinter` library for modern UI
- `pillow` library for image handling

## Installation

1. Clone the repository or download the source code.
2. Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the program using `python test.py`
2. Select a subject from the grid of available subjects
3. Choose a year and season (June/November)
4. Use the paper filter to show specific paper types or view all papers
5. Download individual papers or use "Download All Papers" for bulk download
6. Papers are automatically saved in their respective folders

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.