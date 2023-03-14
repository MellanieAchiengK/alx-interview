#!/usr/bin/python3
"""
calculates fewest no. of operations needed to result
in exactly n H characters in a text file
"""


def minOperations(n):
    """minmum operations"""
    if n < 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations

if __name__ == "__main__":
    n = 4
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

