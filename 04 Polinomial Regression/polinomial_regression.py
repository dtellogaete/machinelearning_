# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 20:06:20 2019

@author: Daniel
"""
# Regresión Polinómica

# Como importar librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar dataset
dataset = pd.read_csv('Position_Salaries.csv')
#Iloc Sirve para localizar elemento de un dataset
X = dataset.iloc[:, 1:2].values 
y = dataset.iloc[:, 2].values

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
"""from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, 
random_state = 0)"""

# Escalado de variables
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Ajustar la regresión lineal con el dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y) 

# Ajustar la regresión polinómica con el dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly, y)

# Visualización de los resultados del modelo lineal
plt.scatter(X, y, color = "red")
plt.plot(X, lin_reg.predict(X), color = "blue")
plt.title("Modelo de regresión lineal")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en ($)")
plt.show()

# Visualización de los resultados del modelo polinómico
X_grid = np.arange(min(X), max(X),0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
plt.scatter(X, y, color = "red")
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)), 
         color = "blue")
plt.title("Modelo de regresión polinómica")
plt.xlabel("Posición del empleado")
plt.ylabel("Sueldo en ($)")
plt.show()

# Predicción de nuestros modelos
lin_reg.predict([[6.5]])
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))

