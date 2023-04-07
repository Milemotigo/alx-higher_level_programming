#!/usr/bin/python3


def matrix_divided(matrix, div):
    """Divides all elemnts of a matrix by div.
    Args:
        matrix: list of lists containing int/ floats.
        div: number to divide matrix by.
    Returns:
        List: list of lists containing divided matrix.
    Raises:
        TypeError: if matrix is not list of lists nor contains ints/ floats.
        TypeError: if sublists are not of the same size.
        TypeError: if div is neither int nor float.
        ZeroDivisionError: when div is zero.
    """
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats.")

    for line in matrix:
        if not all([matrix]) or not isinstance(matrix, list):
            raise TypeError("matrix must be a matrix (list of lists) of \
                    integers/floats.")
        if len(line) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for w in line:
            if not isinstance(w, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats.")
    return [[round(w / div, 2) for w in line] for line in matrix]
