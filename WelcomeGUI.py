from logging import root
import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from tkinter import *
from tkinter import Tk
import webbrowser
from PIL import Image, ImageTk
from Data_Cleaning_wPandas_Purch import formatFile
from purchGUI import launchPURCH
from jbir_creationGUI import jbirWindow, root_window_jbir
from purchGUI import purchWindow, root_window_purch
from ErrorTest import showError
from SortingOptions import sortWindow
import traceback
import codecs
from tkinterdnd2 import *

#programSortWindow = sortWindow()

class fileObject:
    def __init__(self, file=None):
        self._file = file

    def get_file(self):
        return self._file

    def set_file(self, fileName):
        self._file = fileName
        
file1 = fileObject()

inputfile = fileObject()



class mainApp(Tk):

    def __init__(self):
        super().__init__()
        
        self.wm_iconbitmap(bitmap=None, default=None)
        
        # window sizing and positioning       
        window_width = 470
        window_height = 220
        window_ctr_x = (window_width/2)
        window_ctr_y = (window_height/2)
        
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()
        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)
        
        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)

            
        self.c = tk.Canvas(self, bg="black", width = window_width, height = window_height)
        self.c.pack()
        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png")
        self.c.create_image(0, 0, image = self.background_image, anchor = NW)
        
        self.programIcon = Image.open("Files\\EA Logo Bug.png")
        self.icon_resize = self.programIcon.resize((30,30))
        self.programIcon_resized = ImageTk.PhotoImage(self.icon_resize)
        self.iconphoto(False, self.programIcon_resized)

        # setting and positioning the logo header
        self.logo = Image.open("Files\\Logos\\EAlogoHorizonalNobg.png")
        self.logo_resize = self.logo.resize((359,72))
        self.logo_header = ImageTk.PhotoImage(self.logo_resize)
        self.c.create_image((window_ctr_x), (window_ctr_y-87.5), image = self.logo_header, anchor = N)

        # initial window setup
        self.rowconfigure(3, {'minsize': 40})
        self.columnconfigure(3, {'minsize': 40})
        self.title("PURCH List Creator")


        # setting and positiong the prompt
        self.c.create_text((window_ctr_x), (window_ctr_y+5), text="Please Select an Option Below", fill = "white", font=("Segoe UI Variable Text Semibold", 14, "bold"))

        

        #purch_gui.grab_release()
        #purch_gui.withdraw()
        def showPurch(): 
            purch_gui = purchWindow()
            self.grab_release()
            self.withdraw()
            purch_gui.deiconify()
        #    if 'withdrawn' == purch_gui.state():
        #        purch_gui.focus_set()
        #        purch_gui.grab_set_global()
        #        purch_gui.deiconify()
        #    elif 'normal' == self.state():
        #        purch_gui.focus_set()
        #        purch_gui.grab_set_global()
        #        purch_gui.deiconify()

        #purch_btn = tk.Button(self, text = "PURCH List", font=("Segoe UI Variable Text Semibold", 8), width = 10, height = 1, bg = "silver", cursor="hand2")
        #purch_btn.place(x=(window_ctr_x - 100), y=(window_ctr_y +40))
        #purch_btn.configure(command = lambda: showPurch())

        purch_btn_normal = Image.open("Buttons\\purch_btn_normal.png")
        purch_btn_normal_resize = purch_btn_normal.resize((85,55))
        purch_btn_image_normal = ImageTk.PhotoImage(purch_btn_normal_resize, master=self)

        purch_btn_pressed = Image.open("Buttons\\purch_btn_pressed.png")
        purch_pressed_resize = purch_btn_pressed.resize((85,55))
        purch_pressed_image = ImageTk.PhotoImage(purch_pressed_resize, master=self)

        purch = self.c.create_image(window_ctr_x-65, window_ctr_y+52, image=purch_btn_image_normal, tags=["purch_normal_state", "purch_hover_state","purch_click_state"])
        
        
        def purch_hoverEvent(event):    
            self.c.config(cursor="hand2")        
            self.c.itemconfigure(purch, image=purch_pressed_image)
            
            #print('entered hover state')
            
        def purch_normalState(event):    
            self.c.config(cursor="arrow")        
            self.c.itemconfigure(purch, image=purch_btn_image_normal)
            

        
        self.c.tag_bind("purch_hover_state", '<Enter>', purch_hoverEvent)

        self.c.tag_bind("purch_normal_state", '<Leave>', purch_normalState)
        


        def purchClick():
            try:
                self.c.itemconfigure(purch, image=purch_pressed_image)
                showPurch()
                
            except Exception as e: 
                #print("file not found error")
                #print(e)
                self.grab_release()
                traceback.print_exc()               
                
                    
                #open file and print to console to test functionality
           
        self.c.tag_bind("purch_click_state", '<Button-1>', lambda x: purchClick())   


        jbir_btn_normal = Image.open("Buttons\\jbir_btn_normal.png")
        jbir_btn_normal_resize = jbir_btn_normal.resize((85,55))
        jbir_btn_image_normal = ImageTk.PhotoImage(jbir_btn_normal_resize, master=self)

        jbir_btn_pressed = Image.open("Buttons\\jbir_btn_pressed.png")
        jbir_pressed_resize = jbir_btn_pressed.resize((85,55))
        jbir_pressed_image = ImageTk.PhotoImage(jbir_pressed_resize, master=self)

        jbir = self.c.create_image(window_ctr_x+72.5, window_ctr_y+52, image=jbir_btn_image_normal, tags=["jbir_normal_state", "jbir_hover_state","jbir_click_state"])
        
        
        def jbir_hoverEvent(event):    
            self.c.config(cursor="hand2")        
            self.c.itemconfigure(jbir, image=jbir_pressed_image)
            
            #print('entered hover state')
            
        def jbir_normalState(event):    
            self.c.config(cursor="arrow")        
            self.c.itemconfigure(jbir, image=jbir_btn_image_normal)

        
        self.c.tag_bind("jbir_hover_state", '<Enter>', jbir_hoverEvent)

        self.c.tag_bind("jbir_normal_state", '<Leave>', jbir_normalState)
                


        def showJBIR():
            self.grab_release()
            self.withdraw()
            jbir_gui = jbirWindow()
            jbir_gui.deiconify()
            #if 'withdrawn' == jbir_gui.state():
            #    jbir_gui.focus_set()
            #    jbir_gui.grab_set_global()
            #    jbir_gui.deiconify()
            #elif 'normal' == self.state():
            #    jbir_gui.focus_set()
            #    jbir_gui.grab_set_global()
            #    jbir_gui.deiconify()    



        def jbirClick():
            try:
                self.c.itemconfigure(jbir, image=jbir_pressed_image)
                showJBIR()
                
            except Exception as e: 
                #print("file not found error")
                #print(e)
                self.grab_release()
                traceback.print_exc()      
            

        #jbir_btn = tk.Button(self, text = "JBIR", font=("Segoe UI Variable Text Semibold", 8), width = 10, height = 1, bg = "silver", cursor="hand2")
        #jbir_btn.place(x=(window_ctr_x + 37.5), y=(window_ctr_y +40))
        #jbir_btn.configure(command = lambda: showJBIR())
        
        inputfile.set_file("")

        self.c.tag_bind("jbir_click_state", '<Button-1>', lambda x: jbirClick())   


        # setting up the help button
        help = self.c.create_text(435, (window_ctr_y +85), text="Help", fill="gray", font=("Segoe UI Variable Text Semibold", 10), width=30, tags=["help", "normal","highlight"]) 
        
        helpPrompt = tk.Text(self, background = "dark gray", foreground = "black",
                                      width = 10, height = 2, font = ("Segoe UI Variable Text Semibold", 8))
        helpPrompt.insert("1.0", "Click Here" + "\n" + "for Help", "center")
        helpPrompt.tag_configure("center", justify='center')
        helpPrompt.tag_add("center", 1.0, "end")
        
        
        def showHelp(event):
            #showError(label_file_explorer)
            new = 2
            url = "Files\\READ_ME f03ed.html"
            webbrowser.open(url, new=new)
            
                        
        def normalState(event):
            self.c.config(cursor="arrow")
            self.c.itemconfigure(help, fill="gray")
            helpPrompt.place_forget()
        
        def highlightHelp(event):            
            helpPrompt.place(x=window_ctr_x+165, y=window_ctr_y+40)
            self.c.config(cursor="hand2")
            self.c.itemconfigure(help, fill="red")
            
        self.c.tag_bind("help", '<Button-1>', showHelp)        
        
        self.c.tag_bind("highlight", '<Enter>', highlightHelp)

        self.c.tag_bind("normal", '<Leave>', normalState)


        
        def onClose():
            exit()

        self.protocol("WM_DELETE_WINDOW", lambda: onClose())
        
        

#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=305, y=0, height=300)

if __name__ == "__main__":
    welcome_gui = mainApp()
    root_window_purch.set_gui(welcome_gui)
    root_window_jbir.set_gui(welcome_gui)
    welcome_gui.mainloop()
