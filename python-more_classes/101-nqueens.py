#!/usr/bin/python3
"""Module that solves the N queens problem."""
import sys


def is_safe(board, row, col):
    """Check if placing a queen at row, col is safe.

    Args:
        board (list): Current board state.
        row (int): Row to check.
        col (int): Column to check.

    Returns:
        bool: True if safe, False otherwise.
    """
    for r, c in board:
        if c == col or abs(r - row) == abs(c - col):
            return False
    return True


def solve(board, row, n, solutions):
    """Solve the N queens problem using backtracking.

    Args:
        board (list): Current board state.
        row (int): Current row being processed.
        n (int): Size of the board.
        solutions (list): List to store all solutions.
    """
    if row == n:
        solutions.append(board[:])
        return
    for col in range(n):
        if is_safe(board, row, col):
            board.append([row, col])
            solve(board, row + 1, n, solutions)
            board.pop()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    solve([], 0, n, solutions)
    for solution in solutions:
        print(solution)
