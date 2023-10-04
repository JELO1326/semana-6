class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        print(f"Empleado genérico: Realiza tareas generales.")

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        super().describir_rol()
        print(f"Gerente: Maneja el departamento {self.departamento}")

class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        super().describir_rol()
        print(f"Ingeniero: Especializado en {self.especialidad}")

class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, tarea):
        super().__init__(nombre, edad, salario)
        self.tarea = tarea

    def describir_rol(self):
        super().describir_rol()
        print(f"Asistente: Realiza tareas de {self.tarea}")


gerente = Gerente("Jose", 40, 80000, "Ventas")
ingeniero = Ingeniero("Jonathan", 30, 60000, "Software")
asistente = Asistente("Bob", 25, 40000, "Administración")

gerente.describir_rol()
ingeniero.describir_rol()
asistente.describir_rol()
