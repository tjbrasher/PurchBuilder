import tkinter as tk
import pandas as pd


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
        #error = ErrorWindow()
        #error.mainloop()  
        
