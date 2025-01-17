import matplotlib
import statistics as sta
import pandas as pd 


import statsmodels.api as sm

import numpy as np
from sklearn.linear_model import LinearRegression
# La regresión lineal es la recta más adecuada en un conjunto de puntos tenemos
# definir la variable dependiente y la independiente

mes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
gastos =[1000, 4000, 5000, 4500, 3000, 4000, 9000, 11000, 15000, 12000, 7000, 3000]
ventas =[9914, 40487, 54324, 50044, 34719, 42551, 94871, 118914, 158484, 131348, 78504, 36284]

# La lista con columnas específicas
df = pd.DataFrame(list(zip(mes, gastos, ventas)), columns = ['mes', 'gastos', 'ventas'])

# Mostrar los datos del Data Frame
print(df)

# Definir la variable independiente y dependiente

y = np.array(df['gastos'])
x = np.array(df['ventas']).reshape(-1,1)

# Hallar el coeficiente de determinación R^2 es un valor entre 0 y 1, donde 1 es el ajuste perfecto

# Crear un modelo de regresión lineeal
modelo = LinearRegression().fit(x,y)

# Encontrar R^2

r_sq = modelo.score(x,y)
print('coeficiente de determinación:', r_sq)

# Usar .predict y darle un valor a x
print(modelo.predict(np.array([39000]).reshape(-1,1)))