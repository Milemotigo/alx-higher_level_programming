#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by div.

    Args:
        matrix (list of lists): a matrix of integers or floats.
        div (int or float): the number to divide the matrix by.

    Returns:
        A new matrix (list of lists) containing the divided elements.

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats.
        TypeError: if sublists are not of the same size.
        TypeError: if div is not a number (int or float).
        ZeroDivisionError: if div is zero.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists of integers or floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("all rows in the matrix must have the same length")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
