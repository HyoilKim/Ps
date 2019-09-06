import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        Queue<Cell> q = new LinkedList<>();
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        int N = in.nextInt();
        int M = in.nextInt();
        int[][] maze = new int[N][M];
        
        for(int i = 0; i < N; i++){
            String line = in.next();
            for(int j = 0; j < M; j++){
                String st = line.substring(j, j+1);
                maze[i][j] = Integer.parseInt(st);
            }
        }
        //BFS
        Cell startPoint = new Cell(0, 0, 1);
        q.offer(startPoint);
        maze[0][0] = 0;
        
        while(!q.isEmpty()){
            Cell cell = q.poll();          
            for(int i = 0; i < 4; i++){
                int dirX = cell.x + dx[i];
                int dirY = cell.y + dy[i];
                int dis = cell.distance; 
                if(dirX >= 0 && dirX < N && dirY >= 0 && dirY < M){  
                    if(maze[dirX][dirY] == 1){
                        if(dirX == N-1 && dirY == M-1){
                            System.out.print(dis + 1); 
                            return; 
                        }
                        maze[dirX][dirY] = 0;
                        q.offer(new Cell(dirX, dirY, dis + 1));
                    }
                }
            }
        }
        
    }      
}

class Cell{
    int x;
    int y;
    int distance;
    
    Cell(int x, int y, int distance){
        this.x = x;
        this.y = y;
        this.distance = distance;        
    }
}