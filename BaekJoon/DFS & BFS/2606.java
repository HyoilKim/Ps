import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    static Queue<Integer> q = new LinkedList<>();
    static boolean[][] adj;
    static boolean[] visited;
    static int N, E;
    static int numOfVirusComputer;
    
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        N = in.nextInt();
        E = in.nextInt();
        adj = new boolean[N+1][N+1]; 
        visited = new boolean[N+1];
        
        for(int i = 1; i <= E; i++){
            int com1 = in.nextInt();
            int com2 = in.nextInt();
            adj[com1][com2] = true;
            adj[com2][com1] = true;
        }
        
        BFS(1);
        System.out.print(numOfVirusComputer);
    }
    
    public static void BFS(int startPoint){   
        q.offer(startPoint);   
        visited[startPoint] = true;
        
        while(!q.isEmpty()){
            int num = q.poll();
            for(int i = 1; i <= N; i++){
                if(adj[num][i] && !visited[i]){    
                    q.offer(i);
                    visited[i] = true;
                    numOfVirusComputer++;
                }
            }
        }
        
    }
}