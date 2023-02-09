import sys
import copy
import Board
from functions import findStar, printBoard, swapDown, swapLeft, swapRight, swapUp, DFS

class Main:
    if len(sys.argv) <= 1:
        print("Please enter file name in command line.")
        exit(1)
    
    board = Board.Board(sys.argv[1])
    if not DFS(board):
        print("Unable to find goal state at depth.")
    

