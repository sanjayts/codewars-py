# https://www.codewars.com/kata/sudoku-solution-validator/train/python

import itertools
from typing import List

_REFERENCE_CHUNK = set(range(1, 10))


def validSolution(board: List[List[int]]) -> bool:
    return has_valid_chunks(board)


def has_valid_chunks(board: List[List[int]]) -> bool:
    grid_chunks = (c for c in retrieve_chunk(board))
    chunks = itertools.chain(board, grid_chunks, zip(*board))
    return all(set(row) == _REFERENCE_CHUNK for row in chunks)


# Flatten a 3x3 sub-grid within the whole sudoku board as a list and send that back as a "chunk"
def retrieve_chunk(board: List[List[int]]) -> List[int]:
    num_cols, num_rows = len(board[0]), len(board)
    for cur_i in range(0, num_rows, 3):
        for cur_j in range(0, num_cols, 3):
            chunk = [board[i][j] for i in range(cur_i, cur_i + 3) for j in range(cur_j, cur_j + 3)]
            yield chunk


ans1 = validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 5, 3, 4, 8],
                      [1, 9, 8, 3, 4, 2, 5, 6, 7],
                      [8, 5, 9, 7, 6, 1, 4, 2, 3],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 6, 1, 5, 3, 7, 2, 8, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 4, 5, 2, 8, 6, 1, 7, 9]])
assert ans1 is True

ans2 = validSolution([[5, 3, 4, 6, 7, 8, 9, 1, 2],
                      [6, 7, 2, 1, 9, 0, 3, 4, 9],
                      [1, 0, 0, 3, 4, 2, 5, 6, 0],
                      [8, 5, 9, 7, 6, 1, 0, 2, 0],
                      [4, 2, 6, 8, 5, 3, 7, 9, 1],
                      [7, 1, 3, 9, 2, 4, 8, 5, 6],
                      [9, 0, 1, 5, 3, 7, 2, 1, 4],
                      [2, 8, 7, 4, 1, 9, 6, 3, 5],
                      [3, 0, 0, 4, 8, 1, 1, 7, 9]])

assert ans2 is False

ans3 = validSolution([[1, 3, 2, 5, 7, 9, 4, 6, 8],
                      [4, 9, 8, 2, 6, 1, 3, 7, 5],
                      [7, 5, 6, 3, 8, 4, 2, 1, 9],
                      [6, 4, 3, 1, 5, 8, 7, 9, 2],
                      [5, 2, 1, 7, 9, 3, 8, 4, 6],
                      [9, 8, 7, 4, 2, 6, 5, 3, 1],
                      [2, 1, 4, 9, 3, 5, 6, 8, 7],
                      [3, 6, 5, 8, 1, 7, 9, 2, 4],
                      [8, 7, 9, 6, 4, 2, 1, 3, 5]])

assert ans3 is False
