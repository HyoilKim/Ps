import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws Exception {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
		int[] arr = new int[N];
		int[] lis = new int[N];
		int[] lds = new int[N];
		int[] res = new int[N];
		
		StringTokenizer st = new StringTokenizer(in.readLine(), " ");
 		for(int i = 0; i < N; i++) {
 			arr[i] = Integer.parseInt(st.nextToken());
 			lis[i] = 1;
 			lds[i] = 1;
 		}
		
 		//앞에서 부터 증가하는 최장수열의 길이 구하기
		for(int i = 1; i < N; i++) {
			int max = -1;
			for(int j = 0; j < i; j++) {
				if(arr[j] < arr[i]) 
					if(lis[j] > max)
						max = lis[j];			
			}
			if(max != -1) lis[i] += max;
				
		}
		
		//앞에서 부터 감소하는 최장수열의 길이 구하기
		for(int i = N - 2; i >= 0; i--) {
			int max = -1;
			for(int j = i + 1; j <= N - 1; j++) {
				if(arr[j] < arr[i]) 
					if(lds[j] > max)
						max = lds[j];		
			}
			if(max != -1) lds[i] += max;
		}
		
		int max = lis[0] + lds[0];
		for(int i = 0; i < N; i++) {
			res[i] = lis[i] + lds[i];
			if(res[i] > max)
				max = res[i];
		}
		
		System.out.println(max - 1);
	}
}
