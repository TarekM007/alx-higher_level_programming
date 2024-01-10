#!/usr/bin/python3
"""2-matrix_divided module"""


def matrix_divided(matrix, div):
    """
    divides two values

    Args:
        matrix: the matrix
        div: an integer or float

    Returns:
        division of matrix elements
    """
    error_1 = "matrix must be a matrix (list of lists) of integers/floats"
    if not all(isinstance(row, list) for row in matrix) or \
       not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(error_1)

    # Checking if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Checking if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checking if div is not equal to zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Dividing each element of matrix by div and rounding to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
