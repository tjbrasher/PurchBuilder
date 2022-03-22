from calendar import c
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
from Data_Cleaning_wPandas_Purch import formatFile
from ErrorTest import showError
import traceback


class fileObject:
    def __init__(self, file=None):
        self._file = file

    def get_file(self):
        return self._file

    def set_file(self, fileName):
        self._file = fileName
        
file1 = fileObject()

inputfile = fileObject()


class mainApp(tk.Tk):

    def __init__(self):
        super().__init__()

        self.c = tk.Canvas(self, bg="black", width = 620, height = 300)
        self.c.pack()
        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png")
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

        label_file_explorer = tk.Text(self, background = "light gray", foreground = "gray",
                                      width = 57, height = 1, font = ("Arial", 10))
        label_file_explorer.insert("1.0", "Please select a file")
        label_file_explorer.place(x=57.5, y=179)
    

        submit = tk.Button(self, text = "Submit", width = 10, height = 1, bg = "silver")
        submit.place(x=265, y=225)
        
        inputfile.set_file("")

        # setting and positioning the file selection
        def fileExplore():
            inputfile1 = tk.filedialog.askopenfilename(initialdir = "/", title = "Please Select a File to Transform",
                                                filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))
            inputfile.set_file(inputfile1)
            if inputfile.get_file() == "":
                label_file_explorer.delete("1.0", tk.END)
                label_file_explorer.insert("1.0", "Please select a file")
            else:
                label_file_explorer.delete("1.0", tk.END)
                label_file_explorer.configure(foreground = "black")
                label_file_explorer.insert(tk.END, inputfile.get_file())
                

        def submitClick(inputfile):
            try:
                print("Else statement executed")
                print(label_file_explorer.get("1.0", 'end-1c'))
                file1.set_file(label_file_explorer.get("1.0", 'end-1c'))
                print(file1.get_file())
                #getFile(file1)
                print("THIS IS THE SELECTED FILE: ", file1.get_file())
                formatFile(file1, label_file_explorer)
                
            except Exception as e: 
                print("file not found error")
                print(e)
                traceback.print_exc()
                showError(label_file_explorer)
                
                    
                #open file and print to console to test functionality
           
        submit.configure(command = lambda: submitClick(inputfile.get_file()))

            
        
        fileBrowse = tk.Button(self, text = "Browse Files", bg = "silver",
                                 command = lambda: (fileExplore()))
        
        fileBrowse.place(x=485, y=175.5)
        
        # setting up sort selection drop down menu
        options = [
            "None",
            "Source",
            "Item",
            "Cost",
            "Order Status",
            "Source & Item",
            "Item & Cost",
            "Source & Status",
            "Item & Status",
            "Cost & Status",
        ]
        
        # setting up the help button
        sorting = self.c.create_text(530, 225, text="Sorting Options", fill="white", font=("Arial 10"), width=200, tags=["sort", "normalSort","highlightSort"]) 
        
        sortPrompt = tk.Text(self, background = "dark gray", foreground = "black",
                                      width = 15, height = 2, font = ("Arial", 7))
        sortPrompt.insert("1.0", "Click Here for" + "\n" + "Sorting Options", "center")
        sortPrompt.tag_configure("center", justify='center')
        sortPrompt.tag_add("center", 1.0, "end")
        
        def showSort(event):
            showError(label_file_explorer)
            #open Read_Me file
            
            
        def normalSortState(event):
            self.c.itemconfigure(sorting, fill="white")
            sortPrompt.place_forget()
        
        def highlightSort(event):            
            #sortPrompt.place(x=490, y=185)
            self.c.itemconfigure(sorting, fill="red")
            
        self.c.tag_bind("sort", '<Button-1>', showSort)        
        
        self.c.tag_bind("highlightSort", '<Enter>', highlightSort)

        self.c.tag_bind("normalSort", '<Leave>', normalSortState)

        
        
        # setting up the help button
        help = self.c.create_text(577.5, 275, text="Help", fill="gray", font=("Arial 10"), width=30, tags=["help", "normal","highlight"]) 
        
        helpPrompt = tk.Text(self, background = "dark gray", foreground = "black",
                                      width = 10, height = 2, font = ("Arial", 7))
        helpPrompt.insert("1.0", "Click Here" + "\n" + "for Help", "center")
        helpPrompt.tag_configure("center", justify='center')
        helpPrompt.tag_add("center", 1.0, "end")
        
        def showHelp(event):
            showError(label_file_explorer)
            #open Read_Me file
            
            
        def normalState(event):
            self.c.itemconfigure(help, fill="gray")
            helpPrompt.place_forget()
        
        def highlightHelp(event):            
            helpPrompt.place(x=550, y=230)
            self.c.itemconfigure(help, fill="red")
            
        self.c.tag_bind("help", '<Button-1>', showHelp)        
        
        self.c.tag_bind("highlight", '<Enter>', highlightHelp)

        self.c.tag_bind("normal", '<Leave>', normalState)
        

#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=305, y=0, height=300)

if __name__ == "__main__":
    app = mainApp()
    app.mainloop()
    print('fcheck = ', file1.get_file())
