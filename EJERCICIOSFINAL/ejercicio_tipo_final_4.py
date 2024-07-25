# Ejercicio 1
# Se ingresa por teclado, el número de vendedor y el importe de cada venta realizado por éste
# El nro de vendedor puede ser 1, 2 o 3. Este dato deberá controlarse
# En un vector, se deberá ir cargando el número de vendedor y en otro el importe de cada venta, correspondiéndose la posición de uno con la del otro.
# El fin de la carga se indica con el vendedor 0 Por fin de la carga, recorrer los vectores e indicar
# a) Cuanto vendió cada vendedor (en dinero) y cuantas ventas hizo cada vendedor.
# b)Cual fue el vendedor que más vendió, en dinero y cual fue el vendedor que más ventas hizo, en cantidad
# c) Cuantas ventas superiores a $ 5000 hubo y cual fue el porcentaje de éstas en relación a las ventas totales


num_vend_validos = [1, 2, 3]
vendedores = []
ventas = []


def es_vendedor_valido(num_vend):
    es_valido = False
    i = 0
    while i < len(num_vend_validos) and es_valido is False:
        if num_vend == num_vend_validos[i]:
            es_valido = True

    return es_valido


def cant_ventas_x_vendedor(num_vend):
    total_venta = 0
    cant_ventas = 0
    for i in range(len(vendedores)):
        if vendedores[i] == num_vend:
            total_venta += ventas[i]
            cant_ventas += 1

    return total_venta



vendedor = -1
while vendedor != 0:
    vendedor = int(input("Ingrese el numero del vendedor o 0 para terminar: "))
    vend_valido = es_vendedor_valido(vendedor)
    if vendedor != 0:
        while vend_valido is False and vendedor != 0:
            vendedor = int(input("Vendedor invalido. Ingrese el numero del vendedor o 0 para terminar: "))
            vend_valido = es_vendedor_valido(vendedor)
        if vendedor != 0:
            venta = int(input("Ingrese el monto de la venta: "))
            ventas.append(venta)

cant_ventas_1 , total_ventas_1 = cant_ventas_x_vendedor(num_vend=1)
cant_ventas_2 , total_ventas_2 = cant_ventas_x_vendedor(num_vend=2)
cant_ventas_3 , total_ventas_3 = cant_ventas_x_vendedor(num_vend=3)

if cant_ventas_1 > cant_ventas_2 and cant_ventas_1 > cant_ventas_3:
    print("El mayor vendedor es el vendedor 1.")
elif cant_ventas_2 > cant_ventas_1 and cant_ventas_2 > cant_ventas_3:
    print("El mayor vendedor es el vendedor 2.")
elif cant_ventas_3 > cant_ventas_1 and cant_ventas_3>cant_ventas_2:
    print("El mayor vendedor es el vendedor 2.")

