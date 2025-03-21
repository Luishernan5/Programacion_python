"""
Ejercicio 14: Reemplazar un carácter de una cadena.
"""

var = True
while var:
    cadena = input("Ingresa una cadena (0 para salir): ")
    if cadena != "0":
        nueva_cadena = cadena.replace("o", "x","y", "s")
        print(f"La nueva cadena de {cadena} es: ", nueva_cadena)
    else:
        print("Saliendo....")
        var = False