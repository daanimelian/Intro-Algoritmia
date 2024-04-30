""": Una empresa aplica el siguiente procedimiento en la comercialización de sus productos:
· Aplica el precio base a la primera docena de unidades.
· Aplica un 10% de descuento a todas las unidades entre 13 y 100.
· Aplica un 25% de descuento a todas las unidades por encima de las 100.
Por ejemplo, supongamos que vende 230 unidades de un producto cuyo precio
base es 100. El cálculo resultante sería:
100 * 12 + 90 * 88 + 75 * 130 = 18870
y el precio promedio es de 18870/230 = 82.04
Escribir un programa que lea la cantidad solicitada de un producto y su precio
base, y muestre el valor total de la venta y el precio promedio por unidad. El fin
de carga se determina ingresando -1 como cantidad solicitada. Al finalizar informar:
· Cantidad de ventas realizadas total.
· Cantidad de ventas en las que se aplicó un 10% de descuento.
· Cantidad de ventas en las que SOLO se aplicó el precio base, es decir
que no se le realizaron descuentos."""

cant_solicitada = 0
precio_base = 0
cant_primer_desc = 12
cant_seg_desc = 100
valor_primer_desc = 0.90
valor_segundo_desc = 0.75
cant_ventas = 0
cant_ventas_primer_desc = 0
cant_ventas_sin_desc = 0

while cant_solicitada > -1:
    cant_solicitada = int(input("Ingresar la cantidad solicitada del producto: "))
    while cant_solicitada < 0 and cant_solicitada != -1:
        cant_solicitada = int(input("Cantidad incorrecta. Ingresar la cantidad solicitada del producto: "))
    if cant_solicitada != -1:
        precio_base = float(input("Ingresar el precio base del producto: "))
        while precio_base < 0:
            precio_base = float(input("Precio invalido. Ingresar el precio base del producto: "))
        if cant_solicitada <= cant_primer_desc:
            venta = cant_solicitada * precio_base
            cant_ventas_sin_desc += 1
        elif cant_seg_desc < cant_solicitada <= 100:
            venta = (cant_primer_desc * precio_base) + (
                    cant_solicitada - cant_primer_desc) * precio_base * valor_primer_desc
            cant_ventas_primer_desc += 1
        else:
            venta = ((cant_primer_desc * precio_base) + (
                    (cant_seg_desc - cant_primer_desc) * precio_base * valor_primer_desc) +
                     (cant_solicitada - cant_seg_desc) * precio_base * valor_segundo_desc)
            cant_ventas_primer_desc += 1
        if venta > 0:
            precio_promedio = float(venta / cant_solicitada)
        else:
            precio_promedio = 0
        print("El valor de la venta es: ", venta)
        print("El valor de precio promedio es: ", precio_promedio)
        cant_ventas += 1

print("Se realizaron ", cant_ventas, " ventas.")
print("Se realizaron ", cant_ventas_sin_desc, " ventas con precio base.")
print("Se realizaron ", cant_ventas_primer_desc, " ventas con descuento del 10%. ")
