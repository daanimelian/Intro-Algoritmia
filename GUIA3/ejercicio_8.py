"""Leer un número correspondiente a un año e imprimir un mensaje indicando si es
bisiesto o no. Un año es bisiesto cuando es divisible por 4. Sin embargo, aquellos
años que sean divisibles por 4 y también por 100 no son bisiestos, a menos que
también sean divisibles por 400. Por ejemplo, 1900 no fue bisiesto pero sí el
2000."""

año = int(input("Ingrese el año para averiguar si es bisiesto o no: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("Es bisiesto.")
else:
    print("No es bisiesto.")
