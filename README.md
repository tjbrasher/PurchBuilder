NOTE:  If you are experiencing issues with converting a csv file into a purchasing list, please check all fields for any foreign characters or symbols. These will need to be removed in order for the program to properly read and write the files.

     

Program Brief
- The purpose of this program is to read purchasing files generated from JetBuilt and clean, reformat and sort the data into the same format used in the PURCH lists that are used by the EAVI purchasing department.


Instructions:

- Upon launching the program, press the “Browse Files” button and select the file that you would like to convert to a PURCH list.
- Note that the program is designed to work with files generated via the Purchasing tab on JetBuilt
- Once a file has been selected, click on “Sorting Options” and select the desired sorting options and press “Done”.
- If no options are selected, the program will not sort the data and the order of the data in the file that will be output by the program will match the order of the data in the file selected by the user.
- Refer to the “Sorting Options” section under Program Components for more information on this topic.
- Once the file has been selected and any desired sorting options have been chosen, press “Submit”.
- If the file can be processed, a save file dialog should appear. Select the desired location to save the file and rename the file if desired and press “Save”.
- If the file cannot be processed, an error message will appear.
- If this occurs, confirm the file type and open the selected file outside of the program to confirm that there are no formatting issues within the document. Correct any issues and try again.
- Upon a successful save, the file will display a prompt asking if the user would like to continue the program. Select “Yes” to process another file or select “No” to terminate and close the program.


Program Components
Main Window
- Upon launching the program you will be presented with a window that has a file explorer (comprised of the text box and the “Browse” buttons), a “Submit” button, a “Sort Options” selection, and a “Help” selection. The main window launches in the center of the screen and cannot be resized. However, the window can still be minimized or the program can be closed by pressing the “X” in the top right corner of the window. 
File Explorer (File Text Box and Browse Files Button): 
The file explorer is how files are loaded into the program.
To select a file, press the “Browse” button and a file explorer window will open allowing you to find the appropriate file to load into the program. Once the file has been selected press the “Open” button and you will see the file name has been loaded into the text box, indicating that the file has loaded. Note that this program was designed to work only with txt files, csv files, and appropriately formatted Microsoft Excel files.
Sorting Options:
Sorting Options refers to the ways in which the items in the new PURCH list can be organized. 
Once the file has been loaded, you can select how you would like the information to be sorted when the file is formatted and the PURCH list is created. Sorting options include sorting by “Source”, “Item”, “Cost” and “Order Status”. 
Multiple sorting options can be selected but the sorting order will always occur in the order in which the options are listed (i.e; sorted by “Source” first, “Item” second, “Cost” third, and “Order Status” last assuming all sort options are selected. If not all options are selected, sorting will only apply to the options that have been chosen by the user).
By default, No sorting options are applied to the file meaning that the order of the items remains the same as it is in the original file.
Submit:
The submit button will take the file that the user selected along with the selected sorting options and output a cleaned and reformatted file and save the file based on the location the user has designated.
Upon pressing the “Submit” button one of two things will happen:
If the file is valid, the program will display a “Save As” file dialog and the user will be prompted to save the file to a location of their choosing. This dialog is also where the user will have the option to rename their file before they save it if desired.
Upon a successful save, the program will ask the user if they would like to process another file.
Selecting “Yes” resets the file explorer and allows the user to continue the process
Selecting “No” will terminate and close the program
If the file is not valid, an error message will appear notifying the user that the request could not be processed. The user will not be able to proceed until this message has been cleared by pressing the “Okay” button.
Help:
Selecting the help option will display this Read_Me file in order to provide guidance to the user about the operation of the program as well as notes on known issues and troubleshooting help.




Source Code Composition
The program consists of five (5) separate Python modules; four (4) for the different GUI windows utilized within the program and a separate single file that handles the data cleaning, formatting and saving of the new, reformatted file.



purchGUI - (Main User Interface Window for the Program)

- This is the file for the main window that the user will interact with and is the first window that will appear upon launching the program.
- Within this window there is a file explorer for selecting the file to be converted as well as a “submit” button, a “sorting options” selection and a “help” selection. Each of these opens separate dialogs and windows that the user can interact with.



SortingOptions - (Allows the user to select how they want the file to be sorted)

- This file provides the framework to construct the interface by which the user will select how they want the PURCH list items to be sorted.
- Users are able to select multiple buttons and their selections are stored within the Data_Cleaning_wPandas_Purch file where the main logic of the program is executed. If all buttons are unselected or no selection is made, the program defaults to no sorting.



filePrompt - (Displays when the program has successfully formatted and saved a file)

- This file provides the framework for the prompt that asks the user if they would like to process another file.
- If “Yes” is selected, the dialog closes, the file explorer resets and the user can process another file. If “No” is selected, the dialog closes and the program terminates, closing all windows.



ErrorTest - (Displays when the program has encountered an error)

- This file provides the framework for the window that display whenever the program encounters an error.
- This window is trigged through exception handling within all files so if an error occurs in any part of the program, the error window should display and the user will be able to close the dialog and continue the program


Data_Cleaning_wPandas_Purch - (Performs the majority of the logic for the program including cleaning, formatting, and saving the files)

- This file is where the main logic of the program is executed.
- Upon hitting the “Submit” button on the purchGUI window, the file name and location that was selected by the user is retrieved from the file explorer and opened within this file. It is then, cleaned, formatted and sorted as needed.
- Upon successful formatting, the program presents a save file dialog to the user where the location and name of the new file can be entered. Upon pressing “Save”, the filePrompt file will open to ask the user to continue the program. However, if the save file dialog window is closed before saving the file, the file will not be saved. 

