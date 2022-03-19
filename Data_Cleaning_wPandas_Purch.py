import tkinter as tk
import traceback
import pandas as pd
from ErrorTest import showError
from filePrompt import showPrompt
import chardet

 

class programError(Exception):
    def printError():
        print("File Could Not Be Saved!")    
            

def getFile(file1):
        
    print(file1._file)

    #print("THIS IS YOUR FILE NAME: ", file1.get_file)
    #print("THIS MAY ALSO BE THE FILE NAME: ", fileSelect.fileObject.get_file(fileSelect.file1))
    #print("IS THIS THE FILE NAME? ", str(file.get_file))

    

    # Import the dataset
    #pick_list = pd.read_csv(r"C:\Users\travi\Downloads\Worship Center Changes_pick_list.csv")
    #pick_list = pd.read_csv(r"Files\Worship Center Changes_pick_list.csv")


def formatFile(file1, label_file_explorer):
    
    
    pd.set_option('display.max_columns', None)
    
    pickList = pd.read_csv(file1._file)
    #pickList = pickList.read_csv(pickList,)
    print("THIS IS THE CLEANED FILE COLUMNS: ", pickList.columns.values)
    print(pickList)
    
        
    while True:
        try:

            print("THIS IS YOUR FILE NAME: ", file1.get_file)
            print("THIS IS YOUR FILE NAME: ", file1._file)
            
            # Removed unnecessary columns from the dataset
            pickList = pickList.drop(
                columns=['Project Name', 'Client', 'Order Quantity'],
                axis=1
                )

            # Conditionally remove unncessary rows from the dataset
            word= ("EAVI")
            items= pickList[pickList.Item.str.contains(word)].index
            pickList.drop(items, inplace = True)

            # Re-order and add new columns to the dataset
            columns=['Project ID', 'PO Number', 'Date Ordered', 'Tracking Date', 
                    'B\O Lead Time', 'Received Date', 'Warehouse Location', 'Notes',
                    'Project Quantity', 'Source', 'Item', 'Description', 'Cost', 
                    'Cost Extended', 'Status']

            pickList = pickList.reindex(columns, axis = 1)

            # Print the data set and the list of column names
            #print(pick_list)
            print(pickList.columns.values)

            # Get input from the user to name the file
            #title = saveAs(file1)

            #print(title)

            # Export the file
            print("Your list: ", pickList)  
        
            def saveAs(pickList):
                saveAs = tk.filedialog.asksaveasfile(initialfile=file1._file, defaultextension=".csv", title = "Please select a location to save your file",
                                                    filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                   ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))
                pickList.to_csv(saveAs, index=False, line_terminator="\n")
            
            #pickList.to_csv(saveAs(pickList), index=False, line_terminator="\n", encoding="utf-8")
            
            saveAs(pickList)

            if saveAs == "":
                break
            else:
                showPrompt(label_file_explorer)          
                print("File Saved!")
                break

        
        
        except Exception as e:
            print(e)
            traceback.print_exc()
            showError(label_file_explorer)
            break