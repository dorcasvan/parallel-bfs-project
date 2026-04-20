from threading import Thread, Lock

def bfs_parallel(graph, start):
    visited = set()
    visited.add(start)

    visited_lock = Lock()
    frontier = [start]

    while frontier:
        next_frontier = []
        threads = []

        def process_node(node):
            for neighbor in graph.neighbors(node):
                with visited_lock:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        next_frontier.append(neighbor)

        for node in frontier:
            t = Thread(target=process_node, args=(node,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        frontier = next_frontier

    return visited