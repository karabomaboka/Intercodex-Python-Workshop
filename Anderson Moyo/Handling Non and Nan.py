import pandas as pd 
from io import StringIO
import requests
from matplotlib import pyplot as plt

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"
df = pd.read_csv(url)
# df = pd.read_csv(url)
url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

response = requests.get(url)

if response.status_code == 200:
    print(response.text[:200])

    data = pd.read_csv(StringIO(response.text))
    
    
    print("\nOriginal Data Types:")
    print(data.dtypes)    
print(df.dtypes)
categorical_columns = ['Brand', 'Product Name', 'Specials', 'Tag Description', 'Online Only', 'New Product', 'Ratings', 'Department', 'Product URL']
data[categorical_columns] = data[categorical_columns].astype('category')
numeric_columns = ['SKU', 'Price', 'Package Size', 'Price per unit']
data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')
data['Availability'] = data['Availability'].astype('category')
data['Date'] = pd.to_datetime(data['Date'])

print("Before handling missing values:")
print(df.isnull().sum())


numeric_columns = df.select_dtypes(include=['number']).columns


df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())


print("\nAfter handling missing values:")
print(df.isnull().sum())


print('\n******************************************************************************')
print(df.head())
print('\n******************************************************************************')
print(df.info())
print('\n******************************************************************************')
print(df.describe())
