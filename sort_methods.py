from generate_array import *
from sort_algorithms import *

n = 100000

print(f'\n========= N = {n} ========\n')

print('\n\n VETOR ORDENADO - MERGE: ')
c, m, tempo_segundos = merge_sort(vetor_ordenado(n))
print(f'Comparações: {c}')
print(f'Movimentações: {m}')
print(f'Tempo de execução (segundos): {tempo_segundos}')
print(f'Tempo de execução (minutos): {tempo_segundos/60}')
print('\nVETOR DESORDENADO - MERGE: ')
c, m, tempo_segundos = merge_sort(vetor_desordenado(n))
print(f'Comparações: {c}')
print(f'Movimentações: {m}')
print(f'Tempo de execução (segundos): {tempo_segundos}')
print(f'Tempo de execução (minutos): {tempo_segundos/60}')
print('\nVETOR ALEATORIO - MERGE: ')
c, m, tempo_segundos = merge_sort(vetor_aleatorio(n))
print(f'Comparações: {c}')
print(f'Movimentações: {m}')
print(f'Tempo de execução (segundos): {tempo_segundos}')
print(f'Tempo de execução (minutos): {tempo_segundos/60}')

print('\n\nVETOR ORDENADO - SELECTION: ')
selection_sort(vetor_ordenado(n))
print('\nVETOR DESORDENADO - SELECTION: ')
selection_sort(vetor_desordenado(n))
print('\nVETOR ALEATORIO - SELECTION: ')
selection_sort(vetor_aleatorio(n))

print('\n\nVETOR ORDENADO - INSERTION: ')
insertion_sort(vetor_ordenado(n))
print('\nVETOR DESORDENADO - INSERTION: ')
insertion_sort(vetor_desordenado(n))
print('\nVETOR ALEATORIO - INSERTION: ')
insertion_sort(vetor_aleatorio(n))
