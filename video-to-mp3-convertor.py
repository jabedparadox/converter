#!/usr/bin/python
#!/usr/bin/python3

# -*- coding: utf8 -*-
# date                 :- 
# author               :- Md Jabed Ali(jabed)


import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import moviepy
import moviepy.editor as convrt
#pip install -U pyinstaller

# tkinter view
def view():
    level_1 = Label(root, text= "Video Location : ",
                    font=('Helvetica', 12, 'bold'),
                    bg='aquamarine')
    level_1.grid(row=1, column=1, padx=6, pady=20)
    root.entry = Entry(root, width=35, textvariable=source)
    root.entry.grid(row=1, column=2, padx=6, pady=20)

    level_2 = Label(root, text= "Audio Location : ",
                    font=('Helvetica', 12, 'bold'),
                    bg='aquamarine')
    level_2.grid(row=2, column=1, padx=6, pady=20)
    root.save = Entry(root, width=35, textvariable=destination)
    root.save.grid(row=2, column=2, padx=6, pady=20)    

    browse = Button(root, text='Browse', command=browsefolder, width=10)
    browse.grid(row=1, column=3, padx=6, pady=20)

    save = Button(root, text='Browse', command=savefolder, width=10) 
    save.grid(row=2, column=3, padx=6, pady=20)

    convertvideo = Button(root, text="Convert Video", command=convert_video, width=35)
    convertvideo.grid(row=3, column=1, columnspan=3, padx=6, pady=6)

# browse video file
def browsefolder():
    file = filedialog.askopenfilename(initialdir=r"C:\Users\paradox\Desktop\webapp\videotomp3",
                                      filetypes = (("AVI (*.avi)", "*.avi"),
                                                   ("3GP (*.3gp)", "*.3gp"),
                                                   ("MP4 (*.mp4)", "*.mp4"),
                                                   ("FLV (*.flv)", "*.flv"),
                                                   ("All Files", "*.*")
                                                   ))
    root.entry.insert(0, file)
    
# save video file
def savefolder():
    saveaudio = filedialog.asksaveasfilename(initialdir=r"C:\Users\paradox\Desktop\webapp\videotomp3",
                                      filetypes = (("MP3 (*.mp3)", "*.mp3"),
                                                   ("WAV (*.WAV)", "*.WAV"),
                                                   ("All Files", "*.*")
                                                   ))
    root.save.insert(0, saveaudio)

# convert video
def convert_video():
    mainfile = source.get()
    savefile = destination.get()
    videosource = convrt.VideoFileClip(mainfile)
    videosource.audio.write_audiofile(savefile)
    messagebox.showinfo("Done", "Converted Successfully")

root = tkinter.Tk()
root.title("Audio Converter. Md Jabed Ali")
root.config(bg="DarkOliveGreen3")
root.geometry("500x200")
source = StringVar()
destination = StringVar()

if __name__ == "__main__":
    view()
    root.mainloop()
    
                                                                                            
    
