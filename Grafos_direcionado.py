import networkx as nx
import matplotlib.pyplot as plt
import random

#Criando um grafo não dirigido
grafo_dirigido = nx.DiGraph()

#Adicionando 5 vertices ao grafo
num_vertices = 5
grafo_dirigido.add_nodes_from(range(num_vertices))

#Adicionando 10 arestas com rotulos e pesos ao grafo nao dirigido
num_arestas = 10
arestas_adicionadas = 0
while arestas_adicionadas < num_arestas:
    vertice_origem = random.randint(0, num_vertices - 1)
    vertice_destino = random.randint(0, num_vertices - 1)

    #verificando se nao e laço e se aresta já existe
    if vertice_origem != vertice_destino and not grafo_dirigido.has_edge(vertice_origem, vertice_destino):
        peso = random.randint(1, 10)
        grafo_dirigido.add_edge(vertice_origem, vertice_destino, weight=peso)
        grafo_dirigido[vertice_origem][vertice_destino]['label'] = f'Peso: {peso}'
        arestas_adicionadas += 1

#imprimindo o grafo nao dirigido
print("Grafo Direcionado: ")
print(grafo_dirigido.edges(data=True))

#Desenhando o grafo
plt.figure(figsize=(6,6))
pos = nx.spring_layout(grafo_dirigido)
nx.draw_networkx(grafo_dirigido, pos, with_labels=True, node_size=500, node_color='skyblue', font_weight='bold')
labels = nx.get_edge_attributes(grafo_dirigido, 'label')
nx.draw_networkx_edge_labels(grafo_dirigido, pos, edge_labels=labels)
plt.title("Grafo Direcionado")
plt.axis('off')
plt.show()