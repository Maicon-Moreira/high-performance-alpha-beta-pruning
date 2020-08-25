from numba import njit, prange
from isGameOver import isGameOver
from config import BOARD_SIZE


@njit()
def minimax(position, depth, alpha, beta, maximizingPlayer):
    gameOver = isGameOver(position)
    if depth == 0 or gameOver != 0:
        return gameOver

    if maximizingPlayer:
        maxEval = -999999

        # for each child of position
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
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
        for x in range(BOARD_SIZE):
            for y in range(BOARD_SIZE):
                if position[x][y] == 0:

                    position[x][y] = -1
                    _eval = minimax(position, depth-1, alpha, beta, True)
                    position[x][y] = 0

                    minEval = min(minEval, _eval)
                    beta = min(beta, _eval)
                    if beta <= alpha:
                        return minEval

        return minEval
