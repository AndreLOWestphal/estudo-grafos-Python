import networkx as nx
import matplotlib.pyplot as plt
import Grafos_direcionado

#Obtendo matriz de adjacencia do grafo nao dirigido
matriz_adj_nao_direcionado = nx.adjacency_matrix(Grafos_direcionado.grafo_nao_direcionado).todense()

#imprimindo a matriz
print("Matriz de Adjacência do Grafo não Direcionado")
print(matriz_adj_nao_direcionado)