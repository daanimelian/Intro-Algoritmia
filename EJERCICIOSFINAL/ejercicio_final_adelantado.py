# Para un casino se solicita armar un programa que permita realizar n ejecuciones y por cada ejecución determine
# entre 256 valores al azar que pueden ser números entre -8 y -2534, determinar cuál es el valor mayor encontrado.
# Armar la función que permita ingresar los valores y otra que permita ingresar los rangos de valores, determinar
# cuántos números pares e impares se obtuvieron e informarlos. Indicar cuales de los números pares son múltiplos de
# 10 y que cantidad son. Luego solicitar un número dentro del rango de los pares y mostrar un mensaje que diga si
# existe entre los valores ingresados, o un mensaje de error en caso de no hallar ese número. Este proceso deberá
# realizarse mediante búsqueda binaria. También nos pidieron documentar el programa, indicando las funciones,
# y pasos fundamentales para el funcionamiento del programa
import pdb
import random


def definir_rangos_valores():
    rango_inferior = -2534
    while rango_inferior > -8 or rango_inferior < -2534:
        rango_inferior = int(
            input("Rango inferior incorrecto. Ingrese el rango inferior: ")
        )

    rango_superior = -8
    while (
        rango_inferior > rango_superior or rango_superior > -8 or rango_superior < -2534
    ):
        rango_superior = int(
            input("Rango superior incorrecto. Ingrese el rango superior: ")
        )

    return rango_superior, rango_inferior


def generar_valores_aleatorios():
    lista_valores = []
    rango_sup, rango_inf = definir_rangos_valores()
    for i in range(256):
        num_rand = random.randint(rango_inf, rango_sup)
        lista_valores.append(num_rand)
    return lista_valores


def num_pares_impares(lista):
    largo = len(lista)
    num_pares = []
    num_impares = []

    for i in range(largo):
        if lista[i] % 2 == 0:
            num_pares.append(lista[i])
        else:
            num_impares.append(lista[i])
    return num_pares, num_impares


def valores_mult_de_10(lista):
    largo = len(lista)
    mult_10 = []
    for i in range(largo):
        if lista[i] % 2 == 0 and lista[i] % 5 == 0:
            mult_10.append(lista[i])
    return mult_10


def rango_en_lista(lista):
    rango_superior = 0
    rango_inferior = 0
    largo = len(lista)

    for i in range(largo):
        if i == 0:
            rango_inferior = lista[i]
            rango_superior = lista[i]
        elif lista[i] < rango_inferior:
            rango_inferior = lista[i]
        elif lista[i] > rango_superior:
            rango_superior = lista[i]
    return rango_superior, rango_inferior


def ordenar_lista(lista):
    largo = len(lista)

    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista


def busqueda_binaria(lista, elemento):
    largo = len(lista)
    izquierda = 0
    derecha = largo - 1
    posicion = -1

    while izquierda <= derecha and posicion == -1:

        centro = (izquierda + derecha) // 2
        if elemento == lista[centro]:
            posicion = centro
        elif elemento > lista[centro]:
            izquierda = centro + 1
        else:
            derecha = centro - 1

    return posicion


def main():
    n = 2
    while n < 0:
        n = int(
            input("Numero incorrecto. Ingresar el numero de ejecuciones del programa: ")
        )

    for i in range(n):

        lista_valores = generar_valores_aleatorios()
        lista_valores_ordenada = ordenar_lista(lista_valores)
        print(
            "El mayor elemento encontrado de la lista es: ",
            lista_valores_ordenada[len(lista_valores_ordenada) - 1],
        )
        num_pares, num_impares = num_pares_impares(lista_valores_ordenada)
        num_mult_10 = valores_mult_de_10(num_pares)

        print("Se encontraron ", len(num_pares), " numeros pares y son: ", end=" ")
        for i in range(len(num_pares)):
            print(num_pares[i], end=" ")

        print("")

        print("Se encontraron ", len(num_impares), " numeros impares y son: ", end=" ")
        for i in range(len(num_impares)):
            print(num_impares[i], end=" ")

        print("")

        print(
            "Se encontraron ",
            len(num_mult_10),
            " numeros multiplos de 10 y son: ",
            end=" ",
        )
        for i in range(len(num_mult_10)):
            print(num_mult_10[i], end=" ")

        rango_sup_par, rango_inf_par = rango_en_lista(num_pares)
        print("")
        print(
            "El rango de numeros pares es de ", rango_inf_par, " hasta ", rango_sup_par
        )
        elemento = int(
            input(
                "Ingrese un numero dentro del rango para saber si esta o no en la lista: "
            )
        )
        indice = busqueda_binaria(num_pares, elemento)
        if indice == -1:
            print("El numero no se encuentra dentro de la lista.")
        else:
            print("El numero se encuentra dentro de la lista!")
        print(" ")
        print(
            " ------------------------------------------------------------------------------------------- "
        )
        print(" ")


main()
