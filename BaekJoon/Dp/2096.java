import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int[][] minDp = new int[2][3];
		int[][] maxDp = new int[2][3];
		
		//max
		for(int i = 0; i < N; i++) {
			if(i == 0) {
				int n1 = in.nextInt();
				int n2 = in.nextInt();
				int n3 = in.nextInt();
				maxDp[0][0] = minDp[0][0] = n1;
				maxDp[0][1] = minDp[0][1] = n2;
				maxDp[0][2] = minDp[0][2] = n3;
			}else {
				int n1 = in.nextInt();
				int n2 = in.nextInt();
				int n3 = in.nextInt();
				
				maxDp[1][0] = n1 + Integer.max(maxDp[0][0], maxDp[0][1]);
				maxDp[1][1] = n2 + Integer.max(Integer.max(maxDp[0][0], maxDp[0][1]), maxDp[0][2]);
				maxDp[1][2] = n3 + Integer.max(maxDp[0][1], maxDp[0][2]);
				maxDp[0][0] = maxDp[1][0];
				maxDp[0][1] = maxDp[1][1];
				maxDp[0][2] = maxDp[1][2];		
				
				minDp[1][0] = n1 + Integer.min(minDp[0][0], minDp[0][1]);
				minDp[1][1] = n2 + Integer.min(Integer.min(minDp[0][0], minDp[0][1]), minDp[0][2]);
				minDp[1][2] = n3 + Integer.min(minDp[0][1], minDp[0][2]);
				minDp[0][0] = minDp[1][0];
				minDp[0][1] = minDp[1][1];
				minDp[0][2] = minDp[1][2];					

				//System.out.println(minDp[1][0] + " " + minDp[1][1] + " " + minDp[1][2]);
			}		
		}
		System.out.print(Integer.max(Integer.max(maxDp[0][0], maxDp[0][1]), maxDp[0][2]) + " ");
		System.out.print(Integer.min(Integer.min(minDp[0][0], minDp[0][1]), minDp[0][2]));				
	}
}