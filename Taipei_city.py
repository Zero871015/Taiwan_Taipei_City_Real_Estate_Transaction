import pandas as pd
import numpy as np

Data = pd.read_csv("./taipei_city_real_estate_transaction_v2.csv")

Data = Data[~Data['urban_land_use'].isin(['Other','Others'])]

# 產生 CSV
Data.to_csv('New_Data.csv',encoding='utf8') 
