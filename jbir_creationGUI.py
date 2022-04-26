import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from tkinter import *
from tkinter import Tk
import webbrowser
from PIL import Image, ImageTk
#from Data_Cleaning_wPandas_Purch import formatFile
from jbir_format import jbirFormat
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


class gui_window:
    def __init__(self, gui=None):
        self._gui = gui

    def set_gui(self, gui_window):
        self._gui = gui_window

    def get_gui(self):
        return self._gui
    
root_window_jbir = gui_window()




class jbirWindow(TkinterDnD.Tk, tk.Toplevel):

    def __init__(self):
        super().__init__()

        welcome = root_window_jbir.get_gui()
        print("welcome = ", type(welcome))
        #tk3 = tk.Toplevel(welcome)
        
        # window sizing and positioning
        window_width = 620
        window_height = 300
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)
        
        self.focus_set()
        
        self.programIcon = Image.open("Files\\EA Logo Bug.png")
        self.icon_resize = self.programIcon.resize((30,30))
        self.programIcon_resized = ImageTk.PhotoImage(self.icon_resize, master=self)
        self.iconphoto(False, self.programIcon_resized)

        self.c = tk.Canvas(self, bg="black", width = 620, height = 300)
        self.c.pack()
        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png", master=self)
        self.c.create_image(0, 0, image = self.background_image, anchor = NW)

        # setting and positioning the logo header
        self.logo = Image.open("Files\\Logos\\EAlogoHorizonalNobg.png")
        self.logo_resize = self.logo.resize((359,72))
        self.logo_header = ImageTk.PhotoImage(self.logo_resize, master=self)
        self.c.create_image(310,35, image = self.logo_header, anchor = N)

        # initial window setup
        self.rowconfigure(3, {'minsize': 40})
        self.columnconfigure(3, {'minsize': 40})
        self.title("JBIR Creator")


        
        home_icon_normal = Image.open("Files\\home-icon-normal_state.png")
        home_icon_normal_resize = home_icon_normal.resize((40,40))
        home_button_image_normal = ImageTk.PhotoImage(home_icon_normal_resize, master=self)

        home_icon_hover = Image.open("Files\\home-icon-hover.png")
        home_icon_hover_resize = home_icon_hover.resize((40,40))
        home_button_image_hover = ImageTk.PhotoImage(home_icon_hover_resize, master=self)

        home_normal = self.c.create_image(40, 35, image=home_button_image_normal, tags=["normal_state", "highlight_state","click_state"])
                    

        # setting and positiong the prompt
        self.c.create_text(307.5, 142.5, text="Please Select an Equipment List to Use for Creating JBIR", fill = "white", font=("Arial 12 bold"))

        label_file_explorer = tk.Text(self, background = "light gray", foreground = "gray",
                                      width = 57, height = 1, font = ("Arial", 10))
        label_file_explorer.insert("1.0", "Please select a file")
        label_file_explorer.place(x=57.5, y=179)


        submit = tk.Button(self, text = "Submit", width = 10, height = 1, bg = "silver")
        submit.place(x=265, y=225)
        
        inputfile.set_file("")

        
        
        #drag and drop functionality
        
        # drop methods
        def drop_enter(event):
            event.widget.focus_force()
            #print('Entering %s' % event.widget)
            return event.action

        def drop_position(event):
            return event.action

        def drop_leave(event):
            #print('Leaving %s' % event.widget)
            return event.action

        def drop(event):
            #if c.dragging:
                # the canvas itself is the drag source
            #    return REFUSE_DROP
            if event.data:
                files = label_file_explorer.tk.splitlist(event.data)
                for f in files:
                    inputfile.set_file(f)
                    label_file_explorer.delete("1.0", tk.END)
                    label_file_explorer.configure(foreground = "black")
                    label_file_explorer.insert(tk.END, inputfile.get_file())
            return event.action
        
        label_file_explorer.drop_target_register(DND_FILES)
        label_file_explorer.dnd_bind('<<DropEnter>>', drop_enter)
        label_file_explorer.dnd_bind('<<DropPosition>>', drop_position)
        label_file_explorer.dnd_bind('<<DropLeave>>', drop_leave)
        label_file_explorer.dnd_bind('<<Drop>>', drop)



        # setting and positioning the file selection
        def fileExplore():
            inputfile1 = tk.filedialog.askopenfilename(initialdir = "/Downloads", title = "Please Select a File to Transform",
                                                filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))
            inputfile.set_file(inputfile1)
            if inputfile.get_file() == "":
                label_file_explorer.delete("1.0", tk.END)
                label_file_explorer.insert("1.0", "Please select a file")
            else:
                label_file_explorer.delete("1.0", tk.END)
                label_file_explorer.configure(foreground = "black")
                label_file_explorer.insert(tk.END, inputfile.get_file())
                

        def submitClick(inputfile):
            try:
                #print(label_file_explorer.get("1.0", 'end-1c'))
                file1.set_file(label_file_explorer.get("1.0", 'end-1c'))
                #print(file1.get_file())
                #getFile(file1)
                #print("THIS IS THE SELECTED FILE: ", file1.get_file())
                jbirFormat(file1, label_file_explorer)
                
            except Exception as e: 
                #print("file not found error")
                #print(e)
                self.grab_release()
                traceback.print_exc()
                showError(label_file_explorer)
                
                    
                #open file and print to console to test functionality
           
        submit.configure(command = lambda: submitClick(inputfile.get_file()))

            
        
        fileBrowse = tk.Button(self, text = "Browse Files", bg = "silver",
                                 command = lambda: (fileExplore()))
        
        fileBrowse.place(x=485, y=175.5)

 



               
        
        # setting up the help button
        help = self.c.create_text(577.5, 275, text="Help", fill="gray", font=("Arial 10"), width=30, tags=["help", "normal","highlight"]) 
        
        helpPrompt = tk.Text(self, background = "dark gray", foreground = "black",
                                      width = 10, height = 2, font = ("Arial", 7))
        helpPrompt.insert("1.0", "Click Here" + "\n" + "for Help", "center")
        helpPrompt.tag_configure("center", justify='center')
        helpPrompt.tag_add("center", 1.0, "end")
        
        def showHelp(event):
            #showError(label_file_explorer)
            new = 2
            url = "Files\\READ_ME f03ed.html"
            webbrowser.open(url, new=new)
            
            
        def normalState(event):
            self.c.itemconfigure(help, fill="gray")
            helpPrompt.place_forget()
        
        def highlightHelp(event):            
            helpPrompt.place(x=550, y=230)
            self.c.itemconfigure(help, fill="red")
            
        self.c.tag_bind("help", '<Button-1>', showHelp)        
        
        self.c.tag_bind("highlight", '<Enter>', highlightHelp)

        self.c.tag_bind("normal", '<Leave>', normalState)
        

        def onClose(event):
            welcome.deiconify()
            self.grab_release()
            self.withdraw()

        def normalState(event):
            self.c.itemconfigure(home_normal, image=home_button_image_normal)
            print('entered normal state')
       
        def hoverEvent(event):            
            self.c.itemconfigure(home_normal, image=home_button_image_hover)
            
            print('entered hover state')
            
        self.c.tag_bind("click_state", '<Button-1>', onClose)        
        
        self.c.tag_bind("highlight_state", '<Enter>', hoverEvent)

        self.c.tag_bind("normal_state", '<Leave>', normalState)



        self.protocol("WM_DELETE_WINDOW", lambda: onClose(None))


#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=305, y=0, height=300)

def launchJBIR():
    jbir_gui = jbirWindow()
    jbir_gui.mainloop()
    

