#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers"""
    if matrix == [[]]:
        print()
    else:
        for row in matrix:
            for idx, number in enumerate(row):
                if idx == len(row) - 1:
                    print("{:d}".format(number))
                else:
                    print("{:d}".format(number), end=" ")
