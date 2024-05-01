"""Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
Tener en cuenta que el número puede ser negativo. Ejemplo: Si se ingresa
12345 se debe imprimir 5."""
N = "9"
cant_digitos = 1
numero = int(input("Ingrese un numero entero: "))

while numero > int(N):
    N = N + "9"
    cant_digitos += 1

print("El numero tiene", cant_digitos, "digitos.")
