def descomponer_numero_general(numero):
    componentes = []
    posicion = 0
    while numero > 0:
        componente = (numero // (10**posicion)) % 10
        componentes.append(componente)
        numero = numero - (componente * 10**posicion)
        posicion += 1
    return componentes


# Ejemplo de uso
num = 987654321
componentes = descomponer_numero_general(num)
print(componentes)  # Salida: [9, 8, 7, 6, 5, 4, 3, 2, 1]
