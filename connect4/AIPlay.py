from getScores import getScores
from random import choice
from config import *
import numpy as np


def AIPlay(board, depth):
    board_stack = np.zeros((BOARD_WIDTH,)).astype('int')

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[x][y] != 0:
                board_stack[x] += 1

    bestScore = -999999
    bestPlays = []
    possiblePlays = getScores(board, depth, board_stack)

    for possiblePlay in possiblePlays:
        if possiblePlay[2] == bestScore:
            bestScore = possiblePlay[2]
            bestPlays.append(possiblePlay)

        elif possiblePlay[2] > bestScore:
            bestScore = possiblePlay[2]
            bestPlays = [possiblePlay]

    selectedPlay = choice(bestPlays)
    selectedPlay = [int(a) for a in selectedPlay]

    board[selectedPlay[0]][selectedPlay[1]] = 1
