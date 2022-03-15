from hashlib import new
import tkinter as tk
import tkinter.filedialog
import tkinter.ttk
import os
#import Data_Cleaning_wPandas_Purch as purch

from tkinter import *
from PIL import ImageTk
from cgitb import text
from cProfile import label
from ctypes import alignment
from unittest import skip
from PIL import Image
from turtle import color, end_fill, left, position, window_height, window_width
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from numpy import size
import fileinput


class fileObject:
    def __init__(self, file=None):
        self._file = file

    def get_file(self):
        return self._file

    def set_file(self, fileName):
        self._file = fileName

file1 = fileObject()

class mainApp(tk.Tk):

    def __init__(self):
        super().__init__()
        file = None
        self._file = file

        def get_file(self):
            return self._file

        def set_file(self, inputFile):
            self._file = inputFile

        self.c = tk.Canvas(self, bg="black", width = 620, height = 300)
        self.c.pack()
        self.background_image = ImageTk.PhotoImage(file = "Files\\background.png")
        self.c.create_image(10, 10, image = self.background_image, anchor = NW)

        # setting and positioning the logo header
        self.logo = Image.open("Files\\Logos\\EAlogoHorizonalNobg.png")
        self.logo_resize = self.logo.resize((359,72))
        self.logo_header = ImageTk.PhotoImage(self.logo_resize)
        self.c.create_image(310,35, image = self.logo_header, anchor = N)

        # initial window setup
        self.rowconfigure(3, {'minsize': 40})
        self.columnconfigure(3, {'minsize': 40})
        self.title("PURCH List Creator")

        # window sizing and positioning
        window_width = 620
        window_height = 300
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)


        # setting and positiong the prompt
        self.c.create_text(307.5, 142.5, text="Please Select an Equipment List to Use for Creating PURCH List", fill = "white", font=("Arial 12 bold"))

        label_file_explorer = tk.Text(self, background = "light grey", foreground = "black",
                            width = 57, height = 1, font = ("Helvetica", 10))
        label_file_explorer.insert("1.0", "....")
        label_file_explorer.place(x=57.5, y=179)

        submit = tk.Button(self, text = "Submit", width = 10, height = 1)
        submit.place(x=265, y=225)


        # setting and positioning the file selection
        def fileExplore():
            inputfile = tk.filedialog.askopenfilename(initialdir = "/", title = "Please Select a File to Transform",
                                                filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))
            label_file_explorer.delete("1.0", tk.END)
            label_file_explorer.insert(tk.END, inputfile)

            def submitClick():
                submitFile = tk.filedialog.asksaveasfilename(initialfile=inputfile, defaultextension=".csv", title = "Please select a location to save your file",
                                                filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))
                if submitFile:
                    file1.set_file(inputfile)
                    print("THIS IS THE SELECTED FILE: ", file1.get_file())
                    import Data_Cleaning_wPandas_Purch 
                
                
                                   

            #open file and print to console to test functionality

            submit.configure(command = lambda: submitClick())
            
        
        fileBrowse = tk.Button(self, text = "Browse Files",
                                 command = lambda: (fileExplore()))
        
        fileBrowse.place(x=485, y=175.5)

       


#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=305, y=0, height=300)

if __name__ == "__main__":
    app = mainApp()
    print('fcheck = ', file1.get_file())
    app.mainloop()
