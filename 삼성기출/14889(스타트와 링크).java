import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;

public class Main {		
	static int N;
	static int minGap;
	static int[][] graph;
	static boolean[] visited;
	static LinkedList<Integer> startTeam = new LinkedList<>();
	static LinkedList<Integer> linkTeam;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		graph = new int[N+1][N+1];
		visited = new boolean[N+1];
		minGap = Integer.MAX_VALUE;
		
		for(int i = 1; i <= N; i++) {
			String[] str = br.readLine().split(" ");
			for(int j = 1; j <= N; j++) {
				graph[i][j] = Integer.parseInt(str[j-1]);
			}
		}
		
		divTeam(1, 1);			
		System.out.println(minGap);
	}
	
	//dfs
	public static void divTeam(int cur, int cnt) {
		startTeam.add(cur);
		visited[cur] = true;
		
		if(N / 2 == cnt) {
			linkTeam = new LinkedList<>();
			for(int i = 1; i <= N; i++) {
				if(!visited[i]) {
					linkTeam.add(i);
				}
			}
			minGap = Math.min(minGap, gap());
		}
        
		for(int i = cur; i <= N; i++) {
			if(!visited[i]) {
				divTeam(i, cnt + 1);
				visited[i] = false;
				startTeam.removeLast();
			}
		}
	}
	
	public static int gap() {
		int sum1 = 0;
		int sum2 = 0;
        
		for(int i = 0; i < N/2; i++) {
			for(int j = 0; j < N/2; j++) {
				int x1 = startTeam.get(i);
				int y1 = startTeam.get(j);
				sum1 += graph[x1][y1];
				
				int x2 = linkTeam.get(i);
				int y2 = linkTeam.get(j);
				sum2 += graph[x2][y2];
			}
		}
		return Math.abs(sum1 - sum2);
	}
}