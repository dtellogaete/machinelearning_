# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 13:03:20 2019

@author: Daniel
"""

# Plantilla de Pre Procesado

# Cómo importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el data set
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, 
                                                    random_state = 0)

# Escalado de variables
"""
-Cuando es una regresión lineal simple no hace falta hacer el escalado
previo
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Crear modelo de Regresión Lineal Simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression() #Objeto para hacer regresión lineal
regression.fit(X_train, y_train)

# Predecir el conjunto de test
y_pred = regression.predict(X_test)

# Visualizar los resultados de entrenamiento
""" 
- La recta de regresión (plot) tiene la recta con datos de predicción.
"""
plt.scatter(X_train, y_train, color = "red") #Puntos de entrenamiento
plt.plot(X_train, regression.predict(X_train), 
         color = "blue") #Recta de regresión
plt.title("Sueldo vs Años de Experiencia (Conjunto de Entrenamiento)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo ($)")
plt.show()

# Visualizar los resultados del test
plt.scatter(X_test, y_test, color = "red") 
plt.plot(X_train, regression.predict(X_train), color = "blue") 
plt.title("Sueldo vs Años de Experiencia (Conjunto de test)")
plt.xlabel("Años de Experiencia")
plt.ylabel("Sueldo ($)")
plt.show()





