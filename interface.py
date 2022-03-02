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

fileBrowse = tk.Frame(window)

window.mainloop()
