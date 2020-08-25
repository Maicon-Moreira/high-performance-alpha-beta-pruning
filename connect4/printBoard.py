from config import *
from isGameOver import isGameOver


def printBoard(board):
    text = '-'*(6*BOARD_WIDTH+1)+'\n'

    for x in range(BOARD_HEIGHT):
        line = '|'
        for y in range(BOARD_WIDTH):
            item = board[y][BOARD_HEIGHT - 1 - x]

            if item == 0:
                line += f'     |'

            if item == 1:
                line += f'  X  |'

            if item == -1:
                line += f'  O  |'

        line += '     '

        for y in range(BOARD_WIDTH):
            item = board[y][BOARD_HEIGHT - 1 - x]

            if item == 0:
                line += f'  {y}  |'

            else:
                line += f'     |'

        line += '\n'+'-'*(6*BOARD_WIDTH+1)

        text += line+'\n'

    print(text)

    print(isGameOver(board))
