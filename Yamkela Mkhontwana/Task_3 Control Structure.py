
import requests
import pandas as pd
from io import StringIO

# URL for Woolworths sales data CSV
url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

# Fetch data from the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Read CSV data into a DataFrame
    data = pd.read_csv(StringIO(response.text))

    # Convert "Price" column to numeric with errors coerced to NaN
    data["Price"] = pd.to_numeric(data["Price"], errors="coerce")

    # Loop over the first 10 lines and print product names for available products
    counter = 0
    for index, row in data.iterrows():
        if not pd.isnull(row["Product Name"]) and row["Price"] > 0:
            counter += 1
            print(f"\nAvailable Product with Price > 0: {row['Product Name']}")

        # Check if 10 products have been printed
        if counter == 10:
            break
else:
    print("Failed to fetch available products", response.status_code)
