def matrix_divided(matrix, div):
# Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(x, (int, float)) for x in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for ele in row:
            new_ele = round(ele / div, 2)
            new_row.append(new_ele)
        new_matrix.append(new_row)
    return new_matrix
