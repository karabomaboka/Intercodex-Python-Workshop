import pandas as pd

# Load the dataset from the URL
url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
df = pd.read_csv(url)

# Use the DataFrame functions
print("1. df.head():")
print(df.head())
print(df.tail())
print("\n2. df.info():")
print(df.info())

print("\n3. df.describe():")
print(df.describe())