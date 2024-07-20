# En una carrera de ciclistas participan N competidores, donde N se ingresa por
# teclado. Desarrollar un programa que permita cargar, por cada competidor, su
# número y el tiempo de carrera en horas, minutos y segundos. Luego se solicita:
# · Mostrar el número del ganador de la carrera y el tiempo que empleó.
# · Ingresando por teclado el tiempo record registrado para dicha carrera,
# informar si el ganador batió el record anterior.
# · Calcular y mostrar el tiempo promedio entre todos los ciclistas.
# Los ciclistas se identifican con números enteros, no necesariamente correlativos.

competidores_info = [[], []]


def validar_numero_competidores(numero_competidores):
    es_valido = True
    decimales = 0
    numero_competidores_str = str(numero_competidores)
    for i in range(len(numero_competidores_str)):
        if numero_competidores_str[i] == ".":
            decimales = int(numero_competidores_str[i + 1:])
    if 0 < decimales:
        es_valido = False

    return es_valido


def cargar_info_competidor(num_comp, tiempo_com):
    competidores_info[0].append(num_comp)
    competidores_info[1].append(tiempo_com)


def horas_a_seg(horas, min):
    segundos = (horas * 3600) + (min * 60)
    return segundos


def seg_a_horas(segundos):
    horas = segundos // 3600
    min = (segundos % 3600) // 60
    segundos_restantes = segundos - horas * 3600 - min * 60

    return horas, min, segundos_restantes


def calcular_ganador(competidores_tiempo):
    tiempo_ganador = competidores_tiempo[0]
    indice_ganador = 0
    for i in range(len(competidores_tiempo)):
        if tiempo_ganador > competidores_tiempo[i]:
            tiempo_ganador = competidores_tiempo[i]
            indice_ganador = i

    return indice_ganador


def tiempo_promedio(competidores_tiempo):
    suma_tiempos = 0
    for i in range(len(competidores_tiempo)):
        suma_tiempos += competidores_tiempo[i]

    promedio = suma_tiempos / len(competidores_tiempo)

    horas, minutos, segundos = seg_a_horas(promedio)

    return horas, minutos, segundos


def main():
    cant_competidores = float(input("Ingresar la cantidad de competidores de la carrera: "))
    comp_validos = validar_numero_competidores(cant_competidores)
    while comp_validos is False:
        cant_competidores = float(input("Cantidad invalida. Ingresar la cantidad de competidores de la carrera: "))
        comp_validos = validar_numero_competidores(cant_competidores)

    for i in range(int(cant_competidores)):
        numero_competidor = float(input("Ingrese el numero de competidor: "))
        comp_validos = validar_numero_competidores(numero_competidor)
        while comp_validos is False:
            numero_competidor = float(input("Cantidad invalida. Ingresar la cantidad de competidores de la carrera: "))
            comp_validos = validar_numero_competidores(numero_competidor)

        print("Ingresar el tiempo del corredor.")
        horas = int(input("Horas: "))
        min = int(input("Minutos: "))
        segundos = int(input("Segundos: "))
        tiempo_seg = horas_a_seg(horas, min) + segundos

        cargar_info_competidor(numero_competidor, tiempo_seg)

    ganador = calcular_ganador(competidores_info[1])
    print(f"El ganador de la carreras es el corredor {competidores_info[0][ganador]}")

    print("Ingresar el tiempo record.")
    horas = int(input("Horas: "))
    min = int(input("Minutos: "))
    segundos = int(input("Segundos: "))
    tiempo_record_seg = horas_a_seg(horas, min) + segundos

    if competidores_info[1][ganador] < tiempo_record_seg:
        print("El ganador batio el record.")

    else:
        print("El ganador no batio el record.")

    horas_promedio, min_promedio, segundos_promedio = tiempo_promedio(competidores_info[1])

    print("El tiempo promedio fue de: ", horas_promedio, " horas, ", min_promedio, " minutos y ", segundos_promedio, " segundos.")


main()
