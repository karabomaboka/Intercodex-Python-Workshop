import pandas as pd
import requests
from io import StringIO

def calculate_total_and_average_prices(csv_link, group_column, price_column):
    response = requests.get(csv_link)
    df = pd.read_csv(StringIO(response.text))

    # Handling "coarse" values in the 'Price' column
    df[price_column] = pd.to_numeric(df[price_column], errors='coerce')

    # Group by the specified column for grouping
    grouped_data = df.groupby(group_column)

    # Calculate total prices per category
    total_prices = grouped_data[price_column].sum().reset_index()
    total_prices.columns = [group_column, 'Total_Price']

    # Calculate average prices per category
    average_prices = grouped_data[price_column].mean().reset_index()
    average_prices.columns = [group_column, 'Average_Price']

    # Merge the total and average prices into a single DataFrame
    result_df = pd.merge(total_prices, average_prices, on=group_column)

    return result_df

# How to call or use the functions defined in the tasks:
csv_link_task8 = 'https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv'
group_column_task8 = 'Product Name'  # Replace with the actual column name for grouping
price_column_task8 = 'Price'  # Replace with the actual column name for the 'Price' column
result_prices_task8 = calculate_total_and_average_prices(csv_link_task8, group_column_task8, price_column_task8)
print(result_prices_task8.head())

