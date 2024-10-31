def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1

lista_numeros = [64,12,5,8,6,12,45,68,8,98,48,12,1,32]
busca_elemento = 32
print(f'Lista Original: {lista_numeros}.')
print(f'Buscando o elemento {busca_elemento} na posição:  {busca_sequencial(lista_numeros, busca_elemento)}.')