import networkx as nx
import matplotlib.pyplot as plt

#Grafo para fluxo de processo
grafo_molecula = nx.Graph()

#processos e suas conexões
atomo = ["C","H1", "H2", "H3", "H4"]
ligacoes = [
    ("C", "H1"),
    ("C", "H2"),
    ("C", "H3"),
    ("C", "H4")
]

grafo_molecula.add_nodes_from(atomo)
grafo_molecula.add_edges_from(ligacoes)

#alocando a posição de cada molecula
pos = {
    "C": (0,0),
    "H1": (0.5,0.5),
    "H2": (-0.5,-0.5),
    "H3": (-0.5,0.5),
    "H4": (0.5,-0.5)
}

#Visualuzando ligação molecular
plt.figure(figsize=(4,4))
nx.draw(grafo_molecula,pos,with_labels=True,node_size=1000,node_color='yellow',font_weight='bold')
plt.title("Estrutura Molecular (Metano - CH4)")
plt.axis('off')
plt.show()