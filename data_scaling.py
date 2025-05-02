'''
Script:data_scaling.py
Description:
Then, in the case of this script, it first loads the previously encoded loan approval dataset and then 
They then scale the numbers to range from [0, 1] using MinMaxScaler. 
It prints a preview of the scaled features.
'''

import pandas as pd # Import Library For reading the encoded dataset
from sklearn.preprocessing import MinMaxScaler #Import Library for future scaling

# Step1: Load Encoded Dataset
csv_path = "loan_approval_encoded.csv"
df = pd.read_csv(csv_path)

# Step2:We will identify numeric columns which we can scale.
#Take away the target column ('loan_status') because it is not a feature
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
numeric_cols = numeric_cols.drop('loan_status', errors='ignore')  # <- Safe drop

# Step3:. Normalize numeric columns with MinMaxScaler to the range [0, 1].
#That means that all features play the same role during model training.
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Step4:Print out the scaled numeric features to make sure the result is what should be
print(df[numeric_cols].head())
