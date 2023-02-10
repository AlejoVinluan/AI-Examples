import sys
import Board
import copy
from functions import DFS, IDS, astar1, astar2

class Main:
    if len(sys.argv) <= 2:
        print("Please enter arguments as python3 Main.py <algorithm> <file.txt>")
        exit(1)
    if sys.argv[1].lower() not in ['dfs', 'ids', 'astar1', 'astar2']:
        print("Could not find correct search algorithm.")
        print("Please ensure you select one of the valid algorithms.")
        print("Please enter arguments as python3 Main.py <DFS/IDS/astar1/astar2> <file.txt>")
        exit(1)
    
    algo = sys.argv[1].lower()
    board = Board.Board(sys.argv[2])
        
    if algo == 'dfs':
        if not DFS(board):
            print("Unable to find goal state at depth 10.\n")
    elif algo == 'ids':        
        if not IDS(board):
            print("Unable to find goal state at depth 10.\n")
    elif algo == 'astar1':
        if not astar1(board):
            print("Unable to find goal state at depth 10.\n")
    elif algo == 'astar2':
        if not astar2(board):
            print("Unable to find goal state at depth 10.\n")
    else:
        print("Something went wrong.")
            
            

