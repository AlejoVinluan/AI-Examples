import copy

# Have goalState as a global variable for comparisons
goalState = [['7','8','1'],['6','*','2'],['5','4','3']]

# Formats the board into a printable state
def printBoard(state):
    if not state:
        return "null\n"
    
    res = ""
    for i in range(3):
        for j in range(3):
            res += state[i][j] + ' '
        res += '\n'
    return res

# Prints the initial state, adding (Initial input state) to the top
def printInitialState(state):
    if not state:
        return "null\n"
    
    res = ""
    for i in range(3):
        if i == 0:
            for j in range(3):
                res += state[i][j] + ' '
            res += '\t(Initial input state)'
        else:
            for j in range(3):
                res += state[i][j] + ' '
        res += '\n'
    return res
            
# Prints final state, adding (Goal state) to the top
def printFinalState(state):
    if not state:
        return "null\n"
    
    res = ""
    for i in range(3):
        if i == 0:
            for j in range(3):
                res += state[i][j] + ' '
            res += '\t(Goal state)'
        else:
            for j in range(3):
                res += state[i][j] + ' '
        res += '\n'
    return res

# Finds where the location of the star is in the state
def findStar(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '*':
                return [i,j]
    return [-1,-1]

# Swap function to swap the * with the node above it
def swapUp(state):
    starLocation = findStar(state)
    # Ensures that the node above the * is a valid node
    if starLocation[0] - 1 >= 0:
        cloneState = state
        temp = cloneState[starLocation[0]-1][starLocation[1]]
        cloneState[starLocation[0]-1][starLocation[1]] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        # Return the new state with the swapped function
        return cloneState
    else:
        # Return a null value if the move is not valid
        return None
        
# Swap function to swap the * with the node below it
def swapDown(state):
    starLocation = findStar(state)
    # Ensure that the node below the * is a valid node
    if starLocation[0] + 1 <= 2:
        cloneState = state
        temp = cloneState[starLocation[0]+1][starLocation[1]]
        cloneState[starLocation[0]+1][starLocation[1]] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        # Return the state with the valid swap
        return cloneState
    else:
        # Return null value if swap is not valid
        return None

# Swap function to swap the * with the node to the left of it
def swapLeft(state):
    starLocation = findStar(state)
    # Ensure that the node left of the * is a valid node
    if starLocation[1] - 1 >= 0:
        cloneState = state
        temp = cloneState[starLocation[0]][starLocation[1]-1]
        cloneState[starLocation[0]][starLocation[1]-1] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        return cloneState
    else:
        # Return null value if swap is not valid
        return None

# Swap function to swap the * with the node to the right of it
def swapRight(state):
    starLocation = findStar(state)
    # Ensure that the node right of the * is a valid node
    if starLocation[1] + 1 <= 2:
        cloneState = state
        temp = cloneState[starLocation[0]][starLocation[1]+1]
        cloneState[starLocation[0]][starLocation[1]+1] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        return cloneState
    else:
        # Return null value if swap is not valid
        return None

# Depth first search
def DFS(board):
    #  Define max depth at 11 to stop searching once we reach depth 11
    maxDepth = 11
    # Stack is used to iteratively use depth first search
    stack = []
    # Append the following values to the stack
    #  1) Copy of the board (copy.deepcopy() is used since we don't want to modify the current board state)
    #  2) The current depth of the DFS
    #  3) History of the moves to ensure we have a history of how we achieved the goal state
    stack.append([copy.deepcopy(board.getState()),0,[copy.deepcopy(board.getState())]])
    # Keep track of states enqueued
    statesEnqueued = 0
    
    # While there is a stack, keep looping the DFS
    while(len(stack) != 0):
        # Extract the current board state, depth of DFS, and history from current stack
        currState, depth, history = stack.pop(0)
        
        # Return a null value in case we have reached our max depth
        if depth >= maxDepth:
            return None
        
        # Print the history if we happen to reach the goal state
        if currState == goalState:
            print("Output (List of states starting from input to goal state, if found)")
            idx = 0
            for state in history:
                if idx == 0:
                    print(printInitialState(state))
                elif idx == len(history)-1:
                    print(printFinalState(state))
                else:
                    print(printBoard(state))
                idx += 1
                
            print("Number of moves =", len(history)-1)
            print("Number of states enqueued = ", statesEnqueued)
            return True
        
        # Swap a copy of the board up
        upCopy = swapUp(copy.deepcopy(currState))
        # If board is not null, add it to stack for DFS
        if(upCopy):
            historyClone = copy.deepcopy(history)
            historyClone.append(upCopy)
            stack.append([upCopy, depth + 1, historyClone])
            statesEnqueued += 1
        # Swap a copy of the board down
        downCopy = swapDown(copy.deepcopy(currState))
        # If board is not null, add it to stack for DFS
        if(downCopy):
            historyClone = copy.deepcopy(history)
            historyClone.append(downCopy)
            stack.append([downCopy, depth + 1, historyClone])
            statesEnqueued += 1
        # Swap a copy of the board left
        leftCopy = swapLeft(copy.deepcopy(currState))
        # If board is not null, add it to stack
        if(leftCopy):
            historyClone = copy.deepcopy(history)
            historyClone.append(leftCopy)
            stack.append([leftCopy, depth + 1, historyClone])
            statesEnqueued += 1
        # Swap copy of board to the right
        rightCopy = swapRight(copy.deepcopy(currState))
        # If board is not null, add it to stack for DFS
        if(rightCopy):
            historyClone = copy.deepcopy(history)
            historyClone.append(rightCopy)
            stack.append([rightCopy, depth + 1, historyClone])
            statesEnqueued += 1
            

def IDS(board):
    # Keep track of # of states enqueued
    statesEnqueued = 0
    # Keep a copy of state since we don't want to modify original state
    state = copy.deepcopy(board.getState())
    # Preform DFS 10 times
    for idsDepth in range(10):
        # The code below is similair to DFS
        stack = []
        maxDepth = idsDepth + 1
        stack.append([copy.deepcopy(board.getState()),0,[copy.deepcopy(board.getState())]])
        while(len(stack) != 0):
            currState, depth, history = stack.pop(0)
        
            # If we reach maxDepth, we want to break out of the for loop rather than return None
            # since we want to try the search at the next IDS Depth.
            if depth >= maxDepth:
                break
        
            if currState == goalState:
                # We want to specify which idsDepth we found the solution, rather than DFS depth
                print("Goal state found at IDS Depth", idsDepth )
                print("Output (List of states starting from input to goal state, if found)")
                idx = 0
                for state in history:
                    if idx == 0:
                        print(printInitialState(state))
                    elif idx == len(history)-1:
                        print(printFinalState(state))
                    else:
                        print(printBoard(state))
                    idx += 1
                
                print("Number of moves =", len(history)-1)
                print("Number of states enqueued = ", statesEnqueued)
                return True
        
            # The code below is all the same as DFS
            upCopy = swapUp(copy.deepcopy(currState))
            if(upCopy):
                historyClone = copy.deepcopy(history)
                historyClone.append(upCopy)
                stack.append([upCopy, depth + 1, historyClone])
                statesEnqueued += 1
            downCopy = swapDown(copy.deepcopy(currState))
            if(downCopy):
                historyClone = copy.deepcopy(history)
                historyClone.append(downCopy)
                stack.append([downCopy, depth + 1, historyClone])
                statesEnqueued += 1
            leftCopy = swapLeft(copy.deepcopy(currState))
            if(leftCopy):
                historyClone = copy.deepcopy(history)
                historyClone.append(leftCopy)
                stack.append([leftCopy, depth + 1, historyClone])
                statesEnqueued += 1
            rightCopy = swapRight(copy.deepcopy(currState))
            if(rightCopy):
                historyClone = copy.deepcopy(history)
                historyClone.append(rightCopy)
                stack.append([rightCopy, depth + 1, historyClone])
                statesEnqueued += 1
        
        
# Finds where a digit is located in the board
def findDigit(state, digit):
    for i in range(3):
        for j in range(3):
            if state[i][j] == str(digit):
                return [i,j]
    return [-1,-1]

# Find the number of wrong locations in the board
def getNumberOfWrongLocations(state, visited):
    # If our state is not valid or we have already visited the node,
    #  we return a heuristic value of infinity.
    if not state or state in visited:
        return float('inf')
    
    wrongLocations = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goalState[i][j]:
                wrongLocations += 1
    return wrongLocations

# A* search function where we use the number of pieces in the wrong location as the hueristic
def astar1(board):
    # Keep a copy of the visited nodes so that we don't encounter an infinite loop
    visited = []
    # Keep a copy of the history so that we can print the steps from initial state to goal state
    history = []
    history.append(copy.deepcopy(board.getState()))
    # Keep a deep copy of the state so we don't modify original Board
    state = copy.deepcopy(board.getState())
    depth = 0
    
    # We continue to loop until goal state is found
    while state != goalState:
        # Break out of the function in case we exceed maximum depth
        if depth > 10:
            return False
        
        # Make copies of the board where we swap the * with up, down, left, right nodes
        upCopy = swapUp(copy.deepcopy(state))
        downCopy = swapDown(copy.deepcopy(state))
        leftCopy = swapLeft(copy.deepcopy(state))
        rightCopy = swapRight(copy.deepcopy(state))
        
        # Find the heuristic value of each of the resulting swaps
        upHueristic = getNumberOfWrongLocations(upCopy, visited)
        downHueristic = getNumberOfWrongLocations(downCopy, visited)
        leftHueristic = getNumberOfWrongLocations(leftCopy, visited)
        rightHueristic = getNumberOfWrongLocations(rightCopy, visited)
    
        # Find which heuristic would bring us closer to the goal of 0
        minHueristic = min(upHueristic,downHueristic,leftHueristic,rightHueristic)
        
        # Preform the swap with the given heuristic
        if minHueristic == upHueristic and upCopy:
            swapUp(state)
        elif minHueristic == downHueristic and downCopy:
            swapDown(state)
        elif minHueristic == leftHueristic and leftCopy:
            swapLeft(state)
        elif minHueristic == rightHueristic and rightCopy:
            swapRight(state)
            
        # Add our new state to the visited state and history
        visited.append(copy.deepcopy(state))
        history.append(copy.deepcopy(state))
        # Increase depth
        depth += 1
        
    # Print the output if goal state is reached
    print("Goal state found at depth", depth-1)
    print("Output (List of states starting from input to goal state, if found)")
    idx = 0
    for state in history:
        if idx == 0:
            print(printInitialState(state))
        elif idx == len(history)-1:
            print(printFinalState(state))
        else:
            print(printBoard(state))
        idx += 1
    print("Number of moves =", len(history)-1)
    print("Number of states enqueued = ", len(history)-1)
    return True
        
# Get the Manhattan Distance of the current state
#  (total distance of all nodes between their target locations)
def getManhattanDistance(state):
    # If null value is passed in, return infinity
    if not state:
        return float("inf")
    
    manhattanDistance = 0
    for i in range(1,9):
        goalX, goalY = findDigit(goalState,i)
        stateX, stateY = findDigit(state,i)
        manhattanDistance += (abs(goalX-stateX) + abs(goalY-stateY))
    return manhattanDistance

# A* search function two that utilizes Manhattan Distance as hueristic value
def astar2(board):
    # Keep a copy of our current state
    state = copy.deepcopy(board.getState())
    # Keep track of current depth
    depth = 0
    # Keep track of history
    history = []
    # Add the current node to history
    history.append(copy.deepcopy(state))
    
    # Loop until we find goal state
    while state != goalState:
        # Break loop if we exceed maximum depth
        if depth > 10:
            return False
    
        # Keep track of all hueristic values of each move
        moves = []
        # Get move that will return lowest hueristic and append to moves array
        moves.append(getManhattanDistance(swapUp(copy.deepcopy(state))))
        moves.append(getManhattanDistance(swapDown(copy.deepcopy(state))))
        moves.append(getManhattanDistance(swapLeft(copy.deepcopy(state))))
        moves.append(getManhattanDistance(swapRight(copy.deepcopy(state))))
    
        # Find minimum hueristic value in moves
        min_hueristic = min(moves)
        min_idx = -1
        # Find which move gave us the lowest hueristic value
        for idx, val in enumerate(moves):
            if val == min_hueristic:
                min_idx = idx
    
        # Error if no move gave us the lowest heuristic value OR
        #  if all moves result in a null state
        if min_idx == -1 or min_hueristic == float("inf"):
            print("Unable to find best move.")
            exit(1)
    
        # Find which move gave us the lowest heuristic value AND
        #  execute that move on the current state
        if min_idx == 0:
            swapUp(state)
        elif min_idx == 1:
            swapDown(state)
        elif min_idx == 2:
            swapLeft(state)
        elif min_idx == 3:
            swapRight(state)
        else:
            # If min_idx is still -1, throw an error
            print("Something went wrong")
            exit(1)
        # Keep track of history
        history.append(copy.deepcopy(state))
        depth += 1
    
    # Print the output once the goal state is reached
    print("Output (List of states starting from input to goal state, if found)")
    idx = 0
    for state in history:
        if idx == 0:
            print(printInitialState(state))
        elif idx == len(history)-1:
            print(printFinalState(state))
        else:
            print(printBoard(state))
        idx += 1
                
    print("Number of moves =", len(history)-1)
    print("Number of states enqueued = ", len(history)-1)
    return True
        
    