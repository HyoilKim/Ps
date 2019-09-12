import java.util.*;
import java.io.*;

public class Solution {
	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		
		for(int idx = 1; idx <= TC; idx++) {
			int n = Integer.parseInt(br.readLine());
 			int[][] map = new int[n][n];
 			int[][] dp = new int[n][n];
 			for(int i = 0; i < n; i++) {
 				String line = br.readLine();
 				for(int j = 0; j < n; j++) {
 					map[i][j] = line.charAt(j) - '0';
 				}
 			}
 			
 			System.out.println("#" + idx + " " + bfs(map, dp));			
		}
	}

	public static int bfs(int[][] map, int[][] dp) {
		int[] dx = {0, 1, 0, -1};
		int[] dy = {1, 0, -1, 0};
		int mapLen = map.length;
		boolean[][] visit = new boolean[mapLen][mapLen];
		Queue<Pair> q = new LinkedList<>();
		
		q.add(new Pair(0, 0));
		visit[0][0] = true;
		while(!q.isEmpty()) {
			Pair p = q.poll();
			for(int i = 0; i < 4; i++) {
				int x = p.x + dx[i];
				int y = p.y + dy[i];
			
				if(x < 0 || x >= mapLen || y < 0 || y >= mapLen) continue;
				int newScore = dp[p.x][p.y] + map[x][y];
				if(!visit[x][y]) {
					q.add(new Pair(x, y));
					dp[x][y] = newScore;
					visit[x][y] = true;
				}else {
					if(newScore < dp[x][y]) {
						q.add(new Pair(x, y));
						dp[x][y] = newScore;
					}
				}
			}
			
		}
		return dp[mapLen-1][mapLen-1];
	}
}

class Pair{
	int x;
	int y;
	Pair(int x, int y){
		this.x = x;
		this.y = y;
	}	
}