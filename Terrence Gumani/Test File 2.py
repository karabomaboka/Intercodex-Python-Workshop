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

# Convert 'Date' column to numeric (timestamp)
df['Date'] = pd.to_datetime(df['Date']).astype(np.int64) // 10**9  # Convert to seconds for simplicity

# Convert 'Price' column to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Check for and handle NaN values if needed
# For example, fill NaN values with the mean
df['Price'].fillna(df['Price'].mean(), inplace=True)

# Calculate correlation matrix
correlation_matrix = df[['Price', 'Quantity Sold', 'Date']].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
