import sys
import Board
from functions import findStar, printBoard, swapDown, swapLeft, swapRight, swapUp, DFS

class Main:
    if len(sys.argv) <= 1:
        print("Please enter file name in command line.")
        exit(1)
    
    board = Board.Board(sys.argv[1])

    print('original board')
    print(printBoard(board.getState()))
    boardCopy = board.getState().copy()
    print('swapped down')
    print(printBoard(swapDown(boardCopy)))
    print('original board again')
    print(printBoard(board.getState()))

    print('up')
    boardCopy = board.getState().copy()
    print(printBoard(swapUp(boardCopy)))

