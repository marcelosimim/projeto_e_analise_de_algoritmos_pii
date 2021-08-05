import time


def insertion_sort(vetor):
    comparacoes = 0
    movimentacoes = 0
    inicio = time.time()
    for index in range(1, len(vetor)):
        valor = vetor[index]
        movimentacoes += 1
        i = index - 1
        comparacoes += 1
        while i >= 0 and vetor[i] > valor:
            movimentacoes += 1
            vetor[i+1] = vetor[i]
            i = i - 1
        vetor[i+1] = valor
        movimentacoes += 1

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
    for i in range(0, len(vetor)-1):
        menor_index = i
        for j in range(i, len(vetor)-1):
            comparacoes += 1
            if vetor[menor_index] > vetor[j]:
                menor_index = j
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


def merge_sort(vetor):
    dados = [0, 0]  # comparações e movimentações
    dados_esq = [0, 0]
    dados_dir = [0, 0]

    dados[0] += 1  # comparacao
    if len(vetor) > 1:
        meio = len(vetor)//2
        metade_esquerda = vetor[:meio]
        metade_direita = vetor[meio:]

        dados_esq = merge_sort(metade_esquerda)
        dados_dir = merge_sort(metade_direita)

        i = 0
        j = 0
        k = 0

        while i < len(metade_esquerda) and j < len(metade_direita):
            dados[0] += 1  # comparacao
            if metade_esquerda[i] < metade_direita[j]:
                dados[1] += 1  # movimentacao
                vetor[k] = metade_esquerda[i]
                i = i+1
            else:
                dados[1] += 1  # movimentacao
                vetor[k] = metade_direita[j]
                j = j+1
            k = k+1

        while i < len(metade_esquerda):
            dados[1] += 1  # movimentacao
            vetor[k] = metade_esquerda[i]
            i = i+1
            k = k+1

        while j < len(metade_direita):
            dados[1] += 1  # movimentacao
            vetor[k] = metade_direita[j]
            j = j+1
            k = k+1
    dados[0] += dados_esq[0]
    dados[0] += dados_dir[0]
    dados[1] += dados_esq[1]
    dados[1] += dados_dir[1]

    return dados
