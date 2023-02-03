import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;

public class Assignment1{

    static int[][] goalState = new int[][]{
        {7,8,1},
        {6,0,2},
        {5,4,3}
    };

    public static void main(String[] args){
        //Board board = new Board();
        //Board board = new Board(new int[][]{{7,8,1},{6,0,2},{5,4,3}});
        Board board = new Board(new int[][]{{6,7,1},{8,2,0},{5,4,3}});
        board.boardToString();
        try{
            DFS(new ArrayList<Board>(), board, "none", new HashSet<int[][]>());
        } catch(Exception e) {
            e.printStackTrace();
        }
    }

    public static void DFS(ArrayList<Board> pastStates, Board currState, String pastAction, HashSet<int[][]> visited){
        if(visited.contains(currState.getState())){
            currState.boardToString();
            System.out.println("already");
            return;
        }
        if(Arrays.deepEquals(currState.getState(),goalState)){
            for(int i = 0; i < pastStates.size(); i++){
                pastStates.get(i).boardToString();
            }
            return;
        }
        visited.add(currState.getState());
        pastStates.add(currState);

        currState.boardToString();

        // Y, X
        int[] zeroLocation = currState.findZero();

        // Check if 0 can go up
        if(zeroLocation[0] - 1 >= 0 && !pastAction.equals("down")){
            Board clone = currState;
            clone.swapUp();
            DFS(pastStates, clone, "up",visited);
        }

        // Check if 0 can go down
        if(zeroLocation[0] + 1 <= 2 && !pastAction.equals("up")){
            Board clone = currState;
            clone.swapDown();
            DFS(pastStates,clone, "down",visited);
        }

        // Check if 0 can go left
        if(zeroLocation[1] - 1 >= 0 && !pastAction.equals("right")){
            Board clone = currState;
            clone.swapLeft();
            DFS(pastStates,clone,"left",visited);
        }

        //Check if 0 can go right
        if(zeroLocation[1] + 1 <= 2 && !pastAction.equals("left")){
            Board clone = currState;
            clone.swapRight();
            DFS(pastStates,clone, "right",visited);
        }

        return;
    }

}