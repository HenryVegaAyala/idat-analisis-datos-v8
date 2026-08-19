import numpy as np

lista = [1500, 2300, 1800, 2100, 2500]
array = np.array(lista)

# Venta total de la semana
venta_total = np.sum(array)
print(f"La venta total de la semana es {venta_total}.")

# Promedio diario
promedio = np.mean(array)
print(f"El promedio de venta diario es {promedio}.")

# Venta más alta
venta_maxima= np.max(array)
print(f"La venta más alta de la semana es {venta_maxima}.")