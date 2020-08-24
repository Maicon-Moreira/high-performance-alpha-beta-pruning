from numba import njit
from config import *


@njit()
def isGameOver(position):
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            player = position[x][y]
            for vx in range(-1, 2):
                for vy in range(-1, 2):
                    if not (vx == 0 and vy == 0):
                        for d in range(SEQUENCE_TO_WIN):
                            if position[x + vx*d][y + d*vy] != player:
                                break
                            if d == SEQUENCE_TO_WIN - 1:
                                return player
    return 0
