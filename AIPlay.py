from getScores import getScores
from config import BOARD_SIZE
from random import choice

def AIPlay(board):
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