import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from tkinter import *
from tkinter import Tk
import webbrowser
from PIL import Image, ImageTk
from Data_Cleaning_wPandas_Purch import formatFile
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
    
root_window_purch = gui_window()


class purchWindow(TkinterDnD.Tk, tk.Toplevel):

    def __init__(self):
        super().__init__()
        
        welcome = root_window_purch.get_gui()
        print("welcome = ", type(welcome))
        
        # window sizing and positioning
        window_width = 600
        window_height = 275
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)
        
        win_ctr_x = window_width/2
        win_ctr_y = window_height/2

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)
                
        self.focus_set()

        self.programIcon = Image.open("Files\\EA Logo Bug.png")
        self.icon_resize = self.programIcon.resize((30,30))
        self.programIcon_resized = ImageTk.PhotoImage(self.icon_resize, master=self)
        self.iconphoto(False, self.programIcon_resized)

        self.c = tk.Canvas(self, bg="black", width = window_width, height = window_height)
        self.c.pack()
        self.background_image = ImageTk.PhotoImage(file = "Files\\Logos\\background.png", master=self)
        self.c.create_image(0, 0, image = self.background_image, anchor = NW)

        # setting and positioning the logo header
        self.logo = Image.open("Files\\Logos\\EAlogoHorizonalNobg.png")
        self.logo_resize = self.logo.resize((359,72))
        self.logo_header = ImageTk.PhotoImage(self.logo_resize, master=self)
        self.c.create_image(win_ctr_x,win_ctr_y-120, image = self.logo_header, anchor = N)

        # initial window setup
        self.rowconfigure(3, {'minsize': 40})
        self.columnconfigure(3, {'minsize': 40})
        self.title("PURCH List Creator")

        browse_icon_normal = Image.open("Files\\search_icon_normal_state.png")
        browse_icon_normal_resize = browse_icon_normal.resize((30,30))
        browse_button_image_normal = ImageTk.PhotoImage(browse_icon_normal_resize, master=self)

        browse_icon_hover = Image.open("Files\\search_icon_highlight.png")
        browse_icon_hover_resize = browse_icon_hover.resize((30,30))
        browse_button_image_hover = ImageTk.PhotoImage(browse_icon_hover_resize, master=self)
        

        home_icon_normal = Image.open("Files\\home-icon-normal_state.png")
        home_icon_normal_resize = home_icon_normal.resize((35,35))
        home_button_image_normal = ImageTk.PhotoImage(home_icon_normal_resize, master=self)

        home_icon_hover = Image.open("Files\\home-icon-hover.png")
        home_icon_hover_resize = home_icon_hover.resize((35,35))
        home_button_image_hover = ImageTk.PhotoImage(home_icon_hover_resize, master=self)

        home_normal = self.c.create_image(35, 35, image=home_button_image_normal, tags=["normal_state", "highlight_state","click_state"])
        
        
        sort_icon_normal = Image.open("Files\\345-3458587_filter-sort-icon-normal_statexcf.png")
        sort_icon_normal_resize = sort_icon_normal.resize((55,25))
        sort_button_image_normal = ImageTk.PhotoImage(sort_icon_normal_resize, master=self)

        sort_icon_hover = Image.open("Files\\345-3458587_filter-sort-icon-highlight_state.png")
        sort_icon_hover_resize = sort_icon_hover.resize((55,25))
        sort_button_image_hover = ImageTk.PhotoImage(sort_icon_hover_resize, master=self)
        

        # setting and positiong the prompt
        self.c.create_text(win_ctr_x, win_ctr_y-25, text="Please Select a File to Use for Creating the PURCH List", fill = "white", font=("Segoe UI Variable Text Semibold", 14, "bold"))

        label_file_explorer = tk.Text(self, background = "light gray", foreground = "gray",
                                      width = 57, height = 1, font = ("Arial", 10))
        label_file_explorer.insert("1.0", " Please select a file")
        label_file_explorer.place(x=win_ctr_x-222.5, y=win_ctr_y+7)

        #submit = tk.Button(self, text = "Submit", font=("Segoe UI Variable Text Semibold", 8), width = 10, height = 1, bg = "silver", cursor="hand2")
        #submit.place(x=win_ctr_x-50, y=win_ctr_y+50)
        
        
        submit_btn_normal = Image.open("Files\\submit_btn_normal.png")
        submit_btn_normal_resize = submit_btn_normal.resize((85,55))
        submit_btn_image_normal = ImageTk.PhotoImage(submit_btn_normal_resize, master=self)

        submit_btn_pressed = Image.open("Files\\submit_btn_pressed.png")
        submit_pressed_resize = submit_btn_pressed.resize((85,55))
        submit_pressed_image = ImageTk.PhotoImage(submit_pressed_resize, master=self)

        submit = self.c.create_image(win_ctr_x-5, win_ctr_y+62.5, image=submit_btn_image_normal, tags=["submit_normal_state", "submit_hover_state","submit_click_state"])
        
        
        def submit_hoverEvent(event):    
            self.c.config(cursor="hand2")        
            self.c.itemconfigure(submit, image=submit_btn_image_normal)
            
            print('entered hover state')
            
        def submit_normalState(event):    
            self.c.config(cursor="arrow")        
            self.c.itemconfigure(submit, image=submit_btn_image_normal)

        
        self.c.tag_bind("submit_hover_state", '<Enter>', submit_hoverEvent)

        self.c.tag_bind("submit_normal_state", '<Leave>', submit_normalState)
        
        
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
            inputfile1 = tk.filedialog.askopenfilename(initialdir = "Downloads", title = "Please Select a File to Transform",
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
                self.c.itemconfigure(submit, image=submit_pressed_image)
                #print(label_file_explorer.get("1.0", 'end-1c'))
                file1.set_file(label_file_explorer.get("1.0", 'end-1c'))
                #print(file1.get_file())
                #getFile(file1)
                #print("THIS IS THE SELECTED FILE: ", file1.get_file())
                formatFile(file1, label_file_explorer)
                
            except Exception as e: 
                #print("file not found error")
                #print(e)
                self.grab_release()
                traceback.print_exc()
                showError(label_file_explorer)
                
                    
                #open file and print to console to test functionality
           
        self.c.tag_bind("submit_click_state", '<Button-1>', lambda x: submitClick(inputfile.get_file()))   

        browse_normal = self.c.create_image(win_ctr_x+211, win_ctr_y+17.5, image=browse_button_image_normal, tags=["browse_normal_state", "browse_highlight_state","browse_click_state"])

        def onBrowseClick(event):
            fileExplore()

        def browse_normalState(event):
            self.c.config(cursor="arrow")
            self.c.itemconfigure(browse_normal, image=browse_button_image_normal)
            print('entered normal state')
       
        def browse_hoverEvent(event):    
            self.c.config(cursor="hand2")          
            self.c.itemconfigure(browse_normal, image=browse_button_image_hover)
            
            print('entered hover state')
            
        self.c.tag_bind("browse_click_state", '<Button-1>', onBrowseClick)        
        
        self.c.tag_bind("browse_highlight_state", '<Enter>', browse_hoverEvent)

        self.c.tag_bind("browse_normal_state", '<Leave>', browse_normalState)
        

        #fileBrowse = tk.Button(self, text = "Browse Files", bg = "silver",
        #                         command = lambda: (fileExplore()))
        
        #fileBrowse.place(x=485, y=175.5)
        
        
        # setting up the sort button
        #sorting = self.c.create_text(530, 225, text="Sorting Options", fill="white", font=("Arial 10"), width=200, tags=["sort", "normalSort","highlightSort"]) 
        
        sortPrompt = tk.Text(self, background = "dark gray", foreground = "black",
                                      width = 8, height = 2, font = ("Segoe UI Variable Text Semibold", 8))
        sortPrompt.insert("1.0", "Sorting" + "\n" + "Options", "center")
        sortPrompt.tag_configure("center", justify='center')
        sortPrompt.tag_add("center", 1.0, "end")
        
        programSortWindow = sortWindow()
        programSortWindow.grab_release()
        programSortWindow.withdraw()
        def showSortPrompt(event): 
            if 'withdrawn' == programSortWindow.state():
                programSortWindow.focus_set()
                programSortWindow.grab_set_global()
                programSortWindow.deiconify()
            elif 'normal' == self.state():
                programSortWindow.focus_set()
                programSortWindow.grab_set_global()
                programSortWindow.deiconify()
                
                
                
        sort_normal = self.c.create_image(win_ctr_x+212.5, win_ctr_y+60, image=sort_button_image_normal, tags=["sort_normal_state", "sort_highlight_state","sort_click_state"])

        def onSortClick(event):
            showSortPrompt(event)

        def sort_normalState(event):
            self.c.config(cursor="arrow")
            sortPrompt.place_forget()
            self.c.itemconfigure(sort_normal, image=sort_button_image_normal)
            print('entered normal state')
       
        def sort_hoverEvent(event): 
            self.c.config(cursor="hand2")  
            sortPrompt.place(x=win_ctr_x+235, y=win_ctr_y+30)         
            self.c.itemconfigure(sort_normal, image=sort_button_image_hover)
            
            print('entered hover state')
            
        self.c.tag_bind("sort_click_state", '<Button-1>', onSortClick)        
        
        self.c.tag_bind("sort_highlight_state", '<Enter>', sort_hoverEvent)

        self.c.tag_bind("sort_normal_state", '<Leave>', sort_normalState)
        

        
        
        # setting up the help button
        help = self.c.create_text(win_ctr_x+265, win_ctr_y+110, text="Help", fill="gray", font=("Segoe UI Variable Text Semibold", 10), width=30, tags=["help", "normal","highlight"]) 
        
        helpPrompt = tk.Text(self, background = "dark gray", foreground = "black",
                                      width = 10, height = 2, font = ("Segoe UI Variable Text Semibold", 7))
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
            helpPrompt.place(x=win_ctr_x+235, y=win_ctr_y+70)
            self.c.config(cursor="hand2")
            self.c.itemconfigure(help, fill="red")
            
        self.c.tag_bind("help", '<Button-1>', showHelp)        
        
        self.c.tag_bind("highlight", '<Enter>', highlightHelp)

        self.c.tag_bind("normal", '<Leave>', normalState)
        

        def onClose(event):
            welcome.deiconify()
            self.grab_release()
            self.withdraw()

        def normalState(event):
            self.c.config(cursor="arrow")
            self.c.itemconfigure(home_normal, image=home_button_image_normal)
            print('entered normal state')
       
        def hoverEvent(event):   
            self.c.config(cursor="hand2")         
            self.c.itemconfigure(home_normal, image=home_button_image_hover)
            
            print('entered hover state')
            
        self.c.tag_bind("click_state", '<Button-1>', onClose)        
        
        self.c.tag_bind("highlight_state", '<Enter>', hoverEvent)

        self.c.tag_bind("normal_state", '<Leave>', normalState)


        self.protocol("WM_DELETE_WINDOW", lambda: onClose(None))

#tk.ttk.Separator(window, orient=tk.VERTICAL).place(x=305, y=0, height=300)

def launchPURCH():
    purch_gui = purchWindow()
    purch_gui.mainloop()