import pandas as pd
import scipy.stats as st

# 1. Leer y cargar la data
df = pd.read_csv("embalaje_puntaje.csv")

# 2. Separar los puntajes según el tipo de embalaje.
embajale_tradicional = df[df["embalaje"] == "A"]["puntuacion"] # Filtrado avanzado por embalaje del tipo A
embajale_ecologico = df[df["embalaje"] == "B"]["puntuacion"] # Filtrado avanzado por embalaje del tipo B

# 3. Calculo de test A/B
resultado = st.ttest_ind(embajale_tradicional, embajale_ecologico)

# 4. Mostrar el resultado
print(f"Valor P: {resultado.pvalue:.4f}")

if resultado.pvalue < 0.05:
    print(f"Rechazamos la hipotesiss nula, hay diferencia significativa entre los embalajes")
else:
    print("No hay diferencias significativas")