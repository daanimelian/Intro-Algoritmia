"""Una inmobiliaria paga a sus vendedores un salario de $250000, más una comisión de $50000 por cada venta realizada,
más el 5% del valor de las ventas.
Realizar un programa que imprima el número del vendedor y el salario que le
corresponde en un determinado mes. Se leen el número del vendedor, la cantidad de ventas que realizó y el valor total
de las mismas. """

salario = 250000
comision = 50000
porcentaje_venta = 0.5
num_vendendor = int(input("Ingresar el numero del vendedor: "))
cant_ventas = int(input("Ingresar la cantidad de ventas realizadas: "))
valor_total = float(input("Ingresar el valor total de la venta: "))
salario_total = salario + (cant_ventas * comision) + (porcentaje_venta*valor_total)

print("El salario total del vendedor ", num_vendendor, " es de: ", salario_total)
