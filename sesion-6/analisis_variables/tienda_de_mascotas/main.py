import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv("tienda_de_mascotas.csv")

# Calcular la Moda de las categorías
moda_categoria = df['categoria'].mode()[0]
print("La moda de las categorías es:", moda_categoria)

# Calcular el Promedio de los precios
promedio_precio = df['precio'].mean()
print("El precio promedio es:", promedio_precio)

