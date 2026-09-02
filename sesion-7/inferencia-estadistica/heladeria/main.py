import pandas as pd
import numpy as np
import scipy.stats as st

# 1. Leer y cargar datos
df = pd.read_csv("heladeria_gastos.csv")
datos_gasto = df["gasto"]

# 2. Calcular el intervalo de confianza del 95%
intervalo = st.t.interval(
    confidence=0.95,          # Nivel de confianza al 95%
    df=len(datos_gasto) - 1,  # Grados de libertad
    loc=np.mean(datos_gasto), # Media o promedio de los gastos
    scale=st.sem(datos_gasto) # Error estandar de la media
)

# 3. Obtener los limites del intervalo
limite_inferior = intervalo[0]
limite_superior = intervalo[1]

print(
    f"Con un 95% de confianza, el gasto promedio se encuentra "
    f"entre S/.{limite_inferior:.2f} "
    f"y S/.{limite_superior:.2f}"
)

# 4. Calcular le promedio
promedio = np.mean(datos_gasto)
print(f"El gasto promedio es: S/.{promedio:.2f} ")

# 5. Calcular el margen de error
margen_error = limite_superior - promedio
print(f"El margen de error es: S/.{margen_error:.2f}")