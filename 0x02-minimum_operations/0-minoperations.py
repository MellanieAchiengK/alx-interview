#!/usr/bin/python3
"""
calculates fewest no. of operations needed to result
in exactly n H characters in a text file
"""


def minOperations(n):  # pylint: disable=invalid-name
    """minimum operations"""
    dp = [0] * (n+1)
    dp[1] = 0
    for i in range(2, n+1):
        dp[i] = i
        for j in range(2, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i//j)
    return dp[n] if n > 1 else 0
