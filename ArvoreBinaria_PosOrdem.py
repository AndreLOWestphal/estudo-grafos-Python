class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita =None

def pos_ordem(raiz):
    if raiz:
        pos_ordem(raiz.esquerda)
        pos_ordem(raiz.direita)
        print(raiz.valor, end=" ")

raiz = No(4)
raiz.esquerda = No(2)
raiz.direita = No(6)
raiz.esquerda.esquerda = No(1)
raiz.esquerda.direita = No(3)
raiz.direita.esquerda = No(5)
raiz.direita.direita = No(7)

pos_ordem(raiz)