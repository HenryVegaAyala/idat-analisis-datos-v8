class Cliente:
    def __init__(self, nombre, saldo_inicial):
        self.nombre = nombre
        self.saldo_inicial = saldo_inicial

    def comprar(self, monto):
        if self.saldo_inicial >= monto:
            self.saldo_inicial = self.saldo_inicial - monto
            print(f"{self.nombre} ha comprado por S/.{monto}. Saldo restante: S/.{self.saldo_inicial}")
        else:
            print(f"{self.nombre} no tiene suficiente saldo para comprar por S/.{monto}")

# Instanciar la clase
cliente_1 = Cliente("Juan", 1200)
cliente_1.comprar(750) # se ha comprado un celular
cliente_1.comprar(400) # Se ha comprado una laptop
cliente_1.comprar(100) # Se ha comprado un case