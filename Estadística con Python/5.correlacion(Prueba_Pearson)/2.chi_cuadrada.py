'''
Pruebas paramétricas son pruebas sobre parámetros poblacionales
Prueba T, ANOVA, Correlación, Regresión.
La pruebas NO paramétricas se refieren a pruebas que tienen como objetivo las
proporciones/frecuencias de la población.
Pruebas Chi-cuadrada
La prueba Chi-cuadrado de Pearson se utiliza para determinar si dos conjuntos 
independientes de datos están asociados entre sí. La prueba Chi-cuadrado se utiliza
mejor para datos categóricos como sexo/género, día de la semana, etc. Esto se determina
utilizando el valor p que se calcula a partir de la prueba. Un valor p inferior o igual 
a 0,05 significa que los conjuntos de datos están asociados entre sí, mientras que un 
valor p superior significa que los conjuntos de datos no están asociados entre sí. 
El chi-cuadrado no requiere el cumplimiento de supuestos específicos sobre 
los parámetros de la población.
Utilizaremos la biblioteca chi2_contingency de scipy.stats.
'''
import matplotlib
import statistics as sta
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Definimos la tabla
datos = [[18, 25, 32, 22, 33], [30,30,30,30,30]]
print(chisquare(datos[0],datos[1]))