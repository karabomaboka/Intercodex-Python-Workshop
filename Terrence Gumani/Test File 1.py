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

# Convert 'Price' column to numeric (assuming it contains numeric values)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Create a new column 'Date' with random SAST dates
start_date = '2022-01-01'
end_date = '2022-12-31'
num_rows = len(df)

# Generate random dates between start_date and end_date
random_dates = pd.date_range(start=start_date, end=end_date, periods=num_rows, tz='Africa/Johannesburg')

# Add the 'Date' column to the DataFrame
df['Date'] = random_dates

# Add a new column 'Quantity Sold' with random quantities
min_quantity = 1
max_quantity = 100
df['Quantity Sold'] = np.random.randint(min_quantity, max_quantity + 1, size=num_rows)

# Run correlation analysis
correlation_matrix = df[['Price', 'Quantity Sold', 'Date']].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
