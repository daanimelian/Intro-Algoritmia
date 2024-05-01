"""Escribir un programa para convertir un número binario de 4 cifras en un número
decimal. El número binario se ingresa como un solo número entero de cuatro
dígitos.
Procedimiento: Para convertir un número binario a decimal es necesario
multiplicar el valor de cada dígito por el número 2 elevado a un exponente. Este
exponente se obtiene de la posición que ocupa el dígito dentro del número,
comenzando desde la derecha con la posición 0. Todos estos resultados se
suman para obtener el valor final. Ejemplo: Convertir 1011 a decimal:
13 02 11 10 = 1 * 23 + 0 * 22 + 1 * 21 + 1 * 20 = 11"""

num_binario = int(input("Ingresar el numero binario de 4 digitos que quiera pasar a decimal: "))
decimal = 0

miles = num_binario // 1000
if miles > 0:
    decimal += miles * 2 ** 3
num_binario = num_binario - (miles * 1000)
centenas = num_binario // 100
if centenas > 0:
    decimal += centenas * 2 ** 2
num_binario = num_binario - (centenas * 100)
decenas = num_binario // 10
if decenas > 0:
    decimal += decenas * 2 ** 1
num_binario = num_binario - (decenas * 10)
unidades = num_binario // 1
if unidades > 0:
    decimal += unidades
num_binario = num_binario -(unidades)

print("El número ingresado es: ", decimal)

