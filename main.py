from numba import njit, prange
import numpy as np
from tqdm import tqdm
import math
from random import choice
from config import BOARD_SIZE
from isGameOver import isGameOver
from minimax import minimax
from AIPlay import AIPlay
from getScores import getScores
from printBoard import printBoard

board = np.zeros((BOARD_SIZE, BOARD_SIZE))


while True:
    AIPlay(board)
    printBoard(board)

    selectedPlay = input('Insira a jogada: \n')

    selectedPlay = selectedPlay.split(' ')
    selectedPlay = [int(a) for a in selectedPlay]

    print(selectedPlay)

    board[selectedPlay[0]][selectedPlay[1]] = -1

    printBoard(board)
