"""Una empresa cuenta con N empleados, divididos en tres categorías (1, 2 y 3).
Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un
informe que contenga:
· Importe total de salarios pagados por la empresa.
· Cantidad de empleados que ganan más de $200000.
· Cantidad de empleados que ganan menos de $50000, cuya categoría sea
3.
· Legajo del empleado que más gana.
· Sueldo más bajo.
· Importe total de sueldos por cada categoría.
· Salario promedio
"""
total_salarios = 0
empleados_mejores_pagos = 0
empleados_peores_pagos = 0
salarios_mas_bajo = 0
salarios_categoria_1 = 0
salarios_categoria_2 = 0
salarios_categoria_3 = 0
salario_prom = 0
cant_empleados = 0
legajo = 0
mejor_sueldo = 0
peor_sueldo = 0
primer_empleado = True
while legajo != -1:
    legajo = int(input("Ingrese el numero de legajo del trabajador. Para finalizar ingrese -1: "))
    if legajo != -1:
        categoria = int(input("Ingrese la categoria del trabajador (1,2 o 3): "))
        while categoria != 1 and categoria != 2 and categoria != 3:
            categoria = int(input("Categoria incorrecta. Ingrese la categoria del trabajador (1,2 o 3): "))
        salario = int(input("Ingrese el salario del trabajador: "))
        while salario < 0:
            salario = int(input("Salario incorrecto. Ingrese el salario del trabajador: "))
        if salario > 200000:
            empleados_mejores_pagos += 1
        if salario < 50000 and categoria == 3:
            empleados_peores_pagos += 1
        if salario > mejor_sueldo:
            legajo_mejor_sueldo = legajo
            mejor_sueldo = salario
        if salario < peor_sueldo or primer_empleado:
            peor_sueldo = salario
            primer_empleado = False
        if categoria == 1:
            salarios_categoria_1 += salario
        elif categoria == 2:
            salarios_categoria_2 += salario
        elif categoria == 3:
            salarios_categoria_3 += salario
        cant_empleados += 1
        total_salarios += salario

if cant_empleados > 0:
    salario_prom = total_salarios / cant_empleados

print("· Importe total de salarios pagados por la empresa: $", total_salarios, "\n",
      "· Cantidad de empleados que ganan más de $200000:", empleados_mejores_pagos, "\n",
      "· Cantidad de empleados que ganan menos de $50000, cuya categoría sea 3:", empleados_peores_pagos, "\n",
      "· Legajo del empleado que más gana: ", legajo_mejor_sueldo, "\n",
      "· Sueldo más bajo: $", peor_sueldo, "\n",
      "· Importe total de sueldos por cada categoría: Categoria 1 - $", salarios_categoria_1, "Categoria 2 - $",
      salarios_categoria_2, "Categoria 3 - $", salarios_categoria_3, "\n",
      "· Salario promedio: $", total_salarios, "\n")
