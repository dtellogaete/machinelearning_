# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 13:02:11 2020

@author: Daniel
"""
# Regresión con árboles de decisión

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, 
                                                    random_state = 0)
"""

# Escalado de variables
"""
-Cuando es una regresión lineal simple no hace falta hacer el escalado
previo
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Ajustar la regresuón con el dataset
"""
randon_state = 0, semilla random
"""
from sklearn.tree import DecisionTreeRegressor
regression = DecisionTreeRegressor(random_state = 0)
regression.fit(X,y)

# Predecir del modelo
value = np.array(6.5)
y_pred = regression.predict(value.reshape(-1,1))

# Visualizar los resultados del modelo
X_grid = np.arange(min(X), max(X),0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X, regression.predict(X), color = "blue")
plt.title("Modelo de regresión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en ($)")
plt.show()





