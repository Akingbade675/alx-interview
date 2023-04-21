#!/usr/bin/python3
'''A module that determines the pascal triangle of a number'''


def pascal_triangle(n):
    '''
    Returns a list of lists of integers representing the
    Pascal’s triangle of n.
    '''
    if n <= 0:
        return []

    triangle = []
    for i in range(1, n + 1):
        row = []
        for j in range(i):
            if j == 0 or j == i - 1:
                row.append(1)
                continue

            row.append(triangle[i - 2][j - 1] + triangle[i - 2][j])

        triangle.append(row)

    return triangle
