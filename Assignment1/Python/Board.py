class Board:

    def __init__(self, file):
        self.state = [[0 for _ in range(3)] for _ in range (3)]
        self.readFile(file);

        print("Board generated!")
        self.printBoard()

    def readFile(self, file):
        try:
            text = open(file, 'r')
        except:
            print("Unable to find file.")
            exit(1)
        values = text.readline().split(' ')
        values_idx = 0
        for i in range(3):
            for j in range(3):
                self.state[i][j] = values[values_idx]
                values_idx += 1

    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=' ')
            print('')
        print('')

    def getState(self):
        return self.state
