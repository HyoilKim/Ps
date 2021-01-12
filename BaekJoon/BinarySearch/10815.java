import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int[] arr;
	
	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		int N = in.nextInt();
		arr = new int[N];
		for(int i = 0; i < N; i++) {
			arr[i] = in.nextInt();
		}
		
		Arrays.sort(arr);
		
		int M = in.nextInt();
		int[] res = new int[M];
		for(int i = 0; i < M; i++) {
			int val = in.nextInt();
			if(binarySearch(0, N-1, val)) {
				res[i] = 1;
			}else {
				res[i] = 0;
			}
		}
		
		for(int i = 0; i < M; i++) {
			System.out.print(res[i] + " ");
		}
	}
    
	public static boolean binarySearch(int start, int end, int val) {
		int mid = (start + end) / 2;
		if(start <= end) {
			if(val == arr[mid]) {
				return true;
			}else if(val > arr[mid]) {
				return binarySearch(mid+1, end, val);
			}else if(val < arr[mid]) {
				return binarySearch(start, mid-1, val);
			}
		}
		return false;
	}
}