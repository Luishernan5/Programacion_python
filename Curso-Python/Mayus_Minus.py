"""
Ejercicio 19: Pasar una cadena de mayusculas a 
minusculas.
"""

var = True
while var: 
    mayus = input("Ingresa una cadena en mayusculas (0 para salir):")
    if mayus == "0":
        print("Saliendo....")
        var = False
    else: 
        print("Tu cadena original es:", mayus)
        minus = mayus.lower()
        print("Tu cadena en minusculas es: ", minus)
        print("------------------------------------------")