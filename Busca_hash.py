tabela_hash = {
    "chave 1": 10,
    "chave 2": 20,
    "chave 3": 30,
    "chave 4": 40,
    "chave 5": 50   
}

chave = "chave 3"
print(f'Tabela hash: {tabela_hash}')
print(f'Buscando o valor associado a {chave}: {tabela_hash.get(chave, "Chave não encontada")} ')