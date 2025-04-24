import pandas as pd

# Load the dataset
csv_path = "/home/codespace/.cache/kagglehub/datasets/architsharma01/loan-approval-prediction-dataset/versions/1/loan_approval_dataset.csv"
df = pd.read_csv(csv_path)

# Strip whitespace from column names
df.columns = df.columns.str.strip()

# Drop rows with missing target values
df.dropna(subset=['loan_status'], inplace=True)

# Print missing value counts for all columns
print("Missing values per column:")
print(df.isnull().sum())
