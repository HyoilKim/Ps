import java.util.Scanner;
import java.util.Queue;
import java.util.ArrayList;
import java.util.LinkedList;

public class Main {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int M = in.nextInt();
		int N = in.nextInt();
		int K = in.nextInt();
		boolean[][] isInside = new boolean[M][N];
		
		// 기존의 배열 좌표와 x,y좌표가 다르지만, 넓이를 구하는 것이기 때문에 구분x
		for(int i = 0; i < K; i++) {
			int llx = in.nextInt();
			int lly = in.nextInt();
			int rux = in.nextInt();
			int ruy = in.nextInt();
			for(int x = llx; x < rux; x++) {
				for(int y = lly; y < ruy; y++) {
					isInside[y][x] = true;
				}
			}
		}
		/*
		for(int i = 0; i < M; i++) {
			for(int j = 0; j < N; j++) {
				if(isInside[i][j])System.out.print("1 ");
				else System.out.print("0 ");
			}
			System.out.println("");
		}
        */
		
		ArrayList<Integer> areas = new ArrayList<>();
		Queue<Pair> q = new LinkedList<>();
		int[] dr = {1, -1, 0, 0};
		int[] dc = {0, 0, 1, -1};
		int numOfAreas = 0;
		
		for(int r = 0; r < M; r++) {
			for(int c = 0; c < N; c++) {
				if(isInside[r][c]) continue;
				int area = 1;
				
				q.offer(new Pair(r, c));
				isInside[r][c] = true;
				while(!q.isEmpty()) {
					Pair p = q.poll();
					for(int i = 0; i < 4; i++) {
						int nr = p.r + dr[i];
						int nc = p.c + dc[i];
						if(nr < 0 || nr >= M || nc < 0 || nc >= N) continue;
						if(!isInside[nr][nc]) {
							isInside[nr][nc] = true;
							q.offer(new Pair(nr, nc));
							area++;
						}
					}
				}
				numOfAreas++;
				areas.add(area);
			}
		}	
		
		System.out.println(numOfAreas);
		areas.sort(null);
		for(int area: areas) {
			System.out.print(area + " ");
		}
	}
}
class Pair{
	int r, c;

	public Pair(int r, int c) {
		this.r = r;
		this.c = c;
	}
}
