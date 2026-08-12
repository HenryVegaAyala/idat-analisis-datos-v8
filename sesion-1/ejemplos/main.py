# 1. Texto simple -> string
negocio = "Café Python!"

# 2. Texto con comilla simple -> string
slogan = 'El mejor café de la ciudad'

# 3. número entero -> int
sillas_disponibles = 30

# 4. número decimal -> float
precio_cafe = 3.55

# 5. Valor booleano -> bool (True)
esta_abierto = True

# 6. Valor booleano -> bool (False)
tiene_wifi = False

# 7. Texto largos
direccion = "Avenida angamos 635, Miraflores, Lima, Perú"

# 8.número como texto
codigo_postal = "500"

# 9. Variables vacias
proxima_oferta = None

# 10. Variables con caracteres especiales
emoji_cafe = "☕"

# 11. Multiplicador de cadenas
print("-" * 100)

# 12. Concatenar variables
concatenar_v1 = negocio + " " + slogan
print(concatenar_v1)

concatenar_v2 = f"{negocio} {slogan}"
print(concatenar_v2)

# 13. Concatenización final
print(f"Ejemplo del 1-12: Bienvenido a {concatenar_v2} {emoji_cafe}, me ubico en {direccion}")

