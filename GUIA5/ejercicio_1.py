"""Leer números que representan edades de un grupo de personas, finalizando la
lectura cuando se ingrese el número -1. Imprimir cuántos son menores de 18
años, cuántos tienen 18 años o más y el promedio de edad de ambos grupos.
Descartar valores que no representan una edad válida. (Se considera válida una
edad entre 0 y 100)."""
edad = 0
mayor_edad = 18
total_menor_edad = 0
total_mayor_edad = 0
suma_menor_edad = 0
suma_mayor_edad = 0
while edad != -1:
    edad = int(input("Ingrese la edad de la persona entre 0 y 100 años, para finalizar la lista ingrese -1: "))
    while (edad < 0 or edad > 100) and edad != -1:
        edad = int(
            input("Edad incorrecta. Ingrese la edad de la persona 0 y 100 años, para finalizar la lista ingrese -1: "))
    if edad >= mayor_edad:
        suma_mayor_edad += edad
        total_mayor_edad += 1
    elif edad < mayor_edad and edad != -1:
        suma_menor_edad += edad
        total_menor_edad += 1
if total_menor_edad > 0:

    promedio_menor_edad = suma_menor_edad / total_menor_edad
else:
    promedio_menor_edad = 0

if total_mayor_edad > 0:

    promedio_mayor_edad = suma_mayor_edad / total_mayor_edad
else:
    promedio_mayor_edad = 0

print("Hay ", total_mayor_edad, "personas mayores de edad. La edad promedio de este grupo es: ", promedio_mayor_edad)
print("Hay ", total_menor_edad, "personas menores de edad. La edad promedio de este grupo es: ", promedio_menor_edad)
