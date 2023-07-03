#!/usr/bin/python3
'''Minimum Operation Interview problem'''


def minOperations(n):
    '''Returns: an integer'''
    if n <= 1:
        return n  # we need at least one operation to get to one "H"

    num_ops = 0  # number of operations so far
    num_chars = 1  # number of characters in the file so far
    copied_chars = 1  # number of characters that are currently copied

    while num_chars < n:
        # we have two options: copy or paste
        if n % num_chars == 0:  # if num_chars divides n, then we can copy all
            copied_chars = num_chars
            num_ops += 1
        num_chars += copied_chars  # paste the copied characters
        num_ops += 1

    if num_chars == n:
        return num_ops
    else:
        return 0  # impossible to reach n
