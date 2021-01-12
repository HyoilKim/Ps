import java.util.Scanner;

public class Main {
   public static void main(String[] args){
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int dp[][] = new int[N+1][3];	
		int[][] cost = new int[N+1][3];

		for (int i = 1; i < N+1; i++){
			for (int j = 0; j < 3; j++){
				cost[i][j] = in.nextInt();
			}
		}
		dp[1][0] = cost[1][0];
		dp[1][1] = cost[1][1];
		dp[1][2] = cost[1][2];
		
		for (int i = 2; i < N+1; i++){
			dp[i][0] = Integer.min(dp[i-1][1], dp[i-1][2]) + cost[i][0];
			dp[i][1] = Integer.min(dp[i-1][0], dp[i-1][2]) + cost[i][1];
			dp[i][2] = Integer.min(dp[i-1][0], dp[i-1][1]) + cost[i][2];
		}
		int min = Integer.min(dp[N][0],dp[N][1]);
		min = Integer.min(min, dp[N][2]); 
		System.out.print(min);
	}
}