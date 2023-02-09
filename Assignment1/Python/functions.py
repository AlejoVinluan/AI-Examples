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
    stack.append(copy.deepcopy(board.getState()))
    depth = 0
    
    while(len(stack) != 0):
        if depth >= 10:
            print("Unable to find solution at depth 10.")
            return
        
        currState = stack.pop(0)
        if currState == goalState:
            print("Goal state found!")
            print("currState:", currState)
            print("goalState:", goalState)
            return
        
        print("depth", depth)
        print(printBoard(currState))
        
        if(swapUp(copy.deepcopy(currState))):
            stack.append(swapUp(copy.deepcopy(currState)))
        if(swapDown(copy.deepcopy(currState))):
            stack.append(swapDown(copy.deepcopy(currState)))
        if(swapLeft(copy.deepcopy(currState))):
            stack.append(swapLeft(copy.deepcopy(currState)))
        if(swapRight(copy.deepcopy(currState))):
            stack.append(swapRight(copy.deepcopy(currState)))
            
        
        