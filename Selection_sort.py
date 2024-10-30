def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        indice_minimo = i
        for j in range(i+1,n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]
    return arr

#lista_selecao = [65,45,48,7,5,9,53,1,5,4,8,5,2,3,1]
#print(f'Esta é a array: {lista_selecao}')
#print(f'Esta é a lista ordenada por selection: {selection_sort(lista_selecao)}.')