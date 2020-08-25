from numba import njit, prange, jit
from isGameOver import isGameOver
from config import *
import math
import numpy as np
from evaluation import evaluation


@njit()
def minimax(position, stack, depth, alpha, beta, maximizingPlayer, calculations):

    calculations[0] += 1

    gameOver = isGameOver(position)
    if gameOver != 0:
        return gameOver * 10000

    elif depth == 0:
        return evaluation(position)

    if maximizingPlayer:
        maxEval = -99999

        # for each child of position
        for x in [3, 2, 4, 1, 5, 0, 6]:
            y = stack[x]
            if y < BOARD_HEIGHT:

                position[x][y] = 1
                stack[x] += 1
                _eval = minimax(position, stack, depth-1,
                                alpha, beta, False, calculations)
                position[x][y] = 0
                stack[x] -= 1

                maxEval = max(maxEval, _eval)
                alpha = max(alpha, _eval)
                if beta <= alpha:
                    return maxEval

        return maxEval

    else:
        minEval = 99999

        # for each child of position
        for x in [3, 2, 4, 1, 5, 0, 6]:
            y = stack[x]
            if y < BOARD_HEIGHT:

                position[x][y] = -1
                stack[x] += 1
                _eval = minimax(position, stack, depth-1,
                                alpha, beta, True, calculations)
                position[x][y] = 0
                stack[x] -= 1

                minEval = min(minEval, _eval)
                beta = min(beta, _eval)
                if beta <= alpha:
                    return minEval

        return minEval
