from numba import njit
from config import *
import numpy as np
from possibleSequences import possible_sequences, num_possible_sequences

ps = possible_sequences

@njit()
def isGameOver(position):
    for i in range(num_possible_sequences):
        initial_player = position[ps[i][0][0]][ps[i][0][1]]

        if initial_player != 0:
            for dist in range(1, SEQUENCE_TO_WIN):
                if position[ps[i][dist][0]][ps[i][dist][1]] != initial_player:
                    break

                if dist == SEQUENCE_TO_WIN - 1:
                    return initial_player

    return 0


# @njit()
# def isGameOver(position):
#     for x in range(BOARD_SIZE):
#         for y in range(BOARD_SIZE):
#             player = position[x][y]
#             if player != 0:
#                 for vx in range(-1, 2):
#                     for vy in range(-1, 2):
#                         if not (vx == 0 and vy == 0):
#                             for d in range(SEQUENCE_TO_WIN):
#                                 realX = x + vx*d
#                                 realY = y + vy*d
#                                 if realX < 0 or realY < 0 or realX >= BOARD_SIZE or realY >= BOARD_SIZE:
#                                     break

#                                 if position[realX][realY] != player:
#                                     break

#                                 if d == SEQUENCE_TO_WIN - 1:
#                                     return player
#     return 0
