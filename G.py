import random

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj = {i: [] for i in range(num_nodes)}

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # graphe non orienté

    def neighbors(self, node):
        return self.adj[node]


def generate_random_graph(num_nodes, edges_per_node=4):
    graph = Graph(num_nodes)

    for node in range(num_nodes):
        for _ in range(edges_per_node):
            neighbor = random.randint(0, num_nodes - 1)
            if neighbor != node:
                graph.add_edge(node, neighbor)

    return graph
