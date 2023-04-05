#!/usr/bin/python3

def matrix_divided(matrix, div):
    def valid_matrix(matrix):
        if not isinstance(matrix, list):
            return False
        for row in matrix:
            if not isinstance(row, list):
                return False
            for x in row:
                if not isinstance(x, (int, float)):
                    raise TypeError("value must be an integer")
            return True

    if not valid_matrix(matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
# check if any row of the list has a size larger the the other rows
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError
    result = [[round(x/div, 2) for x in row] for row in matrix]
    return result
