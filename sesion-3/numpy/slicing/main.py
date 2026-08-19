import numpy as np

lista = [10, 20, 30, 40, 50]
array = np.array(lista)

# Slicing
rango = array[1:4]
print(rango)

# Slice
rango[0:2] = 0
print(rango)