"""Ingresar un número N y validar que sea positivo. Luego:
a. Mostrar los primeros números impares, hasta alcanzar el número ingresado.
b. Informar la suma de esos números impares.
Ejemplo:
· Si se ingresa 5, se debe mostrar 1 3 5 y la suma es 9.
· Si se ingresa 8, se debe mostrar 1 3 5 7 y la suma es 16.
· Si se ingresa -5, se debe pedir otro número."""

numero = int(input("Ingresar un numero entero y positivo: "))
suma = 0
i = 1
while numero < 0:
    numero = int(input("Numero incorrecto. Ingresar un numero entero y positivo: "))

while i <= numero:
    if i % 2 != 0:
        print(i)
        suma += i

    i += 1

print("La suma es: ", suma)
