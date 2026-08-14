def convertir_a_soles(monto_dolares: float | int, tipo_de_cambio: float = 3.80):
    return monto_dolares * tipo_de_cambio


monto_dolares = float(input("Introduce el monto de dolares: "))
tipo_de_cambio = input("Introduce el tipo de cambio por defecto es [3.80]: ")

if tipo_de_cambio == "": # comparativo de lo que recibo por consola y lo comparo con un cadena vacia que es doble comilla
    resultado_tipo_de_cambio = convertir_a_soles(monto_dolares)
else:
    tipo_de_cambio = float(tipo_de_cambio)  # formatear el tipo de dato de cadena a numero
    resultado_tipo_de_cambio = convertir_a_soles(monto_dolares, tipo_de_cambio)

print(f"El resultado del tipo es cambio es: {resultado_tipo_de_cambio}")