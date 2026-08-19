import numpy as np

# Esto es un array de valores
edades = np.array([10, 30, 15, 40, 45, 17, 55, 16])

# Filtrado por edad mayor o igual a 18.
mayor_de_edad = edades >= 18
print(mayor_de_edad)

# Aplicar el filtrado
resultado = edades[mayor_de_edad]
print(f"Edades mayor de edad: {resultado}")