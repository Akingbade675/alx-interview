#!/usr/bin/python3
'''ALX - Rotate 2D Matrix'''


def transpose_matrix(matrix, n):
    '''Transpose the matrix

    Args:
        matrix (list): matix to transpose
    '''
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    '''Reverse the matrix

    Args:
        matrix (list): matrix to reverse
    '''
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    '''Rotate the matrix

    Args:
        matrix (list): matrix to rotate
    '''
    n = len(matrix)

    transpose_matrix(matrix, n)

    # reverse matrix

    reverse_matrix(matrix)

    return matrix
