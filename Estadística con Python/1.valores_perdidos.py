import matplotlib
import statistics as sta
import pandas as pd
import numpy as np

stocks = [[2015, 1, 1.88], [2015, 2, 0.59], [2015, 3, 0.35], [2015, 4], [2016, 2, 0.92], [2016, 3, 0.17], [2016, 4, 2.66]]
df2 = pd.DataFrame(stocks, columns=['year', 'qtr', 'return'])
print(df2)
print(df2.isna())

"""
NaN (Not a Number) es un marcador estándar de valores perdidos utilizado en pandas para tipos de datos float.
None es el objeto singleton de Python que se utiliza a menudo para los datos que faltan en el código Python.
NaT (Not a Time) se utiliza en pandas para representar valores perdidos para tipos de datos datetime.
Con Pandas 1.0 se introdujo un nuevo tipo de datos perdidos NA, que es una representación de valores perdidos de tipo entero.

"""