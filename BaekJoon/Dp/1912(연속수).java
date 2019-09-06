import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] str = br.readLine().split(" ");
		int max = Integer.parseInt(str[0]);
		int sum = Integer.parseInt(str[0]);
		
		for(int i = 1; i < N; i++) {
			int cur = Integer.parseInt(str[i]);
			sum = Math.max(sum + cur, cur);
			
			if(sum > max)
				max = sum;
		}
		System.out.println(max);
		
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int N = Integer.parseInt(br.readLine());
//		int[] dp = new int[N];
//		String[] str = br.readLine().split(" ");
//		int max = Integer.parseInt(str[0]);
//		dp[0] = Integer.parseInt(str[0]);
//		
//		for(int i = 1; i < N; i++) {
//			int cur = Integer.parseInt(str[i]);
//			dp[i] = Math.max(dp[i-1] + cur, cur);
//			
//			if(dp[i] > max)
//				max = dp[i];
//		}
//		System.out.println(max);
	}	
}