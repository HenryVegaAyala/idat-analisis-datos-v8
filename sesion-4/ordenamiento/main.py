import pandas as pd

data = pd.read_csv("ventas_enero.csv")

# Caso 1: ordenamiento de menor a mayor

orden_caso_1 = data.sort_values("vendedor")
print(orden_caso_1)

print("-" * 30)

# Caso 2: ordenamiento de mayor a menor
orden_caso_2 = data.sort_values("producto", ascending=False)
print(orden_caso_2)

print("-" * 30)

# Caso 3: Ordenamiento multiple
orden_multiple = data.sort_values(["vendedor", "producto"], ascending=[False, True])
print(orden_multiple)