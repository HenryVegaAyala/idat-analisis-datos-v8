import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

clientes = pd.read_csv("clientes.csv")
ventas = pd.read_csv("ventas.csv")

consolidado = pd.merge(
    ventas,
    clientes,
    on="id_cliente",
    how="outer" # right, left, outer, inner
)

print(consolidado)