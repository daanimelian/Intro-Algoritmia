# Hora de jugar: Desarrollar un programa que genere un número entero al azar de cuatro cifras y le proponga al
# usuario que lo descubra, ingresando valores repetidamente hasta hallarlo. En cada intento el programa mostrará
# mensajes indicando si el número ingresado es mayor o menor que el valor secreto. Permitir que el usuario abandone
# la partida al ingresar -1. Al terminar el juego informar la cantidad de intentos realizada, haciendo que el usuario
# ingrese su número de documento si mejoró la mejor marca de intentos obtenida hasta el momento. Luego mostrar la
# lista ordenada de los 5 mejores puntajes (indicando también a quién pertenecen) y preguntar si se desea jugar otra
# vez, reiniciando el juego en caso afirmativo.

# Modificar el programa anterior para que las pistas brindadas por el programa no
# sean del tipo "es mayor" o "es menor" sino "M dígitos correctos y N dígitos
# aproximados". Se considera que un dígito es correcto cuando tanto su valor
# como su posición coinciden con los del número secreto, mientras que un dígito
# es aproximado cuando coincide el valor, pero no su posición.


import random

matriz_jugadores = [[], []]


def de_num_a_lista(num):
    lista = []
    numero_str = str(num)
    for i in range(len(numero_str)):
        lista.append(numero_str[i])

    return lista


def calcular_correctos_y_aproximados(lista_num_real, lista_num_adivinado):
    correctos = 0
    aproximados = 0
    lista_posibles_aprox_adv = []
    lista_posibles_aprox_real = []

    for i in range(len(lista_num_real)):
        if lista_num_real[i] == lista_num_adivinado[i]:
            correctos += 1
        else:
            lista_posibles_aprox_adv.append(lista_num_adivinado[i])
            lista_posibles_aprox_real.append(lista_num_real[i])

    for j in range(len(lista_posibles_aprox_real)):
        h = 0
        while h < len(lista_posibles_aprox_adv):
            if lista_posibles_aprox_real[j] == lista_posibles_aprox_adv[h]:
                aproximados += 1
                h = len(lista_posibles_aprox_adv)
            h += 1

    return correctos, aproximados


def generar_num_aleatorio():
    num_aleatorio = random.randint(1000, 9999)

    return num_aleatorio


def es_mejor_jugador(intentos):
    es_mejor_puntaje = True
    for i in range(len(matriz_jugadores[1])):
        if matriz_jugadores[1][i] < intentos:
            es_mejor_puntaje = False
    return es_mejor_puntaje


def ordenar_matriz(matriz):
    largo = len(matriz[1])
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if matriz[1][i] > matriz[1][j]:
                aux_intentos = matriz[1][i]
                matriz[1][i] = matriz[1][j]
                matriz[1][j] = aux_intentos

                aux_dni = matriz[0][i]
                matriz[0][i] = matriz[0][j]
                matriz[0][j] = aux_dni
    return matriz


def main():
    print("Bienvenidos al juego de adivinanzas.")
    num_real = generar_num_aleatorio()
    num_real_lista = de_num_a_lista(num_real)
    num_adivinado = int(
        input("Ingrese el numero que crea correcto, para finalizar ingresar -1: ")
    )
    num_adivinado_lista = de_num_a_lista(num_adivinado)
    seguir_juego = True
    while seguir_juego is True:
        print(num_real)
        intentos = 1
        while num_adivinado != num_real and num_adivinado != -1:
            num_correctos, num_aproximados = calcular_correctos_y_aproximados(
                num_real_lista, num_adivinado_lista
            )
            print(
                "Numeros correctos: ",
                num_correctos,
                " y numeros aproximados: ",
                num_aproximados,
            )
            num_adivinado = int(
                input(
                    "Ingrese el numero que crea correcto, para finalizar ingresar -1: "
                )
            )
            num_adivinado_lista = de_num_a_lista(num_adivinado)
            intentos += 1

        if num_adivinado == num_real:
            print("Adivinaste!! Lo lograste en ", intentos, " intentos")
            mejor_intento = es_mejor_jugador(intentos)

            if len(matriz_jugadores[0]) == 0 or mejor_intento is True:
                dni = int(input("Ingresa tu  DNI : "))
                matriz_jugadores[0].append(dni)
                matriz_jugadores[1].append(intentos)
                matriz_jugadores_ordenada = ordenar_matriz(matriz_jugadores)
                print("Los mejores puntajes son: ")
                print("| JUGADORES |", " INTENTOS |")
                if len(matriz_jugadores[0]) > 5:
                    rango = 5

                else:
                    rango = len(matriz_jugadores[0])
                for i in range(rango):
                    print(
                        "| ",
                        matriz_jugadores_ordenada[0][i],
                        " | ",
                        matriz_jugadores[1][i],
                        " |",
                    )

        respuesta = input("Queres seguir jugando? Ingresar S/N: ")
        if respuesta == "S" or respuesta == "s":
            seguir_juego = True
            num_real = generar_num_aleatorio()
            num_real_lista = de_num_a_lista(num_real)
            num_adivinado = int(
                input(
                    "Ingrese el numero que crea correcto, para finalizar ingresar -1: "
                )
            )
            num_adivinado_lista = de_num_a_lista(num_adivinado)
        elif respuesta == "N" or respuesta == "n":
            seguir_juego = False


main()
