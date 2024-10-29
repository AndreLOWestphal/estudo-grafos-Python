import networkx as nx
import Grafos_direcionado

grafo = Grafos_direcionado.grafo_nao_direcionado

#Obtento matriz grafo incidencia nao direcioando
matriz_incidencia_nao_dirigido = nx.incidence_matrix(grafo, oriented=False).todense()

#imprimindo a matriz
print("Matriz de Incidencia do grafo nao dirigido")
print(matriz_incidencia_nao_dirigido)