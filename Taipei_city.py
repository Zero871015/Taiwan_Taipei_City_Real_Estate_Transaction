import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
import numpy as np

Data = pd.read_csv("./taipei_city_real_estate_transaction_v2.csv")

labelencoder = LabelEncoder()
Data=pd.DataFrame(Data)
#Data['main_building_material','transaction_type','main_use','carpark_category'] = labelencoder.fit_transform(Data['main_building_material','transaction_type','main_use','carpark_category'])
Data['main_building_material'] = labelencoder.fit_transform(Data['main_building_material'])
Data['transaction_type'] = labelencoder.fit_transform(Data['transaction_type'])
Data['main_use'] = labelencoder.fit_transform(Data['main_use'])
Data['carpark_category'] = labelencoder.fit_transform(Data['carpark_category'])

onehotencoder = OneHotEncoder(sparse = False)
#data_str_ohe=onehotencoder.fit_transform(Data).toarray()
data_str_ohe=Data.reshape(-1,1)
pd.DataFrame(data_str_ohe)

#Data = pd.get_dummies(Data)
#pd.DataFrame(Data)
Data.to_csv('New.csv',encoding='utf8') 

'''
Data1 = Data[Data['urban_land_use'].isin(['work'])]
Data2 = Data[Data['urban_land_use'].isin(['quotient'])]
Data3 = Data[Data['urban_land_use'].isin(['address'])]
Data4 = Data[Data['urban_land_use'].isin(['Agriculture'])]

# 產生 CSV
Data1.to_csv('work.csv',encoding='utf8') 
Data2.to_csv('quotient.csv',encoding='utf8') 
Data3.to_csv('address.csv',encoding='utf8') 
Data4.to_csv('agriculture.csv',encoding='utf8') 
'''
