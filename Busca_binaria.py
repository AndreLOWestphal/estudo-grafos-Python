def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] < item:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

lista_numeros = [1,4,5,8,9,12,13,15,20]
busca_elemento = 4
print(f'Lista Original: {lista_numeros}.')
print(f'Buscando o elemento {busca_elemento} na posição:  {busca_binaria(lista_numeros, busca_elemento)}.')
    