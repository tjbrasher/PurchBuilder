import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from Data_Cleaning_wPandas_Purch import button1, button2, button3, button4, button5
from Data_Cleaning_wPandas_Purch import getBtnSelection
from Data_Cleaning_wPandas_Purch import SortList



class sortWindow(tk.Toplevel):
    
    def __init__(self):
        super().__init__()     
        
        self.focus_set()
        
        title = tk.Text(self, font= ("Arial 10 bold"), background="light gray",
                        padx=120.5, pady=2.5, width = 8, height = 1)
        title.insert("1.0", "Sorting Options")
        title.configure(state="disabled")
        title.place(x=2.5, y=2.5)
        
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
        
        
        #setting outline for sorting buttons
        promptBorder = self.c.create_rectangle(15, 60, 185, 235, outline='silver', width=2, fill="black")


        #setting heading for sort window
        Sortprompt = self.c.create_text(100, 30, text="Please Select Options" + "\n" + "for Sorting File",
                                fill = "white", font=("Segoe UI Variable Text Semibold", 12, "bold"), width = 180, justify=CENTER)


        #setting text for buttons
        rb1_text = self.c.create_text(105, 85, text="None", fill = "white", font=("Segoe UI Variable Text Semibold", 11), justify = LEFT)
        rb2_text = self.c.create_text(110, 115, text="Source", fill = "white", font=("Segoe UI Variable Text Semibold", 11), justify = LEFT)
        rb3_text = self.c.create_text(102.5, 145, text="Item", fill = "white", font=("Segoe UI Variable Text Semibold", 11), justify = LEFT)
        rb4_text = self.c.create_text(101.5, 175, text="Cost", fill = "white", font=("Segoe UI Variable Text Semibold", 11), justify = LEFT)
        rb5_text = self.c.create_text(130, 205, text="Order Status", fill = "white", font=("Segoe UI Variable Text Semibold", 11), justify = LEFT)


        #setting image for when button is selected
        self.buttonSelected = Image.open("Files\\radio_Selected.png")
        self.buttonSelected_resized = self.buttonSelected.resize((22,22))
        self.rbSelected = ImageTk.PhotoImage(self.buttonSelected_resized)


        #setting image for when button is deselected
        self.buttonDeselected = Image.open("Files\\radioButton_deselect.png")
        self.buttonDeselected_resized = self.buttonDeselected.resize((22,22))
        self.rbDeselected = ImageTk.PhotoImage(self.buttonDeselected_resized)
        
        
        #setting and placing "Done" button to close window
        doneButton = tk.Button(self, text = "Done", font=("Segoe UI Variable Text Semibold", 8), width = 10, height = 1, bg="silver", cursor="hand2")                               
        doneButton.place(x=62.5, y=250)
        
        
        #setting button state variables
        bt1SelectState = IntVar()
        bt2SelectState = IntVar()
        bt3SelectState = IntVar()
        bt4SelectState = IntVar()
        bt5SelectState = IntVar()

          
        #getting button status & assigning to variable
        bt1Set = button1.getBtnStatus()
        bt2Set = button2.getBtnStatus()
        bt3Set = button3.getBtnStatus()
        bt4Set = button4.getBtnStatus()
        bt5Set = button5.getBtnStatus()
                
        
        def getButtonStatus():   
            btstate = bt2SelectState.get() + bt3SelectState.get() + bt4SelectState.get() + bt5SelectState.get()
            #print("btstate = ", btstate)
            return btstate


        # retrieve button status from DataCleaning and set
        bstate1 = getBtnSelection(bt2Set, bt3Set, bt4Set, bt5Set)
        if bstate1 != 0:
            #print("bstate1 = ", bstate1)
            bt2SelectState.set(bt2Set)
            bt3SelectState.set(bt3Set)
            bt4SelectState.set(bt4Set)
            bt5SelectState.set(bt5Set)
        else:
            #print("bstate1 = 0")
            bt1SelectState.set(1)
            bt2SelectState.set(0)
            bt3SelectState.set(0)
            bt4SelectState.set(0)
            bt5SelectState.set(0)


        #getting status of first button
        def getRb1State():
            rb1Status = bt1SelectState.get()
            return rb1Status      

        
        #setting and placing checkbuttons to be used         
        bt1 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt1SelectState, onvalue=1, offvalue=0, cursor="hand2")
        
        bt2 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt2SelectState, onvalue=1, offvalue=0, cursor="hand2")
        
        bt3 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt3SelectState, onvalue=1, offvalue=0, cursor="hand2")
        
        bt4 = Checkbutton(self, image=self.rbDeselected, background= "black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt4SelectState, onvalue=1, offvalue=0, cursor="hand2")
        
        bt5 = Checkbutton(self, image=self.rbDeselected, background="black", foreground="black", indicatoron=False, 
                     activebackground="black", activeforeground="black",  highlightcolor="black", border=0,
                     highlightbackground="black", borderwidth=0, variable=bt5SelectState, onvalue=1, offvalue=0, cursor="hand2")
                

        #functions for button selections
        def bt1Selected():
            rb1state = getRb1State()
            if rb1state == 1:
                bt1.configure(selectimage=self.rbSelected, selectcolor="black")
                bt1.select()
                bt2.deselect()
                bt3.deselect()
                bt4.deselect()
                bt5.deselect()
                button2.setBtnStatus(0)
                button3.setBtnStatus(0)
                button4.setBtnStatus(0)
                button5.setBtnStatus(0)
            if rb1state == 0:
                bt1.select()
                bt1Selected()
                       
        def bt2Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                button2.setBtnStatus(bt2SelectState.get())
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                button1.setBtnStatus(0)
                button2.setBtnStatus(bt2SelectState.get())
                bt2.configure(selectimage=self.rbSelected, selectcolor="black")
            
        def bt3Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                button3.setBtnStatus(bt3SelectState.get())
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                button1.setBtnStatus(0)
                button3.setBtnStatus(bt3SelectState.get())
                bt3.configure(selectimage=self.rbSelected, selectcolor="black")
              
        def bt4Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                button1.setBtnStatus(0)
                button4.setBtnStatus(bt4SelectState.get())
                bt4.configure(selectimage=self.rbSelected, selectcolor="black")

        def bt5Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                button1.setBtnStatus(0)
                button5.setBtnStatus(bt5SelectState.get())
                bt5.configure(selectimage=self.rbSelected, selectcolor="black")
                
            
        #setting functions for button selections
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
        
        
        #setting the default button selection if no other buttons are selected
        while bstate1 == 0:
            bt1Selected()
            break
        else:
            pass
        
        
        #setting and passing button status to Data_Cleaning file for formatting
        def setButtons():
            button1.setBtnStatus(button1.getBtnStatus())
            button2.setBtnStatus(button2.getBtnStatus())
            button3.setBtnStatus(button3.getBtnStatus())
            button4.setBtnStatus(button4.getBtnStatus())
            button5.setBtnStatus(button5.getBtnStatus())
            
            
        #function to close window and continue program on clicking "Done" button              
        def doneClick():
            setButtons()
            SortList()
            self.grab_release()
            self.withdraw()
            #exit()


        #assigning function to "Done" button
        doneButton.configure(command = lambda: doneClick())

                

    
#programSortWindow = sortWindow()

def showSort():
    programSortWindow = sortWindow()
    programSortWindow.mainloop()
    
    
#showSort()
