import random

def generate_graph(n, edges):
    graph = {i: [] for i in range(n)}
    for _ in range(edges):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        graph[u].append(v)
        graph[v].append(u)
    return graph
