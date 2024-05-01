"""Un complejo de cines necesita un programa para contabilizar el dinero que recauda. Por cada función se ingresa la
cantidad de espectadores y si esa función
tiene descuento o no (1=Sí, 2=No). La carga finaliza cuando la cantidad de espectadores sea igual a cero. En ese momento
el programa deberá:
· Calcular la recaudación total del complejo, considerando que el valor de la
entrada es de $3500 en los días de descuento $5000 en los días sin
descuento.
· Determinar cuántos espectadores ingresaron con descuento y qué
porcentaje representan sobre el total de funciones."""

valor_entrada_desc = 3500
valor_entrada = 5000
espectadores_desc = 0
espectadores_total = 0
cant_espectadores = 1
recaudacion_total = 0

while cant_espectadores != 0:
    cant_espectadores = int(input("Ingresar la cantidad de espectadores que fueron a ver la funcion. "
                              "Para finalizar ingrese 0: "))
    if cant_espectadores != 0:
        descuento = int(input("Ingresar si la funcion tiene descuento (1=Sí, 2=No): "))

        if descuento == 1:
            recaudado_funcion = cant_espectadores * valor_entrada_desc
            espectadores_desc += cant_espectadores

        else:
            recaudado_funcion = cant_espectadores * valor_entrada

        espectadores_total += cant_espectadores
        recaudacion_total += recaudado_funcion

if espectadores_total > 0:
    porcentaje_descuento = ((espectadores_desc*100)/espectadores_total)

print("La recaudacion total del complejo es de: ", recaudacion_total)
print("Cantidad de espectadores con descuento: ", espectadores_desc)
print("Porcentaje sobre el total de espectadores con descuento: ", porcentaje_descuento)



