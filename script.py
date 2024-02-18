import fitz  # PyMuPDF
import os
import glob
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
import random
import nltk

nltk.download('stopwords')
nltk.download('punkt')
import re
import json


def extract_concepts(file_name, page_number=0):
    # Open the PDF file
    doc = fitz.open(file_name)

    # Check if the page number is within the range of the document's pages
    if page_number < len(doc):
        page = doc.load_page(page_number)

        text = page.get_text()

        # Tokenize the text into sentences
        sentences = sent_tokenize(text)

        # Tokenize the text into words
        tokens = word_tokenize(text)

        # Remove stopwords and non-alphabetic tokens
        tokens = [token for token in tokens if token.isalpha() and token not in stopwords.words('english')]

        # Get unique tokens
        unique_tokens = set(tokens)

        # Extract sentences that contain the unique tokens
        concept_sentences = [sentence for sentence in sentences if any(token in sentence for token in unique_tokens)]

        return concept_sentences
    else:
        return []


# Read the page numbers and file names from the .json file
with open('page_numbers.json', 'r') as f:
    page_info = json.load(f)

# Get all PDF files in the 'notes' folder
pdf_files = sorted(glob.glob("notes/*.pdf"))

# Separate the PDF files mentioned in the JSON file and the others
mentioned_files = [file_name for file_name in pdf_files if file_name in page_info]
other_files = [file_name for file_name in pdf_files if file_name not in page_info]
print(f"Mentioned PDF files: {mentioned_files}")

# Extract concepts from the PDFs mentioned in the JSON file
for file_name in mentioned_files:
    global continue_processing
    page_number = page_info.get(file_name, 0)
    print(f"\nConcepts from {file_name}:")
    concepts = extract_concepts(file_name, page_number)
    for concept in concepts:
        print("- " + concept)

    # Ask the user if they want to continue
    continue_processing = input("\nDo you want to proceed to the next document? (yes/no): ")
    if continue_processing.lower() != 'yes':
        break

    # Increment the page number for the next run
    page_info[file_name] = page_number + 1

if continue_processing.lower() != 'yes':
    exit()

# Extract concepts from the other PDFs
if other_files!=[]:
    for file_name in other_files :
        print(f"\nConcepts from {file_name}:")
        concepts = extract_concepts(file_name)
        for concept in concepts:
            print("- " + concept)

        # Ask the user if they want to continue
        continue_processing = input("\nDo you want to proceed to the next document? (yes/no): ")
        if continue_processing.lower() != 'yes':
            break

        # Add the file name and page number to the JSON file
        page_info[file_name] = 1

# Write the incremented page numbers and file names back to the .json file
with open('page_numbers.json', 'w') as f:
    json.dump(page_info, f)
