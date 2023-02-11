class Board:

    # Execute this once board is made
    def __init__(self, file):
        # Create a 3x3 board of 0's
        self.state = [[0 for _ in range(3)] for _ in range (3)]
        # Read the sample.txt file
        self.readFile(file);

        # Print the board once the initial state is found
        print("Input (Any random position of the tiles): ")
        self.printBoard()

    # Read the sample.txt file
    def readFile(self, file):
        try:
            text = open(file, 'r')
        # Throw an error in case the file is not found
        except:
            print("Unable to find file", file)
            exit(1)
        # Split the file using space as the delimeter
        values = text.readline().split(' ')
        # Apply the values of the file to the state of the board
        values_idx = 0
        for i in range(3):
            for j in range(3):
                self.state[i][j] = values[values_idx]
                values_idx += 1

    # Print the board state after the file was read
    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.state[i][j], end=' ')
            print('')
        print('')

    # Returns the state of the board
    def getState(self):
        return self.state
