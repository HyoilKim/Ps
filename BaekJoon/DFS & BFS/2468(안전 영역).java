import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int n = in.nextInt();
		int maxHeight = 0;
		int res = 0;
		int[][] area = new int[n][n];
		
		for(int i = 0; i < n; i++) {
			for(int j=0; j<n; j++) {
				area[i][j] = in.nextInt();
				if (area[i][j] > maxHeight) {
					maxHeight = area[i][j];    // 최대높이 저장
				}
			}
		}
		
		Queue<Pair> q = new LinkedList<>();
		int[] dr = {0, 0, 1, -1};
		int[] dc = {-1, 1, 0, 0};
		
		for(int h = 0; h <= maxHeight; h++) {
			boolean[][] visit = new boolean[n][n];
			int numOfSafetyArea = 0;
			// 모든 영역에서 범람하지 않는 장소 search
			for(int r = 0; r < n; r++) {
				for(int c = 0; c < n; c++) {
                    // 방문했거나 범람하는 장소는 skip
					if((visit[r][c] == true) || (area[r][c] <= h)) {
						continue;
					}
					
					q.offer(new Pair(r, c));
					while(!q.isEmpty()) {
						Pair pair = q.poll();
						for(int i = 0; i < 4; i++) {
							int nr = pair.r + dr[i];
							int nc = pair.c + dc[i];
							if (nr < 0 || nr >= n || nc < 0 || nc >= n) {
								continue;
							}
							if ((area[nr][nc] > h) && (!visit[nr][nc])) {
								visit[nr][nc] = true;
								q.offer(new Pair(nr, nc));
							}
						}
					}
					
					numOfSafetyArea++;
					if (res < numOfSafetyArea) {
						res = numOfSafetyArea;
					}
				}
			}
		}
		
		System.out.println(res);
	}
}

class Pair{
	int r, c;
	Pair(int r, int c){
		this.r = r;
		this.c = c;
	}
}
