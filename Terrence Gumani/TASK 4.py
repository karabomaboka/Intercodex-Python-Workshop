import requests
import pandas as pd
from io import StringIO
 
url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
 
response = requests.get(url)
data = response.text
 
 
df = pd.read_csv(StringIO(data))
 
df['Price'] = pd.to_numeric(df['Price'], errors='coerce').astype(float)
 
df['Price per unit'] = pd.to_numeric(df['Price per unit'], errors='coerce')
 
df['Specials'] = df['Specials'].astype(bool)
 
df['Ratings'] = df['Ratings'].astype('category')
 
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
 
print("Corrected Data Types:")
 
print(df.dtypes)