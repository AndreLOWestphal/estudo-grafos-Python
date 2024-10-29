
#Criando nó
class No:
    def __init__(self, valor):
        self.valor = valor
        self.anterior = None
        self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None

    def inserir (self, valor):
        novo_no = No(valor)
        if self.cabeca is None:
            self.cabeca = novo_no
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_no
            novo_no.anterior = atual

    def buscar(self, valor):
        atual = self.cabeca
        while atual is not None:
            if atual.valor == valor:
                return True
            atual = atual.proximo
        return False
    
    def remover(self, valor):
        atual = self.cabeca
        #verificar primeiramente se o item e o primeiro da lista
        if atual is not None and atual.valor == valor:
            self.cabeca = atual.proximo
            if self.cabeca is not None:
                self.cabeca.anterior = None
            return
        
        while atual is not None:
            if atual.valor == valor:
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                return
            atual = atual.proximo
           
    def imprimir_lista(self):
        atual = self.cabeca
        while atual is not None:
            print(atual.valor, end= ' <-> ')
            atual = atual.proximo
        print('None')
    
#Criando lista encadeada simples e inserindo valores
lista = ListaDuplamenteEncadeada()
lista.inserir(1)
lista.inserir(5)
lista.inserir(10)
lista.inserir(24)
lista.inserir(8)
lista.inserir(12)
lista.inserir(55)


#Buscando valores na lista simples
valor_busca = 30
resultado_busca = lista.buscar(valor_busca)
if resultado_busca:
    print(f'O valor {valor_busca} está na lista.')
else:
    print(f'O valor {valor_busca} não está na lista.')

print('Lista Iniciada')
lista.imprimir_lista()

#removendo elemento
elemento_remover = 24
lista.remover(elemento_remover)
print(f'\nRemovendo o elemneto {elemento_remover}')
lista.imprimir_lista()