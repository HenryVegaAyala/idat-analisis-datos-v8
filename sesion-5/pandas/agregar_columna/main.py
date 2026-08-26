import pandas as pd

data = pd.read_csv("data_ventas_enero.csv")

data["total"] = data["cantidad"] * data["precio_unitario"]

print(data)