import pandas as pd

data = {
    "nombre": ["Maria", "Juan", "Carlos"],
    "edades": [20, 23, 25]
}

df = pd.DataFrame(data)

print(f"Ejemplo de un dataframe:")
print(df)

data = [20, 60, 50, 90, 60]

serie = pd.Series(data)

print(f"Ejemplo de un serie:")
print(serie)
