from config import *
import numpy as np
from isGameOver import isGameOver
from AIPlay import AIPlay
from printBoard import printBoard

board = np.zeros((BOARD_WIDTH, BOARD_HEIGHT))

while True:
    AIPlay(board, INITIAL_DEPTH)
    printBoard(board)

    board_stack = np.zeros((BOARD_WIDTH,)).astype('int')

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[x][y] != 0:
                board_stack[x] += 1

    selectedPlay = int(input('Insira a jogada: \n'))

    board[selectedPlay][board_stack[selectedPlay]] = -1

    printBoard(board)
    print('\n'*1000)
