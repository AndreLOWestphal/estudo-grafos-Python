import heapq
import networkx as nx
import matplotlib.pyplot as plt

def astar(graph, start, goal, heuristic):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start, [start]))

    while open_set:
        current_cost, current_node, path = heapq.heappop(open_set)

        if current_node == goal:
            return path
        
        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, cost in graph[current_node].items():
            if neighbor in closed_set:
                continue

            heapq.heappush(open_set, (current_cost + cost['weight'] + heuristic(neighbor, goal), neighbor, path + [neighbor]))
    
    return None

#Uso com pesos
graph ={
    'A':{'B': {'weight':4},'C': {'weight':2}},
    'B':{'A': {'weight':4},'C': {'weight':1}, 'D': {'weight':5}},
    'C':{'A': {'weight':2},'B': {'weight':1}, 'D': {'weight':3}},
    'D':{'B': {'weight':5},'C': {'weight':3}}
}

#FUNÇÃO HEURISTICA distancia em linha reta entre nós
def heuristic(node, goal):
    heuristic_costs = {
        'A': 4,
        'B': 3,
        'C': 2,
        'D': 0
    }
    return heuristic_costs[node]

start_node = 'A'
goal_node = 'D'

#encontrando o caminho mais curto
shortest_path = astar(graph, start_node, goal_node, heuristic)
print(f"O menor caminho de {start_node} a {goal_node} é: {shortest_path}")

#grafo para visualização
Grafo = nx.Graph()

#adicionando nos e arestas com pesos
for node, neighbors in graph.items():
    Grafo.add_node(node)
    for neighbor, cost in neighbors.items():
        Grafo.add_edge(node, neighbor, weight=cost['weight'])

#adicionando o caminho mais curto
edges = [(shortest_path[i], shortest_path[i+1]) for i in range(len(shortest_path)-1)]
Grafo.add_edges_from(edges)

#produzindo visualização
plt.figure(figsize=(6,4))
pos = nx.spring_layout(Grafo)
nx.draw(Grafo, pos, with_labels=True, font_weight='bold')
edge_labels = {(u,v): d['weight'] for u,v, d in Grafo.edges(data=True)}
nx.draw_networkx_edge_labels(Grafo, pos, edge_labels=edge_labels)
nx.draw_networkx_edges(Grafo, pos, edgelist=edges, edge_color='r', width=2)
plt.title(f'Caminho mais curto de {start_node} a {goal_node} com pesos das arestas.')
plt.show()