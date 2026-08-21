import pandas as pd

data = pd.read_csv("dataset.txt")

# Paso 1: Implementar filtrado
busqueda_por_tienda = data["Store ID"] == 8091

# Paso: Aplicar el filtro
resultado = data[busqueda_por_tienda]

print(resultado)