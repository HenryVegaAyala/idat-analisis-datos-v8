import pandas as pd
import glob

# Buscar todos los archivos con extensión csv automaticamente
buscar_archivos = glob.glob("data/ventas_*.csv")

print(f"Cantidad de archivos encontrados: {len(buscar_archivos)}")

data_frames = [] # Variable global

for archivo in buscar_archivos:
    # archivo = data\ventas_*.csv
    df = pd.read_csv(archivo)
    data_frames.append(df)

consolidado = pd.concat(data_frames, ignore_index=True)

consolidado.to_csv("resultado/consolidado_trimestral.csv")