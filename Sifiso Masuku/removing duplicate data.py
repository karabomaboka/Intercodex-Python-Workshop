import pandas as pd


sales_data = pd.read_csv("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv")

duplicates = sales_data.duplicated()

print(sales_data[duplicates])


sales_data.drop_duplicates(inplace=True)


print(sales_data)