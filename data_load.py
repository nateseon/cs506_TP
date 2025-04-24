import pandas as pd

csv_path = "/home/codespace/.cache/kagglehub/datasets/architsharma01/loan-approval-prediction-dataset/versions/1/loan_approval_dataset.csv"
df = pd.read_csv(csv_path)

print(df.head())
