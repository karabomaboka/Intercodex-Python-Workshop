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

    # Print the first 200 characters of the DataFrame
    print(data.head(200))

else:
    print("Failed to fetch data. Status code:", response.status_code)