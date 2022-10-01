import random


def gera_matriz(linhas, colunas):
    matriz = []
    for l in range(linhas):
        linha = []
        for c in range(colunas):
            linha.append(random.randint(0, 1))
        matriz.append(linha)
    return matriz


def imprime_matriz(matriz):
    print(*matriz, sep='\n')
