import pandas as pd 
from io import StringIO
import requests
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
df = pd.read_csv(url)


category_column = 'Category'


constant_columns = df.columns[df.nunique() == 1]
df = df.drop(columns=constant_columns)
price_stats = df.groupby(category_column)['Price'].agg(['sum', 'mean'])

print("\nTotal and Average Prices per Category:")
print(price_stats)

print('\n******************************************************************************')
print(df.head())
print('\n******************************************************************************')
print(df.describe())
