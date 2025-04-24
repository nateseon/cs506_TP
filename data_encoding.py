import pandas as pd

# Load dataset
csv_path = "/home/codespace/.cache/kagglehub/datasets/architsharma01/loan-approval-prediction-dataset/versions/1/loan_approval_dataset.csv"
df = pd.read_csv(csv_path)

# Strip whitespace from column names and string values
df.columns = df.columns.str.strip()
df['education'] = df['education'].str.strip()
df['self_employed'] = df['self_employed'].str.strip()
df['loan_status'] = df['loan_status'].str.strip()

# Map binary categorical variables
df['education'] = df['education'].map({'Graduate': 1, 'Not Graduate': 0})
df['self_employed'] = df['self_employed'].map({'Yes': 1, 'No': 0})
df['loan_status'] = df['loan_status'].map({'Approved': 1, 'Rejected': 0})

# Print sample encoded columns
print(df[['education', 'self_employed', 'loan_status']].head())
