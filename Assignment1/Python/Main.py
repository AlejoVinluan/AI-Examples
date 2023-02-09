import sys
import copy
import Board
from functions import findStar, printBoard, swapDown, swapLeft, swapRight, swapUp, DFS

class Main:
    if len(sys.argv) <= 2:
        print("Please enter arguments as python3 Main.py <file.txt> <algorithm>")
        exit(1)
    if sys.argv[2].lower() not in ['dfs', 'ids', 'astar1', 'astar2']:
        print("Please ensure you select one of the valid algorithms.")
        print("(DFS/IDS/astar1/astar2)")
    
    algo = sys.argv[2].lower()
    board = Board.Board(sys.argv[1])
    
    if algo == 'dfs':
        if not DFS(board):
            print("Unable to find goal state at depth.")
            

