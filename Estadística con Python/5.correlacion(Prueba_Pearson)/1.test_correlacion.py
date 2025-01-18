import matplotlib
import statistics as sta
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

'''
Prueba de correlación
La correlación es un método estadístico para medir y describir la relación entre dos variables.
Nota: a diferencia de las pruebas t-test o ANOVA, no compara las diferencias entre grupos, sino que comprueba las relaciones entre dos variables.
Correlación de Pearson: mide la dirección y la fuerza (= grado) de la relación lineal entre dos variables.
El resultado siempre tiene un valor entre -1 y 1.
'''

# Dado el conjunto de datos
x=[27, 32, 38, 94, 70, 29, 17, 8, 48, 82, 52, 14, 91, 22, 58, 96, 73, 99, 75, 76]
y=[78, 35, 28, 75, 2, 22, 25, 17, 72, 45, 86, 96, 24, 41, 73, 51, 58, 76, 90, 77]
 
# Convertir los datos en DataFrame
data = pd.DataFrame (x,y)
 
# Aplicar la correlación de pearsonr()
corr, _ = pearsonr(x, y)
print('Correlación de Pearsons: %.3f' % corr)