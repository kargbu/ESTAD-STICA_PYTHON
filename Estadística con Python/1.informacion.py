import pandas as pd
import matplotlib.pyplot as plt
import statistics as sta

data = pd.read_csv('/Users/del_mal/Desktop/COURSERA/Estadística con Python/Estadística con Python/data_inc.csv')

for col in data.columns:
    print(col)

# print(data.info)

# Contar el número de modalidades del delito
print(data['modalidad_delito'].value_counts())

# Contar el número de valores 'VIOLACION' en la columna 'modalidad_delito' 
num_violaciones = data['modalidad_delito'].value_counts()['VIOLACION']

print(f"Número de violaciones: {num_violaciones}")

print(data.value_counts(['modalidad_delito', 'colonia_hechos']))

# Convertir la columna 'hora_de_inicio' a tipo numérico 
data['hora_de_inicio'] = pd.to_numeric(data['hora_de_inicio'], errors='coerce')

print(sta.mean(data.hora_de_inicio))
print(sta.median(data.hora_de_inicio))
print(sta.mode(data.hora_de_inicio))
print(max(data.hora_de_inicio)- min(data.hora_de_inicio))

# Para contar de una columna la media print(sta.mean(data[data['Zombies']==True].age))
#print(sta.mean(data[data['Zombies']==False].age) y para contar los infectados en la localidad