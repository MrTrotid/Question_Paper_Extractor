# A-Level Question Paper Downloader

This program allows users to download A-Level question papers for various subjects. The user can select a subject, choose a year, and then download the question papers for that year. The downloaded papers are saved in their respective folders.

## Source

Papers are downloaded from [BestExamHelp](https://bestexamhelp.com/), which provides Cambridge International A-Level past papers. Please note that the availability and accessibility of papers depend on the website's content and policies.

Some subjects listed may not work with the current source website, but the source code is simple and can be modified to work with different websites or paper sources as needed.

## Features

- Select a subject from a list of A-Level subjects.
- Choose a year and season (June or November) for the selected subject.
- Download question papers in PDF format.
- Save the downloaded papers in the format `Papers/{subject_name}-{subject_code}/{year}`.
- Currently supports papers from 2021-2024 (both Summer and Winter papers). 2025 Summer option is shown but papers are not yet available.

## Requirements

- Python 3.x (with tkinter, which is included by default)
- `requests` library

## Installation

1. Clone the repository or download the source code.
2. Install the required libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.