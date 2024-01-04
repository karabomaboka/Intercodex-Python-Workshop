import requests
from io import StringIO
import pandas as pd

response = requests.get("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv")
data = pd.read_csv(StringIO(response.text))

print(data.head(200))