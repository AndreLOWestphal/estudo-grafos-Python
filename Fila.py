class Fila:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []
    
    def enqueue(self, items):
        self.items.append(items)

    def dequeue(self):
        if not self.empty():
            return self.items.pop(0)
        return print("A lista está vazia não se pode remover!")
    
    def proximo(self):
        if not self.empty():
            return self.items[0]
        return

    def mostrarFila(self):
        return self.items
   
fila = Fila()
print("Adicionando inteiros a fila.")
fila.enqueue(1)
fila.enqueue(5)
fila.enqueue(4)
fila.enqueue(8)
fila.enqueue(10)
print(f'Fila: {fila.mostrarFila()}')

print("Retirando inteiros a fila.")
fila.dequeue()
fila.dequeue()
fila.dequeue()
print(f'Fila: {fila.mostrarFila()}')

print(f"Proximo elemento a ser removido: {fila.proximo()}.")

print("Retirando demais para teste de erro, vazia.")
fila.dequeue()
fila.dequeue()

print(f"A fila está vazia? {fila.empty()}")

print(f"Tentando remover com fila vazia. Para tratamento de erro:")

fila.dequeue()

