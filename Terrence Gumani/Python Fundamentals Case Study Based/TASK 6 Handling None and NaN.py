import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

# Download the CSV content
response = requests.get(url)
data = response.text

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype(float)
 
df['Price per unit'] = pd.to_numeric(df['Price per unit'], errors='coerce')
 
df['Specials'] = df['Specials'].astype(bool)
 
df['Ratings'] = df['Ratings'].astype('numeric')
 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Check for null values before interpolation
print("Null values before interpolation:")
print(df.isnull().sum())

# Interpolate null values using the interpolate method
df_interpolated = df.interpolate()

# Check for null values after interpolation
print("\nNull values after interpolation:")
print(df_interpolated.isnull().sum())
