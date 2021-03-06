# encoding: utf-8
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
#import numpy as np

Data = pd.read_csv("./taipei_city_real_estate_transaction_v2.csv")

temp = pd.get_dummies(Data.urban_land_use)
#temp = pd.concat([Data,temp])
Data = Data.merge(temp, left_index=True, right_index=True) 
#Data = Data.join(temp)

temp = pd.get_dummies(Data.district)
#temp = pd.concat([Data,temp])
Data = Data.merge(temp, left_index=True, right_index=True) 

temp = pd.get_dummies(Data.carpark_category)
#Data = Data.join(temp)
Data = Data.merge(temp, left_index=True, right_index=True) 

temp = pd.get_dummies(Data.main_building_material)
#Data = pd.merge([Data,temp])
Data = Data.merge(temp, left_index=True, right_index=True) 

temp = pd.get_dummies(Data.main_use)
#Data = Data.join(temp)
#Data = pd.concat([Data,temp])
Data = Data.merge(temp, left_index=True, right_index=True) 

temp = pd.get_dummies(Data.transaction_type)
#temp = Data.join(temp)
#temp = pd.concat([Data,temp])
Data = Data.merge(temp, left_index=True, right_index=True) 

Data = Data.drop(['district','urban_land_use','transaction_type','main_use','main_building_material','carpark_category','number_of_land','unit_ntd','building_age'],axis=1)

#temp = temp.drop(['district'], axis=1)

for i in range(len(Data)):
    if Data.loc[i, 'num_partition'] == '有':
        Data.loc[i, 'num_partition'] = 1
    else:
        Data.loc[i, 'num_partition'] = 0
    if Data.loc[i, 'management_org'] == '有':
        Data.loc[i, 'management_org'] = 1
    else:
        Data.loc[i, 'management_org'] = 0



#temp.to_csv('One.csv',encoding='utf8')
'''
# Classification data by "urban_land_use" and discard(throw away) "Other" & "Others"
Data1 = Data[Data['urban_land_use'].isin(['work'])]
Data2 = Data[Data['urban_land_use'].isin(['Quotient'])]
Data3 = Data[Data['urban_land_use'].isin(['Address'])]
Data4 = Data[Data['urban_land_use'].isin(['Agriculture'])]

# Generate CSV
Data1.to_csv('work.csv',encoding='utf8') 
Data2.to_csv('Quotient.csv',encoding='utf8') 
Data3.to_csv('Address.csv',encoding='utf8') 
Data4.to_csv('Agriculture.csv',encoding='utf8') 


#district
#transaction_type
#main_use
#main_building_material
#carpark_category
'''
Data.to_csv('allData.csv', encoding = 'utf8')
print('OK')
