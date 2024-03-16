---

# PDF Concept Extractor

This Python script extracts concepts from PDF files using Natural Language Processing (NLP) techniques. It processes PDF files mentioned in a JSON file first and then proceeds to other PDFs in the directory.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Suggested Books](#suggested-books)
- [Algorithm](#algorithm)
- [License](#license)

## Installation

You can install the code by running:

```bash
git clone https://github.com/djmahe4/PDF-Concept-Extractor
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
If you want the help of generative-ai in learning concepts use the command, only after getting the api key from - https://ai.google.dev/
```bash
python new.py
```
## 
## Note!: Replace the items within 'page_numbers.json' file with original pdf filename and page number

The script will ask you if you want to continue after processing each file. If you enter 'yes', it will proceed to the next file. If you enter anything else, it will stop processing files and update the 'page_numbers.json' file with the incremented page numbers.

Please save your PDF files within the same directory as the Python script. You can update the page numbers of the PDFs by editing the 'page_numbers.json' file. This file should be a JSON object with filenames as keys and page numbers as values.

## Suggested Books

The script works with any PDF files, but here are a few suggested books that you can use to test the script:

- "Data Communications and Networking By Behrouz A.Forouzan.pdf"
- "The web application hacker's handbook_ finding and exploiting security flaws-Wiley (2011).pdf"

Please note that you need to download these books and save them in the same folder for the script to work.

## Algorithm

```
Start
 |
 |--> Read the page numbers and file names from the .json file
 |
 |--> Get all PDF files in the main folder
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
