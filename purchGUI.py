from cProfile import label
from ctypes import alignment
import tkinter.filedialog
import tkinter as tk
import tkinter.ttk
from turtle import color, left, position, window_height, window_width

from numpy import size

window = tk.Tk()

# initial window setup

window.rowconfigure(3, {'minsize': 40})
window.columnconfigure(3, {'minsize': 40})
window.configure(bg="#2f2f2f")
window.title("PURCH List Creator")


# window sizing and positioning
window_width = 600
window_height = 300
scr_width = window.winfo_screenwidth()
scr_height = window.winfo_screenheight()

ctr_x = int(scr_width/2 - window_width/2)
ctr_y = int(scr_height/2 - window_height/2)

window.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
window.resizable(False, False)


# setting and positiong the prompt
prompt = tk.Label(text = "Please Select an Equipment List to Compare to the Inventory List",
                 foreground="white", background = "black")

# setting and positioning the file selection
def fileExplore():
    fileName = tk.filedialog.askopenfilename(initialdir = "/", title = "Please Select a File to Compare",
                                        filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                        ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))

    if(len(fileName) < label_file_explorer.winfo_width()): 
        fName_length = label_file_explorer.winfo_width()-3
        fName = fileName[0:fName_length] + "..."
        print(len(fileName))
        print(label_file_explorer.winfo_width())
        print(fName)
    else: fName = fileName
    print(len(fileName))
    print(label_file_explorer.winfo_width())
    print(fName)
    label_file_explorer.configure(text = fName, anchor = "w")

label_file_explorer = tk.Label(window, text = "...", 
                               background = "grey", foreground = "black",
                               width = 58, height = 1, anchor = "w")
label_file_explorer.place(x=45, y=127.5)

fileBrowse = tk.Button(window, text = "Browse Files",
                        command = fileExplore)
fileBrowse.place(x=475, y=125)
 
#n setting and positioning submit button
submit = tk.Button(window, text = "Submit", width = 10, height = 1)
submit.place(x=259, y=200)


#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=300, y=0, height=300)



window.mainloop()

