from random import randint


def vetor_ordenado(n):
    vetor_ordenado = []
    for i in range(0, n):
        vetor_ordenado.append(i+1)
    return vetor_ordenado


def vetor_desordenado(n):
    vetor_desordenado = []
    for i in range(n, 0, -1):
        vetor_desordenado.append(i)
    return vetor_desordenado


def vetor_aleatorio(n):
    vetor_aleatorio = []
    for i in range(0, n):
        vetor_aleatorio.append(randint(1, n))
    return vetor_aleatorio
