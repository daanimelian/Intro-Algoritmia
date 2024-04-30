cant_num = 0
numero = int(input("Ingrese un número (-1 para finalizar): "))
while numero != -1:
    cant_num += 1
    numero = int(input("Ingrese un número (-1 para finalizar): "))

if cant_num % 2 == 0:
    print("La cantidad de elementos es par.")
else:
    print("La cantidad de elementos es impar.")
