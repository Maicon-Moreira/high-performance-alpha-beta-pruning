from config import *
import numpy as np

possible_sequences = []


def valid_position(x, y):
    return x >= 0 and y >= 0 and x < BOARD_WIDTH and y < BOARD_HEIGHT


for x in range(BOARD_WIDTH):
    for y in range(BOARD_HEIGHT):

        # horizontal
        if valid_position(x, y) and valid_position(x + SEQUENCE_TO_WIN - 1, y):
            position = []
            for dist in range(SEQUENCE_TO_WIN):
                position.append([x + dist, y])
            possible_sequences.append(position)

        # vertical
        if valid_position(x, y) and valid_position(x, y + SEQUENCE_TO_WIN - 1):
            position = []
            for dist in range(SEQUENCE_TO_WIN):
                position.append([x, y + dist])
            possible_sequences.append(position)

        # diagonal
        if valid_position(x, y) and valid_position(x + SEQUENCE_TO_WIN - 1, y + SEQUENCE_TO_WIN - 1):
            position = []
            for dist in range(SEQUENCE_TO_WIN):
                position.append([x + dist, y + dist])
            possible_sequences.append(position)

        # anti-diagonal
        if valid_position(x, y) and valid_position(x + SEQUENCE_TO_WIN - 1, y - SEQUENCE_TO_WIN + 1):
            position = []
            for dist in range(SEQUENCE_TO_WIN):
                position.append([x + dist, y - dist])
            possible_sequences.append(position)


possible_sequences = np.array(possible_sequences)

num_possible_sequences = possible_sequences.shape[0]
