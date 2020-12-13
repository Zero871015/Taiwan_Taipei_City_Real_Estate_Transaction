import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

Data = pd.read_csv("./taipei_city_real_estate_transaction_v2.csv")

Data1 = Data[Data['urban_land_use'].isin(['work'])]
Data2 = Data[Data['urban_land_use'].isin(['quotient'])]
Data3 = Data[Data['urban_land_use'].isin(['address'])]
Data4 = Data[Data['urban_land_use'].isin(['Agriculture'])]

# 產生 CSV
Data1.to_csv('work.csv',encoding='utf8') 
Data2.to_csv('quotient.csv',encoding='utf8') 
Data3.to_csv('address.csv',encoding='utf8') 
Data4.to_csv('agriculture.csv',encoding='utf8') 
