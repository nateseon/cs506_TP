'''
Script:data_load.py
Description: This script loads the original raw loan approval dataset 
and prints the first few rows for an initial look at the data structure and contents.
'''

import pandas as pd #Import pandas for Reading and Handling Data

# Step 1: Define the path to the original dataset CSV file
csv_path = "loan_approval_dataset.csv"
#Step 2: Read the dataset into a pandas DataFrame
df = pd.read_csv(csv_path)
#Step 3: Print the first 5 rows of the dataset to preview its structure
print(df.head())
