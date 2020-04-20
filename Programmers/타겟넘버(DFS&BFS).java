import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visit = new boolean[n];
       
        for(int i = 0; i < n; i++) {
            if (!visit[i]) {
                answer++;
                dfs(computers, visit, i);
            }
        }
        
        return answer;
    }
    
    public void dfs(int[][] computers, boolean[] visit, int i){
        if (visit[i]) return;
        visit[i] = true;
        
        for (int adj = 0; adj < computers.length; adj++) {
            if (computers[i][adj] == 1)  {
                dfs(computers, visit, adj);
            }
        }
    }
}

// import java.util.*;

// class Solution {
//     public int solution(int n, int[][] computers) {
//         int answer = 0;
        
//         boolean[] visit = new boolean[n];
//         Queue<Integer> q = new LinkedList<>();
        
//         for(int i = 0; i < n; i++){      
//             if (visit[i]) continue;
//             q.offer(i);
            
//             //bfs
//             while (!q.isEmpty()) {
//                 int network = q.poll();
//                 if (visit[network]) continue;
//                 visit[network] = true;
                        
//                 for (int adj = 0; adj < n; adj++) {
//                     if ((computers[network][adj] == 1) && (network != adj)) {
//                         q.offer(adj);
//                     }
//                 }
//             }   
            
//             answer++;
//         }
        
//         return answer;
//     }
// }