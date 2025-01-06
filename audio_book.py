import pyttsx3
import PyPDF2

book = open("DMS.pdf", "rb")
pdfReader = PyPDF2.PdfReader(book)

pages = len(pdfReader.pages)
# print(pages)
# Access the 4th page (index 3)
page = pdfReader.pages[3]
# Extract text from the page
text = page.extract_text()

# Check if the page contains any text
if text:
    # Initialize pyttsx3 for text-to-speech. Character name Cara.
    Cara = pyttsx3.init()
    Cara.say(text)
    Cara.runAndWait()
else:
    print("No text found on the page.")
