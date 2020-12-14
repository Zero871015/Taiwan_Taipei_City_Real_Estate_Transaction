#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import numpy as np

Data = pd.read_csv("./taipei_city_real_estate_transaction_v2.csv")
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

temp = pd.get_dummies(Data.district)
temp = Data.join(temp)
temp = temp.drop(['district'], axis=1)
temp


# In[5]:


Data1


# In[6]:


import pandas as pd
from sklearn.preprocessing import LabelEncoder
Data = pd.read_csv("./work.csv")
labelencoder = LabelEncoder()
data_le=pd.DataFrame(Data)
data_le['main_building_material'] = labelencoder.fit_transform(data_le['main_building_material'])
data_dum = pd.get_dummies(data_le)
pd.DataFrame(data_dum)
data_dum.to_csv('work.csv',encoding='utf8')
data_dum


# In[ ]:




