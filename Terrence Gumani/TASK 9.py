import requests
import pandas as pd
from io import StringIO
import numpy as np

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

# Download the CSV content
response = requests.get(url)
data = response.text

# Read the CSV data into a pandas DataFrame
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

df = df.drop_duplicates() 

# Create a new column 'Date' with random SAST dates
start_date = '2022-01-01'
end_date = '2022-12-31'
num_rows = len(df)

# Generate random dates between start_date and end_date
random_dates = pd.date_range(start=start_date, end=end_date, periods=num_rows, tz='Africa/Johannesburg')

# Add the 'Date' column to the DataFrame
df['Date'] = random_dates

# Add a new column 'Quantity Sold' 
min_quantity = 100
max_quantity = 100000
df['Quantity Sold'] = np.random.randint(min_quantity, max_quantity + 1, size=num_rows)

print(df[['Date', 'Department', 'Price', 'Quantity Sold']])  

