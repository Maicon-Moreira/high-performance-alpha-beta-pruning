from numba import njit
from config import *
import numpy as np
from possibleSequences import possible_sequences, num_possible_sequences

ps = possible_sequences

@njit()
def evaluation(position):
    score = 0

    for i in range(num_possible_sequences):
        sequence_score = 0

        initial_player = position[ps[i][0][0]][ps[i][0][1]]

        if initial_player != 0:
            sequence_score = 1

            for dist in range(1, SEQUENCE_TO_WIN):
                if position[ps[i][dist][0]][ps[i][dist][1]] == 0:
                    pass

                elif position[ps[i][dist][0]][ps[i][dist][1]] == initial_player:
                    sequence_score *= 10

                else:
                    sequence_score = 0
                    break
            
            score += sequence_score

    return score