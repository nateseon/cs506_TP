import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load encoded dataset
csv_path = "/home/codespace/.cache/kagglehub/datasets/architsharma01/loan-approval-prediction-dataset/versions/1/loan_approval_dataset.csv"
df = pd.read_csv(csv_path)

# Strip column names
df.columns = df.columns.str.strip()

# Drop non-feature target column if present in numeric
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
numeric_cols = numeric_cols.drop('loan_status', errors='ignore')  # <- Safe drop

# Apply MinMaxScaler
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Preview result
print(df[numeric_cols].head())
