class Ciudadano:
    def __init__(self, nombre, profesion, telefono):
        self.nombre = nombre
        self.profesion = profesion
        self.telefono = telefono
    def saludar(self):
        print(f"Hola, soy {self.nombre}. Mi profesion es {self.profesion}" 
        + f", mi telefono es {self.telefono}")

class Medico(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "medico", "5559")

class Policia(Ciudadano):
    def __init__(self, nombre):
        super().__init__(nombre, "policía", "000")

persona1 = Ciudadano("Carlos", "Cirujano", "789")
persona2 = Medico("Juan") 
persona3 = Policia("Sergio")

persona1.saludar()
persona2.saludar()
persona3.saludar()

#a = Medico("Luis", "Maestro")
#b = Ciudadano("Hernan", "Informatica")
#
#a.saludar()
#b.saludar()
#