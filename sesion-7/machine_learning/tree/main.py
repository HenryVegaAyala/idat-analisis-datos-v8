import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("dato_credito.csv")

x = df[["ingreso", "morosidad"]]
y = df["aprobado"]

# División de datos
# -----------------------------------------------------------
x_entrenamiento, x_prueba, y_entrenamiento, y_prueba = train_test_split(
    x,
    y,
    test_size=0.20,
    random_state=42
)

modelo = DecisionTreeClassifier()
modelo.fit(x_entrenamiento, y_entrenamiento)

prediccion = modelo.predict(x_prueba)

# Este dataframe sirve para pruebas y calcular el porcentaje de aciertos
comparacion = pd.DataFrame({
    "real": y_prueba.values,
    "prediccion": prediccion
})

aciertos = (comparacion["real"] == comparacion["prediccion"]).sum()

total = len(comparacion)
precision = aciertos / total

print(f"Precisión del modelo {(precision * 100):.2f}")
# -----------------------------------------------------------

# Prediccion

ingreso = input("ingreso del cliente: ")
morosidad = input("morosid del cliente: ")

predicion_credito_aprobado = pd.DataFrame([[ingreso, morosidad]], columns=["ingreso", "morosidad"])
resultado = modelo.predict(predicion_credito_aprobado)

if resultado[0] == 1:
    print("El credito fue aprobado")
else:
    print("El credito no fue aprobado")