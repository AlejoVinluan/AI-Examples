import java.util.Arrays;
import java.util.ArrayList;

public class Assignment1{

    static int[][] goalState = new int[][]{
        {7,8,1},
        {6,0,2},
        {5,4,3}
    };
    public static void main(String[] args){
        Board board = new Board();
        //Board board = new Board(new int[][]{{7,8,1},{6,0,2},{5,4,3}});
        board.boardToString();
        board.DFS();
    }

}