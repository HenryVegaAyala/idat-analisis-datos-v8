import pandas as pd

# Lectura de un archivo csv
df = pd.read_csv("data_enero.csv")
print(df)

# Lectura de un archivo xlsx
df = pd.read_excel("ejemplo_excel.xlsx")
print(df)
