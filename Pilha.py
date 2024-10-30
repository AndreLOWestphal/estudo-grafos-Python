class Pilha:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []
    
    def push(self, items):
        self.items.append(items)

    def pop(self):
        if not self.empty():
            return self.items.pop()
        return print("Não pode ser retirado pois está vazia")
    
    def topo(self):
        if not self.empty():
            return self.items[-1]
        return None
    
    def mostrarPilha(self):
        return self.items
    
pilha = Pilha()

print("Adicionado inteiros na pilha.")
pilha.push(1)
pilha.push(2)
pilha.push(9)
pilha.push(15)
pilha.push(3)
print(pilha.mostrarPilha())

print("Retirando inteiros da pilha.")
pilha.pop()
pilha.pop()
print(pilha.mostrarPilha())

print(f"Topo da pilha: {pilha.topo()}.")

print("Retirando demais para teste de erro.")
pilha.pop()
pilha.pop()
pilha.pop()
print(f"A pilha esta vazia? {pilha.empty()}")

print("Testando erro:")
pilha.pop()

