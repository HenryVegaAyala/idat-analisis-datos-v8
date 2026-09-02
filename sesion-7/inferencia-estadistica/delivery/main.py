import pandas as pd
import scipy.stats as st
import numpy as np

df = pd.read_csv("tiempos_de_entrega_delivery.csv")

vehiculo_tradicional = df[df["vehiculo"] == "Tradicional"]["minutos"]
vehiculo_electrico = df[df["vehiculo"] == "Electrica"]["minutos"]

# Paso 1: Desviación estandar para vehiculos tradicionales.
ic_tradicional = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_tradicional) - 1,
    loc=np.mean(vehiculo_tradicional),
    scale=st.sem(vehiculo_tradicional),
)

print(f"Rangos del intervalo de confianza del vehiculo tradicional: {ic_tradicional[0]:.2f} y {ic_tradicional[1]:.2f}")
print(f"Promedio del vehiculo tradicional {np.mean(ic_tradicional)}")

# Paso 1: Desviación estandar para vehiculos electricos.
ic_electrico = st.t.interval(
    confidence=0.95,
    df=len(vehiculo_electrico) - 1,
    loc=np.mean(vehiculo_electrico),
    scale=st.sem(vehiculo_electrico),
)

print(f"Rangos del intervalo de confianza del vehiculo electrico: {ic_electrico[0]:.2f} y {ic_electrico[1]:.2f}")
print(f"Promedio del vehiculo electrico {np.mean(ic_electrico)}")


# Paso 2: Prueba de test A/B
resultado = st.ttest_ind(vehiculo_tradicional, vehiculo_electrico)
print(f"Valor P: {resultado.pvalue:.4f}")

# Paso 3: Interpretación
if resultado.pvalue < 0.05:
    print(f"Existe una diferencia significativa entre ambos vehiculos")
else:
    print(f"No Existe una diferencia significativa")