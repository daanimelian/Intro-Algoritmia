# A partir de la lista SECUENCIAS generada en el ejercicio anterior, imprimir la
# secuencia más larga almacenada en la misma. Si hubiera varias secuencias con
# la misma longitud máxima deberán mostrarse todas las que correspondan.


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


def detectar_secuencia_mas_larga(lista):
    secuencias_largas = []
    largo_lista = 0
    secuencia = []
    for i in range(len(lista)):
        if lista[i] != 0:
            largo_lista += 1
            secuencia.append(lista[i])
        else:
            if len(secuencias_largas) == 0 or len(secuencias_largas[0]) == largo_lista:
                secuencias_largas.append(secuencia)
                largo_lista = 0
            else:
                if len(secuencias_largas[0]) < largo_lista:
                        secuencias_largas = []
                        secuencias_largas.append(secuencia)
                        largo_lista = 0
            secuencia = []
    return secuencias_largas




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

    for i in range(len(lista_random_con_0)):
        print(lista_random_con_0[i], end=" ")

    secuencias_largas = detectar_secuencia_mas_larga(lista_random_con_0)

    print("Secuencias mas largas: ")
    for i in range(len(secuencias_largas)):
        print(secuencias_largas[i], end=" ")



main()
