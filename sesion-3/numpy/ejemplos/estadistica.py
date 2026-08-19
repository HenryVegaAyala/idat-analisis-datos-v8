import numpy as np

lista = [1, 2, 3]

array = np.array(lista)

# Estadistica descriptiva

# Suma total
suma_total = np.sum(array)
promedio = np.mean(array)
maximo_valor = np.max(array)
desviacion = np.std(array)

print(f"La suma total es {suma_total}")
print(f"El promedio es {promedio}")
print(f"El maximo valor es {maximo_valor}")
print(f"El desviacion es {desviacion}")
