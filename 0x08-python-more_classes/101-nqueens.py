#!/usr/bin/python3
"""
Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    return [[' '] * n for _ in range(n)]


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row[:] for row in board]


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    return [[r, c] for r, row in enumerate(board) for c, val in enumerate(row) if val == 'Q']


def xout(board, row, col):
    """X out spots on a chessboard."""
    for r in range(len(board)):
        board[r][col] = board[row][r] = board[row][col] = board[row][col] = 'x'
        if 0 <= row + r < len(board) and 0 <= col + r < len(board[row]):
            board[row + r][col + r] = 'x'
        if 0 <= row - r < len(board) and 0 <= col - r < len(board[row]):
            board[row - r][col - r] = 'x'


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    for col in range(len(board)):
        if board[row][col] == ' ':
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = 'Q'
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit() or int(sys.argv[1]) < 4:
        print("N must be a number greater than or equal to 4")
        sys.exit(1)

    board_size = int(sys.argv[1])
    board = init_board(board_size)
    solutions = recursive_solve(board, 0, 0, [])

    for sol in solutions:
        print(sol)
