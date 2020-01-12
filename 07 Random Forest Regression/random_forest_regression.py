# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 20:28:13 2020

@author: Daniel
"""

# Random Forest Regression

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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
"""

# Escalado de variables
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Ajustar el Random Forest con el dataset
# Crear aquí nuestro modelo de regresión
from sklearn.ensemble import RandomForestRegressor
regression = RandomForestRegressor(n_estimators = 300,
                                  random_state = 0)
regression.fit(X, y)


# Predicción de nuestros modelos
value = np.array(6.5).reshape(-1,1)
y_pred = regression.predict(value)

# Visualización de los resultados del Random Forest
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, regression.predict(X_grid), color = "blue")
plt.title("Modelo de Regresión")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo (en $)")
plt.show()

