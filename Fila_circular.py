class FilaCircular:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.items = [None] * tamanho
        self.inicio = 0
        self.tamanho_atual = 0

    def vazia(self):
        return self.tamanho_atual == 0
    
    def cheia(self):
        return self.tamanho_atual == self.tamanho
    
    def enfileirar(self,item):
        if not self.cheia():
            fim = (self.inicio + self.tamanho_atual) % self.tamanho
            self.items[fim] = item
            self.tamanho_atual += 1

    def desenfileirar(self):
        if not self.vazia():
            item = self.items[self.inicio]
            self.items[self.inicio] = None
            self.inicio = (self.inicio + 1) % self.tamanho
            self.tamanho_atual -= 1
            return item
        return None
    
    def frente(self):
        if not self.vazia():
            return self.items[self.inicio]
        return None
    
fila_circular = FilaCircular(5)

fila_circular.enfileirar(11)
fila_circular.enfileirar(80)
fila_circular.enfileirar(55)
fila_circular.enfileirar(13)
fila_circular.enfileirar(5)
fila_circular.enfileirar(1)
fila_circular.enfileirar(8)

print(f'Frente da fila circular: {fila_circular.frente()}')

print('Desenfileirar: ')
while not fila_circular.vazia():
    print(fila_circular.desenfileirar())