package ps;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;
import java.util.Queue;

public class Test {	
	static int N;
	static int[][] graph;
	static boolean[][] visited;
	static Queue<Integer> q;
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		N = Integer.parseInt(st.nextToken()); //세로
		graph = new int[N][N];
		
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(in.readLine());
			for(int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i = 0; i < N; i++) {
			int[] line = new int[N];
			q = new LinkedList<Integer>();
			visited = new boolean[N][N];
			
			//bfs
			q.add(i);
			while(!q.isEmpty()) {
				int idx = q.poll();
				for(int j = 0; j < N; j++) {
					if(graph[idx][j] == 1 && !visited[idx][j]) {
						line[j] = 1;
						q.offer(j);
						visited[idx][j] = true;
					}
				}
			}
			
			//출력
			for(int j = 0; j < N; j++) {
				if(line[j] == 0) {
					System.out.print("0 ");
				}else {
					System.out.print("1 ");
				}
			}
			System.out.println("");
		}		
	}
	/*
	public static void main(String args[]){
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(in.readLine());
			for(int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		for(int i = 0; i < N; i++) {
			int[] line = new int[N];
			q = new LinkedList<Integer>();
			visited = new boolean[N][N];
			
			//bfs
			q.add(i);
			while(!q.isEmpty()) {
				int idx = q.poll();
				for(int j = 0; j < N; j++) {
					if(graph[idx][j] == 1 && !visited[idx][j]) {
						line[j] = 1;
						q.offer(j);
						visited[idx][j] = true;
					}
				}
			}
			
			//출력
			for(int j = 0; j < N; j++) {
				if(line[j] == 0) {
					System.out.print("0 ");
				}else {
					System.out.print("1 ");
				}
			}
			System.out.println("");
		}	
	}	
	 */
}

