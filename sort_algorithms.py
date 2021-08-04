import time


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    inicio = time.time()  # captura o tempo de inicio
    for index in range(1, len(vetor)):  # for de 1 até o tamanho do vetor -> custo: n
        valor = vetor[index]
        i = index - 1
        comparacoes += 1
        while i >= 0 and vetor[i] > valor:
            movimentacoes += 1
            vetor[i+1] = vetor[i]
            i = i - 1
        vetor[i+1] = valor

    fim = time.time()
    print(f'Comparações: {comparacoes}')
    print(f'Movimentações: {movimentacoes}')
    tempo_segundos = fim - inicio
    print(f'Tempo de execução (segundos): {tempo_segundos}')
    print(f'Tempo de execução (minutos): {tempo_segundos/60}')
    return vetor


def selection_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    inicio = time.time()  # captura o tempo de inicio
    for i in range(0, len(vetor)):
        menor_index = i
        for j in range(i, len(vetor)):
            comparacoes += 1
            if vetor[menor_index] > vetor[j]:
                menor_index = j
        comparacoes += 1
        if vetor[i] > vetor[menor_index]:
            aux = vetor[i]
            vetor[i] = vetor[menor_index]
            vetor[menor_index] = aux
            movimentacoes += 3

    fim = time.time()
    print(f'Comparações: {comparacoes}')
    print(f'Movimentações: {movimentacoes}')
    tempo_segundos = fim - inicio
    print(f'Tempo de execução (segundos): {tempo_segundos}')
    print(f'Tempo de execução (minutos): {tempo_segundos/60}')
    return vetor
