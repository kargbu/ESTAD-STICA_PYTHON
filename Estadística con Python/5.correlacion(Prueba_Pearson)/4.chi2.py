'''
En la biblioteca de estadística de scipy, podemos llamar a dos comandos de prueba de
chi-cuadrada. Uno de ellos es chisquare y el otro chi2_contingency. El primero es 
usado cuando queremos ver si el dato de una variable se distribuyen uniformemente o no.
Para ello, se comprueba lo bien que se ajustan los datos. EL chisquare devuelve el estadístico
chi-cuadrado y el valor p cuando ejecutamos el comando.
Para chi2_contingency es usado cuando la hipótesis nula es: dos grupos no tienen diferencias
significativas. Este comando devuelve el estadístico chi-cuadrado, el valor p. los grados de
libertad y la tabla de observaciones esperadas. Ahora, el valor p es mayor que nuestro
umbral, aceptamos la hipótesis nula. Si aceptamos la hipótesis nula, podemos concluir que 
no existe una diferencia estadística significativa entre dos grupos.
'''
import matplotlib
import statistics as sta
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt

# Definimos la tabla
datos = [[27, 32, 38, 94, 70, 29, 17, 8], [78, 35, 28, 75, 2, 22, 25, 17]]
stat, p, dof, expected = chi2_contingency(datos)
print(stat)
print(p)
print(dof)
print(expected)