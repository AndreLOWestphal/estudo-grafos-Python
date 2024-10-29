import networkx as nx
import Grafos_direcionado

grafo = Grafos_direcionado.grafo_dirigido

#Obtento matriz grafo incidencia nao direcioando
matriz_incidencia_dirigido = nx.incidence_matrix(grafo, oriented=True).todense()

#imprimindo a matriz
print("Matriz de Incidencia do grafo nao dirigido")
print(matriz_incidencia_dirigido)