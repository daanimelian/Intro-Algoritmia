# Cargar una lista con 30 valores, generados aleatoriamente y que no se repitan, comprendidos entre 1 y 70
# [1, 2, 3, 4, 6, 12, 14, 17, 18, 19, 21, 23, 24, 28, 30, 32, 33, 35, 37, 42, 45, 46, 52, 53, 54, 56, 59, 65, 66, 69]
# Ingresar un dato por teclado, el que deberá estar comprendido entre los valores indicados.
#
# Buscarlo en la lista obtenido utilizando la búsqueda binaria.
#
# Si el valor no está, informarlo y permitir el ingreso de un nuevo dato a buscar
#
# Si el valor está, informar si es un número deficiente
#
# **Número deficiente:** Número que es mayor a la suma de sus divisores, sin considerar el propio número. Ej 8>1+2+4
import random


def es_numero_deficiente(num):
    suma_divisores = 0
    for i in range(1, num - 1):
        if num % i == 0:
            suma_divisores += 0

    if num > suma_divisores:
        es_deficiente = True
    else:
        es_deficiente = False

    return es_deficiente


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
    izquierda = 0
    derecha = len(lista) - 1
    indice = -1

    while izquierda <= derecha and indice == -1:
        centro = (izquierda + derecha) // 2
        if elemento == lista[centro]:
            indice = centro
        elif elemento > lista[centro]:
            izquierda = centro + 1

        else:
            derecha = centro - 1

    return indice


valores = []
while len(valores) < 30:
    num_aleatorio = random.randint(1, 70)
    if len(valores) == 0:
        valores.append(num_aleatorio)
    else:
        valores_ordenados = ordenar_lista(valores)
        indice = busqueda_binaria(valores_ordenados, num_aleatorio)
        if indice == -1:
            valores.append(num_aleatorio)

indice_valor = -1

while indice_valor == -1:
    valor_a_encontrar = int(input("Ingrese un numero entero entre 1 y 70: "))

    while valor_a_encontrar < 1 or valor_a_encontrar > 70:
        valor_a_encontrar = int(
            input("Valor incorrecto. Ingrese un numero entero entre 1 y 70: ")
        )

    valores_ord_final = ordenar_lista(valores)
    print(valores_ord_final)
    indice_valor = busqueda_binaria(valores_ord_final, valor_a_encontrar)
    if indice_valor == -1:
        print("El valor no se encuentra en la lista")

    else:
        es_deficiente = es_numero_deficiente(valor_a_encontrar)
        if es_deficiente:
            print("Es un numero deficiente")
        else:
            print("No es un numero deficiente")
