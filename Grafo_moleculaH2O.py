import networkx as nx
import matplotlib.pyplot as plt

#Grafo para fluxo de processo
grafo_molecula = nx.Graph()

#processos e suas conexões
atomo = ["O","H-1", "H-2"]
ligacoes = [
    ("O", "H-1"),
    ("O", "H-2"),
]

grafo_molecula.add_nodes_from(atomo)
grafo_molecula.add_edges_from(ligacoes)

#alocando a posição de cada molecula
pos = {
    "O": (0,0),
    "H-1": (-0.5,0.0),
    "H-2": (0.5,0.0),
}

#Visualuzando ligação molecular
plt.figure(figsize=(4,4))
nx.draw(grafo_molecula,pos,with_labels=True,node_size=1000,node_color='yellow',font_weight='bold')
plt.title("Estrutura Molecular (Água - H²O)")
plt.axis('off')
plt.show()