import fitz  # PyMuPDF
import glob
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import nltk
import json
#from gemini import pqrst
import os
import google.generativeai as genai
import time

nltk.download('stopwords')
nltk.download('punkt')
api_key = os.getenv('GENERATIVE_AI_KEY')
if api_key is None:
    os.environ['GENERATIVE_AI_KEY'] = input("Enter gen-ai api key:")
genai.configure(api_key=api_key)
    
def pqrst(string,file_name="my_markdown_file.md"):
    actions=["I would like to create a mind map using the Xmind tool. Can you provide me with some text in Markdown format that is compatible with Xmind? Please include a Central Topic with Main Topics, and any additional information goes to Subtopics that will help create an effective mind map","Preview","questions and answers","deep important concepts","summary of key points","Generate flashcards for the main concepts in the text"]
    atext=["Mind map","Preview","questions and answers","deep important concepts","summary of key points","Flashcards"]
    for action,text in zip(actions,atext):
        prompt_parts = [
        f"I am a cyber security student and trainee engineer; from {string} ; {action} in markdown format",
        ]
        print(action)
        response=genai.chat(model="models/chat-bison-001",messages=prompt_parts,temperature=0.5)
        #response = model.generateChat(prompt_parts)
        print(response.last)
        with open(file_name, 'a',encoding='utf-8') as file:
            # Write the response to the file
            #if actions.index(action)==0:
                #action="Mind map"
            #if actions.index(action)==5:
                #action="Flashcards"
            file.write(f"```python\n\n '{text}'\n\n```\n\n")
            file.write(f'{response.last} \n\n')
        time.sleep(5)
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

# Get all PDF files in the folder
pdf_files = sorted(glob.glob("*.pdf"))

# Separate the PDF files mentioned in the JSON file and the others
mentioned_files = [file_name for file_name in pdf_files if file_name in page_info]
other_files = [file_name for file_name in pdf_files if file_name not in page_info]
print(f"Mentioned PDF files: {mentioned_files}")

# Extract concepts from the PDFs mentioned in the JSON file
for file_name in mentioned_files:
    global continue_processing
    page_number = page_info.get(file_name, 0)
    print(f"\nConcepts from {page_number} of {file_name}:")
    concepts = extract_concepts(file_name, page_number)
    text=''
    for concept in concepts:
        #print("- " + concept)
        text=text+concept+"\n"

    pqrst(text,f"{file_name[:-4]}_Page{page_number}.md")

    # Increment the page number for the next run
    page_info[file_name] = page_number + 1

    # Write the incremented page numbers and file names back to the .json file
    with open('page_numbers.json', 'w') as f:
        json.dump(page_info, f)

    # Ask the user if they want to continue
    continue_processing = input("\nDo you want to proceed to the next document? (yes/no): ")
    if continue_processing.lower() != 'yes':
        break

if continue_processing.lower() != 'yes':
    exit()

# Extract concepts from the other PDFs
if other_files!=[]:
    for file_name in other_files :
        print(f"\nConcepts from {file_name}:")
        concepts = extract_concepts(file_name)
        #text=''
        #for concept in concepts:
            #print("- " + concept)
            #text = text + concept + "\n"

        #pqrst(text, f"{file_name[:-4]}_Page1.md")
        print("File is not mentioned in the json file..")
        print("Edit the json file with the name of the pdf and page number")
        print("Unless, the next time the concepts would be parsed from the first page itself!")
        print("Setting page number to 1...")
        # Add the file name and page number to the JSON file
        page_info[file_name] = 1

        # Write the incremented page numbers and file names back to the .json file
        with open('page_numbers.json', 'w') as f:
            json.dump(page_info, f)

        # Ask the user if they want to continue
        continue_processing = input("\nDo you want to proceed to the next document? (yes/no): ")
        if continue_processing.lower() != 'yes':
            break
