import matplotlib
import statistics as sta
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt


'''
Peter trabaja para una empresa de viajes compartidos llamada Rebu. 
Peter trabaja 5 días a la semana. Quiere saber cuál de los días tiene más clientes. 
Espera una distribución igual para los 5 días. 
El número de pasajeros observados y esperados figura en la tabla siguiente. 
Según los datos proporcionados, ¿los días con mayor número de pasajeros tienen la misma frecuencia?
(Utilice un nivel de significación de 0,05).
'''

#1.Necesitamos saber si la hipótesis es nula. H_0: tienen la misma frecuencia y H_1 desigual
#2.Determinar el grado de liberta. D_f=N-1, donde N es el tamaño de la muestra. En el problema D_f=4
#3.El valor significativo nos lo da el problema y es significance level=0.05. La región es 9.488
#4.Corremos la función chisquare(observed_Data,Expected_Data))

# Definimos la tabla
datos = [[18, 25, 32, 22, 33], [30,30,30,30,30]]
print(chisquare(datos[0],datos[1]))

'''
Nuestro valor de Chi-cuadrado calculado se encuentra en la zona de no rechazo. 
Por lo tanto, vamos a aceptar la hipótesis nula. Esta variación no es lo 
suficientemente significativa como para rechazar la hipótesis nula. Basándonos 
en el resultado, podemos decir que ocurren con frecuencias relativamente iguales.
'''