"""Una empresa factura a sus clientes el último día de cada mes. Si el cliente paga
su factura dentro de los primeros 10 días del mes siguiente, tiene un descuento
de $200 o del 2% de la factura, lo que resulte más conveniente para el cliente.
Si paga en los siguientes 10 días del mes deberá pagar el importe original de la
factura, mientras que si paga después del día 20 deberá abonar una multa de
$350 o del 10% de su factura, lo que resulte mayor. Escribir un programa que
lea el número del cliente y el total de la factura, y emita un informe donde conste el número del cliente y los tres
importes que podría abonar según la fecha de pago."""

desc_fijo = 200
desc_porc = 0.02
recargo_fijo = 350
recargo_porc = 0.10
descuento = 0
recargo = 0

nro_cliente = int(input("Ingresar el numero de cliente: "))
total_factura = float(input("Ingresar el total de la factura: "))

desc_variable = total_factura * desc_porc
recargo_variable = total_factura * recargo_porc

if desc_variable <= desc_fijo:
    descuento = desc_fijo
else:
    descuento = desc_variable

if recargo_variable <= recargo_fijo:
    recargo = recargo_fijo
else:
    recargo = recargo_variable

monto_desc = total_factura - descuento
monto_recargo = total_factura + recargo

print("Cliente N°", nro_cliente)
print("Los montos a abonar segun la fecha de pago son: ")
print("Si abona del 1 al 10 del mes corriente: $", monto_desc)
print("Si abona del 11 al 20 del mes corriente: $", total_factura)
print("Si abona del 21 en adelante del mes corriente: $", monto_recargo)