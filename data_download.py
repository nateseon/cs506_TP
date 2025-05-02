'''
Script:data_download.py
Description:
To download dataset, this script uses the kagglehub library to 
It should be placed directly into your environment: Loan Approval Prediction from Kaggle.
'''

import kagglehub #Import the kagglehub library to programmatically download datasets from Kaggle
import pandas as pd #Import pandas for general-purpose data manipulation (used later)

#This will automatically handle caching and versioning of the dataset
#Returns the local path where the dataset is saved
path = kagglehub.dataset_download("architsharma01/loan-approval-prediction-dataset")
print("Dataset path:", path)
