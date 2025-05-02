'''
Script:data_preprocessing.py
Description:
This script loads the loan approval dataset, cleans column names, removes
rows with missing target values (`loan_status`), and reports the number of
missing values per column for further preprocessing decisions.
'''

#Import pandas for data manipulation and analysis
import pandas as pd

# Step 1: Load the dataset from the local CSV file
# Replace the path if using a different working directory
csv_path = "loan_approval_dataset.csv"
df = pd.read_csv(csv_path)

# Step 2: Clean column names by removing any leading/trailing whitespace
# Ensures consistency and prevents errors in column referencing
df.columns = df.columns.str.strip()

# Step 3: Drop rows where the target variable ('loan_status') is missing
# Helps ensure that model training and evaluation are not affected by null targets
df.dropna(subset=['loan_status'], inplace=True)

# Step 4: Report the count of missing values in each column
# Useful for identifying features that need imputation or exclusion
print("Missing values per column:")
print(df.isnull().sum())
