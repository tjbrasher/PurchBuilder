import pandas as pd

pd.set_option('display.max_columns', None)
# Import the dataset
pick_list = pd.read_csv(r"C:\Users\travi\Downloads\Worship Center Changes_pick_list.csv")

# Removed unnecessary columns from the dataset
pick_list = pick_list.drop(
    columns=['Project Name', 'Client', 'Order Quantity'],
    axis=1
    )

# Conditionally remove unncessary rows from the dataset
i=0
for i, row in pick_list.iterrows():
    if pick_list[pick_list['Item'].apply(lambda x: "EAVI" not in x)]:
        print(i)
        i+1
    else:
        break
    
    
#pick_list = pick_list[pick_list['Item'] != 'EAVI Travel']
#pick_list = pick_list[pick_list['Item'] != 'EAVI System Design Services']


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
title = input()

print(title)

# Export the file
pick_list.to_csv(title+".csv", index=False)


