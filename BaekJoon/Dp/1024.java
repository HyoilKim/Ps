// 2019.06.24
// BaekJoon 1024
import java.util.Scanner;

public class asdf {
	static int[] one;
	static int[] zero;
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int iter = in.nextInt();
		int n;
		
		for(int i = 0; i < iter; i++) {
			one = new int[41];
			zero = new int[41];		
			zero[0] = 1; zero[1] = 0;
			one[0] = 0;	one[1] = 1;
			
			n = in.nextInt();	
			fibo(n);
			System.out.println(zero[n] + " " + one[n]);
		}
		in.close();
	}
	public static void fibo(int n) {
		if(n == 0) {
			return;
		}else if(n == 1) {
			return;
		}else{
			if(zero[n] == 0) {
				fibo(n-1);
				fibo(n-2);
				zero[n] = zero[n-1] + zero[n-2];
				one[n] = one[n-1] + one[n-2];
			}
		}
	}
}
