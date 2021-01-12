import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
	static int[][] field;
	static Point[] cabbage;
	static int M, N, K;
	
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int TC = in.nextInt();
		while(TC-->0) {
			//M가로 N세로
			M = in.nextInt();
			N = in.nextInt();
			K = in.nextInt();
			field = new int[N][M];
			cabbage = new Point[K];
			
			for(int i = 0; i < K; i++) {
				int x = in.nextInt();
				int y = in.nextInt();
				field[y][x] = 1;
				cabbage[i] = new Point(x, y);
			}

			BFS();
		}
	}
	
	public static void BFS() {
		Queue<Point> q = new LinkedList<>();
		int cnt = 0;
		int[] dx = {0, 0, 1, -1};
		int[] dy = {1, -1, 0, 0};

		for(int i = 0; i < K; i++) {
			int x = cabbage[i].x;
			int y = cabbage[i].y;
			if(field[y][x] == 0) continue;
			q.offer(new Point(x, y));
			field[y][x] = 0;
			cnt++;
			while(!q.isEmpty()) {
				Point p = q.poll();
				int x1 = p.x;
				int y1 = p.y;
				for(int j = 0; j < 4; j++) {
					int dirX = x1 + dx[j];
					int dirY = y1 + dy[j];
					if(dirX >= 0 && dirX < M && dirY >= 0 && dirY < N) {
						if(field[dirY][dirX] == 1) {
							q.offer(new Point(dirX, dirY));
							field[dirY][dirX] = 0;
						}
					}
				}	
			}

		}

		System.out.println(cnt);
	}
}

class Point{
	int x;
	int y;
	
	Point(int x, int y){
		this.x = x;
		this.y = y;
	}
}