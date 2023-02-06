import java.util.ArrayList;
import java.util.HashSet;
import java.util.Stack;

public class Assignment1{

    public static void main(String[] args){
        //Board board = new Board();
        //Board board = new Board(new int[][]{{7,8,1},{6,0,2},{5,4,3}});
        Board board = new Board(new int[][]{{6,7,1},{8,2,0},{5,4,3}});
        System.out.println("Board generated!");
        board.boardToString();
        
        System.out.println("Running DFS on board.");
        DFS(board);
    }

    public static void DFS(Board originalBoard){
        HashSet<int[][]> visited = new HashSet<int[][]>();
        Stack<Board> stack = new Stack<Board>();
        ArrayList<Board> movesList = new ArrayList<Board>();

        stack.push(originalBoard);
        movesList.add(originalBoard);

        while(stack.size() > 0){
            Board currBoard = stack.pop();
            if(currBoard.isGoal()){
                System.out.println("Solution found!");
                for(Board board : movesList){
                    board.boardToString();
                }
                return;
            }

            if(visited.contains(currBoard.getState())){
                break;
            }

            visited.add(currBoard.getState());

            int[] zeroLocation = currBoard.findZero();
            
            // Check move up
            // Check if 0 can go up
            if(zeroLocation[0] - 1 >= 0){
                Board clone = currBoard;
                currBoard.swapUp();
                stack.push(clone);
            }

            // Check if 0 can go down
            if(zeroLocation[0] + 1 <= 2){
                Board clone = currBoard;
                clone.swapDown();
                stack.push(clone);
            }

            // Check if 0 can go left
            if(zeroLocation[1] - 1 >= 0){
                Board clone = currBoard;
                clone.swapLeft();
                stack.push(clone);
            }

            //Check if 0 can go right
            if(zeroLocation[1] + 1 <= 2){
                Board clone = currBoard;
                clone.swapRight();
                stack.push(clone);
            }
            movesList.remove(currBoard);
        }
        System.out.println("No solution found.");
    }


}