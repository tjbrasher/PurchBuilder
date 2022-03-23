import tkinter as tk
from tkinter import *
from turtle import color, width
from PIL import Image, ImageTk
from ErrorTest import resetFileBox
from tkinter import ttk


class sortWindow(tk.Toplevel):
        
    def __init__(self):#, label_file_explorer):
        super().__init__()     
        
        self.focus_set()
        self.grab_set_global()
        
        title = tk.Text(self, font= ("Arial 10 bold"), background="light gray",
                        padx=120.5, pady=2.5, width = 8, height = 1)
        title.insert("1.0", "Sorting Options")
        title.configure(state="disabled")
        title.place(x=2.5, y=2.5)
        

        #f = tk.Frame(width = 300, height = 150)
        self.c = tk.Canvas(self, bg= "white", width = 200, height =300)
        self.c.pack()      
        
        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png")
        self.c.create_image(0, 0, image = self.background_image, anchor = NW)
      
        self.overrideredirect(True)
        self.resizable(0,0)

        # window sizing and positioning
        window_width = 200
        window_height = 300
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)

        # setting and positiong the prompt
        #promptTitle = self.c.create_text(150, 17, text="Continue Program?",
        #                    fill = "gray", font=("Arial 10"), justify=CENTER)
        
        promptBorder = self.c.create_rectangle(15, 60, 185, 235, outline='silver', width=2)
   
        Sortprompt = self.c.create_text(100, 30, text="Please Select Options" + "\n" + "for Sorting File",
                                fill = "white", font=("Arial 12"), width = 180, justify=CENTER)
        
        #buttonStyle = ttk.Style(self)
        #buttonStyle.theme_use('alt')

        #cbVar = StringVar(self)
        #def onCheck():
        #    cbVar.set(1)
        #cbVar.set(0)
        #rb1 = Radiobutton(self, variable=cbVar, fg="white", bg="black",
        #                  activeforeground="white", activebackground="black",
        #                  selectcolor="black", command=onCheck()) 
        #rb1.place(x=37.5, y=72.5)

        cb1_text = self.c.create_text(105, 85, text="None", fill = "white", font=("Arial 11"), justify = LEFT)
        cb2_text = self.c.create_text(111, 115, text="Source", fill = "white", font=("Arial 11"), justify = LEFT)
        cb3_text = self.c.create_text(102.5, 145, text="Item", fill = "white", font=("Arial 11"), justify = LEFT)
        cb4_text = self.c.create_text(102.5, 175, text="Cost", fill = "white", font=("Arial 11"), justify = LEFT)
        cb5_text = self.c.create_text(130, 205, text="Order Status", fill = "white", font=("Arial 11"), justify = LEFT)

        self.buttonSelected = Image.open("Files\\radio_Selected.png")
        self.buttonSelected_resized = self.buttonSelected.resize((22,22))
        self.rbSelected = ImageTk.PhotoImage(self.buttonSelected_resized)

        self.buttonDeselected = Image.open("Files\\radioButton_deselect.png")
        self.buttonDeselected_resized = self.buttonDeselected.resize((22,22))
        self.rbDeselected = ImageTk.PhotoImage(self.buttonDeselected_resized)


        rb1Deselected = self.c.create_image(50,75, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
        rb2Deselected = self.c.create_image(50,105, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
        rb3Deselected = self.c.create_image(50,135, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
        rb4Deselected = self.c.create_image(50,165, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
        rb5Deselected = self.c.create_image(50,195, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])


        
        rb2Selected = self.c.create_image(50,105, image = self.rbSelected, anchor = N, tags=["select", "deselect"])
        rb3Selected = self.c.create_image(50,135, image = self.rbSelected, anchor = N, tags=["select", "deselect"])
        rb4Selected = self.c.create_image(50,165, image = self.rbSelected, anchor = N, tags=["select", "deselect"])
        rb5Selected = self.c.create_image(50,195, image = self.rbSelected, anchor = N, tags=["select", "deselect"])


        #def showHelp(event):
        #    showError(label_file_explorer)
        #    #open Read_Me file
            
            
        def normalState(event):
            self.c.itemconfigure(help, fill="gray")
        #    helpPrompt.place_forget()
        
        def rb1Selected(event):
            rb1Selected = self.c.create_image(50,75, image = self.rbSelected, anchor = N, tags=["select", "deselect"])
            rb1Deselected = self.c.create_image(50,75, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
            rb2Deselected = self.c.create_image(50,105, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
            rb3Deselected = self.c.create_image(50,135, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
            rb4Deselected = self.c.create_image(50,165, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])
            rb5Deselected = self.c.create_image(50,195, image = self.rbDeselected, anchor = N, tags=["select", "deselect"])            
            
            
        self.c.tag_bind("help", '<Button-1>', showHelp)        
        
        self.c.tag_bind("highlight", '<Enter>', highlightHelp)

        self.c.tag_bind("normal", '<Leave>', normalState)



        
        doneButton = tk.Button(self, text = "Done", width = 10, height = 1, bg="silver")                               
        doneButton.place(x=62.5, y=250)
              
        def doneClick():
            self.grab_release()
            self.destroy()
            exit()
            
        #def YesClick(label_file_explorer):
        #        resetFileBox(label_file_explorer)
        #        self.grab_release()
        #        self.destroy()
             
        doneButton.configure(command = lambda: doneClick())
        
        #yesButton.configure(command = lambda: YesClick(label_file_explorer))
        
        
                
#def showPrompt(label_file_explorer):
#    programPrompt = sortWindow(label_file_explorer)
#    programPrompt.mainloop()

        #tk.ttk.Separator(self, orient=tk.VERTICAL).place(x=87.5, y=0, height=300)
    

def showSort():
    programSortWindow = sortWindow()
    programSortWindow.mainloop()
    
    
showSort()