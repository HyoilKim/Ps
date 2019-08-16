import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	static int[][] map;
	static int cnt = 0;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int M = Integer.parseInt(str[1]);
		map = new int[N][M];
		str = br.readLine().split(" ");
		int x = Integer.parseInt(str[0]);
		int y = Integer.parseInt(str[1]);
		int d = Integer.parseInt(str[2]);
		
		for(int i = 0; i < N; i++) {
			str = br.readLine().split(" ");
			for(int j = 0; j < M; j++) {
				map[i][j] = Integer.parseInt(str[j]);
			}
		}
		// 1:벽, 2:청소완료, 0:청소x
		clean(x, y, d);
		System.out.println(cnt);
	}
	
	public static void clean(int x, int y, int d) {	
		if(map[x][y] == 0) {
			cnt++;
			map[x][y] = 2;		
		}
		
		boolean didClean = false;
		for(int i = 0; i < 4; i++) {
			int tmpX = x;
			int tmpY = y;
			//왼쪽방향
			switch(d) {
			case 0:
				y = y - 1;
				break;
			case 1:
				x = x - 1;
				break;
			case 2:
				y = y + 1;
				break;
			case 3:
				x = x + 1;
				break;
			}
			if(map[x][y] == 0) {	
				didClean = true;	
				clean(x, y, turn(d));
				break;
			}else {
				d = turn(d);
				x = tmpX;
				y = tmpY;
			}
		}
		
		if(!didClean) {
			switch(d) {
			case 0:
				x = x + 1;
				break;
			case 1:
				y = y - 1;
				break;
			case 2:
				x = x - 1;
				break;
			case 3:
				y = y + 1;
				break;
			}
			//벽이 아니라 청소했던 부분만 이동가능(청소안한 부분 존재 불가능)
			if(map[x][y] == 2) {
				clean(x, y, d);
			}
		}
	}
	
	public static int turn(int d) {
		switch(d) {
		case 0: d = 3;
				break;
		case 1: d = 0;
				break;
		case 2: d = 1;
				break;
		case 3: d = 2;
				break;
		}
		return d;
	}
}