#**Data Exploration Function:**
 #def explore_data(data: pd.DataFrame) -> None:

   
#**Data Cleaning Function:**
 #def clean_data(data: pd.DataFrame) -> pd.DataFrame:
   

#Plotting Function:
 #def plot_data(data: pd.DataFrame, column_x: str, column_y: str) -> None:
 

#**Data Filtering Function:**
 #def filter_data(data: pd.DataFrame, condition: str) -> pd.DataFrame:
 
#**Statistical Analysis Function:**
 #def analyze_data(data: pd.DataFrame, column: str) -> dict:

 import pandas as pd
import matplotlib.pyplot as plt

# Data Exploration Function
def explore_data(data: pd.DataFrame) -> None:
    print("Basic Information about the Data:")
    print(data.info())

    print("\nDescriptive Statistics:")
    print(data.describe())

    print("\nFirst 5 Rows of the Data:")
    print(data.head())

# Data Cleaning Function
def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    data = data.dropna()
    return data

# Plotting Function
def plot_data(data: pd.DataFrame, column_x: str, column_y: str) -> None:
    plt.scatter(data[column_x], data[column_y])
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.title(f"Scatter Plot: {column_x} vs {column_y}")
    plt.show()

# Data Filtering Function
def filter_data(data: pd.DataFrame, condition: str) -> pd.DataFrame:
    filtered_data = data.query(condition)
    return filtered_data

# Statistical Analysis Function
def analyze_data(data: pd.DataFrame, column: str) -> dict:
    analysis_results = {
        "Mean": data[column].mean(),
        "Median": data[column].median(),
        "Standard Deviation": data[column].std(),
        "Minimum": data[column].min(),
        "Maximum": data[column].max(),
    }
    return analysis_results

if __name__ == "__main__":
    # Data URL
    data_url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

    # Read data
    data = pd.read_csv(data_url)

    # Explore the data
    explore_data(data)

    # Clean the data
    cleaned_data = clean_data(data)

    # Plot data
    plot_data(data, "Quantity", "Price")  # Replace with actual column names

    # Filter data
    filtered_data = filter_data(data, "Price > 0")

    # Analyze data
    analysis_results = analyze_data(data, "Price")
    print("\nStatistical Analysis Results:")
    print(analysis_results)
