import java.util.HashSet;
import java.lang.Math;

class Board {

    static int[][] state;

    public Board(){
        state = new int[3][3];
        generateBoard();
    }

    public Board(int[][] boardState) {
        state = new int[3][3];
        for(int i = 0; i < boardState.length; i++){
            for(int j = 0; j < boardState[i].length; j++){
                state[i][j] = boardState[i][j];
            }
        }
    }

    public void boardToString(){
        for(int i = 0; i < state.length; i++){
            for(int j = 0; j < state[i].length; j++){
                System.out.print(state[i][j] + " ");
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

            state[randBoardLoc[0]][randBoardLoc[1]] = randNum;
        }
    }

}
