import tkinter as tk
from tkinter import *
from turtle import color
from PIL import Image, ImageTk
from ErrorTest import resetFileBox
import sys


class promptWindow(tk.Toplevel):
        
    def __init__(self, label_file_explorer):
        super().__init__()     
        
        self.focus_set()
        self.grab_set_global()
        
        title = tk.Text(self, font= ("Arial 10 bold"), background="light gray",
                        padx=120.5, pady=2.5, width = 8, height = 1)
        title.insert("1.0", "Message")
        title.configure(state="disabled")
        title.place(x=2.5, y=2.5)
        

        #f = tk.Frame(width = 300, height = 150)
        self.c = tk.Canvas(self, bg= "white", width = 300, height =125)
        self.c.pack()      
        
        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png")
        self.c.create_image(0, 0, image = self.background_image, anchor = NW)
      
        self.overrideredirect(True)
        self.resizable(0,0)

        # window sizing and positioning
        window_width = 300
        window_height = 125
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)

        # setting and positiong the prompt
        #promptTitle = self.c.create_text(150, 17, text="Continue Program?",
        #                    fill = "gray", font=("Arial 10"), justify=CENTER)
        
        #promptBorder = self.c.create_rectangle(10, 10, 290, 115, outline='silver', width=2)
   
        message = self.c.create_text(150, 25, text="Operation Successful!",
                                fill = "white", font=("Arial 11"), width = 280, justify=CENTER)
   
        prompt = self.c.create_text(150, 50, text="Would You Like to Process Another File?",
                        fill = "white", font=("Arial 11"), width = 280, justify=CENTER)


        yes_btn_normal = Image.open("Buttons\\yes_btn_normal.png")
        yes_btn_normal_resize = yes_btn_normal.resize((85,55))
        yes_btn_image_normal = ImageTk.PhotoImage(yes_btn_normal_resize, master=self)

        yes_btn_pressed = Image.open("Buttons\\yes_btn_pressed.png")
        yes_pressed_resize = yes_btn_pressed.resize((85,55))
        yes_pressed_image = ImageTk.PhotoImage(yes_pressed_resize, master=self)

        yes_btn_hover = Image.open("Buttons\\yes_btn_hover.png")
        yes_hover_resize = yes_btn_hover.resize((85,55))
        yes_hover_image = ImageTk.PhotoImage(yes_hover_resize, master=self)


        no_btn_normal = Image.open("Buttons\\no_btn_normal.png")
        no_btn_normal_resize = no_btn_normal.resize((85,55))
        no_btn_image_normal = ImageTk.PhotoImage(no_btn_normal_resize, master=self)

        no_btn_pressed = Image.open("Buttons\\no_btn_pressed.png")
        no_pressed_resize = no_btn_pressed.resize((85,55))
        no_pressed_image = ImageTk.PhotoImage(no_pressed_resize, master=self)

        no_btn_hover = Image.open("Buttons\\no_btn_hover.png")
        no_hover_resize = no_btn_hover.resize((85,55))
        no_hover_image = ImageTk.PhotoImage(no_hover_resize, master=self)

        yes = self.c.create_image(92, 90, image=yes_btn_image_normal, tags=["yes_normal_state", "yes_hover_state","yes_click_state"])

        no = self.c.create_image(207.5, 90, image=no_btn_image_normal, tags=["no_normal_state", "no_hover_state","no_click_state"])
        


        def yes_hoverEvent(event):    
            self.c.config(cursor="hand2")        
            self.c.itemconfigure(yes, image=yes_hover_image)
            
            print('entered hover state')
            
        def yes_normalState(event):    
            self.c.config(cursor="arrow")        
            self.c.itemconfigure(yes, image=yes_btn_image_normal)
            
        #self.c.tag_bind("yes_click_state", '<Button-1>', yes_btnClick())        
        
        self.c.tag_bind("yes_hover_state", '<Enter>', yes_hoverEvent)

        self.c.tag_bind("yes_normal_state", '<Leave>', yes_normalState)


        def no_hoverEvent(event):    
            self.c.config(cursor="hand2")        
            self.c.itemconfigure(no, image=no_hover_image)
            
            print('entered hover state')
            
        def no_normalState(event):    
            self.c.config(cursor="arrow")        
            self.c.itemconfigure(no, image=no_btn_image_normal)
            
        #self.c.tag_bind("yes_click_state", '<Button-1>', yes_btnClick())        
        
        self.c.tag_bind("no_hover_state", '<Enter>', no_hoverEvent)

        self.c.tag_bind("no_normal_state", '<Leave>', no_normalState)

              
        def NoClick():
            self.c.itemconfigure(no, image=no_pressed_image)
            self.grab_release()
            self.destroy()
            self.master.destroy()
            sys.exit()            
            
        def YesClick(label_file_explorer):
            self.c.itemconfigure(yes, image=yes_pressed_image)
            resetFileBox(label_file_explorer)
            self.grab_release()
            self.destroy()


        self.c.tag_bind("yes_click_state", '<Button-1>', lambda x: YesClick(label_file_explorer))   
        self.c.tag_bind("no_click_state", '<Button-1>', lambda x: NoClick())   
        
        
                
def showPrompt(label_file_explorer):
    programPrompt = promptWindow(label_file_explorer)
    programPrompt.mainloop()
    
    
#showPrompt(None)