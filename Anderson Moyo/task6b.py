import pandas as pd 
from io import StringIO
import requests
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
df = pd.read_csv(url)

# Check for missing values
print("Before handling missing values:")
print(df.isnull().sum())

# Identify numeric columns
numeric_columns = df.select_dtypes(include=['number']).columns

# Mean imputation for numeric columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

# Check again for missing values after imputation
print("\nAfter handling missing values:")
print(df.isnull().sum())

# Now, you can proceed with the rest of your analysis or data processing
print('\n******************************************************************************')
print(df.head())
print('\n******************************************************************************')
print(df.info())
print('\n******************************************************************************')
print(df.describe())
