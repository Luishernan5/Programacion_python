class Vehiculo():
    # Atributo:
    color = None # No hay valor nulo (None)
    longitud_m = None
    ruedas = 4
    velocidad_maxima = 0

    # Metodos: 
    def arrancar(self):
        print("El motor ha arrancado.")
    
    def detener(self):
        print("El motor está detenido.")

# Instanciamos dos objetos de tipo Vehiculo
objeto_vehiculo1 = Vehiculo()
objeto_vehiculo2 = Vehiculo()
#
#objeto_vehiculo1.color = "Black"
#objeto_vehiculo2.color = "Red"
#
#
#print(objeto_vehiculo1.color)
#print(objeto_vehiculo2.color)
#
#objeto_vehiculo3 = Vehiculo()
#
#print(objeto_vehiculo3.color)

objeto_vehiculo1.velocidad_maxima = 161
print(objeto_vehiculo1.velocidad_maxima)

print(objeto_vehiculo2.velocidad_maxima)

objeto_vehiculo1.arrancar()


