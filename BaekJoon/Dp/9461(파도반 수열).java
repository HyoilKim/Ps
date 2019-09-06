import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int TC = Integer.parseInt(in.readLine());
		long[] arr = new long[100];
		
		for(int i = 0; i < 100; i++) {
			if(i == 0 || i == 1 || i==2)
				arr[i] = 1;
			else if(i == 3 || i == 4)
				arr[i] = 2;
			else
				arr[i] = arr[i-1] + arr[i-5];
		}
		
		while(TC-->0) {
			int N = Integer.parseInt(in.readLine());
			System.out.println(arr[N - 1]);
		}
	}
}