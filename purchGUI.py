from cgitb import text
from tkinter import *
from cProfile import label
from ctypes import alignment
from unittest import skip
from PIL import ImageTk
from PIL import Image
import tkinter.filedialog
import tkinter as tk
import tkinter.ttk
from turtle import color, end_fill, left, position, window_height, window_width

from numpy import size

window = tk.Tk()


# background image setup
#bckgnd = ImageTk.PhotoImage(file = "Files\\background.png")
#bckgnd_label = tk.Label(window, image=bckgnd)
#bckgnd_label.place(x=0, y=0, relwidth=1, relheight=1)
#bckgnd_label.configure(image=bckgnd)
#bckgnd_label.pack()

# canvas setup
c = tk.Canvas(window, bg="black", width = 620, height = 300)
c.pack()
background_image = ImageTk.PhotoImage(file = "Files\\background.png")
c.create_image(10, 10, image = background_image, anchor = NW)

# initial window setup

window.rowconfigure(3, {'minsize': 40})
window.columnconfigure(3, {'minsize': 40})
window.title("PURCH List Creator")


# window sizing and positioning
window_width = 620
window_height = 300
scr_width = window.winfo_screenwidth()
scr_height = window.winfo_screenheight()

ctr_x = int(scr_width/2 - window_width/2)
ctr_y = int(scr_height/2 - window_height/2)

window.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
window.resizable(False, False)


# setting and positioning the logo header
logo = Image.open("Files\\Logos\\EAlogoHorizonalBlackbg.jpg")
logo_resize = logo.resize((459,161))
logo_header = ImageTk.PhotoImage(logo_resize)
c.create_image(312.5,-10, image = logo_header, anchor = N)


# setting and positiong the prompt
prompt = c.create_text(307.5, 142.5, text="Please Select an Equipment List to Use for Creating PURCH List", fill = "white", font=("Arial 12 bold"))


# setting and positioning the file selection
def fileExplore():
    fileName = tk.filedialog.askopenfilename(initialdir = "/", title = "Please Select a File to Transform",
                                        filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                        ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))


#    if(len(fileName) > 50): 
#        fName_length = 50
#        print("file explore window length: " + str(fName_length))
#        fName = fileName[0:fName_length] + "..."
#        print("file name length: " + str(len(fileName)))
#        print(label_file_explorer.winfo_width())
#        print(fileName[0:fName])
#    else: fName = fileName
#    print(len(fileName))
#    print(label_file_explorer.winfo_width())
#    print(fName)
    label_file_explorer.delete("1.0", tk.END)
    label_file_explorer.insert(tk.END, fileName)

label_file_explorer = tk.Text(window, background = "light grey", foreground = "black",
                               width = 60, height = 1, font = ("Helvetica", 10))

label_file_explorer.insert("1.0", "....")
label_file_explorer.place(x=57.5, y=179)

fileBrowse = tk.Button(window, text = "Browse Files",
                        command = fileExplore)
fileBrowse.place(x=485, y=175.5)
 

# setting and positioning submit button
submit = tk.Button(window, text = "Submit", width = 10, height = 1)
submit.place(x=265, y=225)

#def submit_click():
    #open file and print to console to test functionality


#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=305, y=0, height=300)



window.mainloop()

