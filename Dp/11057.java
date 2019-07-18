import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		int N = Integer.parseInt(st.nextToken());
		int[][] dp = new int[N][1000];
		
		for(int i = 0; i < 10; i++) {
			dp[0][i] = 1;
		}
		
		for(int i = 1; i < N; i++) {
			for(int j = 0; j < 10; j++) {
				for(int k = j; k < 10; k++) {
					dp[i][j] += dp[i - 1][k] % 10007;
				}
			}
		}
		
		int res = 0;
		for(int i = 0; i < 10; i++) {
			res += dp[N-1][i]; 
		}
		System.out.println(res % 10007);
	}
}
