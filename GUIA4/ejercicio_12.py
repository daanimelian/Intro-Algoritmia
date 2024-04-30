# La sucesión de Fibonacci es una sucesión de números enteros donde cada término se obtiene como suma de los dos
# anteriores, siendo los dos primeros 0 y 1.
# Por lo tanto, Fib=0, 1, 1, 2, 3, 5, 8, 13, 21.... Realizar un programa que lea N e
# imprima los N primeros términos de esta sucesión, como así también la suma de
# los mismos.

n = int(input("Ingrese la cantidad de numeros que quiera saber de la sucesion de fibonacci: "))
suma = 0
fib1 = 0
fib2 = 1
i = 1
while i <= n:
    print(fib1)
    suma = suma + fib1
    aux = fib1
    fib1 = fib2
    fib2 = fib2 + aux
    i = i + 1
print("La suma es: ", suma)
