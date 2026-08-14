# 1. Crear una lista de productos: Ejemplo de una lista de cadenas
panaderia = ["pan", "croissant", "baguette", "donut", "muffin"]
# print(panaderia)

# 2. Ejemplo de una lista de números: Ventas por hora
ventas_hora = [10, 20, 15, 30]

# 3. Ejemplo de valores mixtos
valores_mixtos = [10, 20, 20, 50, "Hola", True, 95.60]

# 4. Acceder a un elemento de una lista basada en indice
producto_escogido = panaderia[3]
#print(f"Producto seleccionado de la lista: {producto_escogido}")

# 5. Acceder al último elemento de una lista
ultimo_producto = panaderia[-1]
# print(f"Último producto de la lista: {ultimo_producto}")

# 6. Agregar un nuevo producto a la lista
panaderia.append("aceite")
print(f"Lista de productos y agregados: {panaderia}")

# 7. Cambiar o actualizar producto de la lista
panaderia[5] = "aceite de oliva"
print(f"Lista de productos y actualizados: {panaderia}")

# 8. Eliminar un producto de la lista
panaderia.remove("baguette")
print(f"Lista de productos y eliminados: {panaderia}")

# 9. Eliminar un producto basado en el indice de una lista
del panaderia[2]
print(f"Lista de productos y eliminados por indice: {panaderia}")

# 10. Obtener la cantidad de productos de una lista
total_productos = len(panaderia)
print(f"Total de productos: {total_productos}")