#!/usr/bin/python
#!/usr/bin/python3

# -*- coding: utf8 -*-
# date                 :- 
# author               :- Md Jabed Ali(jabed)


import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from comtypes import client
import time
import sys
import subprocess
import subprocess
from ctypes import cdll, Structure, c_int, c_void_p, POINTER, byref
import win32com.client as clientwin
try:
    from comtypes import client
except ImportError:
    client = None
#import win32api
#import win32console
#pip install pywin32
#pip install -U pyinstaller # to exe

# tkinter view
def view():
    level_1 = Label(root, text= "Document Location (docx/doc) : ",
                    font=('Helvetica', 12, 'bold'),
                    bg='aquamarine')
    level_1.grid(row=1, column=1, padx=6, pady=20)
    root.entry = Entry(root, width=35, textvariable=source)
    root.entry.grid(row=1, column=2, padx=6, pady=20)

    level_2 = Label(root, text= "Save To : ",
                    font=('Helvetica', 12, 'bold'),
                    bg='aquamarine')
    level_2.grid(row=2, column=1, padx=6, pady=20)
    root.save = Entry(root, width=35, textvariable=destination)
    root.save.grid(row=2, column=2, padx=6, pady=20)    

    browse = Button(root, text='Browse', command=browsefolder, width=10)
    browse.grid(row=1, column=3, padx=6, pady=20)

    save = Button(root, text='Browse', command=savefolder, width=10) 
    save.grid(row=2, column=3, padx=6, pady=20)

    convertvideo = Button(root, text="Convert Document", command=convert_docx, width=35)
    convertvideo.grid(row=3, column=1, columnspan=3, padx=6, pady=6)

# browse docx file
def browsefolder():
    file = filedialog.askopenfilename(initialdir=r"C:\Users\paradox\Desktop\webapp\videotomp3",
                                      filetypes = (("DOCX (*.docx)", "*.docx"),
                                                   ("DOC (*.doc)", "*.docx"),
                                                   ("All Files", "*.*")
                                                   ))
    root.entry.insert(0, file)

# save pdf file
def savefolder():
    saveaudio = filedialog.asksaveasfilename(initialdir=r"C:\Users\paradox\Desktop\webapp\videotomp3",
                                      filetypes = (("PDF (*.pdf)", "*.pdf"),
                                                   ("All Files", "*.*")
                                                   ))
    root.save.insert(0, saveaudio)

def doc2pdf(doc):
    doc = os.path.abspath(doc)
    if client is None:
        return doc2pdf_linux(doc)
    name, ext = os.path.splitext(doc)
    try:
        word = client.CreateObject('Word.Application')
        worddoc = word.Documents.Open(doc)
        worddoc.SaveAs(name + '.pdf', FileFormat=17)
    except Exception:
        raise
    finally:
        worddoc.Close()
        word.Quit()

# convert docx
def convert_docx():
    mainfile = source.get()
    savefile = destination.get()
    word = clientwin.DispatchEx("Word.Application")
    #word = client.CreateObject("Word.Application")
    new_name = mainfile.replace(".docx", r".pdf")
    worddoc = word.Documents.Open(mainfile)
    worddoc.SaveAs(savefile + '.pdf', FileFormat = 17)
    worddoc.Close()
    word.Quit()

    messagebox.showinfo("Done", "Converted Successfully")


root = tkinter.Tk()
root.title("DOC to PDF Converter. Md Jabed Ali")
root.config(bg="DarkOliveGreen3")
root.geometry("600x200")
source = StringVar()
destination = StringVar()

if __name__ == "__main__":
    view()
    root.mainloop()
                                                                                     
    
