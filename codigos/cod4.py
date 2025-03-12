class Jugador():
    # Atributos:
    edad = None

    # Metodos:
    def permitir_acceso(self):
        print("Puedes entrar.")

    def denegar_acceso(self):
        print("No puedes entrar.")

    def comprobar_edad(self):
        if self.edad < 18:
            self.denegar_acceso()
        else:
            self.permitir_acceso()

# Objeto a partir de la clase :
jugador1 = Jugador()
jugador2 = Jugador()

jugador1.edad = 15
jugador2.edad = 60

jugador1.comprobar_edad()
jugador2.comprobar_edad()

