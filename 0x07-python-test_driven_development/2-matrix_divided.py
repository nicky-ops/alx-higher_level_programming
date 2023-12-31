#!/usr/bin/python3
"""
Matrix division
"""


def matrix_divided(matrix, div):
    """
    function that takes a matrix and an integer(div) as its arguments
    divides each element of the matrix by integer(div)
    """
    new_matrix = []
    lst = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    for i in matrix:
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    for i in range(0, (len(matrix) - 1)):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [[round(idx / div, 2) for idx in mtx] for mtx in matrix]
    return new_matrix
