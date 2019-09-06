import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static boolean[][] adj;
    static boolean[] visited; 
    static int N, M;
    static int cnt;
    
    public static void main(String[] args){
		Scanner in = new Scanner(System.in);  
        N = in.nextInt();
        M = in.nextInt();
        adj = new boolean[N+1][N+1];     
        visited = new boolean[N+1];  
        
        for(int i = 0; i < M; i++){
            int n1, n2;
            n1 = in.nextInt();
            n2 = in.nextInt();
            adj[n1][n2] = true;
            adj[n2][n1] = true;
        }
        
        for(int i = 1; i <= N; i++){
            BFS(i);
        }
        System.out.print(cnt);
    }   
     public static void BFS(int startPoint){
        Queue<Integer> q = new LinkedList<>();

        if(visited[startPoint] == false){
            q.offer(startPoint);
            cnt++;
        }else{
            return;
        }
         
        visited[startPoint] = true;        
        while(!q.isEmpty()){
            int num = q.poll();
            for(int i = 1; i <= N; i++){
                if(adj[num][i] == true && visited[i] == false){  
                    q.offer(i);
                    visited[i] = true;
                }
            }  
        }
    }
}