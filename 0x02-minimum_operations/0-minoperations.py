#!/usr/bin/python3
'''In a text file, there is a single character H.
Your text editor can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
'''


def minOperations(n):
    '''Returns: an integer'''
    isPrime, div = numIsPrime(n)
    if isPrime:
        return n

    if n < 2:
        return 0
    
    return int(div + minOperations(n / div))


def numIsPrime(num):
    '''Determine if a num is a prime number'''
    prime = [2, 3, 5, 7]
    for i in prime:
        if num % i == 0 and i != num:
            return (False, i)
    return (True, 0)



n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 15
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 14
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
