import pandas as pd

sales_data = pd.read_csv("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv")

print(sales_data.dtypes)

sales_data["Product Name"] = sales_data["Product Name"].astype("string")
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data["Price"] = pd.to_numeric(sales_data["Price"], errors = "coerce")
sales_data["Availability"] = sales_data["Availability"].astype("category")



print(sales_data.dtypes)