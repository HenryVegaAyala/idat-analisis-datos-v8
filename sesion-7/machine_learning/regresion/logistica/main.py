import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("datos_fuga.csv")

x = df[["antiguedad", "cuota_mensual"]]
y = df["fuga"]

modelo = LogisticRegression()
modelo.fit(x, y)

antiguedad = input("Introduce la antiguedad: ")
cuota_mensual = input("Introduce la cuota mensual: ")

prediccion = pd.DataFrame([[antiguedad, cuota_mensual]], columns=["antiguedad", "cuota_mensual"])

resultado = modelo.predict(prediccion)

if resultado[0] == 1:
    print("El cliente se va ir.")
else:
    print("El cliente no se va ir.")