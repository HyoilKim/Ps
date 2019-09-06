package ps;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Test {	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] step = new int[N];
		int[] dp = new int[N];
		
		for(int i = 0; i < N; i++) {
			step[i] = Integer.parseInt(in.readLine());
		}
		
		for(int i = 0; i < N; i++) {	
			if(i == 0) 
				dp[i] = step[i];
			else if(i == 1)	
				dp[i] = dp[i-1] + step[i];
			else if(i == 2) {
				dp[i] = Math.max(step[i-2], step[i-1]);
				dp[i] += step[i];
			}
			else {
				dp[i] = Math.max(dp[i-2], step[i-1] + dp[i-3]);
				dp[i] += step[i];
			}
		}
		
		System.out.println(dp[N-1]);
	}
}