#!/usr/bin/python3
"""Pascals Triangle"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]

    for row_num in range(1, n):
        # Copy values from previous row
        prev_row = triangle[row_num - 1]
        current_row = [1]

        # Compute values of the current row using the prev_row
        for j in range(1, row_num):
            current_row.append(prev_row[j] + prev_row[j - 1])
        # Add last element to the row (always 1)
        current_row.append(1)

        # Append new row to the list of rows
        triangle.append(current_row)
    return triangle
