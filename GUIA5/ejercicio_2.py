"""Escribir un programa que permita ingresar los números de legajo de los alumnos de un curso y su nota de examen
final. El fin de la carga se determina ingresando un -1 en el legajo. Informar para cada alumno si aprobó o no el
examen considerando que se aprueba con nota mayor o igual a 4. Se debe validar que la nota ingresada sea entre 1 y
10. Terminada la carga de datos, informar: · Cantidad de alumnos que aprobaron con nota mayor o igual a 4. · Cantidad
de alumnos que desaprobaron el examen con nota menor a 4. · Porcentaje de alumnos que están aplazados (tienen 1 en el
examen)."""

legajo = 0
nota_min_aprobado = 4
cant_aprobado = 0
cant_desaprobado = 0
cant_aplazos = 0
cant_alumnos = 0

while legajo != -1:
    legajo = int(input("Ingresar el legajo del alumno, para finalizar la lista escriba -1: "))
    if legajo != -1:
        nota = int(input("Ingrese la nota del alumno (entre 1 y 10): "))
        while nota < 1 or nota > 10:
            nota = int(input("Nota incorrecta. Ingrese la nota del alumno: "))

        if nota < nota_min_aprobado:
            print("El alumno esta desaprobado. ")
            cant_desaprobado += 1
            if nota == 1:
                cant_aplazos += 1
        else:
            print("El alumno esta aprobado. ")
            cant_aprobado += 1
        cant_alumnos += 1

porcentaje_aplazos = cant_aplazos*100/cant_alumnos

print("La cantidad de alumnos desaprobados es: ", cant_desaprobado)
print("La cantidad de alumnos aprobados es: ", cant_aprobado)
print("El porcentaje de aplazos es del: ", porcentaje_aplazos, "%." )


