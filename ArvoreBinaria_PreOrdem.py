class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita =None

def pre_ordem(raiz):
    if raiz:
        print(raiz.valor, end=" ")
        pre_ordem(raiz.esquerda)
        pre_ordem(raiz.direita)

raiz = No(4)
raiz.esquerda = No(2)
raiz.direita = No(6)
raiz.esquerda.esquerda = No(1)
raiz.esquerda.direita = No(3)
raiz.direita.esquerda = No(5)
raiz.direita.direita = No(7)

pre_ordem(raiz)