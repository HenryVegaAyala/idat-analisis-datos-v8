import pandas as pd

data = pd.read_csv("dataset.txt")

# Paso 1: Implementar filtro
busqueda_por_tienda = data["Store ID"] == 8091
unidades_vendidas = data["Units Sold"] <= 100

# Paso 2: Implementar filtro
resultado = data[busqueda_por_tienda & unidades_vendidas]

print(resultado)