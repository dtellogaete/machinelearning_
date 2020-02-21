# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:37:23 2020

@author: Daniel
"""

# Upper Confidence Bound (UCB)

# Importar las librerías
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargar el dataset
dataset = pd.read_csv("Ads_CTR_Optimisation.csv")

# Algoritmo de UCB
import math
N = 10000
d = 10
number_of_selections = [0]*d
sum_of_rewards = [0]*d
ads_selected = []
for n in range(0,N):
    max_upper_bound = 0
    for i in range(0,d):
        average_rewards = sum_of_rewards[i]/number_of_selections[i]
        delta_i = math.sqrt(3/2*math.log(n+1)/number_of_selections[i])
        upper_bound = average_rewards + delta_i
        if upper_bound > max_upper_bound:
            max_upper_bound = upper_bound
        
        


