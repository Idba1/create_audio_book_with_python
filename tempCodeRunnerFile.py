import pyttsx3
import pyPDF2
book=open('DATABASE MANAGEMENT SYSTEMS.pdf','rb')
pdfReader=pyPDF2.pdfFileReader(book)
pages=pdfReader.numberPages
print(pages)
Cara = pyttsx3.init()
Cara.say('Cara is very confused about 2nd week interview quiz')
Cara.runAndWait()