import tkinter as tk
from tkinter import *
from turtle import color, width
from PIL import Image, ImageTk
from ErrorTest import resetFileBox
from tkinter import ttk
from Data_Cleaning_wPandas_Purch import setBtnStatus, getBtnStatus
from Data_Cleaning_wPandas_Purch import getBtnSelection
from Data_Cleaning_wPandas_Purch import bt1State, bt2State, bt3State, bt4State, bt5State
from Data_Cleaning_wPandas_Purch import printSortList

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
        
        promptBorder = self.c.create_rectangle(15, 60, 185, 235, outline='silver', width=2, fill="black")
   
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
        
        doneButton = tk.Button(self, text = "Done", width = 10, height = 1, bg="silver")                               
        doneButton.place(x=62.5, y=250)
        
        bt1SelectState = IntVar()
        bt2SelectState = IntVar()
        bt3SelectState = IntVar()
        bt4SelectState = IntVar()
        bt5SelectState = IntVar()
        
        
          
        
        bt1Set = getBtnStatus(bt1SelectState)
        print("bt1 = ", bt1Set)
        bt2Set = getBtnStatus(bt2SelectState)
        print("bt2 = ", bt2Set)
        bt3Set = getBtnStatus(bt3SelectState)
        print("bt3 = ", bt3Set)
        bt4Set = getBtnStatus(bt4SelectState)
        print("bt4 = ", bt4Set)
        bt5Set = getBtnStatus(bt5SelectState)
        print("bt5 = ", bt5Set)
                  
        
        print("bt1Set = ", bt1Set)
        print("bt2Set = ", bt2Set)
        print("bt3Set = ", bt3Set)
        print("bt4Set = ", bt4Set)
        print("bt5Set = ", bt5Set)
        
        #bt1SelectState.set(setRb1Status(bt1SelectState, bt1Set))
        #bt2SelectState.set(setRb2Status(bt2SelectState, bt2Set))
        #bt3SelectState.set(setRb3Status(bt3SelectState, bt3Set))
        #bt4SelectState.set(setRb4Status(bt4SelectState, bt4Set))
        #bt5SelectState.set(setRb5Status(bt5SelectState, bt5Set))
        
        print("bt1SelectState = ", bt1SelectState.get())
        print("bt2SelectState = ", bt2SelectState.get())

        def getButtonState(bt2Set, bt3Set, bt4Set, bt5Set):   
            btstate1 = bt2Set + bt3Set + bt4Set + bt5Set
            print("btstate = ", btstate1)
            return btstate1
        
        def getButtonStatus():   
            btstate = bt2SelectState.get() + bt3SelectState.get() + bt4SelectState.get() + bt5SelectState.get()
            print("btstate = ", btstate)
            return btstate
        
        
        def setBtnSelection(bt2Set, bt3Set, bt4Set, bt5Set):   
            btstate1 = bt2Set + bt3Set + bt4Set + bt5Set
            print("btstate = ", btstate1)
            return btstate1
                
        # retrieve button status from DataCleaning and set

        
        bstate1 = getBtnSelection(bt2Set, bt3Set, bt4Set, bt5Set)
        if bstate1 != 0:
            print("bstate1 = ", bstate1)
            bt2SelectState.set(bt2Set)
            bt3SelectState.set(bt3Set)
            bt4SelectState.set(bt4Set)
            bt5SelectState.set(bt5Set)
        else:
            print("bstate1 = 0")
            bt1SelectState.set(1)
            bt2SelectState.set(0)
            bt3SelectState.set(0)
            bt4SelectState.set(0)
            bt5SelectState.set(0)


        def getRb1State():
            rb1Status = bt1SelectState.get()
            #print("bt1State = ", rb1Status)
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
            rb1state = getRb1State()
            if rb1state == 1:
                bt1.configure(selectimage=self.rbSelected, selectcolor="black")
                bt1.select()
                #setBtnStatus(bt1SelectState, bt1SelectState.get())
                bt2.deselect()
                bt3.deselect()
                bt4.deselect()
                bt5.deselect()
            if rb1state == 0:
                bt1.select()
                #setBtnStatus(bt1SelectState, bt1SelectState.get())
                bt1Selected()
                       
        def bt2Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                setBtnStatus(bt2SelectState, bt2SelectState.get())
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                setBtnStatus(bt2SelectState, bt2SelectState.get())
                bt2.configure(selectimage=self.rbSelected, selectcolor="black")
            
        def bt3Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                setBtnStatus(bt3SelectState, bt3SelectState.get())
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                setBtnStatus(bt3SelectState, bt3SelectState.get())
                bt3.configure(selectimage=self.rbSelected, selectcolor="black")
              
        def bt4Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                setBtnStatus(bt4SelectState, bt4SelectState.get())
                bt4.configure(selectimage=self.rbSelected, selectcolor="black")

        def bt5Selected():
            btstate = getButtonStatus()
            if btstate == 0:
                bt1Selected()
            else:
                bt1.deselect()
                bt1.deselect()
                setBtnStatus(bt5SelectState, bt5SelectState.get())
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
        
        
        totalBtState = getButtonState(bt2Set, bt3Set, bt4Set, bt5Set)
        
        while bstate1 == 0:
            bt1Selected()
            break
        else:
            pass
        
        def setButtons():
            bt1State(bt1Set)
            bt2State(bt2Set)
            bt3State(bt3Set)
            bt4State(bt4Set)
            bt5State(bt5Set)
            
              
        def doneClick():
            setButtons()
            printSortList()
            self.grab_release()
            self.withdraw()
            #exit()

            
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
    
#programSortWindow = sortWindow()

def showSort():
    programSortWindow = sortWindow()
    programSortWindow.mainloop()
    
    
#showSort()