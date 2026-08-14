def saludo_analista(nombre, apellido, edad):
    saludo = f"Hola {nombre} {apellido}!, como estás?, Mi edad es {edad}"
    return saludo

edad = input("Introduce su edad de Juan: ")
saludo_inicial = saludo_analista("Juan", "Perez", edad)
print(saludo_inicial)

edad = input("Introduce su edad de Roberto: ")
saludos_secundario = saludo_analista("Roberto", "Pino", edad)
print(saludos_secundario)