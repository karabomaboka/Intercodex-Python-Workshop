
import pandas as pd
from io import StringIO
import requests
 
 
response = requests.get("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
)
 
if response.status_code ==200:
    print(response.text[:200])
 
    data = pd.read_csv(StringIO(response.text))
   
    print(data.head())
else:
    print(f"401")