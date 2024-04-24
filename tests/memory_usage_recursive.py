''' Performance test - monitoring memory usage of recursive function'''

import tracemalloc
import sys

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0 , 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
         ]
MAX_LENGTH = len(graph[0])

# Add the recursive algorithm
def floyd_warshall(graph):

    def shortest_path(a, z):
        if a == z:
            return 0
        return min(
             shortest_path(a, z), shortest_path(a, m) + shortest_path(m, z))
    for a in range(MAX_LENGTH):
        for m in range(MAX_LENGTH):
            for z in range(MAX_LENGTH):
                graph[a][z] = min(graph[a][z], graph[a][m] + graph[m][z])
    return graph


print(floyd_warshall(graph))
# Initiate tracking of memory allocations
tracemalloc.start()
# Run recursive algorithm on graph to track memory usage
floyd_warshall(graph)
# Add print statement to get current and peak sizes of memory blocks
print(tracemalloc.get_traced_memory())
# Stop tracking
tracemalloc.stop()
