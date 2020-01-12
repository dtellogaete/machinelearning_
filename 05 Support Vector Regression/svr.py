# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 22:37:49 2020

@author: Daniel
"""
# SVR

# Plantilla de Pre Procesado

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
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y.reshape(-1, 1))

#Ajustar la regresión con el dataset
from sklearn.svm import SVR
regression  = SVR(kernel ="rbf")
regression.fit(X,y)

#Predicción de nuestros modelos con SVR
value = np.array(6.5).reshape(-1,1)
y_pred = sc_y.inverse_transform(regression.predict(sc_X.transform(value)))

# Visualización de los resultados del SVR
plt.scatter(X, y, color = "red")
plt.plot(X, regression.predict(X), color = "blue")
plt.title("Modelo de regresión (SVR)")
plt.xlabel("Posición de Empleado")
plt.xlabel("Sueldo (en $)")
plt.show()



