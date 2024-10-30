def inserction_sort(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

#lista_insercao = [1,56,4,8,5,3,1,5,9,84,5,65,85,15,31,2]
#print(f'Lista: {lista_insercao}')
#print(f'Ordenando com Insertion Sort: {inserction_sort(lista_insercao)}')