import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("datos_salarios.csv")

x = df[["experiencia", "estudios"]]
y = df["salario"]

modelo = LinearRegression()
modelo.fit(x, y)

experiencia = input("Introduce los años de experiencia: ")
estudios = input("Introduce los años de estudios: ")

prediccion = pd.DataFrame([[experiencia, estudios]], columns=["experiencia", "estudios"])

resultado = modelo.predict(prediccion)

print(f"Salario sugerido S/. {resultado[0]:.2f}")
