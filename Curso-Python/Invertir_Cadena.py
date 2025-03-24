"""
Ejercicio 13: Invertir una cadena.
"""
var = True
while var:
    cadena = input("ingresa una cadena (0 para salir): ")
    if cadena != "0":
        invertir = cadena[::-1]
        print(f"La cadena inversa de {cadena} es:", invertir)
    else:
        print("Saliendo....")
        break