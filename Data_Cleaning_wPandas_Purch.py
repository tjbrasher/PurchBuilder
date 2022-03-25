from ast import While
import tkinter as tk
import traceback
import pandas as pd
from ErrorTest import showError
from filePrompt import showPrompt

#import chardet

class button():
        
    def __init__(self, state=None):
        self._state = state
            
    def setBtnStatus(self, btState):
        if btState == 0:
            print(self, " selected = False", btState)
        else:
            print(self, " selected = True ", btState)
    
    def getBtnStatus(self):
        return self._state
    
bt1 = button()
bt2 = button()
bt3 = button()
bt4 = button()
bt5 = button()

# var = function that retrieve button state from sortingOptions
def bt1State(b1State):
    bt1 = b1State
    return bt1

def bt2State(b2State):
    bt2 = b2State
    return bt2

def bt3State(b3State):
    bt3 = b3State
    return bt3

def bt4State(b4State):
    bt4 = b4State
    return bt4

def bt5State(b5State):
    bt5 = b5State
    return bt5


def getBtnSelection(bt2, bt3, bt4, bt5):
    btSelected = bt2 + bt3 + bt4 + bt5
    print("button selection = ", btSelected)
    return btSelected

def printSortList():

    sortList=[]
    bt1.getBtnStatus()
    rb2State = bt2State()
    rb3State = bt3State()
    rb4State = bt4State()
    rb5State = bt5State()
    
    
    if rb2State == 1:
        sortList.append("Source")
    else:
        pass
    
    if rb3State == 1:
        sortList.append("Item")
    else:
        pass
    
    if rb4State == 1:
        sortList.append("Cost")
    else:
        pass
    
    if rb5State == 1:
        sortList.append("Status")
    else:
        pass
    
    if rb1State == 1:
        sortList.clear()
    else:
        pass
    
    print(sortList) 


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
            
                       
           
           
            #if sort by "items":
            #pickList = pickList.sort_values(sortList)

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
                pass
            else:
                showPrompt(label_file_explorer)          
                print("File Saved!")
                break
        

        
        
        except Exception as e:
            print(e)
            traceback.print_exc()
            showError(label_file_explorer)
            break
        