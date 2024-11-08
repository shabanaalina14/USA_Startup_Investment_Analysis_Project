# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 12:22:47 2024

@author: shaba
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset=pd.read_csv(r"C:\Users\shaba\OneDrive\csv_xml_sheets\USA_Startups.csv")

#split the datset into independent and dependent var
x=dataset.iloc[:,:-1]
y=dataset.iloc[:,4]

#convert cat to int
x=pd.get_dummies(x,dtype=int)

#spliting the data
#outof 50 ,40 records go to train
#machine learns while testing and traing the data
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#train the model using x train and y train with the help of  regressor
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)

#here regressor is the model and linearregression is algorithm

# we build mlr model
# we have 6 coef
m=regressor.coef_
print(m)

c=regressor.intercept_
print(c)

#in our data constant is missing have to add cons
#ex 3/2=1 so here 1 is constant for all
x=np.append(arr=np.ones((50,1)).astype(int),values=x,axis=1)
#instead of 1 we can use c value  which is 42467 print(c) value


#recresive feature elemenation also called feature elemenation
#rfe divides into 2 parts 1.forward and 2.backward
#used to remove un-relevent attributes from data set so that can expain clearly

import statsmodels.api as sm
x_opt=x[:,[0,1,2,3,4,5]]
#ordinaryleastsquares
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()

##statemets
#as shown if p value greater thn 0.05 thn we reject the null hypo,eleminates the attributes

#feature elemination 
#using backward elemination
import statsmodels.api as sm
x_opt=x[:,[0,1]]
#ordinaryleastsquares
regressor_OLS=sm.OLS(endog=y,exog=x_opt).fit()
regressor_OLS.summary()


#know i can tell to my company to invest R&D spend
