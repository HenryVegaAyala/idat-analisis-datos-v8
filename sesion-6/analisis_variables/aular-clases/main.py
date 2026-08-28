import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("data_alumnos.csv")

# Calcular la Mediana
print(f"La mediana es {df["notas"].median()}.")

# Calcular la Media
print(f"La media es {df["notas"].mean()}.")

