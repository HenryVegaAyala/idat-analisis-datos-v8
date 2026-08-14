# if: "Si pasa esto ..."
# elif: "Si no paso lo anterior, prueba esto"
# else: "Si nada cumple"

# Ejemplo con if - else
# edad = 15
#
# if edad >= 18:
#     print("La edad requerida tiene que se mayor a 18.")
# else:
#     print("La edad ingresada es menor que 18.")

# Ejemplo If elseIf else
nota = 11

if nota >= 18: # delimitamos la primera condicional
    print("Nota excelente")
elif nota >= 14: # delimitamos la segunda condicional
    print("Nota buena")
elif nota >= 12 and nota < 14:
    print("Nota regular")
elif nota >= 12 & nota < 11:
    print("Nota normal")
else: # Ninguna condicional anterior se cumple
    print("Nota insuficiente")