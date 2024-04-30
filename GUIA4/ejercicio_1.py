num_input=int(input("Ingrese un número, para finalizar el programa ingrese -1: "))
first_num = num_input
if num_input != -1:
    while num_input != -1:
        last_num = num_input
        num_input = int(input("Ingrese un número, para finalizar el programa ingrese: "))
    print("El primer numero ingresado es: ", first_num, " y el ultimo numero es: ", last_num)
else:
    print("No se ingresó ningun número.")