import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk


class ErrorWindow(tk.Tk):
        
    def __init__(self):
        super().__init__()     
        
        self.focus_set()
        self.grab_set_global()
                
        
        title = tk.Text(self, font= ("Arial 10 bold"), background="white", foreground="red",
                        padx=123.5, pady=2.5, width = 7, height = 1)
        title.insert("1.0", "ERROR!")
        title.configure(state="disabled")
        title.place(x=2.5, y=2.5)
        
        #f = tk.Frame(width = 300, height = 150)
        self.c = tk.Canvas(self, bg= "dark gray", width = 300, height = 125)
        self.c.pack()      

        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png")
        self.c.create_image(0, 0, image = self.background_image, anchor = NW)
      
        self.overrideredirect(True)
        self.resizable(0,0)

        window_width = 300
        window_height = 130
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)

        # setting and positiong the prompt
        promptTitle = self.c.create_text(150, 17, text="ERROR!",
                            fill = "RED", font=("Arial 12 bold"), justify=CENTER)
        
        windowBackground = self.c.create_rectangle(10, 35, 290, 120, outline='dark gray', width=2)
   
        message = self.c.create_text(150, 58, text="--- File Could Not Be Processed! ---"
                                     + "\n" + "Please Select a Different File",
                        fill = "white", font=("Arial 11"), width = 280, justify=CENTER)

        okButton = tk.Button(self, text = "OK", width = 10, height = 1)
        okButton.place(x=112.5, y=86)
              
        def OKClick():
            self.grab_release()
            self.destroy()
            
              
        okButton.configure(command = lambda: OKClick())
        
        
                
def showError():
    error = ErrorWindow()
    error.mainloop()
    
    
    
#showError()