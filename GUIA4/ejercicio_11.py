# Realizar un programa que lea un número natural H e imprima un mensaje indicando si H es primo o no. Se dice que un número es primo cuando sólo es divisible por sí mismo y por la unidad
n = int(input("Ingrese un numero: "))
i = 2
es_primo = True
while i < n and es_primo:
    if n % i == 0:
        es_primo = False
    i = i + 1
if es_primo:
    print("El numero es primo")
else:
    print("El numero es compuesto.")
