import pandas as pd
from sklearn.preprocessing import LabelEncoder
Data = pd.read_csv("./work.csv")
labelencoder = LabelEncoder()
data_le=pd.DataFrame(Data)
data_le['main_building_material'] = labelencoder.fit_transform(data_le['main_building_material'])
data_dum = pd.get_dummies(data_le)
pd.DataFrame(data_dum)
data_dum.to_csv('work.csv',encoding='utf8') 


Data = pd.read_csv("./quotient.csv")
labelencoder = LabelEncoder()
data_le=pd.DataFrame(Data)
data_le['main_building_material'] = labelencoder.fit_transform(data_le['main_building_material'])
data_dum = pd.get_dummies(data_le)
pd.DataFrame(data_dum)
data_dum.to_csv('quotient.csv',encoding='utf8') 



Data = pd.read_csv("./address.csv")
labelencoder = LabelEncoder()
data_le=pd.DataFrame(Data)
data_le['main_building_material'] = labelencoder.fit_transform(data_le['main_building_material'])
data_dum = pd.get_dummies(data_le)
pd.DataFrame(data_dum)
data_dum.to_csv('address.csv',encoding='utf8') 




Data = pd.read_csv("./agriculture.csv")
labelencoder = LabelEncoder()
data_le=pd.DataFrame(Data)
data_le['main_building_material'] = labelencoder.fit_transform(data_le['main_building_material'])
data_dum = pd.get_dummies(data_le)
pd.DataFrame(data_dum)
data_dum.to_csv('agriculture.csv',encoding='utf8') 
