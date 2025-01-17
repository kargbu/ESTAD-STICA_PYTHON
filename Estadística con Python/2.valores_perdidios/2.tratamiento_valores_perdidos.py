""" 
Podemos eliminar una fila o columna con valores perdidos utilizando la función dropna()
El parámetro axis se utiliza para determinar si se eliminan filas o columnas:
0 elimina las filas que contienen el valor que falta
1 elimina las columnas que contienen el valor que falta
El parámetro how se utiliza para establecer la condición de eliminación.
how='any' : se elimina si falta algún valor
how='all' : elimina todos los valores que faltan
"""
import matplotlib
import statistics as sta
import pandas as pd
import numpy as np

mir =[['1',1,pd.NaT],['2',2,0.59],['3',pd.NaT,0.35], [pd.NaT,pd.NaT,pd.NaT]]
df3 = pd.DataFrame(mir,columns=['string','int','float'])
print (df3)
print(df3.dropna(0,'any'))