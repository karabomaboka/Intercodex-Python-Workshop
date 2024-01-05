import pandas as pd

sales_data = pd.read_csv("https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv")

sales_data["Product Name"] = sales_data["Product Name"].astype("string")
sales_data['Date'] = pd.to_datetime(sales_data['Date'])
sales_data["Price"] = pd.to_numeric(sales_data["Price"], errors = "coerce")
sales_data["Availability"] = sales_data["Availability"].astype("category")

available_products = sales_data [sales_data ["Availability"] == "Available"]

for i in range(10):
    print("\nProduct Name:")
    print(available_products["Product Name"].iloc[i])
    print("\nAvailabilty Status:")
    print(available_products["Availability"].iloc[i])
    