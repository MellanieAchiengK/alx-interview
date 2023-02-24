#!/usr/bin/python3
"""Making Change Module"""

def makeChange(coins, total):
    """determine the fewest number of coins needed 
    to meet a given amount total"""
    if total <= 0:
        return 0

    # Initialize an array to store the fewest number of coins needed for each value from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Compute the fewest number of coins needed for each value from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    if min_coins[total] == float('inf'):
        return -1

    return min_coins[total]
