"""Un banco necesita para sus cajeros automáticos un programa que lea una
cantidad de dinero e imprima a cuántos billetes equivale, considerando que
existen billetes de $1000, $500, $100, $50, $10, $5 y $1. Desarrollar dicho
programa de tal forma que se minimice la cantidad de billetes entregados por el
cajero"""

cant_dinero = int(input("Ingrese la cantidad de dinero a retirar: "))
cant_billete_1000 = cant_dinero//1000
cant_dinero = cant_dinero - cant_billete_1000 * 1000
cant_billete_500 = cant_dinero//500
cant_dinero = cant_dinero - cant_billete_500 * 500
cant_billete_100 = cant_dinero//100
cant_dinero = cant_dinero - cant_billete_100 * 100
cant_billete_50 = cant_dinero//50
cant_dinero = cant_dinero - cant_billete_50 * 50
cant_billete_10 = cant_dinero//10
cant_dinero = cant_dinero - cant_billete_10 * 10
cant_billete_5 = cant_dinero//5
cant_dinero = cant_dinero - cant_billete_5 * 5
cant_billete_1 = cant_dinero//1
cant_dinero = cant_dinero - cant_billete_1

print("Se van a entregar: ", cant_billete_1000, " billetes de $1000, ",  cant_billete_500, " billetes de $500, ",
        cant_billete_100, " billetes de $100, ", cant_billete_50, " billetes de $50, ", cant_billete_10, " billetes de $10, ",
      cant_billete_5, " billetes de $5 ,",  cant_billete_1, " billetes de $1. ",)
