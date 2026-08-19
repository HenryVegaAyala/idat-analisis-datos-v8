class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def actualizar_stock(self, cantidad):
        self.stock = self.stock + cantidad
        print(f"El producto {self.nombre} con el precio {self.precio} se actualizo con {cantidad}, ahora tienen {self.stock} unidades")

producto = Producto("Laptop", 2000, 100)

# La empresa idat ha comprado 10 laptops
producto.actualizar_stock(-10)

# La empresa Nova ha comprado 30 laptops
producto.actualizar_stock(-30)

# Se ha comprado 10 unidades mas para el stock
producto.actualizar_stock(10)