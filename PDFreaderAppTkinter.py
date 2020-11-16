import pyttsx3
import PyPDF2
from tkinter.filedialog import *
import tkinter.messagebox

book =askopenfilename()
pdfreader = PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages
tkinter.messagebox.showinfo("Adithya's pdf reader", "Please listen to your pdf BOOK or DOCUMENT BY CLICKING OK")

for num in range(0,pages):
    page=pdfreader.getPage(num)
    text=page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()
