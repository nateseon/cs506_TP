'''
Script:data_encoding.py
Description:
This script loads the loan approval dataset, cleans column names and string
converts categorical variables into binary numerical values, and 
It saves the processed dataset to a new CSV file to use it sometime later.
'''

import pandas as pd #Read and process csv file using pandas library.

#Step1 : Step is to take the data from the Kaggle path that has been downloaded
#Change to path below if not in the same environment
csv_path = "loan_approval_dataset.csv"
df = pd.read_csv(csv_path)

#Step2: Strip whitespace before/after column names and string values.
#This avoids any issues concerns during data matching and mapping.
# Strip whitespace from column names and string values
df.columns = df.columns.str.strip()
df['education'] = df['education'].str.strip()
df['self_employed'] = df['self_employed'].str.strip()
df['loan_status'] = df['loan_status'].str.strip()

#Step3:Map categorical string values to binary numerical values.
#It is useful when feeding the ML models that require numeric input.
# Map binary categorical variables
df['education'] = df['education'].map({'Graduate': 1, 'Not Graduate': 0})
df['self_employed'] = df['self_employed'].map({'Yes': 1, 'No': 0})
df['loan_status'] = df['loan_status'].map({'Approved': 1, 'Rejected': 0})

#Step4: This saves the encoded DataFrame to a new CSV file.
 #It will use this file in the next step for scaling and modeling.
# Save the encoded file for scaling
encoded_csv_path = "loan_approval_encoded.csv"
df.to_csv(encoded_csv_path, index=False)

#Step5:Display the encoded columns for quick verification.
# Print sample encoded columns
print(df[['education', 'self_employed', 'loan_status']].head())
