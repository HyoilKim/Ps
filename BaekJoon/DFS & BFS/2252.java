import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int M;
	static int[] indegree;
	static boolean visited[];
	static ArrayList<Integer> res;
	static ArrayList<Integer> graph[];
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		indegree = new int[N + 1];
		visited = new boolean[N + 1];
		res = new ArrayList<>();
		graph = new ArrayList[N + 1];
		for(int i = 1; i <= N; i++) graph[i] = new ArrayList<Integer>();
		
		while(M-->0) {
			st = new StringTokenizer(in.readLine(), " ");
			int small = Integer.parseInt(st.nextToken());
			int tall = Integer.parseInt(st.nextToken());
			graph[small].add(tall);
			indegree[tall]++;
		}
		
		for(int i = 1; i <= N; i++) 
			if(indegree[i] == 0) 
				dfs(i);	
		
		for(int i = res.size() - 1; i >= 0; i--)
			System.out.print(res.get(i) + " ");
			
	}
	
	public static void dfs(int n) {
		visited[n] = true;
		for(int i = 0; i < graph[n].size(); i++) {
			int next = graph[n].get(i);
			if(!visited[next]) {
				dfs(next);
			}
		}
		res.add(n);
	}
}