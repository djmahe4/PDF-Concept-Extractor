---

# PDF Concept Extractor

This Python script extracts concepts from PDF files using Natural Language Processing (NLP) techniques. It processes PDF files mentioned in a JSON file first along with the page number ( which can be edited manually) and then proceeds to other PDFs in the directory.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Algorithm](#algorithm)
- [License](#license)

## Installation

Install by running the code:
```
git clone https://github.com/djmahe4/study-csec/
```

Before running the script, make sure you have the following Python libraries installed:

- PyMuPDF (fitz)
- nltk
- glob
- json

You can install them using pip:

```bash
pip install PyMuPDF nltk glob2
```

## Usage

To run the script, simply execute it with Python:

```bash
python script.py
```

The script will ask you if you want to continue after processing each file. If you enter 'yes', it will proceed to the next file. If you enter anything else, it will stop processing files and update the 'page_numbers.json' file with the incremented page numbers.

## Algorithm

```
Start
 |
 |--> Read the page numbers and file names from the .json file
 |
 |--> Get all PDF files in the folder
 |
 |--> Extract concepts from the PDFs mentioned in the JSON file
 |     |
 |     |--> For each file:
 |           |
 |           |--> Extract concepts
 |           |
 |           |--> Print concepts
 |           |
 |           |--> Ask the user if they want to continue
 |           |
 |           |--> Increment the page number for the next run
 |
 |--> Extract concepts from the other PDFs
 |     |
 |     |--> For each file:
 |           |
 |           |--> Extract concepts
 |           |
 |           |--> Print concepts
 |           |
 |           |--> Ask the user if they want to continue
 |           |
 |           |--> Add the file name and page number to the JSON file
 |
 |--> Write the incremented page numbers and file names back to the .json file
 |
Stop
```

## License

This project is licensed under the MIT License.

---
