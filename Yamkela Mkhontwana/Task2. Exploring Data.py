import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

response = requests.get(url)

if response.status_code == 200:
    data = pd.read_csv(StringIO(response.text))
    print(data.head(200))
    print(data.dtypes)
    data["Price"] = pd.to_numeric(data["Price"], errors="coerce")
    print(data)

else:
    print("Failed to fetch data. Status code:", response.status_code)