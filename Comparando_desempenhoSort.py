import timeit
import random
import Bubble_sort
import Selection_sort
import Inserction_sort
import Heap_sort
import Merge_sort
import Quick_sort

def comparando_sort():
    tamanho_lista = 1000
    lista_aleatoria = [random.randint(1,tamanho_lista) for _ in range(tamanho_lista)]

    tempo_bubble = timeit.timeit(lambda: Bubble_sort.bubble_sort(lista_aleatoria.copy()), number=1)
    tempo_selection = timeit.timeit(lambda: Selection_sort.selection_sort(lista_aleatoria.copy()), number=1)
    tempo_inserction = timeit.timeit(lambda: Inserction_sort.inserction_sort(lista_aleatoria.copy()), number=1)
    tempo_heap = timeit.timeit(lambda: Heap_sort.heap_sort(lista_aleatoria.copy()), number=1)
    tempo_merge = timeit.timeit(lambda: Merge_sort.merge_sort(lista_aleatoria.copy()), number=1)
    tempo_quick = timeit.timeit(lambda: Quick_sort.quick_sort(lista_aleatoria.copy(), 0, len(lista_aleatoria)-1), number=1)

    print(f'Tempo do Bubble_sort: {tempo_bubble}')
    print(f'Tempo do Selection_sort: {tempo_selection}')
    print(f'Tempo do Inserction_sort: {tempo_inserction}')
    print(f'Tempo do Inserction_sort: {tempo_heap}')
    print(f'Tempo do Inserction_sort: {tempo_merge}')
    print(f'Tempo do Inserction_sort: {tempo_quick}')

comparando_sort()