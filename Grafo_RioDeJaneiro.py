import networkx as nx
import matplotlib.pyplot as plt

#grafo de mapa ficticio do RJ
grafo_mapa = nx.Graph()

#adicionando cidades do RJ
cidades = {
    "Rio de Janeiro": {"local":(-43.1729,-22.9068)},
    "Niteroi": {"local": (-43.1232,-22.8837)},
    "Duque de Caxias": {"local": (-43.2117,-22.7851)},
    "Nova Iguaçu": {"local": (-43.4512,-22.7551)},
    "Petropolis": {"local": (-43.1787,-22.5096)},
}

#adicionando nós ao grafo
for cidade, info in cidades.items():
    grafo_mapa.add_node(cidade, pos=info['local'])

#definindo conexões e pesos entre cidades
conexoes = [
    ("Rio de Janeiro","Niteroi",{"weight":10}),
    ("Rio de Janeiro","Duque de Caxias",{"weight":20}),
    ("Rio de Janeiro","Nova Iguaçu",{"weight":30}),
    ("Rio de Janeiro","Petropolis",{"weight":50}),
    ("Niteroi","Duque de Caxias",{"weight":25}),
    ("Niteroi","Nova Iguaçu",{"weight":35}),
    ("Duque de Caxias","Nova Iguaçu",{"weight":15}),
    ("Duque de Caxias","Petropolis",{"weight":45}),
    ("Nova Iguaçu","Petropolis",{"weight":40}),
]

#adicionando conexoes ap grafo com peso
grafo_mapa.add_edges_from(conexoes)

#definindo posição dos nós com base nas cordenadas
pos = {cidade:(info["local"][0], info["local"][1]) for cidade, info in cidades.items()}

#cisualizando mapa com tamanho reduzido
plt.figure(figsize=(6,4))
nx.draw(grafo_mapa,pos,with_labels=True,node_size=300,node_color='lightblue',font_size=8,font_weight='bold')
labels = nx.get_edge_attributes(grafo_mapa,'weight')
nx.draw_networkx_edge_labels(grafo_mapa,pos,edge_labels=labels, font_size=6)
plt.title("Mapa Ficticio do Rio de Janeiro")
plt.axis('off')
plt.show()