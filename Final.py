"""Para un casino se solicita armar un programa que permita realizar n ejecuciones y por cada ejecución determine
 entre 256 valores al azar que pueden ser números entre -8 y -2534, determinar cuál es el valor mayor encontrado.
Armar la función que permita ingresar los valores y otra que permita ingresar los rangos de valores,
determinar cuántos números pares e impares se obtuvieron e informarlos.
Indicar cuales de los números pares son múltiplos de 10 y que cantidad son.
Luego solicitar un número dentro del rango de los pares y mostrar un mensaje que diga si existe entre los valores ingresados,
o un mensaje de error en caso de no hallar ese número. Este proceso deberá realizarse mediante búsqueda binaria.
También nos pidieron documentar el programa, indicando las funciones, y pasos fundamentales para el funcionamiento del programa.
"""

import random  # importo la libreria random para poder utilizarla


def retorno_valor_entre(
    limite_inf, limite_sup
):  # Funcion que me servira para retornar valores random en un rango determinado
    return random.randint(limite_inf, limite_sup)


def carga_lista(
    lista, limite_inf, limite_sup, cantidad
):  # Funcion para llenar con los valores mi lista
    while cantidad > 0:
        lista.append(retorno_valor_entre(limite_inf, limite_sup))
        cantidad -= 1


def ingreso_valores():  # Funcion para ingresar cantidad de valores y limites superior e inferior
    cantidad = int(input("Ingrese la cantidad de numeros a llenar en la lista: "))
    limite_inf = int(input("Ingrese el limite inferior de numeros: "))
    limite_sup = int(input("Ingrese el limite superior de numeros: "))
    while limite_sup < limite_inf:
        limite_sup = int(
            input(
                "Ingrese el limite superior de numeros QUE debe ser mayor al limite inferior: "
            )
        )
    return cantidad, limite_inf, limite_sup


def numeros_multiploDe_10(
    lista,
):  # Funcion que me busca los multiplos de 10 dentro de los pares y los imprime
    lista_multiplo_10 = []
    for i in lista:
        if i % 10 == 0:
            lista_multiplo_10.append(i)
    print()
    print(
        "----------------------------------------------------------------------------------------"
    )
    print(
        "La cantidad de numeros pares que son multiplo de 10 es: ",
        len(lista_multiplo_10),
    )
    print("Y son estos: ")
    impresion_lista(lista_multiplo_10)


def impresion_lista(
    lista,
):  # Funcion auxiliar para imprimir por consola la lista que queramos
    for i in range(len(lista)):
        if i == len(lista) - 1:
            print(lista[i])
        else:
            print(lista[i], end=", ")


def numeros_pares_e_impares(
    lista, lista_pares, lista_impares
):  # Funcion para encontrar los numeros pares e impares
    for i in lista:
        if i % 2 == 0:  # Verifico si es par
            lista_pares.append(i)
        else:  # si no es par, es impar
            lista_impares.append(i)
    print()
    print(
        "----------------------------------------------------------------------------------------"
    )
    print("La cantidad de numeros pares es: ", len(lista_pares))
    print("Estos fueron los hallados:")
    impresion_lista(lista_pares)
    print("La cantidad de numeros impares es: ", len(lista_impares))
    print("Estos fueron los hallados:")
    impresion_lista(lista_impares)


def ordenamiento_insercion(lista):  # Algoritmo de ordenamiento por insercion
    for i in range(len(lista)):
        aux = lista[i]
        j = i
        while j > 0 and lista[j - 1] > aux:
            lista[j] = lista[j - 1]
            j -= 1
            lista[j] = aux


# Algoritmo de busqueda binaria, siempre debe ejecutarse con una lista previamente ordenada de manera ascendente
def busqueda_binaria(lista, digito):
    izq = 0
    der = len(lista) - 1
    posicion = -1
    while der >= izq and posicion == -1:
        centro = (izq + der) // 2
        if lista[centro] == digito:
            posicion = centro
        elif lista[centro] > digito:
            der = centro - 1
        else:
            izq = centro + 1
    return posicion


def busqueda_numero_par(
    lista, limite_inf, limite_sup
):  # Funcion para buscar numero dentro de los pares
    print()
    print(
        "----------------------------------------------------------------------------------------"
    )
    numero = int(input("Ingrese numero par a buscar: "))
    while numero < limite_inf or numero > limite_sup or numero % 2 != 0:
        print(
            "Ingrese un numero par dentro de los rangos dados ",
            limite_inf,
            "A",
            limite_sup,
            "Y que sea par: ",
            end="",
        )
        numero = int(input())
    posicion = busqueda_binaria(lista, numero)
    print()
    print(
        "----------------------------------------------------------------------------------------"
    )
    print("La lista ordenada de numeros pares es asi: ")
    impresion_lista(lista)
    if posicion == -1:  # cuando busqueda_binaria nos devuelve -1 es que no se encontro
        print("El numero", numero, "no se encuentra en la lista")
    else:
        print("El numero se encuentra en la posicion: ", posicion)


# Programa principal
"""Para el correcto funcionamiento del programa se deben ingresar la cantidad de numeros a llenar en nuestra lista,
el limite inferior y superior.
Y luego ingresar el numero par a buscar dentro de nuestro rango de valores previamente ingresado."""
lista = []
lista_pares = []
lista_impares = []
cantidad, limite_inf, limite_sup = ingreso_valores()
carga_lista(lista, limite_inf, limite_sup, cantidad)
numeros_pares_e_impares(lista, lista_pares, lista_impares)
numeros_multiploDe_10(lista_pares)
ordenamiento_insercion(lista_pares)
busqueda_numero_par(lista_pares, limite_inf, limite_sup)
