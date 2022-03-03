from cProfile import label
import tkinter as tk
from turtle import window_height, window_width

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

    label_file_explorer.configure(text = "File Opened: " + fileName)

label_file_explorer = tk.Label(window, text = "...", 
                               background = "grey", foreground = "black",
                               width = 80, height = 25)
label_file_explorer.grid(columnspan=2, column=0, row=1)

fileBrowse = tk.Button(window, text = "Browse Files",
                        command = fileExplore)
 
#n setting and positioning submit button
submit = tk.Button(window, text = "Submit")

label_file_explorer.pack()


window.mainloop()

