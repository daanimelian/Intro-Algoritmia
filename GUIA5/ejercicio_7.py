"""Leer un número entero e invertir las cifras que contiene. Imprimir por pantalla el
número invertido. Tener en cuenta que el número puede ser negativo. Por ejemplo, si se ingresa 1234 debe mostrar 4321."""
reversa = ""
extension = 1
es_negativo = False

numero = int(input("Ingrese el numero que desea invertir: "))

#Si el numero es negativo, busco el modulo
if numero < 0:
    es_negativo = True
    numero = int((numero**2)**(1/2))

# Calculo cual es su mayor divisor multiplo de 10
while numero // extension > 9:
    extension = extension * 10


while numero > 0:
    # Divido el numero por el multiplo de 10 para ver digito por digito
    digito = int(numero // extension)
    # Los voy acumulando en un string
    reversa = str(digito) + reversa
    # Resto los digitos que ya sume al string
    numero = numero - (digito * extension)

    extension = extension / 10

if es_negativo:
    reversa = "-" + reversa

print("El numero invertido es: ", reversa)
