# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 14:07:12 2019
@author: Daniel
"""

# Datos Categoricos - Datos faltantes

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importar dataset
dataset = pd.read_csv('Data.csv')
#Iloc Sirve para localizar elemento de un dataset
X = dataset.iloc[:, :-1].values 
y = dataset.iloc[:, 3].values


#Tratamiento de los NAs
"""
Remplazar los datos faltantes por la media es una buena
estrategia para eliminar los NAs
missing_value = "NaN": Valor faltante
strategy = mean : que valor se NaN se va a reemplazar
axis = 0. Aplicar a columna
"""
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis = 0)
imputer.fit(X[:, 1:3]) #fit para aplicar el imputer, 1 incluye/3 excluye
X[:, 1:3] = imputer.transform(X[:,1:3]) #Transforma valores desconocidos

#Codificar datos categóricos
"""
Detectar columnas con datos categoricos.
Transformar los datos a categoricos.
Variable categorica: no existe un orden.
Variable dummy (one hot vector / one hot enconding)
OneHotEncoder: donde se encuentra el vector a transformar
"""
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() # No necesita ningún parámetro
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])# Transforma texto en número
onehotenconder = OneHotEncoder(categorical_features=[0])
X = onehotenconder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) # No: 0 Yes: 1

#Dividir el dataset en conjunto de entrenamiento y conjunto de testing
"""
Dividir los datos entre entrenamiento y testing
-test_size = tamaño del conjunto de testing en porcentaje (20-30% para 
testing) Entre más datos se tienen para entrenar
-random_state = numero para poder reproducir el algoritmo, para que siempre
devuelva el mismo resultado.
-El modelo va a ser capaz de hacer predicciones.
-Cuando no hace buenas predicciones se habla de sobreajuste o overfitting
"""
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2,
                                                    random_state = 0)
# Escalado de variables
"""
StantardScaler 
-Cuando se toman los datos de entrenamiento hay variables Dummy
- Las variables dummy se escalan para que se comporten del mismo modo.
- No hay escalarlas ya que se pierde la nocion a la que representa 
la categoría.
- No hay que estandarizar los datos de algoritmos de compra o no compra.
Si existen otro tipos de datos 
"""

"""
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
"""





