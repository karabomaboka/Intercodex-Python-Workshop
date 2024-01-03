import pandas as pd
import numpy as np
from io import StringIO
import requests

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
response = requests.get(url)

# Load the CSV data into a DataFrame
df = pd.read_csv(StringIO(response.text))

# Create a column called "quantity" and fill it with random numbers from NumPy
df['quantity'] = np.random.rand(len(df))

# Run a correlation analysis on price, quantity, and rating
correlation_matrix = df[['Price', 'quantity', 'Ratings']].corr()

print("Correlation Matrix:")
print(correlation_matrix)
