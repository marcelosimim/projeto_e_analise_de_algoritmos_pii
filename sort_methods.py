from generate_array import *
from sort_algorithms import *

n = 1000000

vetor_ordenado = vetor_ordenado(n)
vetor_desordenado = vetor_desordenado(n)
vetor_aleatorio = vetor_aleatorio(n)


print('VETOR ORDENADO - INSERTION: ')
insertion_sort(vetor_ordenado)
print('\nVETOR DESORDENADO - INSERTION: ')
insertion_sort(vetor_desordenado)
print('\nVETOR ALEATORIO - INSERTION: ')
insertion_sort(vetor_aleatorio)

print('\n\nVETOR ORDENADO - SELECTION: ')
selection_sort(vetor_ordenado)
print('\nVETOR DESORDENADO - SELECTION: ')
selection_sort(vetor_desordenado)
print('\nVETOR ALEATORIO - SELECTION: ')
selection_sort(vetor_aleatorio)
