"""
Ejercicio 17: Calcular una potencia sin usar
el doble asterisco.
"""
var = True
while var:
    print("-------------------------------------------------")
    num = int(input("Ingresa el numero a elevar (0 para salir): "))
    if num != 0:
        pot = int(input("Ingresa la potencia: "))
        resultado = pow(num, pot)
        print("El resultado es: ", resultado)
    else:
        print("Saliendo ....")
        break