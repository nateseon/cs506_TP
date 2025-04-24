import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load encoded dataset
csv_path = "loan_approval_encoded.csv"
df = pd.read_csv(csv_path)

# Drop target column from numeric features
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
numeric_cols = numeric_cols.drop('loan_status', errors='ignore')  # <- Safe drop

# Apply MinMaxScaler
scaler = MinMaxScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# Print scaled features
print(df[numeric_cols].head())
