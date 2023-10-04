class Reserva:
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = numero_de_vuelo
        self.fecha = fecha

    def mostrar_detalle(self):
        print(f"Nombre del Pasajero: {self.nombre_del_pasajero}\nNúmero de Vuelo: {self.numero_de_vuelo}\nFecha: {self.fecha}")

class ReservaEconomica(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, asiento):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.asiento = asiento

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Asiento: {self.asiento}\nTipo de Reserva: Económica")

class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, servicio):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.servicio = servicio

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Servicio: {self.servicio}\nTipo de Reserva: Business")

class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, suite):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.suite = suite

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Suite: {self.suite}\nTipo de Reserva: Primera Clase")


reserva_economica = ReservaEconomica("John Doe", "ABC123", "2023-01-01", "A23")
reserva_business = ReservaBusiness("Jane Smith", "XYZ456", "2023-01-02", "VIP Lounge")
reserva_primera_clase = ReservaPrimeraClase("Bob Johnson", "DEF789", "2023-01-03", "Suite1")

reserva_economica.mostrar_detalle()
reserva_business.mostrar_detalle()
reserva_primera_clase.mostrar_detalle()
