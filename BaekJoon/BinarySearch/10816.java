import java.util.Arrays;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
	static int[] arr;
	static int[] res;
	static int[] chk = new int[20000001];
	
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter out = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(in.readLine());
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
		
		arr = new int[N];
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr);
		
		int M = Integer.parseInt(in.readLine());
		res = new int[M];
		st = new StringTokenizer(in.readLine(), " ");
		for(int i = 0; i < M; i++) {	
			int val = Integer.parseInt(st.nextToken());
			if(chk[val + 10000000] != 0) {
				System.out.print(res[chk[val + 10000000]] + " ");
				continue;
			}
			res[i] = search(0, N-1, val);
			chk[val + 10000000] = i;	
			System.out.print(res[i] + " ");
		}	
		
		
	}
	
	public static int search(int start, int end, int val) {
		int cnt;		
		if(start <= end) {	
			int mid = (start + end) / 2;		
			if(val == arr[mid]) {
				cnt = 1;
				cnt += search(start, mid - 1, val);
				cnt += search(mid + 1, end, val);
				return cnt;
			}else {
				if(val > arr[mid]) {
					return search(mid+1, end, val);
				}else if(val < arr[mid]) {
					return search(start, mid-1, val);
				}
			}
		}
		return 0;	
	}
}
