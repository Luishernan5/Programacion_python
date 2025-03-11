class Usuario:
    # Atributos de instancia:
    # Self es un parametro y se puede cambiar por otra palabra
    def __init__(self, nombre, apellidos, edad, direccion, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad 
        self.direccion = direccion
        self.telefono = telefono

    def iniciar_sesion(self):
        print(f"El usuario {self.nombre} ha iniciado sesión.")
    def cerrar_sesión(self):
        print("El usuario ha cerrado sesión.")
    def cambiar_nombre_perfil(self):
        print("Se cambio el nombre.")

# Estado inicial de los atributos de instancia:
usuario_1 = Usuario("Luis", "Ramirez", 20, "Jilotepec", "5565656562")
usuario_2 = Usuario("Hernan", "Ortiz", 20, "Soyaniquilpan", "5565656511")

#Usuario.iniciar_sesion(usuario_1)
#
#usuario_1.iniciar_sesion()

usuario_2.iniciar_sesion()
usuario_1.iniciar_sesion()