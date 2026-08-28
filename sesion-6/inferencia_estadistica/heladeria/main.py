import pandas as pd
import numpy as np
import scipy.stats as st

# 1. Leer archivos
df = pd.read_csv("heladeria_gastos.csv")

dato_gastos_mes = df["gasto"]

# 2. calcular el intervalo de confianza al 95%

# Calcular el intervalo
intervalo = st.t.interval(
    confidence=0.95,              # porcentaje de intervalo de confianza
    df=len(dato_gastos_mes),      # Ajustes de cantidad de datos
    loc=np.mean(dato_gastos_mes), # media de los datos -> promedio
    scale=st.sem(dato_gastos_mes) # error estandar de la media
)

print(f"El cliente en promedio gasta entre S/.{intervalo[0]:.2f} y S/.{intervalo[1]:.2f}")

# Punto medio
promedio = (intervalo[0] + intervalo[1]) / 2
print(f"El promedio de gasto es: S/.{promedio:.2f}")

# margen de error
print(promedio - intervalo[0])
print(intervalo[1] - promedio)