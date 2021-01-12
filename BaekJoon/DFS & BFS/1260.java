import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static boolean[][] adj;
    static boolean[] visited; 
    static int N, M;
    static int startPoint;
    
    public static void main(String[] args){
		Scanner in = new Scanner(System.in);  
        N = in.nextInt();
        M = in.nextInt();
        adj = new boolean[N+1][N+1];     
        visited = new boolean[N+1];  
        startPoint = in.nextInt();
        
        for(int i = 0; i < M; i++){
            int n1, n2;
            n1 = in.nextInt();
            n2 = in.nextInt();
            adj[n1][n2] = true;
            adj[n2][n1] = true;
        }
        
        visited[startPoint] = true;
        DFS(startPoint);
        
        System.out.println("");  
        
        visited = new boolean[N+1];
        visited[startPoint] = true;
        BFS(startPoint);
    }   
        
    public static void DFS(int startPoint){
        System.out.print(startPoint + " ");
        
        for(int i = 1; i <= N; i++){
            if(adj[startPoint][i] == true && visited[i] == false){  
                visited[i] = true;
                DFS(i);
            }
        }
    }
    
     public static void BFS(int startPoint){
        Queue<Integer> q = new LinkedList<>(); 
        q.offer(startPoint);
        visited[startPoint] = true;
        
        while(!q.isEmpty()){
            int num = q.poll();
            System.out.print(num + " ");
            for(int i = 1; i <= N; i++){
                if(adj[num][i] == true && visited[i] == false){  
                    q.offer(i);
                    visited[i] = true;
                }
            }
            
        }
    }
}