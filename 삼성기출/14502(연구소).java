import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;

public class Main {	
	static int N;
	static int M;
	static int[][] lab;
	static int[][] tmpLab;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};
	static boolean[][] visit;
	static int maxSafetyZone = 0;
	static LinkedList<Pair> virusPos = new LinkedList<>();
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine());
		N = Integer.parseInt(st.nextToken()); //����
		M = Integer.parseInt(st.nextToken()); //����
		lab = new int[N][M];
		tmpLab = new int[N][M];
		//�Է�
		for(int i = 0; i < N; i++) {
			st = new StringTokenizer(in.readLine());
			for(int j = 0; j < M; j++) {
				lab[i][j] = Integer.parseInt(st.nextToken());
				if(lab[i][j] == 2) {
					virusPos.add(new Pair(i, j));
				}
			}
		}
		
		for(int i = 0; i < N*M; i++) {
			setWall(i, 0);	
		}
		
		System.out.println(maxSafetyZone);
	}
	
	public static void setWall(int k, int wall) {
		if(wall == 3) {			
			copyLab();
			visit = new boolean[N][M];
			for(int i = 0; i < virusPos.size(); i++) {
				spreadVirus(tmpLab, virusPos.get(i).x, virusPos.get(i).y);
			}
			maxSafetyZone = Math.max(maxSafetyZone, cntSafetyZone());
			
			return;
		}
		
		//������ ��ġ�� ��3�� ����(���ڸ� 0 ~ n*m ���� ������ų�� (i/m, i%m) �� ��ǥ�� �ϸ� 2���� �迭�� ��� �ε����� Ž���� �� �ִ�)
		for(int i = k; i < N*M; i++) {
			int x = i / M;
			int y = i % M;
			if(lab[x][y] == 0) {
				lab[x][y] = 1;
				setWall(i, wall + 1);
				lab[x][y] = 0;
			}			
		}
	}
	
	public static void spreadVirus(int[][] lab, int x, int y) {		
		for(int i = 0; i < 4; i++) {
			int dirX = dx[i] + x;
			int dirY = dy[i] + y;
			if(dirX >= N || dirX < 0 || dirY >= M || dirY < 0 || visit[dirX][dirY]) 
				continue;
			if(tmpLab[dirX][dirY] == 0) { 
				tmpLab[dirX][dirY] = 2;
				visit[dirX][dirY] = true;
				spreadVirus(tmpLab, dirX, dirY);
			}
		}
	}
	
	public static int cntSafetyZone() {
		int cnt = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(tmpLab[i][j] == 0)
					cnt++;
			}
		}
		return cnt;
	}
	
	public static void copyLab() {
		//lab -> tmpLab
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				tmpLab[i][j] = lab[i][j];
			}
		}
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
