"""Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
un número entero N que representa una cantidad de días. Realizar un programa
que imprima la nueva fecha que resulta de sumar N días a la fecha dada. Tener
en cuenta los años bisiestos tal como se detalla en el ejercicio 7 de la práctica 3."""

D = int(input("Ingresar el dia: "))
M = int(input("Ingresar el mes: "))
A = int(input("Ingresar el año: "))
N = int(input("Ingresar la cantidad de dias que queres sumarle a la fecha que ingresaste anteriormente: "))

while N > 0:
    if ((A % 4 == 0 and A % 100 != 0) or (A % 400 == 0)) and M == 2 and D < 29:
        D += 1
    elif M == 2 and D < 28:
        D += 1
    elif (M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12) and D < 31:
        D += 1
    elif (M == 4 or M == 6 or M == 9 or M == 11) and D < 30:
        D += 1
    elif M < 12:
        M += 1
        D = 1
    else:
        D = 1
        M = 1
        A += 1
    N = N - 1

print("La fecha es : ", D, "/", M, "/", A)
