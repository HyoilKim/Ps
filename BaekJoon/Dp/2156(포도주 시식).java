import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] arr = new int[N];
		int[] dp = new int[N];
		
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(in.readLine());
		}
		
		for(int i = 0; i < N; i++) {			
			if(i == 0) 
				dp[0] = arr[0];
			else if(i == 1) 
				dp[1] = arr[0] + arr[1];
			else if(i == 2) 
				dp[2] = Math.max(dp[1], Math.max(dp[0] + arr[2], arr[1] + arr[2]));
			else 
				//현재 포도주를 먹고 - 이전의 포도주를 먹은경우, 이전의 포도주를 먹지 않은 경우
				//현재 포도주를 먹지 않은 경우
				dp[i] = Math.max(dp[i-1], Math.max(arr[i] + arr[i-1] + dp[i-3], arr[i] + dp[i-2]));
			
		}
		System.out.println(dp[N-1]);
		
	}
}