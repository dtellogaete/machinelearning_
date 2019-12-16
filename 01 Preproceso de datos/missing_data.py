# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 01:13:55 2019
@author: Daniel

En caso de datos faltantes, NA
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

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values="NaN", strategy="mean", axis = 0)
imputer.fit(X[:, 1:3]) #fit para aplicar el imputer, 1 incluye/3 excluye
X[:, 1:3] = imputer.transform(X[:,1:3]) #Transforma valores desconocidos
