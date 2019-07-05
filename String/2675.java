import java.util.Scanner;

public class Test {
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int TC = in.nextInt();
		
		while(TC-->0) {
			int N = in.nextInt();
			String str = in.next();
			for(int i = 0; i < str.length(); i++) {
				for(int j = 0; j < N; j++) {
					System.out.print(str.charAt(i));
				}
			}
			System.out.println("");
		}
		in.close();
	}
}