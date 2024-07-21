# Ingresar por teclado un número N y construir una lista llamada SECUENCIAS con
# N números enteros al azar entre 1 y 20. Esta lista se caracterizará porque sus
# valores deben encontrarse divididos en secuencias de números separadas por
# ceros, cuya suma no sea mayor que 20. Para eso se deberá agregar un elemento
# de valor 0 a fin de separar cada secuencia de la siguiente, cuidando que ninguna
# secuencia sume más de 20. Agregar un 0 adicional al final de la lista y mostrar la
# lista obtenida por pantalla.

import random


def generar_lista_secuencia(largo):
    secuencias = []
    for i in range(largo):
        num_random = random.randint(1, 20)
        secuencias.append(num_random)

    return secuencias


def separar_secuencias(lista):
    secuencia_con_0 = []
    suma_num = 0
    for i in range(len(lista)):
        if i < (len(lista)):

            suma_num += lista[i]
            if suma_num < 20:
                secuencia_con_0.append(lista[i])
            else:
                secuencia_con_0.append(0)
                secuencia_con_0.append(lista[i])
                suma_num = lista[i]
        else:
            secuencia_con_0.append(0)

    return secuencia_con_0


def detectar_entero(numero):
    es_entero = False
    suma = 0
    for i in range(numero):
        suma += 1
    if suma == numero:
        es_entero = True

    return es_entero


def main():
    largo = int(input("Ingresar el largo de la lista: "))
    es_entero = detectar_entero(largo)
    while es_entero is False:
        largo = int(input("Largo incorrecto. Ingresar el largo de la lista: "))
        es_entero = detectar_entero(largo)

    lista_random = generar_lista_secuencia(largo)
    lista_random_con_0 = separar_secuencias(lista_random)
    for i in range(len(lista_random)):
        print(lista_random[i], end=" ")
    print("")
    print(" ----------------------- ")
    for i in range(len(lista_random_con_0)):
        print(lista_random_con_0[i], end=" ")


main()
