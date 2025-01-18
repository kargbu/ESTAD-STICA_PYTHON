import matplotlib
import statistics as sta
import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

#given data

x=[27, 32, 38, 94, 70, 29, 17, 8, 4,3 ]
y=[56, 45, 40, 10, 22, 33, 75, 85, 90,95]

datos = pd.DataFrame(x,y)
corr,_= pearsonr(x,y)
print('El test de la correlación de Pearson es:%.4f' % corr)