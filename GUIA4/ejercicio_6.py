# Mostrar la tabla de multiplicar (entre 1 y 12) del número 4. ¿Cómo cambiaría el
# algoritmo para que el usuario pueda decidir la tabla de multiplicar a mostrar?

# multiplicador = 1
# while multiplicador <= 12:
#     print(multiplicador*4)
#     multiplicador += 1

num = int(input("Ingrese un numero del cual quiera saber la tabla de multiplicar: "))
mult = 1
while mult <= 12:
    res = num * mult # por perdida de decimales hacemos el res afuera
    print(res)
    mult += 1
