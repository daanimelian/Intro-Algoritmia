"""Diseñar un programa que calcule y muestre el sueldo neto de un empleado en
base a su sueldo básico y su antigüedad en años. Si es soltero se le incrementa
el sueldo en 5% del salario bruto por cada año de antigüedad, mientras que si es
casado se le incrementa el sueldo en 7% del bruto por cada año de antigüedad.
También se le realizan los siguientes descuentos: Jubilación: 11%, Obra Social:
3%, Sindicato: 3%. Como datos de entrada se ingresa por teclado el sueldo básico, antigüedad y
estado civil (1 si es soltero o 2 si es casado). Se debe informar: (reemplazar los
9 por los valores que correspondan)"""
sueldo_bruto = 0
incremento_soltero = 1.05
incremento_casado = 1.07
desc_jubilacion = 0.11
desc_os = 0.03
desc_sindc = 0.03
sueldo_basico =  float(input("Ingresar el sueldo basico del trabajador: "))
antiguedad = int(input("Ingresar la antiguedad del trabajador: "))
estado_civil = int(input("Ingresar el estado civil del trabajador (1 si es soltero o 2 si es casado): "))

if estado_civil == 1:
    sueldo_bruto = sueldo_basico * (incremento_soltero ** antiguedad)
elif estado_civil == 2:
    sueldo_bruto = sueldo_basico * (incremento_casado ** antiguedad)
else:
    sueldo_bruto = sueldo_basico

monto_desc_jubilacion = sueldo_bruto * desc_jubilacion
monto_desc_os = sueldo_bruto * desc_os
monto_desc_sindc = sueldo_bruto * desc_sindc

sueldo_neto = sueldo_bruto - (monto_desc_jubilacion) - (monto_desc_os) - (monto_desc_sindc)

print("El sueldo basico es: $", sueldo_basico)
print("El sueldo bruto es: $", sueldo_bruto)
print("Los descuentos son de : $", monto_desc_jubilacion, " por jubilacion, $", monto_desc_os,
      " por obra social y $", monto_desc_sindc, " por sindicato.")

print("El sueldo neto es de: $", sueldo_neto)
