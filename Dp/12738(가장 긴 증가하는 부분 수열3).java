import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		long[] arr = new long[N];
		ArrayList<Long> dp = new ArrayList<>();
		
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		for(int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}

		//Lis(O(N*logN))
		for(int i = 0; i < N; i++) {	
			int idx = lower_bound(dp, 0, dp.size(), arr[i]);
			if(idx == dp.size()) 
				dp.add(arr[i]);
			else
				dp.set(idx, arr[i]);
		}				

		System.out.println(dp.size());
	}
	
	public static int lower_bound(ArrayList<Long> dp, int start, int end, long target) {
		while(start < end) {
			int mid = (start + end) / 2;
			if(dp.get(mid) < target)
				start = mid + 1;
			else
				end = mid;	
		}
		return end;
	}
}
