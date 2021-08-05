from generate_array import *
from sort_algorithms import *

n = 100


print('VETOR ORDENADO - INSERTION: ')
insertion_sort(vetor_ordenado(n))
print('\nVETOR DESORDENADO - INSERTION: ')
insertion_sort(vetor_desordenado(n))
print('\nVETOR ALEATORIO - INSERTION: ')
insertion_sort(vetor_aleatorio(n))

print('\n\nVETOR ORDENADO - SELECTION: ')
selection_sort(vetor_ordenado(n))
print('\nVETOR DESORDENADO - SELECTION: ')
selection_sort(vetor_desordenado(n))
print('\nVETOR ALEATORIO - SELECTION: ')
selection_sort(vetor_aleatorio(n))

dados = []

print('\n\n VETOR ORDENADO - MERGE: ')
dados = merge_sort(vetor_ordenado(n))
print(dados)
print('\nVETOR DESORDENADO - MERGE: ')
dados2 = merge_sort(vetor_desordenado(n))
print(dados2)
print('\nVETOR ALEATORIO - MERGE: ')
dados3 = merge_sort(vetor_aleatorio(n))
print(dados3)
