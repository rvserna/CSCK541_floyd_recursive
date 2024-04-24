"""The following graphs are test
    cases that will be used
    to verify that the algorithm
     is operating correctly"""
import sys

NO_PATH = sys.maxsize

# Add different graph
testCaseA = [[0, 7, NO_PATH, 8],
             [NO_PATH, 8, 5, NO_PATH],
             [NO_PATH, NO_PATH, 3, 0],
             [ NO_PATH, NO_PATH, NO_PATH, 4]]
# Add the expected output for the above graph
testOutputA = [[0, 7, 12, 8],
               [9223372036854775807, 8, 5, 5],
               [9223372036854775807, 9223372036854775807, 3, 0],
               [9223372036854775807, 9223372036854775807, 9223372036854775807, 4]]
# Add graph with 6 vertices
testCaseB = [[0, 5, NO_PATH, 8, 6, NO_PATH],
             [NO_PATH, 2, 7, NO_PATH, 5],
             [NO_PATH, NO_PATH, 8, 2, NO_PATH, 5],
             [ NO_PATH, NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH]]
# Add the expected output for the graph with 6 vertices
testOutputB = [[0, 5, 12, 8, 6, NO_PATH],
             [NO_PATH, 2, 7, 9, 5],
             [NO_PATH, NO_PATH, 8, 2, NO_PATH, 5],
             [NO_PATH, NO_PATH, NO_PATH, 3, NO_PATH, NO_PATH]]

