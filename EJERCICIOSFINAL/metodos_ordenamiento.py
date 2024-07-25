# Ordenamiento de burbuja

def bubblesort(lista):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                lista[i], lista[i + 1] = lista[i + 1], lista[i]
                intercambio = True
            print(lista)

    return lista


def selectionsort(lista):
    largo = len(lista)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
            print(lista)
    return lista


def insertionsort(lista):
    for i in range(1, len(lista)):
        item_to_insert = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > item_to_insert:
            lista[j + 1] = lista[j]
            j -= 1
            print(lista)
        lista[j + 1] = item_to_insert
        print("------------------------------------------------------------------------")
        print(lista)
    return lista


lista_1 = [15, 25, 13, 10, 90, 1, 4, 3, 7, 6, 5, 8, 9, 0]

insertionsort(lista_1)
