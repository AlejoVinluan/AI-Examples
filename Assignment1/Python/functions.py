import copy

goalState = [['7','8','1'],['6','*','2'],['5','4','3']]

def printBoard(state):
    if not state:
        return "null\n"
    
    res = ""
    for i in range(3):
        for j in range(3):
            res += state[i][j] + ' '
        res += '\n'
    return res

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

def findStar(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == '*':
                return [i,j]
    return [-1,-1]

def swapUp(state):
    starLocation = findStar(state)
    if starLocation[0] - 1 >= 0:
        cloneState = state
        temp = cloneState[starLocation[0]-1][starLocation[1]]
        cloneState[starLocation[0]-1][starLocation[1]] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        return cloneState
    else:
        return None
        
def swapDown(state):
    starLocation = findStar(state)
    if starLocation[0] + 1 <= 2:
        cloneState = state
        temp = cloneState[starLocation[0]+1][starLocation[1]]
        cloneState[starLocation[0]+1][starLocation[1]] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        return cloneState
    else:
        return None

def swapLeft(state):
    starLocation = findStar(state)  
    if starLocation[1] - 1 >= 0:
        cloneState = state
        temp = cloneState[starLocation[0]][starLocation[1]-1]
        cloneState[starLocation[0]][starLocation[1]-1] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        return cloneState
    else:
        return None

def swapRight(state):
    starLocation = findStar(state)
    if starLocation[1] + 1 <= 2:
        cloneState = state
        temp = cloneState[starLocation[0]][starLocation[1]+1]
        cloneState[starLocation[0]][starLocation[1]+1] = '*'
        cloneState[starLocation[0]][starLocation[1]] = temp
        return cloneState
    else:
        return None

def DFS(board):
    maxDepth = 11
    stack = []
    stack.append([copy.deepcopy(board.getState()),0,[copy.deepcopy(board.getState())]])
    statesEnqueued = 0
    
    while(len(stack) != 0):
        currState, depth, history = stack.pop(0)
        
        if depth >= maxDepth:
            return None
        
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
            
def IDS(board):
    statesEnqueued = 0
    state = copy.deepcopy(board.getState())
    for idsDepth in range(10):
        stack = []
        maxDepth = idsDepth + 1
        stack.append([copy.deepcopy(board.getState()),0,[copy.deepcopy(board.getState())]])
        while(len(stack) != 0):
            currState, depth, history = stack.pop(0)
        
            if depth >= maxDepth:
                break
        
            if currState == goalState:
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
        
        

def findDigit(state, digit):
    for i in range(3):
        for j in range(3):
            if state[i][j] == str(digit):
                return [i,j]
    return [-1,-1]

def getNumberOfWrongLocations(state, visited):
    if not state or state in visited:
        return float('inf')
    
    wrongLocations = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goalState[i][j]:
                wrongLocations += 1
    return wrongLocations

def astar1(board):
    visited = []
    history = []
    state = copy.deepcopy(board.getState())
    depth = 0
    
    while state != goalState:
        if depth > 10:
            return False
        
        upCopy = swapUp(copy.deepcopy(state))
        downCopy = swapDown(copy.deepcopy(state))
        leftCopy = swapLeft(copy.deepcopy(state))
        rightCopy = swapRight(copy.deepcopy(state))
        
        upHueristic = getNumberOfWrongLocations(upCopy, visited)
        downHueristic = getNumberOfWrongLocations(downCopy, visited)
        leftHueristic = getNumberOfWrongLocations(leftCopy, visited)
        rightHueristic = getNumberOfWrongLocations(rightCopy, visited)
    
        minHueristic = min(upHueristic,downHueristic,leftHueristic,rightHueristic)
        
        if minHueristic == upHueristic and upCopy:
            swapUp(state)
        elif minHueristic == downHueristic and downCopy:
            swapDown(state)
        elif minHueristic == leftHueristic and leftCopy:
            swapLeft(state)
        elif minHueristic == rightHueristic and rightCopy:
            swapRight(state)
        visited.append(copy.deepcopy(state))
        history.append(copy.deepcopy(state))
        depth += 1
        
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
        

def getManhattanDistance(state):
    if not state:
        return float("inf")
    
    manhattanDistance = 0
    for i in range(1,9):
        goalX, goalY = findDigit(goalState,i)
        stateX, stateY = findDigit(state,i)
        manhattanDistance += (abs(goalX-stateX) + abs(goalY-stateY))
    return manhattanDistance

def astar2(board):
    state = copy.deepcopy(board.getState())
    depth = 0
    history = []
    history.append(copy.deepcopy(state))
    
    while state != goalState:
        if depth >= 11:
            return False
    
        moves = []
        # Get move that will return lowest hueristic
        moves.append(getManhattanDistance(swapUp(copy.deepcopy(state))))
        moves.append(getManhattanDistance(swapDown(copy.deepcopy(state))))
        moves.append(getManhattanDistance(swapLeft(copy.deepcopy(state))))
        moves.append(getManhattanDistance(swapRight(copy.deepcopy(state))))
    
        # Find min in moves
        min_hueristic = min(moves)
        min_idx = -1
        for idx, val in enumerate(moves):
            if val == min_hueristic:
                min_idx = idx
    
        if min_idx == -1 or min_hueristic == float("inf"):
            print("Unable to find best move.")
            exit(1)
    
        if min_idx == 0:
            swapUp(state)
        elif min_idx == 1:
            swapDown(state)
        elif min_idx == 2:
            swapLeft(state)
        elif min_idx == 3:
            swapRight(state)
        else:
            print("Something went wrong")
            exit(1)
        history.append(copy.deepcopy(state))
        depth += 1
    
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
        
    