# Definindo a classe Node referente ao nó da árvore
class Node:
    def __init__(self, valor):
        self.esquerda = None
        self.direita = None
        self.valor = valor

# Definindo a classe BinaryTree com métodos para inserção e percursos
class BinaryTree:
    def __init__(self):
        self.raiz = None

    # Inserindo um nó na árvore
    def inserir(self, raiz, valor):
        if raiz is None:
            return Node(valor)
        else:
            if raiz.valor < valor:
                raiz.direita = self.inserir(raiz.direita, valor)
            else:
                raiz.esquerda = self.inserir(raiz.esquerda, valor)
        return raiz

    # Método de percurso em Pré-Ordem
    def pre_ordem(self, raiz):
        if raiz:
            print(raiz.valor, end=" ")
            self.pre_ordem(raiz.esquerda)
            self.pre_ordem(raiz.direita)

    # Método de percurso Em Ordem
    def em_ordem(self, raiz):
        if raiz:
            self.em_ordem(raiz.esquerda)
            print(raiz.valor, end=" ")
            self.em_ordem(raiz.direita)

    # Método de percurso Pós-Ordem
    def pos_ordem(self, raiz):
        if raiz:
            self.pos_ordem(raiz.esquerda)
            self.pos_ordem(raiz.direita)
            print(raiz.valor, end=" ")

# Instanciando a árvore binária
arvore = BinaryTree()

# Inserindo valores na árvore
valores = [50, 30, 20, 40, 70, 60, 80]
for valor in valores:
    arvore.raiz = arvore.inserir(arvore.raiz, valor)

# Testando os métodos de percurso
print("Percurso Pré-Ordem:")
arvore.pre_ordem(arvore.raiz)
print("\nPercurso Em Ordem:")
arvore.em_ordem(arvore.raiz)
print("\nPercurso Pós-Ordem:")
arvore.pos_ordem(arvore.raiz)
