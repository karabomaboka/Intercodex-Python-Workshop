import pandas as pd
import requests
from io import StringIO

def perform_null_value_imputation(csv_link):
    response = requests.get(csv_link)
    df = pd.read_csv(StringIO(response.text))

    # Handling "coarse" values in the 'Price' column
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Replace 'Price' with any column name you want to perform imputation
    column_name = 'Price'

    # Display the count of null values before imputation
    print("Null values count before imputation:")
    print(df[column_name].isnull().sum())

    # Strategy 1: Mean Imputation
    mean_value = df[column_name].mean()
    df[column_name].fillna(mean_value, inplace=True)

    # Display the count of null values after imputation
    print("\nNull values count after mean imputation:")
    print(df[column_name].isnull().sum())

    # I can add other imputation strategies as needed

    return df

# How to call or use the functions defined in the tasks:
csv_link_task6 = 'https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv'
df_task6 = perform_null_value_imputation(csv_link_task6)
print(df_task6.head())


