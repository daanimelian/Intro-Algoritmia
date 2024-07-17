# Leer los números de legajo de los alumnos de un curso y su nota de examen
# final. El fin de la carga se determina ingresando un -1 como legajo. Se debe validar que la nota ingresada esté entre
# 1 y 10. Terminada la lectura de datos, informar:
# · Cantidad de alumnos que aprobaron con nota mayor o igual a 4
# · Cantidad de alumnos que desaprobaron el examen. Nota menor a 4
# · Promedio de nota y los legajos que superan el promedio
# Luego se solicita mostrar un listado de legajos y calificaciones ordenado de manera ascendente según el número de
# legajo. Resolver de dos formas: Utilizando
# dos listas paralelas y utilizando una matriz de dos filas.

legajos = []
notas = []


def carga_notas_fila(legajo, nota):
    """ """
    legajos.append(legajo)
    notas.append(nota)

    return legajo, notas


def validar_nota(nota):
    """"""
    es_valida = False
    if 0 < nota < 11:
        es_valida = True

    return es_valida


def cantidad_aprobados_desaprobados(notas_totales):
    cant_aprobados = 0
    cant_desaprobados = 0
    for i in range(0, len(notas_totales)):
        if notas_totales[i] >= 4:
            cant_aprobados += 1
        else:
            cant_desaprobados += 1
    return cant_aprobados, cant_desaprobados


def nota_promedio(notas_totales):
    suma_total = 0
    for i in range(0, len(notas_totales)):
        suma_total += notas_totales[i]
    if len(notas_totales) > 0:
        promedio = suma_total / len(notas_totales)
    else:
        promedio = 0

    return promedio


def legajos_sup_prom(promedio, legajos, notas_totales):
    legajos_sup = []
    for i in range(0, len(notas_totales)):
        if notas_totales[i] > promedio:
            legajos_sup.append(legajos[i])

    return legajos_sup


def ordenar_lista_legajos(lista_legajos, lista_notas, asc=True):
    largo = len(lista_legajos)
    for i in range(largo - 1):
        for j in range(i + 1, largo):
            if asc is True:
                if lista_legajos[j] < lista_legajos[i]:
                    aux = lista_legajos[i]
                    lista_legajos[i] = lista_legajos[j]
                    lista_legajos[j] = aux
                    aux_notas = lista_notas[i]
                    lista_notas[i] = lista_notas[j]
                    lista_notas[j] = aux_notas
            else:
                if lista_legajos[j] > lista_legajos[i]:
                    aux = lista_legajos[i]
                    lista_legajos[i] = lista_legajos[j]
                    lista_legajos[j] = aux
                    aux_notas = lista_notas[i]
                    lista_notas[i] = lista_notas[j]
                    lista_notas[j] = aux_notas

    return lista_legajos, lista_notas


def main():
    print("Ingrese el número de legajo de sus alumnos seguida de su nota, para finalizar ingrese -1 como legajo.")

    legajo = 0
    while legajo != -1:
        legajo = int(input("Ingrese el legajo del alumno: "))
        if legajo != -1:
            nota = int(input("Ingresa la nota del alumno (debe ser un numero entero entre el 1 y el 10): "))
            nota_valida = validar_nota(nota)
            while nota_valida is False:
                nota = int(input("Por favor ingresar una nota valida: "))
                nota_valida = validar_nota(nota)
            carga_notas_fila(legajo=legajo, nota=nota)

    cant_aprobados, cant_desaprobados = cantidad_aprobados_desaprobados(notas)
    nota_promedio_gral = nota_promedio(notas_totales=notas)
    legajos_sup = legajos_sup_prom(promedio=nota_promedio_gral, legajos=legajos, notas_totales=notas)
    lista_legajos_ord, lista_notas_ord = ordenar_lista_legajos(lista_legajos=legajos, lista_notas=notas)

    print("Cantidad de alumnos aprobados: ", cant_aprobados)
    print("Cantidad de alumnos desaprobados: ", cant_desaprobados)
    print("La nota promedio es: ", nota_promedio_gral)
    print("Los alumnos que superan la nota promedio son: ")
    for i in range(0, len(legajos_sup)):
        print("    ", legajos_sup[i])
    print("El listado de alumnos y sus notas: ")
    for i in range(0, len(lista_legajos_ord)):
        print("    ", "Numero de legajo: ", lista_legajos_ord[i], "-", "Nota: ", lista_notas_ord[i])


main()

