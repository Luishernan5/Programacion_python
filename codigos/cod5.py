class Usuario():
    # Atributos de clase:
    hora_ultimo_inicio = None

    # Atributos de instancia:
    def __init__(self, nombre, apellidos, edad, telefono):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.telefono = telefono

        self.direccion = "Sin direccion"

    def iniciar_sesion():
        print("El usuario ha iniciado sesión.")
    def cerrar_sesion(self):
        print("El usuario ha cerrado sesión.")
    def cambiar_nombre_perfil(self):
        print("Se cambió el nombre.")

usuario1 = Usuario("Luis Hernán", "Ramírez", 18, "55555555")
print(usuario1.nombre)
print(usuario1.direccion)
# Reasignaciones:
usuario1.nombre = "Luis"
usuario1.hora_ultimo_inicio = "10/03/25"

# Probamos los atributos:
print(usuario1.nombre)
print(usuario1.hora_ultimo_inicio)

usuario1.iniciar_sesion()