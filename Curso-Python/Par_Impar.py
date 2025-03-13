var = True
while var:
    print("---------------------------------------------")
    num1 = int(input("Ingresa un numero (0 para salir): "))
    if num1 == 0:
        print("Saliendo")
        break
    if num1 % 2 == 0:
        print("Es par")
    else: 
        print("Es impar")
