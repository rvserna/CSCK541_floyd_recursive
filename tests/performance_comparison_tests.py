""" Compare performance of the recursive,
    imperative, and Geeks for Geeks
    algorithm, measuring execution time."""
# Import 'sys' and 'time' modules to run tests
import sys
import time
# Import each of the algorithms
from CSCK541_floyd_recursive.floyd_warshall_recursive import floyd_recursive
from CSCK541_floyd_recursive.floyd_algorithms_for_comparison import floyd_geeks_for_geeks
from CSCK541_floyd_recursive.floyd_algorithms_for_comparison import floyd_warshall_imperative
# Create a comparison function that
# will track the execution time
# of each algorithm.
def perform_comparison():
    NO_PATH = sys.maxsize
    graph = [[0, 7, NO_PATH, 8],
             [NO_PATH, 0, 5, NO_PATH],
             [NO_PATH, NO_PATH, 0, 2],
             [NO_PATH, NO_PATH, NO_PATH, 0]
             ]
    v = len(graph[0])
    # Initiate tracking by adding start
    # time and set range to 10,000
    start_time = time.time()
    for _ in range(10000):
        # Run algorithm
        floyd_recursive.floyd_warshall(graph)
    # Define elapsed time as the
    # difference between the execution time
    # and start time
    elapsed_recursive = time.time() - start_time
    # Repeat process for imperative algorithm
    start_time = time.time()
    for _ in range(10000):
        floyd_warshall_imperative.floyd_imperative(graph)
    elapsed_imperative = time.time() - start_time
    # Repeat process for Geeks for
    # Geeks algorithm
    start_time = time.time()
    for _ in range(10000):
        floyd_geeks_for_geeks.floydWarshall(graph)
    elapsed_geeksforgeeks = time.time() - start_time
    # Return elapsed time for each algorithm
    return (elapsed_recursive, elapsed_imperative, elapsed_geeksforgeeks)
# Print result to show comparison
print(perform_comparison())