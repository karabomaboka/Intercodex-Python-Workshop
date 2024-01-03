import requests
import pandas as pd 
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

response = requests.get(url)
if response.status_code == 200:

    csv_content = StringIO(response.text)
    df = pd.read_csv(csv_content)

   
    first_20_lines = df.head(20)

   
    print(first_20_lines)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")