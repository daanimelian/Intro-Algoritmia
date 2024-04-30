# Desarrollar un programa que imprima los números naturales comprendidos entre
# 1 y N. El valor de N se ingresa desde el teclado.
# TODO: Validaciones con ciclo while

n = int(input("Ingrese un numero: "))
i = 1
while n < 1:
    n = int(input("El numero no es natural, ingrese un numero: "))
while i <= n:
    print(i)
    i = i + 1
