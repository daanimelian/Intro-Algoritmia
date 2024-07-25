# Ingresar un número entero y positivo y generar la siguiente serie
#
# Si el valor es impar, multiplicarlo por 3 y sumarle 1; si el valor es par, dividirlo por 2.
#
# Evaluar el resultado obtenido e Ir repitiendo las operaciones, según corresponda, hasta que el valor final sea 1
#
# Por ejemplo, se ingresa el 7
#
# 7*3+1=**22**/2=**11***3+1=**34**/2=**17***3+1=**52**/2=**26**/2=**13***3+1=**40**/2=**20**/2=**10**/2=**5***3+1=**16**/2=**8**/2=**4**/2=**2**/2=**1**
#
# Se solicita:
#
# - Ir guardando los resultados obtenidos en una lista
# - Informar cuantos valores se guardaron en la lista
# - Informar si en la lista hay valores primos, y cuantos. Determinar si el valor es primo con una función
# - Mostrar la lista original con los valores separados por 3 espacios
# - Ordenar la lista de manera descendente y volverla a mostrar
#
# **Número primo:** Número divisible solamente por 1 y por si mismo. Ej 5

lista_resultados = []


def realizar_cuenta(numero):
    if numero % 2 == 0:
        numero = numero / 2
    else:
        numero = (numero * 3) + 1

    return int(numero)


def ordenar_lista(lista, asc=True):
    largo = len(lista)

    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if asc is True:
                if lista[i] > lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux
            else:
                if lista[i] < lista[j]:
                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

    return lista


def numeros_primos(lista):
    largo = len(lista)
    num_primo = []
    for i in range(largo):
        cant_divisores = 0
        for j in range(1, lista[i]):
            if lista[i] % j == 0:
                cant_divisores += 1
        if cant_divisores == 1:
            num_primo.append(lista[i])
    return num_primo


n = int(input("Ingresar un numero entero y positivo: "))
while n < 0:
    n = int(input("El numero no es positivo. Ingresar un numero entero y positivo: "))

while n > 1:

    n = realizar_cuenta(n)
    lista_resultados.append(n)
num_primos = numeros_primos(lista_resultados)


print("La lista de num es: ", len(lista_resultados), " y son: ", end=" ")
for i in range(len(lista_resultados)):
    print(lista_resultados[i], end=" ")
print("")


lista_ordenada = ordenar_lista(lista_resultados, asc=True)
print("La lista de num ordenada asc es: ", len(lista_ordenada), " y son: ", end=" ")
for i in range(len(lista_ordenada)):
    print(lista_ordenada[i], end=" ")
print("")

lista_ordenada_des = ordenar_lista(lista_resultados, asc=False)
print("La lista de num desc es: ", len(lista_ordenada_des), " y son: ", end=" ")
for i in range(len(lista_ordenada_des)):
    print(lista_ordenada_des[i], end=" ")

print("")
print("Se encontraron ", len(num_primos), " numeros primos y son: ", end=" ")
for i in range(len(num_primos)):
    print(num_primos[i], end=" ")
