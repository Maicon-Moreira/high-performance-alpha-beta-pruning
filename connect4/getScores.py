from numba import njit, prange, jit
from config import *
import math
import numpy as np
from minimax import minimax


@jit(nopython=False)
def print_results(column, score, calculations):
    print('coluna:', column, '     pontuação:', score)
    print('cenários futuros visitados:', calculations[0])
    print()


@njit(parallel=True)
def getScores(board, depth, board_stack):
    scores = []

    for x in prange(BOARD_WIDTH):
        y = board_stack[x]

        if y < BOARD_HEIGHT:
            copiedBoard = np.copy(board)
            copiedBoard[x][y] = 1

            copiedStack = np.copy(board_stack)
            copiedStack[x] += 1

            calculations = np.array([0])

            score = minimax(copiedBoard, copiedStack,
                            depth, -99999, 99999, False, calculations)
            scores.append([x, y, score])

            print_results(x, score, calculations)

    return scores
