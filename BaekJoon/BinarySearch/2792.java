import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static long N;
	static long M;
	static long[] jwry;	
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		N = Long.valueOf(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		jwry = new long[(int)M];	
		long max = Long.MIN_VALUE;
		
		for(int i = 0; i < M; i++) {
			jwry[i] = Integer.parseInt(in.readLine());
			if(max <= jwry[i]) max = jwry[i];
		}
	
		long start = 1;
		long end = max;
		long res = Long.MAX_VALUE;
		while(start <= end) {
			long mid = (start + end) / 2;
			if(findAnswer(mid)) {
				res = Math.min(res, mid);
				end = mid - 1;
			}else {
				start = mid + 1;
			}
 		}
		
		System.out.println(res);
	}
	
	public static boolean findAnswer(long mid) {
		long studentNumber = 0;
		for(int i = 0; i < M; i++) {
			if(jwry[i] % mid == 0) {
				studentNumber += jwry[i] / mid;
			}else {
				studentNumber += jwry[i] / mid + 1;
			}
		}
		
		if(studentNumber <= N) return true;
		else return false;
			
	}
}