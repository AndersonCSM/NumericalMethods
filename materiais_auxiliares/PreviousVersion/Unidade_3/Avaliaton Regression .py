# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy import log as ln, exp

df = pd.read_csv("https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv")

size = df['country'].count()
countries = []
for i in range(size):
    if df['country'][i] not in countries:
        countries.append(df['country'][i])

x_old = []
y_old  = []
for i in range(size):
    if df['country'][i] == 'Brazil':
        x_old.append(df['year'][i])
        y_old.append(df['co2'][i])

x = np.array(x_old, dtype= np.float64)
y = np.array(y_old, dtype = np.float64)


def plot_grafico(x, y, fun):
    plt.scatter(x, y, color = 'm', marker = 'o', s = 30)
    
    y_pred = eval(fun)
    
    plt.plot(x, y_pred, color='g')
    
    plt.xlabel('year')
    plt.ylabel('Co2')
    plt.title('Co2 x year in Brazil')
    plt.show()
    
import minimos_quadrados as mq

x_new = x/max(x)
y_new = y/max(y)

import warnings
warnings.filterwarnings('ignore')

#fun = mq.Regressão_Linear(x, y, True)
#fun = mq.Regressão_Exponencial(x, y, True)
fun = mq.Regressão_potência(x, y, True)
#fun = mq.Regressão_logaritmica(x, y, True)

plot_grafico(x, y, fun)
