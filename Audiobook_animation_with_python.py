import pyttsx3
import PyPDF2
book = open('oop.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
page = pdfReader.getPage(4)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()


# install the package "pyttsx3" (python text to speech version 3) and the package "PyPDF2" by the command,,,
# -pip install pyttsx3
# -pip install PyPDF2
# make sure that the book is pdf that you want to use here
# write the above code and run this code
# now open that pdf incase you want to check that this code is working properly or not
# enjoy as the pdf is read by your friend
