import pandas as pd
from sklearn.cluster import KMeans

# lectura del archivo
df = pd.read_csv("datos_clientes.csv")

# usando solo las variables X o causas
x = df[["gasto_anual", "visitas_mes"]]

# modelo usando 2 agrupadores
modelo = KMeans(n_clusters=2)
modelo.fit(x)

# Seteo de los grupos
df["cluster"] = modelo.labels_

gasto_anual = input("Ingrese el gasto anual: ")
visitas_mes = input("Ingrese la cantidad de visitas mes: ")

agrupador = pd.DataFrame([[gasto_anual, visitas_mes]], columns=["gasto_anual", "visitas_mes"])
resultado = modelo.predict(agrupador)

# Resultado
agrupador["cluster"] = resultado[0]

# Carga de data + Data de predicción
print(pd.concat([df, agrupador], ignore_index=True))