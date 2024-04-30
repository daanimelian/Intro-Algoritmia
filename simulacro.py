#TODO: Usar banderas para menor y mayor precio
menor_precio = 0
mayor_precio = 0
cant_tipo_instrumentos = 0
cant_total_instrumentos = 0
precio_total = 0
stock_minimo = 5
es_primer_instrumento = True
nombre_instrumento = ""
while nombre_instrumento != "fin":
    nombre_instrumento = input("Ingrese el nombre del instrumento: ")
    if nombre_instrumento != "fin":
        precio_instrumento = float(input("Ingrese el precio del instrumento: "))
        stock_instrumento = int(input("Ingrese la cantidad en stock: "))
        if (precio_instrumento < menor_precio) or es_primer_instrumento:
            menor_precio = precio_instrumento
            nombre_instrumento_barato = nombre_instrumento
        if precio_instrumento > mayor_precio or es_primer_instrumento:
            mayor_precio = precio_instrumento
            nombre_instrumento_caro = nombre_instrumento
        es_primer_instrumento=False
        if stock_instrumento < stock_minimo:
            lista_instrumentos = lista_instrumentos + "-" + nombre_instrumento
        cant_total_instrumentos += stock_instrumento
        cant_tipo_instrumentos += 1
        precio_total += precio_instrumento

promedio_precio = precio_total / cant_tipo_instrumentos

print("El precio promedio es: ", promedio_precio)
print("La cantidad total de instrumentos es: ", cant_total_instrumentos)
print("El instrumento con menor precio es: ", nombre_instrumento_barato)
print("El instrumento con mayor precio es: ", nombre_instrumento_caro)
print("El promedio de precios es: ", promedio_precio)
print("Lista de intrumentos con stock menor a 5: ", lista_instrumentos)
