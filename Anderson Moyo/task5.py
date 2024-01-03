import pandas as pd 
from io import StringIO
import requests
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
df = pd.read_csv(url)
print('******************************************************************************')
print(df.head())
print('******************************************************************************')
print(df.info())
print('******************************************************************************')
print(df.describe())
