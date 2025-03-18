"""
Ejercicio 18: Extrae una subcadena de una cadena dada.
"""
var = True
while var:
    cadena = (input("Ingresa tu cadena (0 para salir): "))
    if cadena != "0":
        print("Tu cadena original es: ", cadena)
        subcadena = cadena[1:2]
        print("Tu subcadena es: ", subcadena)
        print("----------------------------------")
    else:
        print("Saliendo....")
        var = False