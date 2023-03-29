#!/usr/bin/python3
"""N queens puzzle challenge"""


def print_solutions(queens, n):
    """
    Print all solutions to N Queens problem

    :param queens: a list of size N that stores the position of queens 
    in the current solution
    :param n: the number of rows and columns on the chessboard
    """

    # If all queens are placed, print the solution
    if len(queens) == n:
        print([[i, queens[i]] for i in range(n)])
        return

    # Check every row in the current column for a valid position
    for i in range(n):
        # Assume the current position is valid
        valid = True

        # Check for any queens in the same row or diagonal
        for j in range(len(queens)):
            if queens[j] == i or queens[j] - j == i - len(queens) or queens[j] + j == i + len(queens):
                valid = False
                break

        # If the current position is valid, add it to the list 
        # and continue to the next column
        if valid:
            queens.append(i)
            print_solutions(queens, n)
            queens.pop()

# Driver code to parse command line argument and call print_solutions
if __name__ == '__main__':
    import sys

    # Check if correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if n is valid
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Call print_solutions with an empty list of queens and n
    print_solutions([], n)
