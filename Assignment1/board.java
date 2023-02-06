import java.util.HashSet;
import java.lang.Math;

class Board {
    private int[][] state;
    private int[][] goalState = new int[][]{
        {7,8,1},
        {6,0,2},
        {5,4,3}
    };

    public Board() {
        this.state = new int[3][3];
        generateBoard();
    }

    public Board(int[][] BoardState) {
        this.state = new int[3][3];
        for (int i = 0; i < BoardState.length; i++) {
            for (int j = 0; j < BoardState[i].length; j++) {
                this.state[i][j] = BoardState[i][j];
            }
        }
    }

    public void boardToString() {
        System.out.print("\n");
        for (int i = 0; i < this.state.length; i++) {
            for (int j = 0; j < this.state[i].length; j++) {
                System.out.print(this.state[i][j] != 0 ? this.state[i][j] + " " : "* ");
            }
            System.out.print("\n");
        }
    }

    public void generateBoard() {
        HashSet<Integer> possibleNumbers = new HashSet<Integer>();
        HashSet<int[]> possibleLocations = new HashSet<int[]>();
        for (int i = 1; i <= 8; i++) {
            possibleNumbers.add(i);
        }
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                possibleLocations.add(new int[] { i, j });
            }
        }

        for (int i = 0; i < 8; i++) {
            // Get random value from possibleNumbers
            int randNum = 0;
            int randIdx = (int) (Math.random() * possibleNumbers.size());
            int currIdx = 0;
            for (int j : possibleNumbers) {
                if (currIdx == randIdx) {
                    randNum = j;
                    possibleNumbers.remove(randNum);
                    break;
                }
                currIdx++;
            }

            int[] randBoardLoc = new int[2];
            int randIdx2 = (int) (Math.random() * possibleLocations.size());
            int currIdx2 = 0;
            for (int[] j : possibleLocations) {
                if (currIdx2 == randIdx2) {
                    randBoardLoc[0] = j[0];
                    randBoardLoc[1] = j[1];
                    possibleLocations.remove(j);
                    break;
                }
                currIdx2++;
            }

            this.state[randBoardLoc[0]][randBoardLoc[1]] = randNum;
        }
    }

    public int[] findZero() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (this.state[i][j] == 0) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[] { 0, 0 };
    }

    public int[][] getState() {
        return this.state;
    }

    public boolean isGoal(){
        // NOTE: Arrays.equals() not working for some reason
        for(int i = 0; i < 3; i++){
            for(int j = 0; j < 3; j++){
                if(state[i][j] != goalState[i][j]){
                    return false;
                }
            }
        }
        return true;
    }

    public void swapUp() {
        int[] zeroLocation = findZero();
        int temp = this.state[zeroLocation[0]-1][zeroLocation[1]];
        this.state[zeroLocation[0]-1][zeroLocation[1]] = 0;
        this.state[zeroLocation[0]][zeroLocation[1]] = temp;
    }

    public void swapDown() {
        int[] zeroLocation = findZero();
        int temp = this.state[zeroLocation[0]+1][zeroLocation[1]];
        this.state[zeroLocation[0]+1][zeroLocation[1]] = 0;
        this.state[zeroLocation[0]][zeroLocation[1]] = temp;
    }

    public void swapLeft() {
        int[] zeroLocation = findZero();
        int temp = this.state[zeroLocation[0]][zeroLocation[1]-1];
        this.state[zeroLocation[0]][zeroLocation[1]-1] = 0;
        this.state[zeroLocation[0]][zeroLocation[1]] = temp;
    }

    public void swapRight() {
        int[] zeroLocation = findZero();
        int temp = this.state[zeroLocation[0]][zeroLocation[1]+1];
        this.state[zeroLocation[0]][zeroLocation[1]+1] = 0;
        this.state[zeroLocation[0]][zeroLocation[1]] = temp;
    }
}
