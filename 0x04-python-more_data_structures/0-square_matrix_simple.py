#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of all integers in a matrix."""
    squared_matrix = []
    for row in matrix:
        squared_matrix.append([x ** 2 for x in row])

    return squared_matrix
