import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
		int max = 0;
		int sum = 0;
		
		for(int i = 0; i < 4; i++) {
			StringTokenizer st = new StringTokenizer(input.readLine());
			int out = Integer.parseInt(st.nextToken());
			int in = Integer.parseInt(st.nextToken());
			sum += in - out;
			if(sum > max)
				max = sum;	
		}
	
		System.out.println(max);	
	}
}
