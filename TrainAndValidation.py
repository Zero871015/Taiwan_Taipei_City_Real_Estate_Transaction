#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd  
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate
from sklearn.tree import DecisionTreeRegressor
from sklearn import metrics
import matplotlib.pyplot as plt


# In[5]:


data = pd.read_csv("./allData.csv")
data = data.drop(columns = ['district'])
data


# In[18]:


#Model
reg = LinearRegression()
#Data and target
X = data.drop(columns=['total_ntd']).values
y = data['total_ntd'].values
#Cross validation
#Score = ((y_true - y_pred) ^ 2).sum()
predicted = cross_validate(reg, X, y, cv = 10)
predicted


# In[25]:


#Model
reg = DecisionTreeRegressor()
#Data and target
X = data.drop(columns=['total_ntd']).values
y = data['total_ntd'].values
#Cross validation
#Score = ((y_true - y_pred) ^ 2).sum()
predicted = cross_validate(reg, X, y, cv = 10)
predicted


# In[ ]:




