# Una Administradora de Consorcios necesita un sistema para poder gestionar el cobro de las expensas de un edificio
# de departamentos de 20 unidades. En dos listas almacena la siguiente información: Número de unidad y superficie en
# metros cuadrados. Validar que no se ingresen números de unidades duplicadas. Cada unidad paga de expensas un valor
# fijo por metro cuadrado, el que se ingresa por teclado. Se pide:
# · Informar el promedio de expensas del mes.
# · Ordenar los listados de mayor a menor según la superficie.
# . Mostrar por pantalla el listado ordenado informando el número de unidad y la superficie en metros cuadrados.

matriz_depto_info = [[], [], []]


def ingresar_unidad_superficie_expensa(nro_unidad, sup, valor_expensa):
    """"""
    matriz_depto_info[0].append(nro_unidad)
    matriz_depto_info[1].append(sup)
    matriz_depto_info[2].append(valor_expensa)

    return matriz_depto_info


def validar_nro_unidad(nro_unidad):
    depto_valido = True
    i = 0

    while i < (len(matriz_depto_info[0])) and depto_valido is True:
        if matriz_depto_info[0][i] == nro_unidad:
            depto_valido = False
        i += 1

    return depto_valido


def validar_monto_expensa(valor_expensa):
    if valor_expensa < 0:

        es_valido = False
    else:
        es_valido = True

    return es_valido


def validar_superficie(superficie):
    if superficie < 0:

        es_valido = False
    else:
        es_valido = True

    return es_valido


def promedio_expensas(lista_expensas):
    suma_expensas = 0
    cant_deptos = len(lista_expensas)
    for i in range(len(lista_expensas)):
        suma_expensas += lista_expensas[i]

    promedio = suma_expensas / cant_deptos

    return promedio


def ordenar_matriz_por_sup(matriz_depto):
    superficies = matriz_depto[1]
    nro_unidad = matriz_depto[0]
    expensas = matriz_depto[2]

    largo = len(superficies)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if superficies[i] > superficies[j]:
                aux_sup = superficies[i]
                superficies[i] = superficies[j]
                superficies[j] = aux_sup

                aux_nro_unidad = nro_unidad[i]
                nro_unidad[i] = nro_unidad[j]
                nro_unidad[j] = aux_nro_unidad

                aux_expensas = expensas[i]
                expensas[i] = expensas[j]
                expensas[j] = aux_expensas

    matriz_ordenada = [nro_unidad, superficies, expensas]

    return matriz_ordenada


def main():
    expensa_m2 = int(input("Ingrese el valor de expensa por m2: "))

    print("Ingrese el nro de depto seguido de su superficie en m2. Para finalizar ingrese -1 en nro de depto.")
    nro_depto = 0
    while nro_depto != -1:
        nro_depto = int(input("Ingrese el numero de depto: "))
        depto_valido = validar_nro_unidad(nro_depto)
        while depto_valido is False:
            nro_depto = int(input("Numero de departamento duplicado. Ingrese el numero de depto correcto: "))
            depto_valido = validar_nro_unidad(nro_depto)

        if nro_depto != -1:
            sup_depto = int(input("Ingrese la superficie del depto: "))
            sup_depto_valido = validar_superficie(sup_depto)
            while sup_depto_valido is False:
                sup_depto = int(input("Superficie invalida. Ingrese la superficie del depto: "))
                sup_depto_valido = validar_superficie(sup_depto)

            valor_expensa = expensa_m2 * sup_depto
            ingresar_unidad_superficie_expensa(nro_unidad=nro_depto, sup=sup_depto,
                                               valor_expensa=valor_expensa)
    matriz_depto_info_ordenada = ordenar_matriz_por_sup(matriz_depto_info)

    promedio_exp = promedio_expensas(matriz_depto_info[2])

    print("Valor promedio de las expensas: ", promedio_exp)

    for i in range(len(matriz_depto_info_ordenada[0])):
        print(
            f"El depto numero {matriz_depto_info_ordenada[0][i]} tiene una superficie de {matriz_depto_info_ordenada[1][i]} m2 y paga ${matriz_depto_info_ordenada[2][i]} de expensas.")


main()
