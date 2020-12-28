from sklearn.preprocessing import  PolynomialFeatures
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
import pandas as pd
from sklearn import metrics
import matplotlib.pyplot as plt

Data = pd.read_csv("./allData.csv")
Data = Data.drop(columns=['urban_land_use'])
Data=Data[~Data['land_shift_area'].isin([0])]
Data.to_csv('N0land_shiftData.csv', encoding = 'utf8')
Data.dropna()
"""
for i in range(len(Data)):
    if Data.loc[i,'land_shift_area']==0 :
        Data
    else:    
        Data2.append(Data.loc[i])
 """       

Data = (Data - Data.min()) / (Data.max() - Data.min())

Data.dropna()
Data.to_csv('normalizeallData.csv', encoding = 'utf8')

X = Data.drop(columns=['unit_ntd']).values
y = Data['unit_ntd'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
lin_reg = LinearRegression()  
poly_reg = PolynomialFeatures(degree=2)
X_poly = poly_reg.fit_transform(X_train)
lin_reg.fit(X_poly, y_train)
#regressor.fit(X_train, y_train)
lin_reg.predict(poly_reg.fit_transform(X_test))

#plt.scatter(X_train, y_train, color = 'red')
#plt.plot(X_train, lin_reg.predict(poly_reg.fit_transform(X_train)), color = 'blue')
#plt.title('Polynomial Regression')
#plt.show()
