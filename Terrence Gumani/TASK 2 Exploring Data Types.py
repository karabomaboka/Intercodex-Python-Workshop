import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

response = requests.get(url)
data = response.text

df = pd.read_csv(StringIO(data))

# Loop over the first 10 lines and print product names of available products
for index, row in df.head(10).iterrows():
    if row['Availability']:
        print(f"Product Name: {row['Product Name']}")
