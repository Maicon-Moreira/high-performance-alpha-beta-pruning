from numba import njit, prange
from config import BOARD_SIZE
import math
import numpy as np
from minimax import minimax

@njit(parallel=True, nogil=True)
def getScores(board, depth):
    scores = []

    for value in prange(BOARD_SIZE**2):
        x = math.floor(value/5)
        y = value % 5

        if board[x][y] == 0:
            copiedArray = np.copy(board)
            copiedArray[x][y] = 1

            score = minimax(copiedArray, depth, -999999, 999999, False)
            scores.append([x, y, score])

            print(x, y, score)

    return scores
