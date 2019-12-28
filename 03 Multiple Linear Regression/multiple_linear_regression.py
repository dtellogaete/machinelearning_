# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 15:48:18 2019
regression.coef_ coeficientes de la recta
regression.intercept_ intercepción de la recta
@author: Daniel
"""

# Regresion Lineal Múltiple

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

#Codificar datos categóricos
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() 
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotenconder = OneHotEncoder(categorical_features=[3])
X = onehotenconder.fit_transform(X).toarray()

# Deberíamos evitar la trampa de las variables ficticias
X = X[:,1:] # Se elimina la primera columna (California)

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
                                                    random_state = 0)

# Ajustar el modelo de regresión lineal con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

# Prediccion de los resultados en el conjunto de testing
y_pred = regression.predict(X_test)

# Construir el modelo optimo de RLM utilizando la Eliminación hacia atrás
"""-Encontrar un conjunto optimo de variables independientes, para poder hacer 
el mejor modelo posible.
- Preparar la Eliminación hacia atrás (muchos de estos coeficientes 
podrían ocurrir que sea 0)
"""
import statsmodels.api as sm
X = np.append(arr = np.ones((50,1)).astype(int), values=X , axis=1)
X_opt = X[:,[0,1,2,3,4,5]]
# 1.-Crear SL
SL = 0.05

# 2.- Crear el modelo con variables predictora OLS Ordinal Least Scuared
regression_OLS = sm.OLS(endog = y, exog = X_opt).fit()

# 3.- Considera la variable predictora con el p-valor más grande
regression_OLS.summary()

# 4 Se elimina la columna numero 2, ya que tienen 
X_opt = X[:,[0,1,3,4,5]]
SL = 0.05
regression_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regression_OLS.summary()

X_opt = X[:,[0,3,4,5]]
SL = 0.05
regression_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regression_OLS.summary()

X_opt = X[:,[0,3,5]]
SL = 0.05
regression_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regression_OLS.summary()

X_opt = X[:,[0,3]]
SL = 0.05
regression_OLS = sm.OLS(endog = y, exog = X_opt).fit()
regression_OLS.summary()