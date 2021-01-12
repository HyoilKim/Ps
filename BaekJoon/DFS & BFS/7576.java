import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static Queue<Tomato> q = new LinkedList<>();
    static int[][] adj;
    static int N, M;
    
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        M = in.nextInt();    //가로
        N = in.nextInt();    //세로
        adj = new int[N+2][M+2]; 
        
        for(int i = 0; i <= N+1; i++){
            for(int j = 0; j <= M+1; j++){
                if(i == 0 || i == N+1 || j == 0 || j == M+1){
                    adj[i][j] = -1;
                    continue;
                }
                int tomatoStatus = in.nextInt();
                adj[i][j] = tomatoStatus;
            }
        }      
        
        System.out.print(BFS());  
    }
    
    public static int BFS(){ 
        //startPoint 모두 offer
        int raw = 0;
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= M; j++){
                int tomatoStatus = adj[i][j];
                if(tomatoStatus == 1){
                    q.offer(new Tomato(i, j, 1, 0)); 
                }if(tomatoStatus == 0){
                    raw++;
                }
            }
        }   
        //raw tomato가 존재 x
        if(raw == 0) return 0;
        
        //days를 BFS로 찾기 
        int days = 0;  
        while(!q.isEmpty()){            
            Tomato tomato = q.poll();
            int x = tomato.x;
            int y = tomato.y;
            days = tomato.days;
                    
            int[] xDir = {0, 0, 1, -1};
            int[] yDir = {1, -1, 0, 0}; 
            for(int j = 0; j < 4; j++){
                int adj_X = x + xDir[j];
                int adj_Y = y + yDir[j];
                
                if(adj[adj_X][adj_Y] == 0){               
                    q.offer(new Tomato(adj_X, adj_Y, 1, days + 1));
                    adj[adj_X][adj_Y] = 1; 
                }
            }
            
        }
        
        // 익을 수 없는 토마토 존재
        for(int i = 1; i <= N; i++){
            for(int j = 1; j <= M; j++){
                int tomatoStatus = adj[i][j];
                if(tomatoStatus == 0){
                    return -1;
                }
            }
        }  
        
        return days;
    }      
}

class Tomato{ 
    int x;
    int y;
    int status;
    int days;
    
    Tomato(int x, int y, int status, int days){
        this.x = x;
        this.y = y;
        this.status = status;
        this.days = days;
    }
}