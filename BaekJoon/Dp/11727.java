import java.util.Scanner;

public class Main {
	public static void main(String args[]) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
				
		if(N == 1) {
			System.out.print("1");
		}else if(N == 2) {
			System.out.print("3");
		}else {
			int[] arr = new int[N + 1];
			arr[1] = 1;
			arr[2] = 3;
			
			for(int i = 3; i <= N; i++) {
				arr[i] = (arr[i-1] + arr[i-2] * 2) % 10007;				
			}
			
			System.out.print(arr[N]);
		}
		
	}
}