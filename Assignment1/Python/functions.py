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
    print(board.findStar())