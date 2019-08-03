import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		ArrayList<Integer> dp = new ArrayList<Integer>(100000);
		ArrayList<Integer> dpIndex = new ArrayList<Integer>(100000);
		ArrayList<Integer> tracking = new ArrayList<Integer>(100000);
		Pair[] elec = new Pair[N];
		
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(in.readLine(), " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			elec[i] = new Pair(a, b);
		}
        
		Arrays.sort(elec);

		//Lis(O(N*logN))
		for(int i = 0; i < N; i++) {	
			int idx = lower_bound(dp, 0, dp.size(), elec[i].y);
			dpIndex.add(idx);
			if(idx == dp.size()) 
				dp.add(elec[i].y);
			else
				dp.set(idx, elec[i].y);
		}				

		System.out.println(N - dp.size());
		
        //dpIndex에서 tracking하여 dp의 lis를 구한다
		int len = dp.size() - 1;
		for(int i = N - 1; i >= 0; i--) {
			int lisIdx = dpIndex.get(i);
			if(lisIdx == len) 
				len--;
			else
				tracking.add(elec[i].x);
		}

		tracking.sort(null);
		for(Integer i: tracking) System.out.println(i);
	}
	
	public static int lower_bound(ArrayList<Integer> dp, int start, int end, int target) {
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

class Pair implements Comparable<Pair>{
	int x;
	int y;
	
	public Pair(int x, int y) {
		this.x = x;
		this.y = y;
	}

	@Override
	public int compareTo(Pair o) {
		if(this.x > o.x) return 1;
		else if(this.x < o.x) return -1;
		else return 0;
	}	
}