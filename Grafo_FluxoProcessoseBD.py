import networkx as nx
import matplotlib.pyplot as plt

#Grafo para fluxo de processo
grafo_processo = nx.DiGraph()

#processos e suas conexões
etapas = ["Inicio","Etapa 1", "Etapa 2", "Etapa 3", "Fim"]
conexoes_processo = [
    ("Inicio", "Etapa 1"),
    ("Etapa 1", "Etapa 2"),
    ("Etapa 2", "Etapa 3"),
    ("Etapa 3", "Fim")
]

grafo_processo.add_nodes_from(etapas)
grafo_processo.add_edges_from(conexoes_processo)

#Visualuzando fluxo do processo
plt.figure(figsize=(6,4))
pos_processo = nx.spring_layout(grafo_processo)
nx.draw(grafo_processo,pos_processo,with_labels=True,node_size=500,node_color='lightgreen',font_weight='bold')
plt.title("Fluxo de Processo ou pode ser de Banco de Dados")
plt.axis('off')
plt.show()