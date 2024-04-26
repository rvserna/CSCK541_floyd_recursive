''' Imperative version of Floyd-Warshall algorithm.
    This algorithm was the provided
    example for the UoL CSCK541 mid-module
    assignment. This algorithm will be
    used for comparison purposes.
    It is available at:
    https://liverpool-online-study.com/pluginfile.php/228862/mod_assign/intro/FloydAlgorithm%20-%20Imperative.pdf?time=1712139479871'''

import itertools
import sys

NO_PATH = sys.maxsize

graph = [[0, 7, NO_PATH, 8],
[NO_PATH, 0 , 5, NO_PATH],
[NO_PATH, NO_PATH, 0, 2],
[NO_PATH, NO_PATH, NO_PATH, 0]]
MAX_LENGTH = len(graph[0])

def floyd_imperative(distance):
    """A simple implementation of Floyd's algorithm"""
    for intermediate, start_node, end_node\
    in itertools.product\
        (range(MAX_LENGTH), range(MAX_LENGTH), range(MAX_LENGTH)):
        # Assume that if start_node and end_node are the same
        # then the distance would be zero
        if start_node == end_node:
            distance[start_node][end_node] = 0
            continue
        # return all possible paths and find the minimum
        distance[start_node][end_node] = min(distance[start_node][end_node],
                distance[start_node][intermediate] + distance[intermediate][end_node])
    # Any value that have sys.maxsize has no path
    print(distance)
floyd_imperative(graph)