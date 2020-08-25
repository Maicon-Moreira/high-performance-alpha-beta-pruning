from numba import njit, prange
from isGameOver import isGameOver
from config import BOARD_SIZE
import math
import numpy as np
from evaluation import evaluation


def does_not_exist(x, y):
    for order in child_order:
        if order[0] == x and order[1] == y:
            return False
    return True


child_order = []
dist = 0

while len(child_order) < BOARD_SIZE ** 2:
    dist += 0.1
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if math.dist([BOARD_SIZE/2, BOARD_SIZE/2], [x + 0.5, y+0.5]) < dist:
                if does_not_exist(x, y):
                    child_order.append([x, y])

child_order = np.array(child_order)


@njit()
def minimax(position, depth, alpha, beta, maximizingPlayer):
    gameOver = isGameOver(position)
    if gameOver != 0:
        return gameOver * 10000

    elif depth == 0:
        return evaluation(position)

    if maximizingPlayer:
        maxEval = -999999

        # for each child of position
        for child in child_order:
            x = child[0]
            y = child[1]
            if position[x][y] == 0:

                position[x][y] = 1
                _eval = minimax(position, depth-1, alpha, beta, False)
                position[x][y] = 0

                maxEval = max(maxEval, _eval)
                alpha = max(alpha, _eval)
                if beta <= alpha:
                    return maxEval

        return maxEval

    else:
        minEval = 999999

        # for each child of position
        for child in child_order:
            x = child[0]
            y = child[1]
            if position[x][y] == 0:

                position[x][y] = -1
                _eval = minimax(position, depth-1, alpha, beta, True)
                position[x][y] = 0

                minEval = min(minEval, _eval)
                beta = min(beta, _eval)
                if beta <= alpha:
                    return minEval

        return minEval
