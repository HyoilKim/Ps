import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;
import java.util.List;

public class Main {
    public static void main(String args[]){
        Queue<Cell> q = new LinkedList<>();
        List<Integer> numOfComplex = new LinkedList<>(); 
        Scanner in = new Scanner(System.in);
        int N = in.nextInt();
        int[][] map = new int[N][N];
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};
        
        for(int i = 0; i < N; i++){
            String line = in.next();
            for(int j = 0; j < N; j++){
                map[i][j] = Integer.parseInt(line.substring(j, j+1));
            }
        }
        
        //BFS
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
                if(map[i][j] == 1){
                    q.offer(new Cell(i, j));
                    map[i][j] = 0;
                    int cnt = 1;
                    while(!q.isEmpty()){
                        Cell cell = q.poll();
                        for(int k = 0; k < 4; k++){
                            int dirX = cell.x + dx[k];
                            int dirY = cell.y + dy[k];  
                            if(dirX < N && dirX >= 0 && dirY < N && dirY >= 0){
                                if(map[dirX][dirY] == 1){
                                    q.offer(new Cell(dirX, dirY));
                                    cnt++;
                                    map[dirX][dirY] = 0;                          
                                }
                            }
                        }
                    }
                    numOfComplex.add(cnt);
                }
            }
        }
        
        //°á°ú
        numOfComplex.sort(null); 
        System.out.println(numOfComplex.size());
        for(int i = 0; i < numOfComplex.size(); i++){
            System.out.println(numOfComplex.get(i));
        }
        
    }    
}

class Cell{
    int x;
    int y;
    
    Cell(int x, int y){
        this.x = x;
        this.y = y;
    }
}