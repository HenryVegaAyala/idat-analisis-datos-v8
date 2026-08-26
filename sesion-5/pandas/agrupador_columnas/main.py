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
    how="left" # right, left, outer, inner
)

# Crear una nueva columna
consolidado["total"] = consolidado["precio"] * consolidado["cantidad"]

# Retornar columnas especificas
resultado = consolidado[["total", "pais", "nivel"]]

# Agrupador por pais y nivel
resultado_agrupacion = resultado.groupby(["pais", "nivel"])["total"].sum().reset_index()

print(resultado_agrupacion)