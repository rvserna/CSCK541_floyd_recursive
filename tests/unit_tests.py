"""Unit Tests to verify that
 the recursive algorithm returns the
  expected output"""

import unittest
import sys
# Import recursive algorithm and test cases
from CSCK541_floyd_recursive.floyd_warshall_recursive import floyd_recursive
from test_cases import (testCaseA,
                        testOutputA, testCaseB, testOutputB)


class FloydTestCase(unittest.TestCase):
    # Test the floyd warshall function against expected output
    def test_floyd_function(self):
        NO_PATH = sys.maxsize
        # Add example graph
        graph = [[0, 7, NO_PATH, 8],
                 [NO_PATH, 0, 5, NO_PATH],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]
                 ]
        v = len(graph[0])
        # Add expected output for example graph
        shortest_graph = [[0, 7, 12, 8],
                 [NO_PATH, 0, 5, 7],
                 [NO_PATH, NO_PATH, 0, 2],
                 [NO_PATH, NO_PATH, NO_PATH, 0]
                          ]
        result = floyd_recursive.floyd_warshall(graph)
        self.assertEqual(result, shortest_graph, "Incorrect output")


class TestDifferentGraphs(unittest.TestCase):
    # Conduct unit tests to verify
    # that the output of running
    # the recursive algorithm on different
    # graphs matches the expected output.
    # Test a different graph with 4 vertices

    def test_A(self):
        self.assertEqual(floyd_recursive.floyd_warshall(testCaseA), testOutputA, "Incorrect output")

    # Test a graph with 6 vertices.
    # Repeat the process used for
    # testCaseA.
    def test_B(self):
        self.assertEqual(floyd_recursive.floyd_warshall(testCaseB), testOutputB, "Incorrect output")

