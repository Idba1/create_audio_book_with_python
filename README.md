# Audio Book Reader with Python

This project converts the text from a PDF file into speech using Python. It reads the PDF, extracts the text from a specific page, and uses the `pyttsx3` library to convert the text into audible speech.

## Requirements

Before running the script, ensure you have the following Python libraries installed:

- **pyttsx3**: A text-to-speech library for Python.
- **PyPDF2**: A library for reading and extracting text from PDF files.

You can install these libraries using `pip`:

```bash
pip install pyttsx3 PyPDF2
```

## Setup

1. **Clone this repository** (or download the files):

   ```bash
   https://github.com/Idba1/create_audio_book_with_python.git
   ```

2. **Add your PDF file**: Place the PDF file (e.g., `DMS.pdf`) in the project directory.

## How It Works

1. The script opens a PDF file (`DMS.pdf` in this case).
2. It uses the `PyPDF2` library to read the PDF and extract text from a specific page (default is the 4th page, i.e., index 3).
3. It then uses the `pyttsx3` library to convert the extracted text into speech and reads it aloud.

## Running the Script

To run the script, execute the following command in the terminal:

```bash
python audio_book.py
```

Make sure the PDF file (`DMS.pdf`) is located in the same directory as the script or update the script to point to the correct path.

## Example Output

If the 4th page of the PDF contains text, you should hear the text being read aloud by the `pyttsx3` engine.

## Notes

- You can modify the script to extract text from different pages by changing the `pdfReader.pages[3]` index to the page you want.
- The text extraction depends on the PDF content. If the PDF contains images or scanned text (like an image of text), `PyPDF2` might not extract it properly.
