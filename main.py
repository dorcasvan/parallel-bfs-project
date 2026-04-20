from G import generate_random_graph
from benchmark import benchmark

if __name__ == "__main__":
    NUM_NODES = 20000     # augmente à 5000 ou 10000 pour voir le gain
    START_NODE = 0

    graph = generate_random_graph(NUM_NODES)
    benchmark(graph, START_NODE)