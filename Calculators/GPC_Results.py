import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk




class sortWindow(tk.Toplevel):
    
    def __init__(self):
        super().__init__()     
        
        self.focus_set()
        
        window_width = 600
        window_height = 515
        
        window_ctrX = window_width/2
        window_ctrY = window_height/2
        
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)
        
        title = tk.Text(self, font= ("Arial 10 bold"), background="light gray",
                        padx=120.5, pady=2.5, width = 8, height = 1)
        title.insert("1.0", "Sorting Options")
        title.configure(state="disabled")
        title.place(x=window_ctrX, y=2.5)
        
        self.c = tk.Canvas(self, bg= "white", width = window_width, height =window_height)
        self.c.pack()      
        
        self.background_image = Image.open("Files\\Logos\\background.png")
        self.background_image_resize = self.background_image.resize((window_width, window_height))
        self.background_image_sized = ImageTk.PhotoImage(self.background_image_resize, master=self)
        self.c.create_image(0, 0, image = self.background_image_sized, anchor = NW)
        
        # setting and positioning the logo header
        self.logo = Image.open("Files\\Logos\\EAlogoHorizonalNobg.png")
        self.logo_resize = self.logo.resize((359,72))
        self.logo_header = ImageTk.PhotoImage(self.logo_resize, master=self)
        self.c.create_image(window_ctrX, 15, image = self.logo_header, anchor = N)
        
      
        self.overrideredirect(True)
        self.resizable(0,0)


        # window sizing and positioning
        

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)
        
        
        #setting outline for sorting buttons
        promptBorder = self.c.create_rectangle(35, 100, 565, 450, outline='silver', width=2, fill="black")


        #setting heading for sort window
        Sortprompt = self.c.create_text(window_ctrX, 110, text="GPC Totals", fill = "white",
                                        font=("Segoe UI Variable Text Semibold", 18, "bold"),
                                        width = 180, anchor=N)


        #setting text for buttons
        design_txt = self.c.create_text(70, 170, text="System Design Services", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        pm_txt = self.c.create_text(70, 210, text="Project Management", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        planning_txt = self.c.create_text(70, 250, text="Project Planning", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        travel_txt = self.c.create_text(70, 290, text="Travel", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        hardware_txt = self.c.create_text(70, 330, text="Hardware", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        finish_txt = self.c.create_text(70, 370, text="Finish (Installation Testing)", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        commisioning_txt = self.c.create_text(70, 410, text="System Commissioning", fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=W)
        
        
        eqpt_cost = 0.00
        eqpt_price = 0.00
        project_distance = 0.00
        
        
        design_hrs = 0.00
        pm_hrs = 0.00
        planning_hrs = 0.00
        travel_hrs = 0.00
        hardware_amt = 0.00
        finish_hrs = 0.00
        commissioning_hrs = 0.00
        
        
        
        #setting text for buttons
        design_hrs_txt = self.c.create_text(530, 170, text=design_hrs, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)
        pm_hrs_txt = self.c.create_text(530, 210, text=pm_hrs, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)
        planning_hrs_txt = self.c.create_text(530, 250, text=planning_hrs, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)
        travel_hrs_txt = self.c.create_text(530, 290, text=travel_hrs, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)
        hardware_amt_txt = self.c.create_text(530, 330, text=hardware_amt, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)
        finish_hrs_txt = self.c.create_text(530, 370, text=finish_hrs, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)
        commisioning_hrs_txt = self.c.create_text(530, 410, text=commissioning_hrs, fill = "white", font=("Segoe UI Variable Text Semibold", 14), anchor=E)



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
        doneButton.place(x=window_ctrX-35, y=470) 

        



                

    
#programSortWindow = sortWindow()

def showSort():
    programSortWindow = sortWindow()
    programSortWindow.mainloop()
    
    
showSort()
