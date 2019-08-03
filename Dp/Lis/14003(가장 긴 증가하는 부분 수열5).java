import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		ArrayList<Long> dp = new ArrayList<>(1000000);
		ArrayList<Integer> dpIndex = new ArrayList<>(1000000);
		ArrayList<Long> tracking = new ArrayList<>(1000000);
		Long[] arr = new Long[N];
		
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		for(int i = 0; i < N; i++) {
			arr[i] = Long.parseLong(st.nextToken());
		}
        
		//Lis(O(N*logN))
		for(int i = 0; i < N; i++) {	
			int idx = lower_bound(dp, 0, dp.size(), arr[i]);
			dpIndex.add(idx);
			if(idx == dp.size()) 
				dp.add(arr[i]);
			else
				dp.set(idx, arr[i]);
		}				

		System.out.println(dp.size());
		
        //dpIndex에서 tracking하여 dp의 lis를 구한다
		int len = dp.size() - 1;
		for(int i = N - 1; i >= 0; i--) { 
			if(dpIndex.get(i) == len) { 
				tracking.add(arr[i]);
				len--;
			}
		}
		
		//정렬하여 결과 tracking출력
		tracking.sort(null);
		for(Long i: tracking) 
			System.out.print(i + " ");
	}
	
	public static int lower_bound(ArrayList<Long> dp, int start, int end, Long target) {
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