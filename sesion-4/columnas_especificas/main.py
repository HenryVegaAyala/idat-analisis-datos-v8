import pandas as pd

dataframe = pd.read_csv("data_enero.csv")

# Solo obtener una columna
print(dataframe["producto"])

# Multiples columnas
print(dataframe[["producto", "precio_unitario"]])