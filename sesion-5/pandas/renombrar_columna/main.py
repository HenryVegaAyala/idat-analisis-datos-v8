import pandas as pd

data = pd.read_csv("data_ventas_enero.csv")

data["total"] = data["cantidad"] * data["precio_unitario"]

print(data)

data.rename(columns={"total": "precio_total"}, inplace=True)
data.rename(columns={"vendedor": "nombre_vendedor"}, inplace=True)

print(data)