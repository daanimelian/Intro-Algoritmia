"""Una persona invierte su capital en un banco y desea saber cuánto dinero ganará
en un mes, teniendo en cuenta que el banco paga 2% mensual. ¿Cuánto ganará
en seis meses si deja su dinero invertido?"""
interes = 1.02
cant_meses = 6
capital = float(input("Ingresar el capital que desea invertir: "))
ganancia = (capital * (interes ** cant_meses)) - capital
capital_total = capital * (interes ** cant_meses)

print("La ganancia es de: $", ganancia)
print("Su capital total es de: $", capital_total)