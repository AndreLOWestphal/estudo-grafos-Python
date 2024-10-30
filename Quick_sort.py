def partition(arr, inicio, fim):
    pivo = arr[fim]
    i = inicio - 1

    for j in range(inicio, fim):
        if arr[j] <= pivo:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[fim] = arr[fim], arr[i+1]
    return i+1

def quick_sort(arr, inicio, fim):
    if inicio < fim:
        pivo = partition(arr, inicio, fim)
        quick_sort(arr, inicio, pivo -1)
        quick_sort(arr, pivo + 1, fim)
    return arr

#lista_numeros = [12,5,6,849,81,5,36,4,8,6,54,12,65,4]
#print(f'Lista: {lista_numeros}')
#print(f'Ordenando via quick_sort: {quick_sort(lista_numeros.copy(), 0, len(lista_numeros)-1)}')