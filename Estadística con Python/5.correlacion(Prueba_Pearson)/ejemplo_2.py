import matplotlib
import statistics as sta
import pandas as pd
from scipy.stats import pearsonr
from scipy.stats import chisquare
from scipy.stats import chi2_contingency
import matplotlib.pyplot as plt
from scipy.stats import chisquare


gender  = ['M', 'M', 'M', 'M', 'M']
test    = ['P', 'P', 'P', 'P', 'P']

datos = pd.DataFrame(list(zip(gender, test)), columns = ['Gender', 'Test'])
print(datos)


datos.replace('P', True,inplace=True)
datos.replace('N',False,inplace=True)
print(datos.value_counts(["Gender","Test"]))
stat, p, dof, expected = chi2_contingency(([20,5],[18,7]))

print(p)

