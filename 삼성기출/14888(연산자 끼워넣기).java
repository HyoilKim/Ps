import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int min = Integer.MAX_VALUE;
	static int max = Integer.MIN_VALUE;
	static int[] num = new int[11];
	static int[] op = new int[4]; // +, -, *, -
	static int N;
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(in.readLine());			
		//inputÀÔ·Â
		StringTokenizer st = new StringTokenizer(in.readLine());
		for(int i = 0; i < N; i++) { 
			num[i] = Integer.parseInt(st.nextToken());
		}
		st = new StringTokenizer(in.readLine());
		for(int i = 0; i < 4; i++) {
			op[i] = Integer.parseInt(st.nextToken());
		}
		dfs(1, 0, 0, 0, 0, num[0]);
		
		System.out.println(max);
		System.out.println(min);
	}
	
	public static void dfs(int idx, int plus, int minus, int mul, int div, int total) {
		if(idx == N) {
			max = Math.max(total, max);
			min = Math.min(total, min);
			return;
		}else {
			if(plus < op[0]) {
				dfs(idx + 1, plus + 1, minus, mul, div, total + num[idx]);
			}if(minus < op[1]) {
				dfs(idx + 1, plus, minus + 1, mul, div, total - num[idx]);
			}if(mul < op[2]) {
				dfs(idx + 1, plus, minus, mul + 1, div, total * num[idx]);
			}if(div < op[3]) {
				dfs(idx + 1, plus, minus, mul, div + 1, total / num[idx]);
			}
		}
	}
}
