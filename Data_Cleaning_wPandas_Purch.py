import tkinter as tk
from tkinter.filedialog import SaveAs
import traceback
import pandas as pd
from ErrorTest import showError
from filePrompt import showPrompt
from xlsxwriter.utility import xl_rowcol_to_cell
import xlsxwriter
import os
import win32com.client as win32
from win32com.client import Dispatch
from datetime import date
from pathlib import Path


class button():
        
    def __init__(self, state=None):
        self._state = state
            
    def setBtnStatus(self, btState):
        if btState == 0:
            self._state = 0
            #print(self, " selected = False", btState)
        else:
            self._state = btState
            #print(self, " selected = True ", btState)
    
    def getBtnStatus(self):
        return self._state
   
#initializing button objects for setting and getting values    
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


#setting initial/default button status
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


#getting number of selected buttons
def getBtnSelection(bt2Var, bt3Var, bt4Var, bt5Var):
    btSelected = bt2Var + bt3Var + bt4Var + bt5Var
    #print("button selection = ", btSelected)
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
    
    return sortList
    
    
class programError(Exception):
    def printError():
        print("File Could Not Be Saved!")    
            

def getFile(file1):
    
    #print file name to console    
    #print(file1._file)
    return file1._file


def formatFile(file1, label_file_explorer):
    
    #setting up dataframe and reading file into dataframe
    pd.set_option('display.max_columns', None)
    pickList = pd.read_csv(file1._file)
    
        
    while True:
        try:            
            # Removed unnecessary columns from the dataset
            pickList = pickList.drop(
                columns=['Project Name', 'Client', 'Order Quantity'],
                axis=1
                )


            # Conditionally remove unncessary rows from the dataset
            word= ("EAVI")
            items= pickList[pickList.Item.str.contains(word)].index
            pickList.drop(items, inplace = True)


            #formatting data in 'Cost' column to allow proper sorting
            pickList['Cost'] = pickList['Cost'].map(lambda x: x.lstrip('$'))
            pickList['Cost'] = (pickList['Cost'].str.split()).apply(lambda x: float(x[0].replace(',','')))
            
            
            #setting 'Cost' column to type float
            pickList.Cost = pickList.Cost.astype(float)


            #printing types of dataframe columns
            #types = pickList.dtypes
            #print(types)
           
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
            #print(pickList.columns.values)
            
            def get_fileName():
                print('file is: ', file1._file[:-4])
                #file_name = [re.sub(r'^.*?/', '',str) for c in file1._file]
                #print(file_name)
            
            get_fileName()
            
            project_number = pickList.iloc[2]['Project ID']

            current_date = date.today()
            current_date_string = str(current_date)

            file_path = Path(file1._file)
            file_name = file_path.with_suffix('')
            file_name = os.path.basename(str(file_name))
            
            file_name = file_name.replace("_pick_list", "")
            
            file_name = project_number + "_" + file_name + '_' + current_date_string + '_PURCH'

            #print('filename is: ',project_number + "_" + file_name[:-4] + '_' + current_date_string + '_PURCH')
            


            # Export the file
            #print("Your list: ", pickList)  
            
            def directory_initial():
                try:
                    directory = "X:\Projects ACTIVE"
                    return directory
                except:
                    directory = "/Downloads"


            def saveAs(pickList):
                saveAs = tk.filedialog.asksaveasfilename(initialdir = directory_initial(),
                                                         initialfile = file_name,
                                                         defaultextension=".xlsx",
                                                         title = "Please select a location to save your file",
                                                    filetypes = (("Microsoft Excel Files (*.xls, *.xlsx, *.xlsm)", "*.xlsx*"), ("Comma Separated Values (*.csv)", "*.csv*"),
                                                                 ("Text Files (*.txt)", "*.txt*"), ("All Files", "*.*")))
                
                if saveAs:
                    #pickList.to_csv(saveAs, index=False, line_terminator="\n")
                    #print(file1._file)
                    writer = pd.ExcelWriter(saveAs, engine='xlsxwriter')
                    pickList.to_excel(writer, sheet_name="PURCH", index=False)
                    purchList = writer.book
                    #saveAs_xlsm = purchList.filename = saveAs[-1]+"m"
                    #print("new file name: ", saveAs_xlsm)
                    #purchList.add_vba_project('Files/read_only_VBA.xlsm./vbaProject.bin')
                    purchSheet = writer.sheets['PURCH']
                    borderFormat = purchList.add_format({'border': 1})
                    headerFormat = purchList.add_format({
                        'font_color': 'white',
                        'bg_color': '#800000',
                        'bold': True,
                        'border': 1,
                        'text_wrap': True})
                    
                    
                    #getting number of total rows and columns
                    col_num = pickList.shape[1]
                    row_num = len(pickList)
                    row_num1 = row_num+2
                    
                    
                    #getting first and last cell position for setting borders
                    last_col_cell = xl_rowcol_to_cell(row_num, col_num-1)
                    second_cell = xl_rowcol_to_cell(1,1)
                    
                    for col_num, value in enumerate(pickList.columns.values):
                            purchSheet.write(0, col_num, value, headerFormat) 
                            col_num+1 
  
                    
                    # Setting column widths
                    purchSheet.set_column(0, 0, 9)
                    purchSheet.set_column(0, 5, 9)
                    purchSheet.set_column(6, 6, 12)
                    purchSheet.set_column(7, 7, 33)
                    purchSheet.set_column(8, 8, 11)
                    purchSheet.set_column(9, 9, 25)
                    purchSheet.set_column(10, 11, 40)
                    purchSheet.set_column(12, 12, 12)
                    purchSheet.set_column(13, 13, 16)
                    purchSheet.set_column(14, 14, 14)
                    

                    
                    #setting borders on cells                  
                    purchSheet.conditional_format(second_cell+':'+ last_col_cell, {'type': 'blanks',
                                                                          'format': borderFormat})
                    purchSheet.conditional_format(second_cell+':'+ last_col_cell, {'type': 'no_blanks',
                                                                          'format': borderFormat})
                    
                    
                    #initializing conditional formatting options
                    bg_green = purchList.add_format({'bg_color': '#92D050'})
                    bg_yellow = purchList.add_format({'bg_color': '#FFFF00'})
                    


                    # Setting conditional formatting (green if ready to order, yellow if not ready;
                    # (purple if in stock - later implementation))             
                    def check_status(i):
                        #print('rows = ', row_num)
                        cols = [8, 9, 10, 11]
                        for i in range(1, row_num1):
                            status = pickList['Status'].values[i-2]
                            purchSheet.set_row(i, 19.5)

                            #print('i=', i)
                            #print(status)


                                                        
                            if i==0:
                                pass
                            
                            if status == "Ready To Order":
                                #print("item is ready to order")
                                i = i-1
                                if i==0:
                                    pass
                                else:
                                    for c in cols:
                                        try:
                                            cell_value = pickList.iloc[i-1][c]
                                            try:
                                                purchSheet.write(i, c, cell_value, bg_green)
                                            except:
                                                purchSheet.write(i, c, '', bg_green)
                                        except:
                                            pass

                                    #purchSheet.conditional_format(i, 8, i, 11, 
                                    #                                            {'type':     'no_blanks',
                                    #                                            'format':    bg_green})
                                    #purchSheet.conditional_format(i, 8, i, 11, 
                                    #                                            {'type':     'blanks',
                                    #                                            'format':    bg_green})
                                                    
                            elif status == 'Not Ordered':
                                #print('item is not ready to order')
                                i= i-1
                                if i==0:
                                    pass
                                else:
                                    for c in cols:
                                        try:
                                            cell_value = pickList.iloc[i-1][c]
                                            try:
                                                purchSheet.write(i, c, cell_value, bg_yellow)
                                            except:
                                                purchSheet.write(i, c, '', bg_yellow)
                                        except:
                                            pass
                                    
                            #print('end of loop')
                            i = i+1
                            
                    i=0
                    check_status(i)
                    

                    #applying filters to column headers
                    purchSheet.autofilter(0, 0, 0, col_num)
                  

                    #setting file to open read only
                    #def set_password():
                        
                        #excel = win32.gencache.EnsureDispatch('Excel.Application')
                        #wb = excel.Workbooks.Open(saveAs)
                        
                        #wb.SaveAs()

                    #    if os.path.exists(saveAs):
                    #        xl = Dispatch("Excel.Application")
                    #        wb = xl.Workbooks.Add(saveAs)
                            
                    #        saveAs = saveAs[-1]+"m"
                    #        print("new file name = ", saveAs)
                            
                    #        wb.SaveAs(saveAs[-1]+"m", FileFormat = 52)
                    #        xl.Quit()
                            
                    #        xl=win32.Dispatch("Excel.Application")
                    #        xl.Workbooks.Open(os.path.abspath(saveAs), ReadOnly=1)
                    #        xl.Application.Run("C:\\Users\\tbrasher\\Documents\\GitHub\\DataCleaningProjects\\Files\\read_only_VBA.xlsm!Module1")
                        
                    #    del xl

                    
                    #saving file to user specified location
                    writer.save()

                    #set_password()
                   
                                     
                    showPrompt(label_file_explorer)          
                    #print("File Saved!")
                else:
                    pass
                
            
            saveAs(pickList)  
            break      
                
        
        except Exception as e:
            #print(e)
            traceback.print_exc()
            showError(label_file_explorer)
            break
        