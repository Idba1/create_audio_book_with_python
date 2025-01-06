import pyttsx3
import PyPDF2

# Initialize pyttsx3 for text-to-speech. Character name Cara.
Cara = pyttsx3.init()

try:
    book = open("DMS.pdf", "rb")
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
except FileNotFoundError:
    print("The PDF file was not found.")
    exit()

for num in range(3, pages):
    # Access the 4th page (index 3)
    page = pdfReader.pages[num]
    # Extract text from the page
    text = page.extract_text()

    # Check if the page contains any text
    if text:
        Cara.say(text)
        Cara.runAndWait()
    else:
        print(f"No text found on page {num + 1}.")
