import requests
import pandas as pd
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

# Download the CSV content
response = requests.get(url)
data = response.text

# Read the CSV data into a pandas DataFrame
df = pd.read_csv(StringIO(data))

# Find and remove duplicate columns
df = df.loc[:, ~df.columns.duplicated()]

# Find and remove constant columns
constant_columns = df.columns[df.nunique() == 1]
df = df.drop(columns=constant_columns)

# Display the DataFrame after removing duplicates and constants
print(df)
