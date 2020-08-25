from config import BOARD_SIZE
from isGameOver import isGameOver

def printBoard(board):
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

        line += '     '

        for y in range(BOARD_SIZE):
            item = board[x][y]

            if item == 0:
                line += f' {x} {y} |'

            else:
                line += f'     |'

        line += '\n'+'-'*(6*BOARD_SIZE+1)

        text += line+'\n'

    print(text)

    print(isGameOver(board))
