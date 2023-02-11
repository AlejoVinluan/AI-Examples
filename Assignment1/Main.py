import sys
import Board
from functions import DFS, IDS, astar1, astar2

class Main:
    # Ensure that system arguments include an algorithm and file
    if len(sys.argv) <= 2:
        print("Please enter arguments as python3 Main.py <algorithm> <file.txt>")
        exit(1)
    # Ensure that the algorithm is valid and part of the list of usable algorithms
    if sys.argv[1].lower() not in ['dfs', 'ids', 'astar1', 'astar2']:
        print("Could not find correct search algorithm.")
        print("Please ensure you select one of the valid algorithms.")
        print("Please enter arguments as python3 Main.py <DFS/IDS/astar1/astar2> <file.txt>")
        exit(1)
    
    algo = sys.argv[1].lower()
    board = Board.Board(sys.argv[2])
        
    # Find which algorithm is being used and execute the algorithm
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
        exit(1)
    exit(0)
            
            

