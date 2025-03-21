"""
Ejercicio 3: Ingreso de califcaciones para las materias,
imprimir cada calificacion y calcular el promedio.
"""
materias = ["Español", "Matematicas", "Ingles", "Fisíca", "Desarrollo S"]
calificaciones = []
sumas_cal = 0

print("-------------------------------------------")
for materia in materias:
    for _ in range(1):
        calificacion = float(input(f"Ingresa tu calificacion de {materia}: "))
        calificaciones.append(calificacion)
        print(f"{materia}: {calificacion}")
        print("---------------------------------------------")
        sumas_cal += calificacion 
for i in range(len(materias)):
    print(f"{materias[i]}:{calificaciones[i]}")

print("-------------------------------------------")
promedio = sumas_cal / len(materias)
print("El Promedio es: ", promedio)