import pandas as pd


df = pd.read_csv("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv")


print(df.head(5))

print(df.info(5))

print(df.describe())