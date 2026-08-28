import pandas as pd

df = pd.read_csv("venta_casas.csv")

cantidad_nulos = df["precios"].isnull().sum()

print(f"Cantiad de regisros nullos: {cantidad_nulos}")

descripcion = df.describe()

print("-" * 60)

print(f"La cantiadd de nullos: {cantidad_nulos}")
print(f"Malores maiximos", descripcion)