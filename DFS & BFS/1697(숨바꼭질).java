import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] str = br.readLine().split(" ");
		int N = Integer.parseInt(str[0]);
		int K = Integer.parseInt(str[1]);
		Queue<Pos> q = new LinkedList<>();
		int[] dx = {1, -1, 0};
		boolean[] visited = new boolean[100001];
		
		q.offer(new Pos(N, 0));
		visited[N] = true;
		
		while(!q.isEmpty()) {
			Pos p = q.poll();
			int pos = p.pos;
			int sec = p.sec;
			dx[2] = pos;
			
			if(pos == K) {
				System.out.println(sec);
				break;
			}
		
			for(int i = 0; i < 3; i++) {
				int newPos = dx[i] + pos;
				if(inBoundary(newPos) && !visited[newPos]) {
                    visited[newPos] = true;
					q.offer(new Pos(newPos, sec + 1));
				}
			}
		}
	}	
	
	public static boolean inBoundary(int pos) {
		if(pos >= 0 && pos <= 100000) return true;
		else return false;
	}
}

class Pos{
	int pos;
	int sec;
	
	Pos(int pos, int sec) {
		this.pos = pos;
		this.sec = sec;
	}
}