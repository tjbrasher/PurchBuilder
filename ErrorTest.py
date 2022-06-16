import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image


def resetFileBox(self):
    self.delete("1.0", tk.END)
    self.configure(foreground = "gray")         
    self.insert("1.0", "Please select a file")
   
class ErrorWindow(tk.Toplevel):
    
        
    def __init__(self, label_file_explorer):
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
                            fill = "RED", font=("Segoe UI Variable Text Semibold", 14), justify=CENTER)
        
        windowBackground = self.c.create_rectangle(10, 35, 290, 120, outline='dark gray', width=2)
   
        message = self.c.create_text(150, 58, text="--- Request Could Not Be Processed! ---"
                                     + "\n" + "Please Try Again",
                        fill = "white", font=("Segoe UI Variable Text Semibold", 11), width = 280, justify=CENTER)

        okButton = tk.Button(self, text = "OK", font=("Segoe UI Variable Text Semibold", 8), width = 10, height = 1, bg = "silver", cursor="hand2")
        #okButton.place(x=112.5, y=86)


        ok_btn_normal = Image.open("Buttons\\ok_btn_normal.png")
        ok_btn_normal_resize = ok_btn_normal.resize((85,55))
        ok_btn_image_normal = ImageTk.PhotoImage(ok_btn_normal_resize, master=self)

        ok_btn_pressed = Image.open("Buttons\\ok_btn_pressed.png")
        ok_pressed_resize = ok_btn_pressed.resize((85,55))
        ok_pressed_image = ImageTk.PhotoImage(ok_pressed_resize, master=self)

        ok = self.c.create_image(147.5, 98, image=ok_btn_image_normal, tags=["ok_normal_state", "ok_hover_state","ok_click_state"])
        
        
        def ok_hoverEvent(event):    
            self.c.config(cursor="hand2")        
            self.c.itemconfigure(ok, image=ok_pressed_image)
            
            #print('entered hover state')
            
        def ok_normalState(event):    
            self.c.config(cursor="arrow")        
            self.c.itemconfigure(ok, image=ok_btn_image_normal)

        
        self.c.tag_bind("ok_hover_state", '<Enter>', ok_hoverEvent)

        self.c.tag_bind("ok_normal_state", '<Leave>', ok_normalState)


              
        def OKClick(label_file_explorer):
            resetFileBox(label_file_explorer)
            self.grab_release()
            self.destroy()            
            
              
        #okButton.configure(command = lambda: OKClick(label_file_explorer))

        self.c.tag_bind("ok_click_state", '<Button-1>', lambda x: OKClick(label_file_explorer))   

                
def showError(label_file_explorer):
    error = ErrorWindow(label_file_explorer)
    error.mainloop()
    
    
    
#showError(None)