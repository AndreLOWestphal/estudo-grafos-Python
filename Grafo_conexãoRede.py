import networkx as nx
import matplotlib.pyplot as plt

topologia_rede = nx.Graph()

dispositivos = {'PC1','PC2','Roteador1','Roteador2','Servidor'}

topologia_rede.add_nodes_from(dispositivos)

conexoes = [
    ('PC1', 'Roteador1'),
    ('PC2', 'Roteador1'),
    ('Roteador1', 'Roteador2'),
    ('Roteador2', 'Servidor')
]

topologia_rede.add_edges_from(conexoes)

try:
    caminho = nx.shortest_path(topologia_rede, source='PC1', target="Servidor")
    print(f"Caminho para roteamento de PC1 ao Servidor: {caminho}.")
except nx.NetworkXNoPath:
    print(f"Não foi possivel encontrar um caminho de roteamento entre PC1 e o Servidor.")

plt.figure(figsize=(8,6))
pos = nx.spring_layout(topologia_rede)
nx.draw(topologia_rede, pos, with_labels=True, font_weight='bold')
plt.title('Topologia de Rede de Computadores')
plt.show()

