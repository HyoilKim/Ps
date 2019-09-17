import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
	static int N;
	static int cnt = 0;
	static Stack<Pair> stack;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		stack = new Stack<>();

		dfs(0);	
		System.out.println(cnt);
	}	
	
	public static void dfs(int numOfQueen) {
		if(numOfQueen == N) {
			cnt++;
			return;
		}
		for(int i = 0; i < N; i++) {
			if(queenIsIndependent(numOfQueen, i)) {
				stack.push(new Pair(numOfQueen, i));
				dfs(numOfQueen + 1);
				stack.pop();
			}
		}
	}
	
	public static boolean queenIsIndependent(int newX, int newY) {
		for(int i = 0; i < stack.size(); i++) {
			int x = stack.get(i).x;
			int y = stack.get(i).y;
			//이동경로 중복
			if(x == newX) return false;
			if(y == newY) return false;
			if(Math.abs(x - newX) == Math.abs(y - newY)) return false;		
		}
		return true;
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