from numba import njit, prange, jit
import numpy as np
from tqdm import tqdm
from config import *
from isGameOver import isGameOver
import math
from random import choice

board = np.zeros((BOARD_SIZE, BOARD_SIZE))
# board = np.array([
#     [1, 1, 1, 0, 0],
#     [-1, -1, -1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ])


# print(isGameOver(board))
# for i in tqdm(range(1000000)):
#     isGameOver(board)

calculations = 0


@njit()
def minimax(position, depth, alpha, beta, maximizingPlayer):
    # global calculations
    # calculations += 1

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


def AIPlay():
    bestScore = -999999
    bestPlays = []
    possiblePlays = getScores(board)

    for possiblePlay in possiblePlays:
        if possiblePlay[2] == bestScore:
            bestScore = possiblePlay[2]
            bestPlays.append(possiblePlay)

        elif possiblePlay[2] > bestScore:
            bestScore = possiblePlay[2]
            bestPlays = [possiblePlay]

    print(bestPlays)

    selectedPlay = choice(bestPlays)
    selectedPlay = [int(a) for a in selectedPlay]
    print(selectedPlay)

    board[selectedPlay[0]][selectedPlay[1]] = 1


@njit(parallel=True)
def getScores(board):
    scores = []

    for value in prange(BOARD_SIZE**2):
        x = math.floor(value/5)
        y = value % 5

        if board[x][y] == 0:
            copiedArray = np.copy(board)
            copiedArray[x][y] = 1

            score = minimax(copiedArray, 8, -999999, 999999, False)
            scores.append([x, y, score])

            print(x, y, score)

    return scores


# print(getScores(board))

def printBoard():
    text = '-'*(6*BOARD_SIZE+1)+'\n'

    for x in range(BOARD_SIZE):
        line = '|'
        for y in range(BOARD_SIZE):
            item = board[x][y]

            if item == 0:
                line += f'     |'

            # if item == 0:
            #     line += f' {x} {y} |'

            if item == 1:
                line += f'  X  |'

            if item == -1:
                line += f'  O  |'

        line += '\n'+'-'*(6*BOARD_SIZE+1)

        text += line+'\n'

    print(text)


while True:
    AIPlay()
    printBoard()

    selectedPlay = input('Insira a jogada: \n')

    selectedPlay = selectedPlay.split(' ')
    selectedPlay = [int(a) for a in selectedPlay]

    print(selectedPlay)

    board[selectedPlay[0]][selectedPlay[1]] = -1

    printBoard()
