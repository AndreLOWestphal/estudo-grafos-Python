def busca_por_indice(lista, indice):
    if 0 <= indice < len(lista):
        return lista[indice]
    return None
    
lista_indices = [10,20,30,40,50,60]
indice = 2
print(f'Lista: {lista_indices}.')
print(f'Buscando elemento no indice {indice}, {busca_por_indice(lista_indices, indice)}')