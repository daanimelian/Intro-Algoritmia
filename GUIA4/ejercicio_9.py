# Se desea analizar cuántos autos circulan con patente con numeración par y cuántos con numeración impar en un día.
# Escribir un programa que permita ingresar la terminación de la patente (entre 0 y 9) hasta ingresar -1 e informe
# cuántos vehículos pasaron con numeración par y cuántos con numeración impar.
last_digit = 0
even_license_plate = 0
odd_license_plate = 0
print("Ingrese los ultimos dígitos de las patentes y al final ingrese -1.")
while last_digit != -1:
    last_digit = int(input("Ingrese el ultimo digito de la patente (entre 0 y 9): "))
    if last_digit % 2 == 0:
        even_license_plate += 1
    elif last_digit % 2 == 1 and last_digit != -1:
        odd_license_plate += 1

print("En el dia de hoy circularon ", even_license_plate, "pantentes pares y ", odd_license_plate, "patentes impares.")
