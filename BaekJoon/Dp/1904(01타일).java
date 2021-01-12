import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] arr = new int[N];
		for(int i = 0; i < N; i++) {
			if(i == 0) 
				arr[i] = 1;
			else if(i == 1) 
				arr[i] = 2;
			else 
				arr[i] = (arr[i-1] + arr[i-2]) % 15746;
		}
		
		System.out.println(arr[N-1]);
	}
}