import pandas as pd
from matplotlib import pyplot as plt
def load_csv(file: str) -> pd:
    dataframe = pd.read_csv(file)
    return dataframe
 
my_file = "pandas_retail_data.csv"
my_file2 = "pandas_suppliers_stock.csv"
df = load_csv(my_file)
df2 = load_csv(my_file2)
 
df_imputed = df.interpolate(method = "linear")
 
df_dedup = df_imputed.drop_duplicates()
df_merged = df_dedup.merge(df2, on = "ProductID")
#print(df_merged)
def plot_bar_chart(df: pd.DataFrame, xlab: str, ylab: str,ylab2:str,ylab3:str, title: str="mybar"):
    plt.bar(df[xlab],df[ylab],label=ylab)
    plt.bar(df[xlab],df[ylab2],label=ylab2)
    plt.bar(df[xlab],df[ylab3],label=ylab3)
    plt.title(title)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend()
    plt.grid()
    plt.show()

plot_bar_chart(df=df_merged,xlab="ProductID",ylab="Sales",ylab2="Returns", ylab3="Stock",title="Sales Barchart")
    
    
    
