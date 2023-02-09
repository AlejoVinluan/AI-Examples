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
    stack = []
    stack.append([copy.deepcopy(board.getState()),0,[]])
    
    while(len(stack) != 0):
        currState, depth, history = stack.pop(0)
        
        if depth >= 11:
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
            return True
        
        if(swapUp(copy.deepcopy(currState))):
            stateClone = copy.deepcopy(currState)
            historyClone = copy.deepcopy(history)
            swapUp(stateClone)
            historyClone.append(stateClone)
            stack.append([stateClone, depth + 1, historyClone])
        if(swapDown(copy.deepcopy(currState))):
            stateClone = copy.deepcopy(currState)
            historyClone = copy.deepcopy(history)
            swapDown(stateClone)
            historyClone.append(stateClone)
            stack.append([stateClone, depth + 1, historyClone])
        if(swapLeft(copy.deepcopy(currState))):
            stateClone = copy.deepcopy(currState)
            historyClone = copy.deepcopy(history)
            swapLeft(stateClone)
            historyClone.append(stateClone)
            stack.append([stateClone, depth + 1, historyClone])
        if(swapRight(copy.deepcopy(currState))):
            stateClone = swapRight(copy.deepcopy(currState))
            historyClone = copy.deepcopy(history)
            swapRight(stateClone)
            historyClone.append(stateClone)
            stack.append([stateClone, depth + 1, historyClone])
                    