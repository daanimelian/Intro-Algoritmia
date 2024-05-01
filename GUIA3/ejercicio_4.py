"""En el congreso se vota una ley muy importante. Desarrollar un programa que
permita ingresar la cantidad de votos a favor y en contra, e informe el porcentaje obtenido en cada caso y si la misma fue aprobada o no.
"""
cant_positivos = int(input("Ingrese la cantidad de votos positivos: "))
cant_negativos = int(input("Ingrese la cantidad de votos negativos: "))
cant_total = cant_negativos + cant_positivos
porc_positivo = cant_positivos * 100 / cant_total
porc_negativo = cant_negativos * 100 / cant_total

if porc_positivo <= porc_negativo:
    print("La ley no paso. Tuvo un ", porc_negativo, "% de votos negativos.")
else:
    print("La ley paso. Tuvo un ", porc_positivo, "% de votos positivos.")