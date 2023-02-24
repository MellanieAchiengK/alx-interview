#!/usr/bin/python3
"""
calculates fewest no. of operations needed to result
in exactly n H characters in a text file
"""


def minOperations(n):  # pylint: disable=invalid-name
    """minimum operations"""
    if n < 0:
        return 0
    operations = 0
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        operations += 1

    operations += n
    return operations
