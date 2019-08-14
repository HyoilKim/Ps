import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		//i 자리 수 일때 j로 끝나는 경우를 저장하는 dp배열
		//i 자리 수 일때 j로 시작하는 경우도 가능 dp[i][0]만 고려
		int[][] dp = new int[N][10];
		int BILLION = 1000000000; // 변수명 mod도 좋은듯
		
		for(int i = 1; i < 10; i++) {
			dp[0][i] = 1;	
		}
		
		for(int i = 1; i < N; i++) {
			for(int j = 0; j < 10; j++) {
				if(j == 0) {
					dp[i][j] = dp[i-1][j+1];
				}else if(j == 9){
					dp[i][j] = dp[i-1][j-1];
				}else {
					dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % BILLION;
				}
			}
		}
		
		int sum = 0;
		for(int i = 0; i < 10; i++) {
			sum = (sum + dp[N-1][i]) % BILLION;
		}
		
		System.out.println(sum);	
	}
	
}
