# El factorial de un número entero N mayor que cero se define como el producto de todos los enteros X tales que 0 < X
# <= N. Desarrollar un programa para calcular el factorial de un número dado. Deberán rechazarse las entradas
# inválidas (menores que 0).

n = int(input("Ingrese un numero para calcular su factorial: "))
while n <= 0:
    n = int(input("Ingrese un numero valido: "))

i = 1
factorial = 1
while i <= n:
    factorial = factorial * i
    i = i + 1
print("El factorial es: ", factorial)
