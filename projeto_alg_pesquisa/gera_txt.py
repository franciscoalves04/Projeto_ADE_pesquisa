import random

def gerar_numeros_aleatorios(arquivo, quantidade):
    with open(arquivo, 'w') as file:
        for _ in range(quantidade):
            numero = random.randint(0, 1000000)
            file.write(str(numero) + '\n')

def gerar_numeros_ordenados(arquivo, quantidade):
    with open(arquivo, 'w') as file:
        numeros = [random.randint(0, 1000000) for _ in range(quantidade)]
        numeros.sort()
        for numero in numeros:
            file.write(str(numero) + '\n')

#gerar_numeros_aleatorios('numeros_aleatorios_1000000.txt', 1000000)
gerar_numeros_ordenados('numeros_ordenados_1000000.txt', 1000000)

