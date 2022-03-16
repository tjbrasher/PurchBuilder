import pandas as pd
import tkinter as tk


class ErrorWindow(tk.Tk):

    def __init__(self):
        super().__init__()

        self.c = tk.Canvas(self, bg="black", width = 300, height = 150)
        self.c.pack()
        self.background_image = ImageTk.PhotoImage(file = "Files\\background.png")
        self.c.create_image(10, 10, image = self.background_image, anchor = NW)

        # setting and positioning the logo header
        self.logo = Image.open("Files\\Logos\\EAlogoHorizonalNobg.png")
        self.logo_resize = self.logo.resize((359,72))
        self.logo_header = ImageTk.PhotoImage(self.logo_resize)
        self.c.create_image(310,35, image = self.logo_header, anchor = N)

        # initial window setup
        self.rowconfigure(3, {'minsize': 40})
        self.columnconfigure(3, {'minsize': 40})
        self.title("PURCH List Creator")

        # window sizing and positioning
        window_width = 620
        window_height = 300
        scr_width = self.winfo_screenwidth()
        scr_height = self.winfo_screenheight()

        ctr_x = int(scr_width/2 - window_width/2)
        ctr_y = int(scr_height/2 - window_height/2)

        self.geometry(f'{window_width}x{window_height}+{ctr_x}+{ctr_y}')
        self.resizable(False, False)


        # setting and positiong the prompt
        self.c.create_text(307.5, 142.5, text="Please Select an Equipment List to Use for Creating PURCH List", fill = "white", font=("Arial 12 bold"))

        label_file_explorer = tk.Text(self, background = "light grey", foreground = "black",
                            width = 57, height = 1, font = ("Helvetica", 10))
        label_file_explorer.insert("1.0", "....")
        label_file_explorer.place(x=57.5, y=179)

        submit = tk.Button(self, text = "Submit", width = 10, height = 1)
        submit.place(x=265, y=225)

        
file1 = fileObject()


def getFile(file1):
        
    print(file1._file)

    #print("THIS IS YOUR FILE NAME: ", file1.get_file)
    #print("THIS MAY ALSO BE THE FILE NAME: ", fileSelect.fileObject.get_file(fileSelect.file1))
    #print("IS THIS THE FILE NAME? ", str(file.get_file))

    pd.set_option('display.max_columns', None)

    # Import the dataset
    #pick_list = pd.read_csv(r"C:\Users\travi\Downloads\Worship Center Changes_pick_list.csv")
    #pick_list = pd.read_csv(r"Files\Worship Center Changes_pick_list.csv")



def formatFile(file1):
    try:
            
        pick_list = pd.read_csv(file1._file)
        
        print("THIS IS YOUR FILE NAME: ", file1.get_file)
        print("THIS IS YOUR FILE NAME: ", file1._file)
        
        # Removed unnecessary columns from the dataset
        pick_list = pick_list.drop(
            columns=['Project Name', 'Client', 'Order Quantity'],
            axis=1
            )

        # Conditionally remove unncessary rows from the dataset
        word= ("EAVI")
        items= pick_list[ pick_list.Item.str.contains(word)].index
        pick_list.drop(items, inplace = True)

        # Re-order and add new columns to the dataset
        columns=['Project ID', 'PO Number', 'Date Ordered', 'Tracking Date', 
                'B\O Lead Time', 'Received Date', 'Warehouse Location', 'Notes',
                'Project Quantity', 'Source', 'Item', 'Description', 'Cost', 
                'Cost Extended', 'Status']

        pick_list = pick_list.reindex(columns, axis = 1)

        # Print the data set and the list of column names
        print(pick_list)
        print(pick_list.columns.values)

        # Get input from the user to name the file
        #title = saveAs(file1)

        #print(title)

        # Export the file
        #pick_list.to_csv(title+".csv", index=False)
        
        def saveAs(file1):
            saveAs = tk.filedialog.asksaveasfile(initialfile=file1._file, defaultextension=".csv", title = "Please select a location to save your file",
                                                filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))
            pick_list.to_csv(saveAs, index=False, line_terminator="\n")
            
        saveAs(file1)

        
        
    except:
        print("The process could not be completed. Please try selecting a different file.")
        error = ErrorWindow()
        error.mainloop()  
        
