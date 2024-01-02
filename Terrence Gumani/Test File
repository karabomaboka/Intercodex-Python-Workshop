import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

response = requests.get(url)
data = response.text

df = pd.read_csv(StringIO(data))

df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype(float)
df['Price per unit'] = pd.to_numeric(df['Price per unit'], errors='coerce')
df['Specials'] = df['Specials'].astype(bool)
df['Ratings'] = df['Ratings'].astype('category')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Extract numeric and alphabetic parts from the 'Price' column
df[['Price Numeric', 'Price Alphabetic']] = df['Price'].astype(str).str.extract('(\d+\.?\d*)\s*([a-zA-Z]+)')

# Convert the 'Price' column to numeric values
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype(float)

# Drop the original 'Price per unit' column
df = df.drop(columns=['Price per unit'])


# Display the DataFrame with separated columns
print("\nDataFrame with Separated Columns:")
print(df[['Price Numeric', 'Price Alphabetic']])


# Group by 'Department' and calculate total and average prices
department_stats = df.groupby('Department')['Price'].agg(['sum', 'mean']).reset_index()

# Rename columns for clarity
department_stats.columns = ['Department', 'Total Price', 'Average Price']

# Display the results
print(department_stats)
