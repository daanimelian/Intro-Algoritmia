# Desarrollar una función que reciba como parámetro un número entero positivo cualquiera y lo devuelva invertido,
# es decir que la última cifra pase a ser la primera, la penúltima pase a ser la segunda, etc. Por ejemplo, si la función
# recibe como parámetro el número 123, debe devolver 321.

def invertir(num):
    num_invertido = 0
    while num > 0:
        digito = num % 10
        num_invertido = num_invertido * 10 + digito
        num = num // 10

    return num


invertir(123)


# Escribir una función que ordene un vector en forma ascendente y además elimine los elementos repetidos del mismo.
# La función debe recibir como parámetro el vector y la cantidad de elementos que contiene (hasta un máximo de MAX
# elementos), y devolver como valor de retorno un entero indicando cuántos elementos contiene el vector luego del
# proceso. Puede utilizar funciones auxiliares en caso necesario, y utilizar cualquiera de los métodos de
# ordenamiento estudiados.

def ordenar_vector_bubble(vector):
    intercambio = True
    while intercambio:
        intercambio = False
        for i in range(len(vector) - 1):
            if vector[i] > vector[i + 1]:
                aux = vector[i]
                vector[i] = vector[i + 1]
                vector[i + 1] = aux

                intercambio = True
    return vector


def ordenar_vector_insertion(vector):
    largo = len(vector)
    for i in range(1, largo):
        elem_insert = vector[i]
        j = i - 1
        while j >= 0 and vector[j] > elem_insert:
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = elem_insert
    return vector


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


def eliminar_repetido(vector):
    largo = len(vector)
    nueva_lista = []
    for i in range(largo):
        nueva_lista = ordenar_vector_insertion(nueva_lista)
        indice = busqueda_binaria(nueva_lista, vector[i])
        if indice == -1:
            nueva_lista.append(vector[i])

    return nueva_lista


lista_ordenada = eliminar_repetido([15, 25, 13, 10, 90, 1, 4, 3, 7, 6, 5, 8, 9, 0, 4, 10, 5, 2, 22, 11, 67])
print(lista_ordenada)
