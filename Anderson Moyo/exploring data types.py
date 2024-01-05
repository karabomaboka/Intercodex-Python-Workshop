import pandas as pd 
from io import StringIO
import requests

# Read the CSV file from the URL
url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
df = pd.read_csv(url)

# Display original data types
print("Original Data Types:")
print(df.dtypes)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nUpdated Data Types:")
print(df.dtypes)

print("\nDataFrame Preview:")
print(df.head())
