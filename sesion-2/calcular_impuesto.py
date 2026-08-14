def calcular_precio_final(precio_base: float | int):
    igv = 0.18
    impuesto = precio_base * igv
    total = precio_base + impuesto
    return total


print("-" * 100)
print("Calcular el precio final de su producto")
print("-" * 100)

precio_base = float(input("Introduce el precio base: "))
resultado_precio_final = calcular_precio_final(precio_base)
print(f"Resultado final: {resultado_precio_final}")

listado_de_precio_base = [150, 200, 20, 5]

for precio_base in listado_de_precio_base:
    resultado = calcular_precio_final(precio_base)
    print(f"Resultado final: {resultado}")