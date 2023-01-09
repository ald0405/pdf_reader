# importing the modules
import PyPDF2
import pyttsx3
  
# path of the PDF file
path = open('/-/-/-/.pdf', 'rb')
  
# creating a PdfFileReader object
pdfReader = PyPDF2.PdfReader(path)
  
# this will read the 1st page.
from_page = pdfReader.pages[0]
  
# Text extraction 
text = from_page.extract_text()
  
# Initiation and reading 
speak = pyttsx3.init()
speak.say(text)
# Stop the reader 
speak.stop()
speak.runAndWait()
