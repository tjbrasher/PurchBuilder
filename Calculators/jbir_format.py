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

class programError(Exception):
    def printError():
        print("File Could Not Be Saved!")    
            

def getFile(file1):
    
    #print file name to console    
    #print(file1._file)
    return file1._file

def jbirFormat(file1, label_file_explorer):
    
    pd.set_option('display.max_columns', None)
    #jbir_init = pd.read_csv(file1._file)
    jbir_init = pd.read_csv(file1._file)

    while True:
        try:
            
            project_number = jbir_init.iloc[2]['Project']
            
            #list of columns to keep for JBIR                
            jbir_columns = ["Room", "System", "Tag", "Quantity", "Manufacturer",
                            "Model", "Owner Furnished", "Short Description",
                            "ICO Shop Minutes Ext", "ICO Trim Minutes Ext",
                            "Shop Minutes Ext", "Trim Minutes Ext", "Travel Minutes Ext",
                            "Prewire Minutes Ext", "Finish Minutes Ext",
                            "Project Management Minutes Ext", "Programming Minutes Ext"]
            
            
            #removing unnecessary columns from df
            for c in jbir_init.columns:   
                jbir_rev1 = jbir_init.filter(items=jbir_columns, axis=1)

            
            #new column names    
            new_jbir_cols = ["Room", "System", "Tag", "Quantity", "Manufacturer",
                            "Model", "Owner Furnished", "Short Description",
                            "ICO Shop Hours", "ICO Trim Hours", "Shop Hours",
                            "Trim Hours", "Travel Hours", "Prewire Hours",
                            "Finish Hours", "PM Hours", "Programming Hours"]
            
            
            # renaming columns
            column_names = {}
            for key in jbir_columns:
                for value in new_jbir_cols:
                    column_names[key] = value
                    new_jbir_cols.remove(value)
                    break        
            jbir_rev1 = jbir_rev1.rename(column_names, axis = 1)

            
            # reordering columns
            def df_column_switch(df, c1, c2):
                col_list = list(df.columns)
                col_list[c2], col_list[c1] = col_list[c1], col_list[c2]
                df = df[col_list]
                return df 

            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Owner Furnished"),
                                        jbir_rev1.columns.get_loc("Short Description"))
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Prewire Hours"), 8)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Trim Hours"), 9)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Finish Hours"), 10)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Shop Hours"), 11)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Travel Hours"), 12)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("ICO Shop Hours"), 13)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("ICO Trim Hours"), 14)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("PM Hours"), 15)
            jbir_rev1 = df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Programming Hours"), 16)
            
            
            #dropping unnecessary rows
            jbir_rev1 = jbir_rev1[jbir_rev1["Short Description"].str.contains("Shipping|Prepaid Design Fee|System Design Services|Misc. Hardware") ==False]
            
            
            #dividing cells by 60 to get hours instead of minutes
            hour_cells = jbir_rev1.iloc[0:, 8:]
            jbir_rev1.iloc[0:, 8:] = hour_cells/60
            

            #print("jbir1 revised columns= ", jbir_rev1.columns)
            sortList = ["Room", "System", "Manufacturer", "Model"]
            jbir_rev1 = jbir_rev1.sort_values(sortList)
            
            
            def get_fileName():
                print('file is: ', file1._file[:-4])
                #file_name = [re.sub(r'^.*?/', '',str) for c in file1._file]
                #print(file_name)
            
            get_fileName()
            
    

            current_date = date.today()
            current_date_string = str(current_date)

            file_path = Path(file1._file)
            file_name = file_path.with_suffix('')
            file_name = os.path.basename(str(file_name))
            
            file_name = file_name.replace(file_name, "")
            
            file_name = project_number + "_" + file_name + '_' + current_date_string + '_JBIR'
                
            
            
            def directory_initial():
                try:
                    directory = "X:\Projects ACTIVE"
                    return directory
                except:
                    directory = "/Downloads"

            
            def saveAs(jbir_rev1):
                saveAs = tk.filedialog.asksaveasfilename(initialdir = directory_initial(),
                                                            initialfile = file_name,
                                                            defaultextension=".xlsx",
                                                            title = "Please select a location to save your file",
                                                    filetypes = (("Microsoft Excel Files (*.xls, *.xlsx, *.xlsm)", "*.xlsx*"), ("Comma Separated Values (*.csv)", "*.csv*"),
                                                                    ("Text Files (*.txt)", "*.txt*"), ("All Files", "*.*")))
                
                if saveAs:
                    writer = pd.ExcelWriter(saveAs, engine='xlsxwriter')
                    jbir_rev1.to_excel(writer, sheet_name="JBIR", float_format = "%0.1f", index=False)
                    JBIR = writer.book
                    jbir_sheet = writer.sheets['JBIR']
                    borderFormat = JBIR.add_format({'border': 1})
                    headerFormat = JBIR.add_format({
                                    'bold': True,
                                    #'border': 1,
                                    'text_wrap': True})

                    #setting column and row number variables
                    col_num = jbir_rev1.shape[1]    
                    row_num = len(jbir_rev1)
                    
                    #setting first and last cell variables for formatting
                    last_col_cell = xl_rowcol_to_cell(row_num, col_num-1)
                    first_cell = xl_rowcol_to_cell(0,0) 

                    
                    #formatting column headers
                    for col_num, value in enumerate(jbir_rev1.columns.values):
                        jbir_sheet.write(0, col_num, value, headerFormat) 
                        
                    jbir_sheet.autofilter(0, 0, 0, col_num)
                                
                    jbir_sheet.freeze_panes(1, 0)
                    
                    
                    # Setting column widths
                    jbir_sheet.set_column(0, 1, 16)
                    jbir_sheet.set_column(2, 2, 8)
                    jbir_sheet.set_column(3, 3, 11)
                    jbir_sheet.set_column(4, 5, 22)
                    jbir_sheet.set_column(6, 6, 32)
                    jbir_sheet.set_column(7, 7, 12)
                    jbir_sheet.set_column(8, 14, 8.5)
                    jbir_sheet.set_column(15, 15, 8)
                    jbir_sheet.set_column(16, 16, 12.5)
                    
                    
                    #setting borders on cells                  
                    jbir_sheet.conditional_format(first_cell+':'+ last_col_cell, {'type': 'blanks',
                                                                            'format': borderFormat})
                    jbir_sheet.conditional_format(first_cell+':'+ last_col_cell, {'type': 'no_blanks',
                                                                            'format': borderFormat})

                    
                    #setting subtotals below labor columns
                    lcn=8
                    for lcn in range(8, 17):
                        col_letter = xlsxwriter.utility.xl_col_to_name(lcn)
                        subtotal_function = f'=SUBTOTAL(9,'+str(col_letter)+'2:'+ str(col_letter)+str(row_num+1)+')'
                        jbir_sheet.write(row_num+1, lcn, subtotal_function)
                        lcn = lcn+1
                                    
                    jbir_sheet.write(row_num+1, 7, "Total")
                    
                    
                    #placing borders around total cells
                    first_total_cell = xl_rowcol_to_cell(row_num+1, 7)
                    last_total_cell = xl_rowcol_to_cell(row_num+1, 16) 
                            
                    jbir_sheet.conditional_format(first_total_cell+':'+ last_total_cell,
                                                {'type': 'no_blanks',
                                                'format': borderFormat})
                    
                    #print(jbir_rev1)
                    
                    
                            
                    jbir_rev1.to_csv("jbir1.csv", index=False, line_terminator="\n")
                    writer.save()
                    
                    showPrompt(label_file_explorer)          
                    print("File Saved!")
                
                else:
                    print('cannot save file')
                    pass
                
            
            saveAs(jbir_rev1)  
            break      

        
        except Exception as e:
                #print(e)
                traceback.print_exc()
                showError(label_file_explorer)

            
