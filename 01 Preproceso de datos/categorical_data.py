# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 01:12:52 2019
@author: Daniel

Solo para tratamiento de datos categóricos
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

#Codificar datos categóricos

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() # No necesita ningún parámetro
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])# Transforma texto en número
onehotenconder = OneHotEncoder(categorical_features=[0])
X = onehotenconder.fit_transform(X).toarray()
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y) # No: 0 Yes: 1