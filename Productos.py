class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        print(f"Nombre: {self.nombre}\nPrecio: {self.precio}\nCategoría: {self.categoria}")

class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, marca):
        super().__init__(nombre, precio, categoria)
        self.marca = marca

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Marca: {self.marca}")

class Alimenticio(Producto):
    def __init__(self, nombre, precio, categoria, caducidad):
        super().__init__(nombre, precio, categoria)
        self.caducidad = caducidad

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Caducidad: {self.caducidad}")

class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, talla):
        super().__init__(nombre, precio, categoria)
        self.talla = talla

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Talla: {self.talla}")


electronico = Electronico("Laptop", 1000, "Electrónico", "Dell")
alimenticio = Alimenticio("Manzanas", 2, "Alimenticio", "2023-01-01")
vestimenta = Vestimenta("Camisa", 20, "Vestimenta", "M")

electronico.mostrar_detalle()
alimenticio.mostrar_detalle()
vestimenta.mostrar_detalle()
