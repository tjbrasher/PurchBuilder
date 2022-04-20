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

def jbirFormat():
    
    pd.set_option('display.max_columns', None)
    #jbir_init = pd.read_csv(file1._file)
    jbir_init = pd.read_csv("C:/Users/tbrasher/Downloads/Office AV System.csv")

    try:
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
        #print(str(column_names))
        
        jbir_rev1 = jbir_rev1.rename(column_names, axis = 1)

                
        # reordering columns
        def df_column_switch(jbir_rev1, c1, c2):
            col_list = list(jbir_rev1)
            col_list[c1], col_list[c2] = col_list[c2], col_list[c1]
            jbir_rev1.columns = col_list        


        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Owner Furnished"),
                         jbir_rev1.columns.get_loc("Short Description"))
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Prewire Hours"), 8)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Trim Hours"), 9)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Finish Hours"), 10)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Shop Hours"), 11)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Travel Hours"), 12)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("ICO Shop Hours"), 13)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("ICO Trim Hours"), 14)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("PM Hours"), 15)
        df_column_switch(jbir_rev1, jbir_rev1.columns.get_loc("Programming Hours"), 16)
        
        
        # setting column widths
        jbir_rev1.style.set_properties(subset=['Room', 'System', 'Manufacturer', 'Model'],
                                       **{'width': '215px'})
        
        #print("jbir1 revised columns= ", jbir_rev1.columns)
        
        
        
        
        jbir_rev1.to_csv("jbir1.csv", index=False, line_terminator="\n")

        
    except Exception as e:
            #print(e)
            traceback.print_exc()
            #showError(label_file_explorer)

            
jbirFormat()
exit()
