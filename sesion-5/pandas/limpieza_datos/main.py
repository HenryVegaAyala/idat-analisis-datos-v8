import pandas as pd

data = pd.read_csv("facturacion_datos.csv")

# Fillna -> Reemplazar por valores
data["id_cliente"] = data["id_cliente"].fillna("Desconocido")

print(data)
print("-" * 50)

# Dropna se encarga de eliminar todos los valores null
data_sin_nan = data.dropna()

print(data_sin_nan)
print("-" * 50)

# Drop_duplicates se encarga de eliminar valores duplicados

data_corregida = data_sin_nan.drop_duplicates()
print(data_corregida)
