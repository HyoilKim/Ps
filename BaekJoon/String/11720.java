import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		int sum = 0;
		
		String line = in.next();
		for(int i = 0; i < N; i++) {
			sum += line.charAt(i) - '0';
		}
		System.out.print(sum);
	}
}