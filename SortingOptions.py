from this import d
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


        rb1_text = self.c.create_text(105, 85, text="None", fill = "white", font=("Arial 11"), justify = LEFT)
        rb2_text = self.c.create_text(111, 115, text="Source", fill = "white", font=("Arial 11"), justify = LEFT)
        rb3_text = self.c.create_text(102.5, 145, text="Item", fill = "white", font=("Arial 11"), justify = LEFT)
        rb4_text = self.c.create_text(102.5, 175, text="Cost", fill = "white", font=("Arial 11"), justify = LEFT)
        rb5_text = self.c.create_text(130, 205, text="Order Status", fill = "white", font=("Arial 11"), justify = LEFT)

        self.buttonSelected = Image.open("Files\\radio_Selected.png")
        self.buttonSelected_resized = self.buttonSelected.resize((22,22))
        self.rbSelected = ImageTk.PhotoImage(self.buttonSelected_resized)
        

        self.buttonDeselected = Image.open("Files\\radioButton_deselect.png")
        self.buttonDeselected_resized = self.buttonDeselected.resize((22,22))
        self.rbDeselected = ImageTk.PhotoImage(self.buttonDeselected_resized)
        
        bt1SelectState = IntVar()
        bt2SelectState = IntVar()
        bt3SelectState = IntVar()
        bt4SelectState = IntVar()
        bt5SelectState = IntVar()
        
        def getButtonStatus():   
            btstate = bt2SelectState.get() + bt3SelectState.get() + bt4SelectState.get() + bt5SelectState.get()
            print("btstate = ", btstate)
            return btstate
        
        def getRb1Status():
            rb1Status = bt1SelectState.get()
            print("bt1State = ", rb1Status)
            return rb1Status
                
        bt1 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt1SelectState, onvalue=1, offvalue=0)
        
        bt2 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt2SelectState, onvalue=1, offvalue=0)
        
        bt3 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt3SelectState, onvalue=1, offvalue=0)
        
        bt4 = Checkbutton(self, image=self.rbDeselected, background= "black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt4SelectState, onvalue=1, offvalue=0)
        
        bt5 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt5SelectState, onvalue=1, offvalue=0)
        

        def bt1Selected():
            rb1state = getRb1Status()
            if rb1state == 1:
                bt1.configure(selectimage=self.rbSelected, selectcolor="black")
                bt1.select()
                bt2.deselect()
                bt3.deselect()
                bt4.deselect()
                bt5.deselect()
            if rb1state == 0:
                bt1.select()
                bt1Selected()
                       
        def bt2Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                bt2.configure(selectimage=self.rbSelected, selectcolor="black")
            
        def bt3Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                bt3.configure(selectimage=self.rbSelected, selectcolor="black")
              
        def bt4Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                bt4.configure(selectimage=self.rbSelected, selectcolor="black")

        def bt5Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                bt5.configure(selectimage=self.rbSelected, selectcolor="black")

                   
        bt1.configure(command=lambda: bt1Selected())
        bt1.place(x=37, y=72)
        
        bt2.configure(command=lambda: bt2Selected())
        bt2.place(x=37, y=102)
        
        bt3.configure(command=lambda: bt3Selected())
        bt3.place(x=37, y=132)
        
        bt4.configure(command=lambda: bt4Selected())
        bt4.place(x=37, y=162)
        
        bt5.configure(command=lambda: bt5Selected())
        bt5.place(x=37, y=192)
        
        
        totalBtState = getButtonStatus()
        
        while totalBtState == 0:
            bt1Selected()
            break
        else:
            pass
        
     
        
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