import pandas as pd

data = pd.read_csv("../data_ventas_enero.csv")

# Eliminar filas del archivo en memoria
data.drop([3, 5], axis=0, inplace=True)
print(data)

# Eliminar columnas del archivo en memoria
data.drop(["id_venta", "vendedor"], axis=1, inplace=True)
print(data)
