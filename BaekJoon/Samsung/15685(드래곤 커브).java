import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main {
	static int[][] map = new int[101][101];
	static ArrayList<Integer> dir;
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(br.readLine());
		
		while(TC-->0) {
			String[] str = br.readLine().split(" ");
			int x = Integer.parseInt(str[0]);
			int y = Integer.parseInt(str[1]);
			int d = Integer.parseInt(str[2]);
			int g = Integer.parseInt(str[3]);
			
			dir = new ArrayList<>();
			map[y][x] = 1;
			dir.add(d);		
			//1세대 이상 그리기
			dragonCurve(x, y, d, g);
		}
		
		System.out.println(cntSquare());	
	}
	public static void dragonCurve(int x, int y, int d, int g) {
		//0세대 그리기
		switch(d) {
		case 0: x += 1; //  (→)
				break;
		case 1: y -= 1; // (↑)
				break;
		case 2: x -= 1; // (←)
				break;
		case 3: y += 1; // (↓)
				break;
		}
		map[y][x] = 1;
		
		//1세대 이상이면 이전 세대에 갔던 방향에 따라 현재 움직일 방향이 정해짐
		//이전 세대 방향과 대칭적인 구조를 가지며 방향에 +1을 해주면 된다.		
		while(g-- > 0) {	
			for(int i = dir.size() - 1; i >= 0; i--) {
				d = dir.get(i);
				switch(d) {
				case 0: y = y - 1; // (→) - (↑)
						dir.add(1);
						break;
				case 1: x = x - 1; // (↑) - (←)
						dir.add(2);
						break;
				case 2: y = y + 1; // (←) - (↓)
						dir.add(3);
						break;
				case 3: x = x + 1; // (↓) - (→)
						dir.add(0);
						break;
				}
				map[y][x] = 1;	
			}
		}		
	}
	
	public static int cntSquare() {
		int cnt = 0;
		for(int y = 0; y < 100; y++) {
			for(int x = 0; x < 100; x++) {
				if(map[y][x] == 1) {
					if(map[y][x + 1] == 1 && map[y + 1][x] == 1 && map[y + 1][x + 1] == 1) {
						cnt++;
					}
				}
			}
		}
		return cnt;
	}
}