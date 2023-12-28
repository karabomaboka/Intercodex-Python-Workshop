import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv")

available_products = data[data["Availability"] == "Available"]

for i in range(10):
    print(data["Product Name"][i])