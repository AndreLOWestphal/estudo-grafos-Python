import networkx as nx
import matplotlib.pyplot as plt

#grafo com peso para usar kruskal
grafo_kruskal = nx.Graph()
grafo_kruskal.add_edge('A','B',weight=4)
grafo_kruskal.add_edge('A','C',weight=2)
grafo_kruskal.add_edge('B','C',weight=1)
grafo_kruskal.add_edge('B','D',weight=5)
grafo_kruskal.add_edge('C','D',weight=3)

#Grafo Orginal
plt.figure(figsize=(4,3))
pos = nx.spring_layout(grafo_kruskal)
edge_labels = nx.get_edge_attributes(grafo_kruskal,'weight')
nx.draw(grafo_kruskal,pos,with_labels=True,font_weight='bold')
nx.draw_networkx_edge_labels(grafo_kruskal,pos,edge_labels=edge_labels)
plt.title("Grafo Original")
plt.show()

#Algoritmo prim
mst_prim = nx.minimum_spanning_tree(grafo_kruskal, algorithm='prim')

#Visualizando grafo com prim
plt.figure(figsize=(4,3))
pos = nx.spring_layout(mst_prim)
edge_labels_mst = nx.get_edge_attributes(mst_prim,'weight')
nx.draw(mst_prim,pos,with_labels=True,font_weight='bold')
nx.draw_networkx_edge_labels(mst_prim,pos,edge_labels=edge_labels_mst)
plt.title('Grafo com o kruskal(Prim)')
plt.show()