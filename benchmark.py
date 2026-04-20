import time
from bfs_sequential import bfs_sequential
from bfs_parallel import bfs_parallel

def benchmark(graph, start):
    start_time = time.time()
    seq_result = bfs_sequential(graph, start)
    seq_time = time.time() - start_time

    start_time = time.time()
    par_result = bfs_parallel(graph, start)
    par_time = time.time() - start_time

    print("BFS Séquentiel:")
    print(" Temps:", seq_time)
    print(" Nœuds visités:", len(seq_result))

    print("\nBFS Parallèle:")
    print(" Temps:", par_time)
    print(" Nœuds visités:", len(par_result))

    if seq_result == par_result:
        print("\n✅ Les résultats sont identiques")
    else:
        print("\n❌ Résultats différents (erreur)")