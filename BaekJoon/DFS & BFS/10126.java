import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);
        int TC = in.nextInt();
        
        while(TC-->0){
            int N = in.nextInt();
            Camp[] camp = new Camp[N];
            boolean[][] isAdj = new boolean[N][N]; 
            
            for(int i = 0; i < N; i++){
                int x = in.nextInt();
                int y = in.nextInt();
                int r = in.nextInt();
                camp[i] = new Camp(x, y, r);
            }
            
            for(int i = 0; i < N; i++){
                for(int j = i+1; j < N; j++){                  
                    if(Camp.isAdj(camp[i], camp[j])){
                        isAdj[i][j] = isAdj[j][i] = true;
                    }
                }
            }
            
            //BFS
            Queue<Integer> q = new LinkedList<>();
            boolean[] visited = new boolean[N];
            int cnt = 0;
            for(int i = 0; i < N; i++){
                if(!visited[i]){
                    cnt++;
                    q.add(i);
                    visited[i] = true;
                    while(!q.isEmpty()){
                        int tmp = q.poll();  
                        for(int j = 0; j < N; j++){                 
                            if(!visited[j] && isAdj[tmp][j]){
                                visited[j] = true;
                                q.add(j);
                            }
                        }
                    }
                }
            }
            System.out.println(cnt);          
        }
    }   
}

class Camp{
    int x;
    int y;
    int r;
    
    Camp(int x, int y, int r){
        this.x = x;
        this.y = y;
        this.r = r;
    }
    
    public static boolean isAdj(Camp c1, Camp c2){
        return Math.sqrt(Math.pow(c1.x - c2.x, 2) + Math.pow(c1.y - c2.y, 2)) <= c1.r + c2.r; 
    }    
}
