from graph import generate_graph
from bfs import bfs

graph = generate_graph(10, 15)
result = bfs(graph, 0)

print("Visited nodes:", result)
