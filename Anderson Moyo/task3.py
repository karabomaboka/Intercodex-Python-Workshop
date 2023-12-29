import pandas as pd 
from io import StringIO
import requests
import pandas as pd
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

df = pd.read_csv(url)
# counter=0
# while counter!=0:
    
for index, row in df[df['Availability']=='Available'].head(10).iterrows():
    product_name = row["Product Name"]
    print(f" {product_name}")
