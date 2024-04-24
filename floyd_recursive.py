"""Recursive Version of Floyd Warshall Algorithm"""

# Import sys module to define NO_PATH variable
import sys
# Set NO_PATH equal to maximize value to represent infinity
NO_PATH = sys.maxsize
# Create new graph variable with same lists as example algorithm
graph = [[0, 7, NO_PATH, 8],
        [NO_PATH, 0 , 5, NO_PATH],
        [NO_PATH, NO_PATH, 0, 2],
        [NO_PATH, NO_PATH, NO_PATH, 0]
         ]
MAX_LENGTH = len(graph[0])


def floyd_warshall(graph):
    """ Calculates shortest distance between all
        pairs of nodes in graph """
    # Create nested function to find the minimum distance using recursion
    def shortest_path(a, z):
        # Create a base case where
        # the distance will be zero
        # because the start node and
        # end node are the same
        if a == z:
            return 0
        # Calculate minimum distance using recursive calls
        return min(
             shortest_path(a, z), shortest_path(a, m) + shortest_path(m, z))
    # Add all vertices and update graph
    for a in range(MAX_LENGTH):
        for m in range(MAX_LENGTH):
            for z in range(MAX_LENGTH):
                graph[a][z] = min(graph[a][z], graph[a][m] + graph[m][z])
    return graph

# Print updated graph
print(floyd_warshall(graph))
