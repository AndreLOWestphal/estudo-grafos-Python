class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def altura(self, no):
        if not no:
            return 0
        return no.altura
    
    def rotacao_simples_direita(self,z):
        y = z.esquerda
        T3= y.direita

        y.direita = z
        z.esquerda = T3

        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y
    
    def rotacao_simples_esquerda(self,z):

        y = z.direita
        T2= y.esquerda

        y.esquerda = z
        z.direita = T2

        z.altura = 1 + max(self.altura(z.esquerda), self.altura(z.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))

        return y
    
    def inserir(self, no, valor):
        if not no:
            return No(valor)
        
        if valor < no.valor:
            no.esquerda = self.inserir(no.esquerda, valor)
        else:
            no.direita = self.inserir(no.direita,valor)

        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

        balanceamento = self.altura(no.esquerda) - self.altura(no.direita)

        if balanceamento > 1 and valor < no.esquerda.valor:
            return self.rotacao_simples_direita(no)
        return no

    def pre_ordem(self, no):
        if not no:
            return []
        
        resultado = [no.valor]
        resultado += self.pre_ordem(no.esquerda)
        resultado += self.pre_ordem(no.direita)

        return resultado

    def imprime_arvore(self, no, espaco):
        if not no:
            return
        
        espaco += 10

        if no.direita:
            self.imprime_arvore(no.direita, espaco)

        print()
        for i in range(10, espaco):
            print(" ", end=" ")

        print(no.valor)

        if no.esquerda:
            self.imprime_arvore(no.esquerda, espaco)
            
def inserir_valores(arvore, valores):
    raiz = None
    for valor in valores:
        raiz = arvore.inserir(raiz, valor)
    return raiz

arvore = ArvoreAVL()
valores = [10, 20, 30, 40, 50, 25]

raiz = inserir_valores(arvore, valores)

print(f'Árvore AVL Original (pré ordem): ')
print(arvore.pre_ordem(raiz))

raiz = arvore.rotacao_simples_esquerda(raiz)
print(f'\nArvore AVL apos rotação sompres a Esquerda (Pré Ordem)')
print(arvore.pre_ordem(raiz))