import pandas as pd 
data=pd.read_csv("C:\projects\deeplnproject\converted_output.csv")
data.drop(columns={'index_name'},inplace=True)