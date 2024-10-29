import networkx as nx
import matplotlib.pyplot as plt
import Grafos_direcionado

#Imprimindo a lista de adj grafo nao direcionado
print("Lista de Adjacência do Grafo Não Direcionado: ")
grafo_dirigido = Grafos_direcionado.grafo_dirigido
for node in grafo_dirigido.nodes():
    sucessores = list(grafo_dirigido.successors(node))
    predecessores = list(grafo_dirigido.predecessors(node))
    print(f"Vértice {node}: Sucessores: {sucessores} Predecessores: {predecessores}")