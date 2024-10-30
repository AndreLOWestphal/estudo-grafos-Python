def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        trocou = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocou = True
        if not trocou:
            break
    return arr

#lista_bolha = [64,12,5,8,6,12,45,68,8,98,48,12,1,32]
#print(f'Lista Original: {lista_bolha}.')
#print(f'Lista com Bubble_sort: {bubble_sort(lista_bolha)}.')