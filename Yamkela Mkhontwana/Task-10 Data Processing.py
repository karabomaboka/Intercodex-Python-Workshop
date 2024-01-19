import pandas as pd
import numpy as np
import requests
from io import StringIO

def analyze_data_with_numpy(csv_link):
    # Fetch data from the provided link
    response = requests.get(csv_link)
    df = pd.read_csv(StringIO(response.text))

    # Handling non-numeric values in the 'Price' column
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Create a column called "quantity" with random numbers from NumPy
    np.random.seed(42) # Set a seed for reproducibility
    df['quantity'] = pd.to_numeric(np.random.randint(1, 100, size=len(df)), errors='coerce')

    # Create a 'datetime' column
    df['datetime'] = pd.to_datetime(df['Date'], errors='coerce') # Assuming 'Date' is the column name containing date information

    # Coerce 'Ratings' to numeric
    df['Ratings'] = pd.to_numeric(df['Ratings'], errors='coerce')

    # Run a correlation analysis on 'Price', 'quantity', and 'Ratings'
    correlation_matrix = df[['Price', 'quantity', 'Ratings']].corr()

    return df, correlation_matrix

# Example Usage:
csv_link_task8 = 'https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv'
result_df_task8, correlation_matrix_task8 = analyze_data_with_numpy(csv_link_task8)

print(result_df_task8.head())
print("\nCorrelation Matrix:")
print(correlation_matrix_task8)

