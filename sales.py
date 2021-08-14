import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

import warnings
warnings.filterwarnings('ignore')

dtrain = pd.read_csv('Train.csv')
dtest = pd.read_csv('Test.csv')
dtrain['Outlet_Size']= dtrain['Outlet_Size'].fillna(dtrain['Outlet_Size'].mode()[0])
dtest['Outlet_Size']= dtest['Outlet_Size'].fillna(dtest['Outlet_Size'].mode()[0])
dtrain['Item_Weight']= dtrain['Item_Weight'].fillna(dtrain['Item_Weight'].mean())
dtest['Item_Weight']= dtest['Item_Weight'].fillna(dtest['Item_Weight'].mean())
dtrain['Item_Fat_Content'].replace(['low fat','LF','reg'],['Low Fat','Low Fat','Regular'],inplace = True)
dtest['Item_Fat_Content'].replace(['low fat','LF','reg'],['Low Fat','Low Fat','Regular'],inplace = True)
dtrain['Outlet_Establishment_Year']=dtrain['Outlet_Establishment_Year'].apply(lambda x: 2021-x)
dtest['Outlet_Establishment_Year']=dtest['Outlet_Establishment_Year'].apply(lambda x: 2021-x)
dtrain['Item_Type_Combined'] = dtrain['Item_Identifier'].apply(lambda x: x[0:2])
#Rename them to more intuitive categories:
dtrain['Item_Type_Combined'] = dtrain['Item_Type_Combined'].map({'FD':'Food',
                                                             'NC':'Non-Consumable',
                                                             'DR':'Drinks'})
dtest['Item_Type_Combined'] = dtest['Item_Identifier'].apply(lambda x: x[0:2])
#Rename them to more intuitive categories:
dtest['Item_Type_Combined'] = dtest['Item_Type_Combined'].map({'FD':'Food',
                                                             'NC':'Non-Consumable',
                                                             'DR':'Drinks'})
dtrain['Item_Type_Combined'].value_counts()
dtrain['Item_Type_Combined'].value_counts()

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dtrain['Outlet'] = le.fit_transform(dtrain['Outlet_Identifier'])
dtest['Outlet'] = le.fit_transform(dtest['Outlet_Identifier'])
var_mod = [ 'Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet']
le = LabelEncoder()
for i in var_mod:
    dtrain[i] = le.fit_transform(dtrain[i])
    dtest[i] = le.fit_transform(dtest[i])



dtrain = pd.get_dummies(dtrain, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet'])
dtest = pd.get_dummies(dtest, columns=['Item_Fat_Content','Outlet_Location_Type','Outlet_Size','Item_Type_Combined','Outlet_Type','Outlet'])
dtrain.drop(['Item_Type','Outlet_Establishment_Year','Item_Identifier','Item_Type','Outlet_Identifier'],axis=1,inplace=True)
dtest.drop(['Item_Type','Outlet_Establishment_Year','Item_Identifier','Item_Type','Outlet_Identifier'],axis=1,inplace=True)
y_train= dtrain['Item_Outlet_Sales']

dtrain.drop(['Item_Outlet_Sales'],axis=1,inplace=True)
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn import  metrics
from sklearn.metrics import mean_squared_error
features=dtrain.columns
LR = LinearRegression(normalize=True)
LR.fit(dtrain,y_train)
y_pred = LR.predict(dtrain)
coef2 = pd.Series(LR.coef_,features).sort_values()
print("constant",LR.intercept_)
#LR.score(dtrain, y_train)
print("rsquare",metrics.r2_score(y_train,y_pred))
print("mse",metrics.mean_squared_error(y_train,y_pred))
print("rmse",np.sqrt(metrics.mean_squared_error(y_train, y_pred)))
print("mae",metrics.mean_absolute_error(y_train,y_pred))
print("coefficents",LR.coef_)
from sklearn.ensemble import RandomForestRegressor
rf= RandomForestRegressor(n_estimators=400,max_depth=6, min_samples_leaf=100,n_jobs=4)
from sklearn.model_selection import RandomizedSearchCV
# Number of trees in random forest
n_estimators = [int(x) for x in np.linspace(start = 100, stop = 1200, num = 12)]
# Number of features to consider at every split
max_features = ['auto', 'sqrt']
# Maximum number of levels in tree
max_depth = [int(x) for x in np.linspace(5, 30, num = 6)]
# max_depth.append(None)
# Minimum number of samples required to split a node
min_samples_split = [2, 5, 10, 15, 100]
# Minimum number of samples required at each leaf node
min_samples_leaf = [1, 2, 5, 10]
random_grid = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}
rf_random = RandomizedSearchCV(estimator = rf, param_distributions = random_grid,scoring='neg_mean_squared_error', n_iter = 10, cv = 5, verbose=2, random_state=42, n_jobs = 1)
rf_random.fit(dtrain, y_train)
outrf=rf_random.predict(dtrain)

filename="sales.sav"
joblib.dump(rf_random, filename)