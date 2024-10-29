import networkx as nx
import matplotlib.pyplot as plt

#grafo com peso para usar kruskal
grafo_djikstra = nx.DiGraph()
grafo_djikstra.add_edge('A','B',weight=4)
grafo_djikstra.add_edge('A','C',weight=2)
grafo_djikstra.add_edge('B','C',weight=1)
grafo_djikstra.add_edge('B','D',weight=5)
grafo_djikstra.add_edge('C','D',weight=3)

#Algoritmo Dijkstra para encontrar o menor caminho de A a D
shortest_path = nx.shortest_path(grafo_djikstra,'A','D', weight='weight')

#Visualizando grafo com Dijkstra
plt.figure(figsize=(4,3))
pos = nx.spring_layout(grafo_djikstra)
edge_labels_dijkstra = nx.get_edge_attributes(grafo_djikstra,'weight')
path_edges = [(shortest_path[i],shortest_path[i+1]) for i in range(len(shortest_path)-1)]
nx.draw_networkx_edges(grafo_djikstra, pos, edgelist=path_edges, edge_color='r',width=2)
nx.draw(grafo_djikstra,pos,with_labels=True,font_weight='bold')
nx.draw_networkx_edge_labels(grafo_djikstra, pos, edge_labels=edge_labels_dijkstra)
plt.title('Menor Caminho (Dijkstra)')
plt.show()