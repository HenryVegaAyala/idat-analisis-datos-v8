import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Carga de los datos
df = pd.read_csv("ventas_marketing.csv")

# 2. Variable independiente (X)
x = df[["marketing"]] # Dataframe de una sola columna

# 3. Variable dependiente (Y)
y = df["ventas"] # Serie con los valores a predecir

# Modelo
modelo = LinearRegression()
modelo.fit(x, y) # Se encarga de entrenar el modelos con los datos de marketing y ventas

variable_a_predecir = input("Ingrese la inversión de marketing: ")

# Crear un dataframe con el nuevo valor de marketing
nueva_prediccion = pd.DataFrame([[variable_a_predecir]], columns=["marketing"])

# Realizar la predicción
prediccion = modelo.predict(nueva_prediccion)

print(f"La predicción de ventas  para una inversión de ${variable_a_predecir} en marketing: {prediccion[0]:.2f}")
