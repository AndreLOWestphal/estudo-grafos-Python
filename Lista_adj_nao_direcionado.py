import networkx as nx
import matplotlib.pyplot as plt
import Grafos_direcionado

#Imprimindo a lista de adj grafo nao direcionado
print("Lista de Adjacência do Grafo Não Direcionado: ")
grafo_nao_dirigido = Grafos_direcionado.grafo_nao_direcionado
for node in grafo_nao_dirigido.nodes():
    vizinhos = list(grafo_nao_dirigido.neighbors(node))
    print(f"Vertiice {node}: {vizinhos}")