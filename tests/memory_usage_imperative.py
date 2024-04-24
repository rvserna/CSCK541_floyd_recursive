''' Performance test - monitoring memory usage of recursive function'''

import tracemalloc
import itertools
import sys

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0 , 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])
# Add the provided imperative algorithm
def floyd_imperative(distance):
    for intermediate, start_node, end_node\
    in itertools.product\
        (range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        distance[start_node][end_node] = min(distance[start_node][end_node],
                distance[start_node][intermediate] + distance[intermediate][end_node])
    print(distance)
floyd_imperative(graph)
# Initiate tracking of memory allocations
tracemalloc.start()
# Run imperative algorithm on graph to track memory usage
floyd_imperative(graph)
# Add print statement to get current and peak sizes of memory blocks
print(tracemalloc.get_traced_memory())
# Stop tracking
tracemalloc.stop()
