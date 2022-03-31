from ast import While
import tkinter as tk
import traceback
import pandas as pd
from ErrorTest import showError
from filePrompt import showPrompt
import xlsxwriter

#import chardet

class button():
        
    def __init__(self, state=None):
        self._state = state
            
    def setBtnStatus(self, btState):
        if btState == 0:
            self._state = 0
            print(self, " selected = False", btState)
        else:
            self._state = btState
            print(self, " selected = True ", btState)
    
    def getBtnStatus(self):
        return self._state
    
button1 = button()
button2 = button()
button3 = button()
button4 = button()
button5 = button()

def setInitialStatus():
    button1.setBtnStatus(1)
    button2.setBtnStatus(0)
    button3.setBtnStatus(0)
    button4.setBtnStatus(0)
    button5.setBtnStatus(0)

if button1.getBtnStatus() == None:
    setInitialStatus()
    
elif button2.getBtnStatus() == None:
    setInitialStatus()

elif button3.getBtnStatus() == None:
    setInitialStatus()

elif button4.getBtnStatus() == None:
    setInitialStatus()

elif button5.getBtnStatus() == None:
    setInitialStatus()



# var = function that retrieve button state from sortingOptions
def bt1State():
    bt1Var = button1.getBtnStatus()
    return bt1Var

def bt2State():
    bt2Var = button2.getBtnStatus()
    return bt2Var

def bt3State():
    bt3Var = button3.getBtnStatus()
    return bt3Var

def bt4State():
    bt4Var = button4.getBtnStatus()
    return bt4Var

def bt5State():
    bt5Var = button5.getBtnStatus()
    return bt5Var


def getBtnSelection(bt2Var, bt3Var, bt4Var, bt5Var):
    btSelected = bt2Var + bt3Var + bt4Var + bt5Var
    print("button selection = ", btSelected)
    return btSelected

def SortList():

    sortList=[]
    rb1State = bt1State()
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
    
    return sortList
    
    
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

            pickList['Cost'] = pickList['Cost'].map(lambda x: x.lstrip('$'))
            pickList['Cost'] = (pickList['Cost'].str.split()).apply(lambda x: float(x[0].replace(',','')))
            
            pickList.Cost = pickList.Cost.astype(float)

            types = pickList.dtypes

            print(types)
           
            #if sort by "items":
            pickList = pickList.sort_values(SortList())

            pickList['Cost'] = pickList['Cost'].apply(lambda x: "${:.2f}".format((x/1)))

            
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
            
            str_df = pickList.stack().str.decode('utf-8').unstack()
            
            for col in str_df:
                pickList[col] = str_df[col]
        
            def saveAs(pickList):
                saveAs = tk.filedialog.asksaveasfile(initialfile=file1._file, defaultextension=".xlsx", title = "Please select a location to save your file",
                                                    filetypes = (("Comma Separated Values (*.csv)", "*.csv*"), ("Text Files (*.txt)", "*.txt*"),
                                                   ("Microsoft Excel Files (*.xls, *.xlsx)", ".xlsx"), ("All Files", "*.*")))

                file1._file.set_file(saveAs)
                
                if saveAs:
                    #pickList.to_csv(saveAs, index=False, line_terminator="\n")
                    writer = pd.ExcelWriter(file1._file, engine='xlsxwriter')
                    pickList.to_excel(writer, sheet_name="PURCH", encoding = 'utf-8', startrow=0, index=False)
                    writer.save()
                    showPrompt(label_file_explorer)          
                    print("File Saved!")
                else:
                    pass
                    

            #pickList.to_csv(saveAs(pickList), index=False, line_terminator="\n", encoding="utf-8")
            
            saveAs(pickList)  
            break      
                
        
        except Exception as e:
            print(e)
            traceback.print_exc()
            showError(label_file_explorer)
            break
        