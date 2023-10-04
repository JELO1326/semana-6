class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        pass  

class Perro(Animal):
    def sonido(self):
        return "Guau guau"

class Gato(Animal):
    def sonido(self):
        return "Miau miau"

class Pajaro(Animal):
    def sonido(self):
        return "Pío pío"


perro = Perro("doggy", 3)
gato = Gato("michi", 2)
pajaro = Pajaro("Tweety", 1)

print(perro.sonido())
print(gato.sonido())
print(pajaro.sonido())
