import pandas as pd
import requests
from io import StringIO

def remove_duplicates_and_constants(csv_link):
    response = requests.get(csv_link)
    df = pd.read_csv(StringIO(response.text))

    # Handling "coarse" values in the 'Price' column
    df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

    # Display the count of duplicate rows before removal
    print("Duplicate rows count before removal:", df.duplicated().sum())

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Display the count of duplicate rows after removal
    print("Duplicate rows count after removal:", df.duplicated().sum())

    # Display the count of constant columns before removal
    constant_columns_count_before = (df.nunique() == 1).sum()
    print("\nConstant columns count before removal:", constant_columns_count_before)

    # Remove constant columns
    df = df.loc[:, df.nunique() != 1]

    # Display the count of constant columns after removal
    constant_columns_count_after = (df.nunique() == 1).sum()
    print("Constant columns count after removal:", constant_columns_count_after)

    return df

# How to call or use the functions defined in the tasks:
csv_link_task7 = 'https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv'
df_task7 = remove_duplicates_and_constants(csv_link_task7)
print(df_task7.head())
